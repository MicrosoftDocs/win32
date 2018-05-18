---
Description: 'The FaxDevices object represents the global collection of all the fax devices that are exposed by all the fax service providers (FSPs) currently registered with the fax service.'
ms.assetid: '88598e24-6339-49d9-8887-7370aa402135'
title: Fax Device Groups
---

# Fax Device Groups

The [**FaxDevices**](-mfax-faxdevices.md) object represents the global collection of all the fax devices that are exposed by all the fax service providers (FSPs) currently registered with the fax service. You cannot add or remove devices from the global device collection, but you can group the devices in the collection and assign names to device groups. A group can include devices from different FSPs.

Device groups can enable you to transmit faxes in a cost-effective manner. For example, if you send transmissions regularly to local recipients, you could define a device group named *Carrier1* that contains devices connected to *Carrier1* because that carrier provides the lowest rate for local calls. If you send transmissions regularly to international destinations, you could define a device group that contains devices connected to fax-over-Internet Protocol (FoIP) service providers. Internet-enabled devices use the Internet to send a fax, thereby saving the cost of an international call.

In a fax device group, the relative order of the devices within the group is significant. When the fax service initiates an outgoing job, it attempts to select the first fax device in the device group. If that device is not available, the service selects the next available device that follows in rank order, and so on. (In the global collection of fax devices, the order of the devices does not matter.) Device groups can overlap and a device can be a member of more than one group.

You can create fax device groups and define outbound routing rules that map outgoing fax jobs to a fax device group (or to an individual fax device) using the fax recipient's telephone number.

If you have a small number of fax devices, it may not be effective to create device groups. In fact, creating device groups that contain only one device can be time-consuming. In this instance you can associate a single device ID with an outbound routing rule.

## Related topics

<dl> <dt>

[**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md)
</dt> <dt>

[**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md)
</dt> <dt>

[Outbound Routing Rules](-mfax-outbound-routing-rules.md)
</dt> </dl>

 

 



