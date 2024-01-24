---
description: This per-machine system policy can be used to specify that the Windows Installer pass all public properties to the server side during a managed installation using elevated privileges.
ms.assetid: 437ceef2-730f-47ae-9b1f-dfc7c6d2d132
title: EnableUserControl
ms.topic: article
ms.date: 05/31/2018
---

# EnableUserControl

In the case of a managed installation, the package author may need to limit which public properties are passed to the server side and can be changed by a user that is not a system administrator. Some restrictions are commonly necessary to maintain a secure environment when the installation requires the installer to use elevated privileges.

If this per-machine [system policy](system-policy.md) is set to "1", then the installer can pass all [public properties](public-properties.md) to the server side during a managed installation using elevated privileges. Setting this policy has the same effect as setting the **EnableUserControl** property. Setting this policy allows all public properties to be passed to the service and to be changeable by nonadministrative users. By default, this policy is not enabled; only restricted public properties are passed to the server side and changeable by a nonadministrative user. All other public properties are ignored.

If the operating system is Windows 2000, the user is not a system administrator, and the application or product is being installed with elevated privileges, then a user that is not a system administrator can only override an approved list of restricted public properties. For more information see [Restricted Public Properties](restricted-public-properties.md).

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

 

 



