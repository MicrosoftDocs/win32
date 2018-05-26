---
Description: The WMI policy provider provides extensions to group policy through classes, permitting refinements in the application of policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d4d4fd2-ecd0-4546-b919-1e75199a403c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Policy Provider Classes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Policy Provider Classes

The WMI policy provider provides extensions to group policy through classes, permitting refinements in the application of policy. Policy is set using the WMI Query Language (WQL) and resides in the Active Directory for easy deployment.

The following table lists the classes for the WMI policy provider.



| Class                                               | Description                                                       |
|-----------------------------------------------------|-------------------------------------------------------------------|
| [**MSFT\_Providers**](https://msdn.microsoft.com/library/aa392509) | Exposes configuration relating to provider instances.             |
| [**MSFT\_Rule**](https://msdn.microsoft.com/library/aa392510)                | Defines a single rule within a Scope of Management (SOM).         |
| [**MSFT\_SomFilter**](https://msdn.microsoft.com/library/aa392511)      | Provides a list of rules which are evaluated on a target machine. |



 

 

 



