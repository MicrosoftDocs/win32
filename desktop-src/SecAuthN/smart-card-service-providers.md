---
description: Smart Card Service Providers (SCSP) provide access to Smart Card capabilities.
ms.assetid: f214385f-3e65-4175-925c-3d1dc4060185
title: Smart Card Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card Service Providers

Smart Card Service Providers (SCSP) provide access to [*Smart Card*](../secgloss/s-gly.md) capabilities. They can provide access to a single capability, such as the base service providers provided by the Smart Card SDK, or they can provide access to several capabilities to accomplish a more complex task.

Service providers provide access through COM interfaces. The Smart Card SDK provides the COM interfaces used by its own base service providers as well as several application interfaces that can be used when developing custom service providers.



| Topic                                                                                   | Description                                            |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------|
| [Base Service Providers](base-service-providers.md)<br/>                         | Base service providers.<br/>                     |
| [Building an ISO7816-4 APDU Command](building-an-iso7816-4-apdu-command.md)<br/> | Adding functionality to a service provider.<br/> |
| [Vendor Wrapper Service Provider](vendor-wrapper-service-provider.md)<br/>       | A vendor wrapper example.<br/>                   |



 

For an overview of all the COM interfaces provided by the smart card SDK (base service provider and application interfaces), see [Smart Card Interfaces](smart-card-interfaces.md).

 

 
