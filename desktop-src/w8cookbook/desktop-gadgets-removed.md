---
title: Desktop gadgets removed
description: Desktop gadgets removed
ms.assetid: 0074204B-F568-4F9B-A0F7-3E330B91E4CD
keywords:
- gadgets
- desktop gadgets
- Windows Sidebar
- Sidebar
ms.topic: article
ms.date: 05/31/2018
---

# Desktop gadgets removed

## Platforms

 **Clients** - Windows 8  
**Servers** - Windows Server 2012  



## Description

From a functionality standpoint, Gadgets have already been deprecated and are outclassed by new live tiles and apps. Gadgets also present a security risk to users. As a platform, vulnerabilities exist such that even benign Gadgets could be exploited. Therefore, in order to uphold Windows 8 as our most modern and secure operating system, we have chosen to remove Gadgets from the operating system entirely. Windows 7 users with Gadgets on their Desktop will be notified and Gadgets will be uninstalled.

## Manifestation

Desktop Gadgets will not be available on the Windows Desktop.

## Mitigation

The Desktop Gadgets API and folder structure will remain in place for Windows 8. Applications which programmatically install and run Gadgets using this API will continue to run without fail (although the Gadgets themselves will not).

## Solution

Desktop app developers should not package Gadgets in their installers. These Gadgets will just take up space for the user and will not be able to be run in the system.

## Tests

Developers are able to test compatibility of this change by disabling the optional component for Desktop Gadgets in Windows 7. To disable Gadgets on a Windows 7 PC, follow the steps below:

1.  Navigate to Turn Windows Features on or off from the Control Panel.
2.  Uncheck the box next to “Windows Gadget Platform”.
3.  Click OK and follow any additional on-screen instructions.

## Resources

[Vulnerabilities in Gadgets Could Allow Remote Code Execution](https://support.microsoft.com/kb/2719662)

 

 




