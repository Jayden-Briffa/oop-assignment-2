import pytest
from FeatureRequest import FeatureRequest, Priority, Status
import tests.helpers as helpers


def testStatusDefaultsToNeedsApproval():
    featureRequest = FeatureRequest(
        1,
        Priority.HIGH,
        "Test Feature",
        "Description",
        "Test Technician",
    )

    assert featureRequest.getStatus() is Status.NEEDS_APPROVAL


def testValidateStatusAllowsChangeWhenApproved():
    featureRequest = helpers.generateTestFeatureRequest()
    featureRequest.approve()

    msg = featureRequest._validateStatus(Status.TO_DO)

    assert msg is None, f"Expected no error for status change when approved, got: {msg}"


def testValidateStatusRejectsChangeBeforeApproval():
    featureRequest = helpers.generateTestFeatureRequest()

    pytest.raises(ValueError, featureRequest._validateStatus, Status.TO_DO)
