from notion_client import Client
from pprint import pprint

def notion_test():

    private_key="secret_BagWaishDYjawGs7XKPpGWXqRwHSeIDruQ7gnV2BRoq"
    database_id='c985b36c8cec439182cc0e322c863478'


    notion = Client(auth=private_key)
    print("client 생성")
    db = notion.databases.retrieve(database_id)
    print("자료 생성")

    new_page = {
        "이름": {"title": [{"text": {"content": "New Page Title"}}]},
    }

    new_children = [{

                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {
                        "content": "You made this page using the Notion API. Pretty cool, huh? We hope you enjoy building with us."}}]
                }
            }]

    created_page = notion.pages.create(parent={"database_id": database_id}, properties=new_page, children=new_children)


    id_page=created_page['id']

    new_block = {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "text": [
                {
                    "type": "text",
                    "text": {
                        "content": "New text block"
                    }
                }
            ]
        }
    }


    #notion.blocks.parent.pages.create(id_page,)

    #new_block = created_page.add_new(type="paragraph", title=[{"type": "text", "text": {"content": "This is a new paragraph."}}])

    return database_id




