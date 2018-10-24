---
Description: When Terminal Services are enabled, the GINA must call Winlogon support functions to complete the setup for each user, to query the credentials of a Terminal Services client session, and to disconnect from a Terminal Services network session.Note   GINA DLLs are ignored in Windows Vista. 
ms.assetid: 70b55b99-b350-4638-84ba-e5580d9d992f
title: Terminal Services GINA Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Terminal Services GINA Functions

When Terminal Services are enabled, the [*GINA*](https://msdn.microsoft.com/en-us/library/ms721584(v=VS.85).aspx) must call [*Winlogon*](https://msdn.microsoft.com/en-us/library/ms721635(v=VS.85).aspx) support functions to complete the setup for each user, to query the [*credentials*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) of a Terminal Services client session, and to disconnect from a Terminal Services network session.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

These support functions include the following.



| Function                                                                     | Description                                                                                         |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WlxWin31Migrate**](https://msdn.microsoft.com/en-us/library/Aa381090(v=VS.85).aspx)                                   | Completes the setup of the user.                                                                    |
| [**WlxQueryClientCredentials**](https://msdn.microsoft.com/en-us/library/Aa380576(v=VS.85).aspx)               | Called to query the credentials of remote clients that are not using an Internet connector license. |
| [**WlxQueryInetConnectorCredentials**](https://msdn.microsoft.com/en-us/library/Aa380578(v=VS.85).aspx) | Called to query the credentials of remote clients that are using an Internet connector license.     |
| [**WlxQueryTerminalServicesData**](https://msdn.microsoft.com/en-us/library/Aa380579(v=VS.85).aspx)         | Called to retrieve Terminal Services user configuration information.                                |
| [**WlxDisconnect**](https://msdn.microsoft.com/en-us/library/Aa380559(v=VS.85).aspx)                                       | Called to disconnect from a Terminal Services network session.                                      |



 

In order to access these Winlogon support functions, the GINA DLL must use the [**WLX\_DISPATCH\_VERSION\_1\_3**](/windows/desktop/api/Winwlx/ns-winwlx-_wlx_dispatch_version_1_3) structure. In the GINA's [**WlxNegotiate**](/windows/desktop/api/Winwlx/nf-winwlx-wlxnegotiate) function, both parameters must be at least WLX\_VERSION\_1\_3.

 

 



