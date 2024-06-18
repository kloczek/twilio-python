r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Marketplace
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class InstalledAddOnUsageInstance(InstanceResource):
    """
    :ivar billable_items:
    :ivar total_submitted: Represents the total quantity submitted.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], installed_add_on_sid: str
    ):
        super().__init__(version)

        self.billable_items: Optional[List[str]] = payload.get("billable_items")
        self.total_submitted: Optional[float] = deserialize.decimal(
            payload.get("total_submitted")
        )

        self._solution = {
            "installed_add_on_sid": installed_add_on_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Marketplace.V1.InstalledAddOnUsageInstance {}>".format(context)


class InstalledAddOnUsageList(ListResource):

    class CreateMarketplaceBillingUsageRequest(object):
        """
        :ivar billable_items:
        """

        def __init__(self, payload: Dict[str, Any], installed_add_on_sid: str):

            self.billable_items: Optional[
                List[
                    InstalledAddOnUsageList.CreateMarketplaceBillingUsageRequestBillableItems
                ]
            ] = payload.get("billable_items")

        def to_dict(self):
            return {
                "billable_items": [
                    billable_items.to_dict() for billable_items in self.billable_items
                ],
            }

    class CreateMarketplaceBillingUsageRequestBillableItems(object):
        """
        :ivar quantity:
        :ivar sid:
        """

        def __init__(self, payload: Dict[str, Any], installed_add_on_sid: str):

            self.quantity: Optional[float] = payload.get("quantity")
            self.sid: Optional[str] = payload.get("sid")

        def to_dict(self):
            return {
                "quantity": self.quantity,
                "sid": self.sid,
            }

    def __init__(self, version: Version, installed_add_on_sid: str):
        """
        Initialize the InstalledAddOnUsageList

        :param version: Version that contains the resource
        :param installed_add_on_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "installed_add_on_sid": installed_add_on_sid,
        }
        self._uri = "/InstalledAddOns/{installed_add_on_sid}/Usage".format(
            **self._solution
        )

    def create(
        self,
        create_marketplace_billing_usage_request: CreateMarketplaceBillingUsageRequest,
    ) -> InstalledAddOnUsageInstance:
        """
        Create the InstalledAddOnUsageInstance

        :param create_marketplace_billing_usage_request:

        :returns: The created InstalledAddOnUsageInstance
        """
        data = create_marketplace_billing_usage_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InstalledAddOnUsageInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
        )

    async def create_async(
        self,
        create_marketplace_billing_usage_request: CreateMarketplaceBillingUsageRequest,
    ) -> InstalledAddOnUsageInstance:
        """
        Asynchronously create the InstalledAddOnUsageInstance

        :param create_marketplace_billing_usage_request:

        :returns: The created InstalledAddOnUsageInstance
        """
        data = create_marketplace_billing_usage_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InstalledAddOnUsageInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Marketplace.V1.InstalledAddOnUsageList>"