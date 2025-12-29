from __future__ import annotations

from typing import List

from models.user import User


def select_top_users_by_rate(users: List[User], top_size: int) -> List[User]:
    return sorted(users, key=lambda user: user.rate, reverse=True)[:top_size]
