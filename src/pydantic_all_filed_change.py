from typing import Any
from pydantic import BaseModel


class Url(BaseModel):
    base_url: str
    foo: str = "/foo"
    bar: str = "/bar"

    def model_post_init(self, __context: Any) -> None:
        for filed in self.model_fields:
            if filed == "base_url":
                continue
            setattr(self, filed, self.base_url + getattr(self, filed))


if __name__ == "__main__":
    url = Url(base_url="http://localhost:8000")
    print(url)
    # output
    # base_url='http://localhost:8000/' foo='http://localhost:8000//foo' bar='http://localhost:8000//bar'
