from faker import Faker
from src.utils.factories.gist_factory import RequestGistFactory

def test_delete_gist():
    file_name = f"{Faker().slug()}.txt"
    file_content = Faker().slug()
    payload = {
        "description": "This is simple txt gist",
        "public": True,
        "files":
            {
                file_name:
                    {
                        "content": f"{file_content}"
                    }
            }
    }
    gist = RequestGistFactory.post_gist(payload)
    RequestGistFactory.delete_gist(gist.id_)
