---
Description: Smart Card Authentication
ms.assetid: 'cb5c80ea-c15e-4f68-a94b-b458d69ff474'
title: Smart Card Authentication
---

# Smart Card Authentication

The basic parts of the [*smart card subsystem*](security.s_gly#-security-smart-card-subsystem-gly) are based on PC/SC standards (see the specifications at [http://www.pcscworkgroup.com/](http://go.microsoft.com/fwlink/p/?linkid=84156)). These basic parts include:

-   A [*resource manager*](security.r_gly#-security-resource-manager-gly) that uses a Windows API.
-   A [*user interface*](security.u_gly#-security-user-interface-smart-card-gly) (UI) that works with the resource manager.
-   Several base [*service providers*](security.s_gly#-security-service-provider-smart-card--gly) that provide access to specific services. In contrast to the resource manager's Windows API, service providers use a COM interface model to provide [*smart card*](security.s_gly#-security-smart-card-gly) services.

The following illustration shows the relationships of these parts in the overall smart card architecture.

![smart card architecture](images/smartovr2a.png)

For information about how the [*smart card subsystem*](security.s_gly#-security-smart-card-subsystem-gly) works with other services available in the Microsoft Internet Security Framework, see [Relation to Other Services](relation-to-other-services.md).

For information about smart card authentication, see the following topics.



| Topics                                                                      | Contents                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Smart Card Concepts](smart-card-concepts.md)<br/>                   | Basic concepts and description of the interaction between users and smart cards.<br/>                                                                                                                                                        |
| [Smart Card Resource Manager](smart-card-resource-manager.md)<br/>   | Information about the resource manager API, which manages the access to [*readers*](security.r_gly#-security-reader-gly) and to [*smart cards*](security.s_gly#-security-smart-card-gly).<br/> |
| [Smart Card User Interface](smart-card-user-interface.md)<br/>       | Information about the [*smart card common dialog box*](security.s_gly#-security-smart-card-common-dialog-gly).<br/>                                                                                   |
| [Smart Card Service Providers](smart-card-service-providers.md)<br/> | Information about interfaces, commands, and wrappers that provide smart card capabilities.<br/>                                                                                                                                              |



 

Additionally, current Microsoft smart card developments can be found at [http://www.microsoft.com/whdc/device/input/smartcard/default.mspx](http://go.microsoft.com/fwlink/p/?linkid=84133).

 

 




