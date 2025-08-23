from asyncmy.pool import Pool
from asyncmy import create_pool

from core.settings import settings

async def create_mysql_pool() -> Pool:
    """
    Create a connection pool to the MySQL database.
    """
    return await create_pool(
        host=settings.db.ip,
        port=3306,
        user=settings.db.user,
        password=settings.db.password,
        db=settings.db.db,
        autocommit=True
    )

async def db_setup(pool: Pool):
    
    # users_table = (
    #     'CREATE TABLE IF NOT EXISTS Users ('
    #     ' user_id BIGINT(16) NOT NULL PRIMARY KEY,'
    #     ' full_name VARCHAR(128) NOT NULL,'
    #     ' username VARCHAR(32) DEFAULT NULL'
    #     ');'
    # )

    # tasks = [
    #     users_table,
    # ]
    
    # async with pool.acquire() as conn:
    #     async with conn.cursor() as cur:
    #         for ex in tasks:
    #             await cur.execute(ex)
    ...

