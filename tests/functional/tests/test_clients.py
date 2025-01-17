import pytest


class TestClients(object):
    @pytest.mark.client
    def test_ceph_config_file(self, node, host):
        assert host.file('/etc/ceph/ceph.conf').exists
        assert host.file('/etc/ceph/ceph.conf').mode == 0o600

    @pytest.mark.client
    def test_ceph_keyring(self, node, host):
        assert host.file('/etc/ceph/ceph.keyring').exists
        assert host.file('/etc/ceph/ceph.keyring').mode == 0o600