#!/usr/bin/env python
#-*- coding: utf-8 -*-
import aiosqlite
from constants import DATA_DIR


async def get_sql(sql, args=None, fetch_all: bool = False):
    async with aiosqlite.connect(DATA_DIR) as conn:
        cur = await conn.execute(sql, args)
        r = await cur.fetchall() if fetch_all else await cur.fetchone()
        await cur.close()
        return r



async def set_sql(sql, args=None, script: bool = False):
    async with aiosqlite.connect(DATA_DIR) as conn:
        if not script:
            cur = await conn.execute(sql, args)
        else:
i            cur = await conn.executescript(sql)
        await cur.close()
        await conn.commit()
