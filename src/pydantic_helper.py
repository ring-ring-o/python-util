from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, TypeVar, cast

from pydantic import BaseModel


@dataclass(frozen=True)
class _GetFields:
    _model: type[BaseModel]

    def __getattr__(self, item: str) -> Any:
        if item in self._model.model_fields:
            return item

        return getattr(self._model, item)


TModel = TypeVar("TModel", bound=type[BaseModel])


def fields(model: TModel, /) -> TModel:
    return cast(TModel, _GetFields(model))


if __name__ == "__main__":

    class Sample(BaseModel):
        foo: str
        bar: str

    print(fields(Sample).foo)
    # output
    # foo
