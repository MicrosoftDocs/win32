---
title: Disabling Remote Desktop Services features
description: For enhanced security, you might choose to disable Remote Desktop Services features.
ms.assetid: 93505e3a-a4f8-4b94-8dbb-646140b6fa58
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Disabling Remote Desktop Services features

For enhanced security, you might choose to disable Remote Desktop Services features such as clipboard redirection and printer redirection for clients that connect to Remote Desktop Session Host (RD Session Host) servers using the Remote Desktop ActiveX Control.

**To disable Remote Desktop Services features**

1.  Edit the registry of the client computer and add the following keys:

    -   **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Terminal Server Client\\DisableClipboardRedirection**
    -   **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Terminal Server Client\\DisableDriveRedirection**
    -   **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Terminal Server Client\\DisablePrinterRedirection**

2.  Set the value of both keys to **REG\_DWORD** 1.

 

 




