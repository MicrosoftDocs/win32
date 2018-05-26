---
Description: The extended fax client Component Object Model (COM) implementation eases the routing of outbound faxes.
ms.assetid: 8da75129-a19e-4c14-8940-a706b68ce860
title: Outbound Routing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Outbound Routing

The extended fax client Component Object Model (COM) implementation eases the routing of outbound faxes. By creating outbound routing rules, you can determine which device or group of devices will handle faxes to a particular area code or country/region code. You can use outbound routing to enhance the efficiency of a fax-sending network and to manage the cost of transmitting faxes.

At initial startup, the fax service includes one device group called the "All devices" group, and a default outbound routing rule called the "All other" rule. If you do not define outbound routing rules, the fax service sends each outbound fax using the "All other" rule and any device that is available. By default, the "All other" rule points to the "All devices" group. You can change the group to which the "All other" rule points.

## Related topics

<dl> <dt>

[Fax Device Groups](-mfax-fax-device-groups.md)
</dt> <dt>

[Outbound Routing Rules](-mfax-outbound-routing-rules.md)
</dt> </dl>

 

 



