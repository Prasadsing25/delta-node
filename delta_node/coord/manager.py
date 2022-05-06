from abc import ABC, abstractmethod

from delta.core.task import ServerContext

class Manager(ABC):
    def __init__(self, task_id: str, ctx: ServerContext) -> None:
        self.task_id = task_id
        self.ctx = ctx

    @abstractmethod
    async def init(self):
        ...

    @abstractmethod
    async def run(self):
        ...

    @abstractmethod
    async def finish(self):
        ...
