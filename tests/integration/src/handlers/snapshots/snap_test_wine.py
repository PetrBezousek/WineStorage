# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots["test_autocomplete[attribute] 1"] = ["attribute"]

snapshots["test_autocomplete[sugar] 1"] = ["sugar"]

snapshots["test_autocomplete[unknown column] 1"] = []

snapshots["test_autocomplete[variety] 1"] = ["variety"]

snapshots["test_autocomplete[winery] 1"] = ["winery"]

snapshots["test_autocomplete[year] 1"] = ["2020"]
