from tests.utils import pool
from indy.pool import open_pool_ledger
from indy.error import ErrorCode, IndyError

import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.mark.asyncio
async def test_open_pool_ledger_works(cleanup_storage):
    name = "open_pool_ledger_works"
    await pool.create_pool_ledger_config(name)
    pool_handle = await open_pool_ledger(name, "")
    assert pool_handle is not None


@pytest.mark.asyncio
async def test_open_pool_ledger_works_for_config(cleanup_storage):
    name = "open_pool_ledger_works_for_config"
    config = '{"refreshOnOpen": true}'
    await pool.create_pool_ledger_config(name)
    pool_handle = await open_pool_ledger(name, config)
    assert pool_handle is not None


@pytest.mark.asyncio
async def test_open_pool_ledger_works_for_twice(cleanup_storage):
    name = "open_pool_ledger_works_for_twice"
    await pool.create_pool_ledger_config(name)
    pool_handle = await open_pool_ledger(name, "")
    assert pool_handle is not None
    with pytest.raises(IndyError) as e:
        await open_pool_ledger(name, "")
    assert ErrorCode.PoolLedgerInvalidPoolHandle == e.value.error_code


@pytest.mark.asyncio
async def test_open_pool_ledger_works_for_two_nodes(cleanup_storage):
    name = "open_pool_ledger_works_for_two_nodes"
    nodes = [
        "{\"data\":{\"alias\":\"Node1\",\"client_ip\":\"10.0.0.2\",\"client_port\":9702,\"node_ip\":\"10.0.0.2\",\"node_port\":9701,\"services\":[\"VALIDATOR\"]},\"dest\":\"Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv\",\"identifier\":\"Th7MpTaRZVRYnPiabds81Y\",\"txnId\":\"fea82e10e894419fe2bea7d96296a6d46f50f93f9eeda954ec461b2ed2950b62\",\"type\":\"0\"}\n",
        "{\"data\":{\"alias\":\"Node2\",\"client_ip\":\"10.0.0.2\",\"client_port\":9704,\"node_ip\":\"10.0.0.2\",\"node_port\":9703,\"services\":[\"VALIDATOR\"]},\"dest\":\"8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb\",\"identifier\":\"EbP4aYNeTHL6q385GuVpRV\",\"txnId\":\"1ac8aece2a18ced660fef8694b61aac3af08ba875ce3026a160acbc3a3af35fc\",\"type\":\"0\"}\n"
    ]
    await pool.create_pool_ledger_config(name, nodes)
    pool_handle = await open_pool_ledger(name, None)
    assert pool_handle is not None


@pytest.mark.asyncio
async def test_open_pool_ledger_works_for_three_nodes(cleanup_storage):
    name = "open_pool_ledger_works_for_three_nodes"
    nodes = [
        "{\"data\":{\"alias\":\"Node1\",\"client_ip\":\"10.0.0.2\",\"client_port\":9702,\"node_ip\":\"10.0.0.2\",\"node_port\":9701,\"services\":[\"VALIDATOR\"]},\"dest\":\"Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv\",\"identifier\":\"Th7MpTaRZVRYnPiabds81Y\",\"txnId\":\"fea82e10e894419fe2bea7d96296a6d46f50f93f9eeda954ec461b2ed2950b62\",\"type\":\"0\"}\n",
        "{\"data\":{\"alias\":\"Node2\",\"client_ip\":\"10.0.0.2\",\"client_port\":9704,\"node_ip\":\"10.0.0.2\",\"node_port\":9703,\"services\":[\"VALIDATOR\"]},\"dest\":\"8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb\",\"identifier\":\"EbP4aYNeTHL6q385GuVpRV\",\"txnId\":\"1ac8aece2a18ced660fef8694b61aac3af08ba875ce3026a160acbc3a3af35fc\",\"type\":\"0\"}\n",
        "{\"data\":{\"alias\":\"Node3\",\"client_ip\":\"10.0.0.2\",\"client_port\":9706,\"node_ip\":\"10.0.0.2\",\"node_port\":9705,\"services\":[\"VALIDATOR\"]},\"dest\":\"DKVxG2fXXTU8yT5N7hGEbXB3dfdAnYv1JczDUHpmDxya\",\"identifier\":\"4cU41vWW82ArfxJxHkzXPG\",\"txnId\":\"7e9f355dffa78ed24668f0e0e369fd8c224076571c51e2ea8be5f26479edebe4\",\"type\":\"0\"}\n"
    ]
    await pool.create_pool_ledger_config(name, nodes)
    pool_handle = await open_pool_ledger(name, None)
    assert pool_handle is not None
