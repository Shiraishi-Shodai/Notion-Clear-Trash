
from notion.client import NotionClient


def get_trash(client):
    query = {
              "type": "BlocksInSpace",
              "query": "",
              "filters": {
                "isDeletedOnly": True,
                "excludeTemplates": False,
                "isNavigableOnly": True,
                "requireEditPermissions": False,
                "ancestors": [],
                "createdBy": [],
                "editedBy": [],
                "lastEditedTime": {},
                "createdTime": {}
              },
              "sort": "Relevance",
              "limit": 1000,
              "spaceId": client.current_space.id,
              "source": "trash"
            }
    results = client.post('/api/v3/search', query)
    block_ids = results.json()['results']

    return [block_id['id'] for block_id in block_ids]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def delete_permanently(client, block_ids):
    for block_batch in chunks(block_ids, 10):
        try:
            client.post("deleteBlocks", {"blockIds": block_batch, "permanentlyDelete": True})
        except Exception as err:
            print(err)
            print(block_batch)


if __name__== "__main__":
    token = 'v02%3Auser_token_or_cookies%3AVS6djkqmACJml1g-BqRcn7fsbucCyPDYzw-tofnm12CqjTEiZEUQxa1EuiLsnZhYjEFfu4NE41WBTxXl2DdVXAZiqYGNqaN5WVvrp1PZEZwp9EeymOzy1pOK4CMO8T0wioc5'
    client = NotionClient(token_v2=token)
    print(client)

    # block_ids = get_trash(client)
    # delete_permanently(client, block_ids)
    # print('Successfully cleared all trash blocks.')
