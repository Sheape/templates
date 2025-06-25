"""Define the configurable parameters for the agent."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from functools import lru_cache
from dotenv import load_dotenv

from langchain_core.runnables import RunnableConfig, ensure_config

load_dotenv()

### Uncomment this if you want to use Pydantic settings
# class Settings(BaseSettings):
#     """General settings."""
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         env_file_encoding="utf-8",
#         extra="ignore"
#     )
#
#


@lru_cache
def get_config() -> Settings:
    """Retrieve the settings and cache it."""
    settings = Settings() # type: ignore
    return settings

@dataclass(kw_only=True)
class Settings:
    """Default fields. This is useful when you want to retrieve metadata from auth middleware."""
    metadata: dict
    run_id: str
    callbacks: list
    recursion_limit: int
    tags: list

    """The configuration for the agent."""
    system_prompt: str = field(
        default="You are a helpful assistant that provides relevant information based on user queries.",
        metadata={
            "description": "The system prompt to use for the agent."
        },
    )

    max_search_results: int = field(
        default=3,
        metadata={
            "description": "The maximum number of search results to return for"
            "each search query."
        },
    )

    @classmethod
    def from_runnable_config(
        cls, config: RunnableConfig | None = None
    ) -> Settings:
        """Create a Configuration instance from a RunnableConfig object."""
        config = ensure_config(config)
        configurable = config.get("configurable") or {}
        _fields = {f.name for f in fields(cls) if f.init}
        configurable.update({
            k: v for k, v in config.items() if k in _fields
        })
        return cls(**{k: v for k, v in configurable.items() if k in _fields})
