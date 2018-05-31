---
Description: The Fax Service Client API allows you to incorporate basic fax functionality for users in client applications. This technology is available on computers that are running Windows 2000 and later.
ms.assetid: cbc79dc5-d0ca-418d-8572-64b0a582056f
title: Fax Service Client API for Windows 2000
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Service Client API for Windows 2000

The Fax Service Client API allows you to incorporate basic fax functionality for users in client applications. This technology is available on computers that are running Windows 2000 and later.

The fax service for Windows XP introduces the [Fax Service Extended COM implementation](-mfax-about-the-fax-service-extended-com-api.md) objects. New fax features are supported in the Fax Service Extended Component Object Model (COM) API, not in the Fax Service Client API for Windows 2000. New fax client applications should use the extended COM interfaces rather than the C/C++ functions or COM interfaces that shipped with the Windows 2000 Windows Software Development Kit (SDK).

The Fax Service Client API for Windows 2000 includes both Microsoft Win32 functions and an implementation of COM dual interfaces.

## About this overview

The first part of this overview outlines the tasks an application can perform using the Fax Service Client API, and the components you need to support its functionality. It also describes in detail the security features the fax service provides. Finally, it provides a brief discussion about fax ports, fax transmissions, cover pages, and fax routing methods.

The second section addresses differences between fax client applications that run in the Win32 environment and those that run in the COM implementation environment. It also discusses the fax service client functions, the COM dual interfaces, and the following related programming tasks:

-   [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md)
-   [Fax Server Configuration Management](-mfax-fax-server-configuration-management.md)
-   [Fax Device Management](-mfax-fax-device-management.md)
-   [Managing Fax Routing Data](-mfax-managing-fax-routing-data.md)
-   [Transmitting Faxes](-mfax-transmitting-faxes.md)
-   [Managing Fax Jobs](-mfax-managing-fax-jobs.md)
-   [Freeing Fax Resources](-mfax-freeing-fax-resources.md)
-   [Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md)

For more information, see [Fax Client API Programming Tasks](-mfax-fax-client-api-programming-tasks.md) and the [Fax Service Client API Reference](-mfax-fax-service-client-api-reference.md).

You should be familiar with the *Telephony Application Programming Interface (TAPI) Programmer's Reference* and the *Microsoft Telephony Service Provider (TSPI) Programmer's Reference* before you read this overview. If you plan to use the fax client COM implementation, you should also be familiar with COM (the Component Object Model) and Automation programming concepts.

 

 



