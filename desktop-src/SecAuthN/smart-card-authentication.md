---
description: Smart Card Authentication
ms.assetid: cb5c80ea-c15e-4f68-a94b-b458d69ff474
title: Smart Card Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card Authentication

The basic parts of the [*smart card subsystem*](../secgloss/s-gly.md) are based on PC/SC standards (see the specifications at [https://www.pcscworkgroup.com/](https://www.pcscworkgroup.com/)). These basic parts include:

-   A [*resource manager*](../secgloss/r-gly.md) that uses a Windows API.
-   A [*user interface*](../secgloss/u-gly.md) (UI) that works with the resource manager.
-   Several base [*service providers*](../secgloss/s-gly.md) that provide access to specific services. In contrast to the resource manager's Windows API, service providers use a COM interface model to provide [*smart card*](../secgloss/s-gly.md) services.

The following illustration shows the relationships of these parts in the overall smart card architecture.

![smart card architecture](images/smartovr2a.png)

For information about how the [*smart card subsystem*](../secgloss/s-gly.md) works with other services available in the Microsoft Internet Security Framework, see [Relation to Other Services](relation-to-other-services.md).

For information about smart card authentication, see the following topics.



| Topics                                                                      | Contents                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Smart Card Concepts](smart-card-concepts.md)<br/>                   | Basic concepts and description of the interaction between users and smart cards.<br/>                                                                                                                                                        |
| [Smart Card Resource Manager](smart-card-resource-manager.md)<br/>   | Information about the resource manager API, which manages the access to [*readers*](../secgloss/r-gly.md) and to [*smart cards*](../secgloss/s-gly.md).<br/> |
| [Smart Card User Interface](smart-card-user-interface.md)<br/>       | Information about the [*smart card common dialog box*](../secgloss/s-gly.md).<br/>                                                                                   |
| [Smart Card Service Providers](smart-card-service-providers.md)<br/> | Information about interfaces, commands, and wrappers that provide smart card capabilities.<br/>                                                                                                                                              |



 

Additionally, current Microsoft smart card developments can be found at [https://www.microsoft.com/whdc/device/input/smartcard/default.mspx](https://www.microsoft.com/whdc/device/input/smartcard/default.mspx).

 

 
