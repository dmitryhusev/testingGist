from faker import Faker
from src.utils.factories.gist_factory import RequestGistFactory

def test_create_gist(cleanup_gist):
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
    res = RequestGistFactory.post_gist(payload)
    cleanup_gist(res.id_)
    assert file_content == res.file_name.get(file_name).get('content')
