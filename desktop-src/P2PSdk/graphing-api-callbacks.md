---
Description: The Graphing API uses the following callbacks
ms.assetid: a8e083ab-b5e3-4186-99fb-cbb536e9d529
title: Graphing API Callbacks
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Graphing API Callbacks

The Graphing API uses the following callbacks:



| Callback                                                          | Description                                                                                                                                                                                                                  |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*PFNPEER\_FREE\_SECURITY\_DATA*](/windows/win32/P2P/nc-p2p-pfnpeer_free_security_data?branch=master) | Specifies the function that the Peer Graphing Infrastructure calls to free data returned by [*PFNPEER\_SECURE\_RECORD*](/windows/win32/P2P/nc-p2p-pfnpeer_secure_record?branch=master) and [*PFNPEER\_VALIDATE\_RECORD*](/windows/win32/P2P/nc-p2p-pfnpeer_validate_record?branch=master) callbacks. |
| [*PFNPEER\_SECURE\_RECORD*](/windows/win32/P2P/nc-p2p-pfnpeer_secure_record?branch=master)            | Specifies the function that the Peer Graphing Infrastructure calls to secure records.                                                                                                                                        |
| [*PFNPEER\_VALIDATE\_RECORD*](/windows/win32/P2P/nc-p2p-pfnpeer_validate_record?branch=master)        | Specifies the function that the Peer Graphing Infrastructure calls to validate records.                                                                                                                                      |



 

 

 



