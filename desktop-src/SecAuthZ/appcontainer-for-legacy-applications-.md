---
description: The AppContainer environment is a restrictive process execution environment that can be used for legacy applications to provide resource security.
ms.assetid: 28498D4E-DCA4-4A85-B474-C3C328BD3022
title: AppContainer for Legacy Applications
ms.topic: article
ms.date: 05/31/2018
---

# AppContainer for Legacy Applications

The AppContainer environment is a restrictive process execution environment that can be used for legacy applications to provide resource security. An application running in an AppContainer can only access resources specifically granted to it. As a result, applications implemented in an AppContainer cannot be hacked to allow malicious actions outside of the limited assigned resources.

## Benefits of using an AppContainer environment

The AppContainer environment provides secure sandboxing of applications. This isolates the application from accessing hardware, files, registry, other applications, network connectivity, and network resources without specific permission. Individual resources may be targeted without exposing other resources. Additionally, user identity is protected by using a unique identity that is a concatenation of the user and the app and resources are granted using a least-privilege model. This further protects against an app impersonating the user to gain access to other resources.

For more information about using AppContainer for Legacy Applications, see the following topics.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AppContainer Isolation](appcontainer-isolation.md)<br/>             | Isolation is the primary goal of an AppContainer execution environment. By isolating an application from unneeded resources and other applications, opportunities for malicious manipulation are minimized. Granting access based upon least-privilege prevents applications and users from accessing resources beyond their rights. Controlling access to resources protects the process, the device, and the network.<br/> |
| [Implementing an AppContainer](implementing-an-appcontainer.md)<br/> | An AppContainer is implemented by adding new information to the process token, changing [**SeAccessCheck()**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-seaccesscheck) so that all legacy, unmodified access control list (ACL) objects block access requests from AppContainer processes by default, and re-ACL objects that should be available to AppContainers.<br/>                                                                                        |



 

 

