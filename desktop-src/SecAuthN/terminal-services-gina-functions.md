---
description: When Terminal Services are enabled, the GINA must call Winlogon support functions to complete the setup for each user, to query the credentials of a Terminal Services client session, and to disconnect from a Terminal Services network session.Note   GINA DLLs are ignored in Windows Vista.
ms.assetid: 70b55b99-b350-4638-84ba-e5580d9d992f
title: Terminal Services GINA Functions
ms.topic: article
ms.date: 05/31/2018
---

# Terminal Services GINA Functions

When Terminal Services are enabled, the [*GINA*](../secgloss/g-gly.md) must call [*Winlogon*](../secgloss/w-gly.md) support functions to complete the setup for each user, to query the [*credentials*](../secgloss/c-gly.md) of a Terminal Services client session, and to disconnect from a Terminal Services network session.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

These support functions include the following.



| Function                                                                     | Description                                                                                         |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WlxWin31Migrate**](/windows/win32/api/winwlx/nc-winwlx-pwlx_win31_migrate)                                   | Completes the setup of the user.                                                                    |
| [**WlxQueryClientCredentials**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_client_credentials)               | Called to query the credentials of remote clients that are not using an Internet connector license. |
| [**WlxQueryInetConnectorCredentials**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_ic_credentials) | Called to query the credentials of remote clients that are using an Internet connector license.     |
| [**WlxQueryTerminalServicesData**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_terminal_services_data)         | Called to retrieve Terminal Services user configuration information.                                |
| [**WlxDisconnect**](/windows/win32/api/winwlx/nc-winwlx-pwlx_disconnect)                                       | Called to disconnect from a Terminal Services network session.                                      |



 

In order to access these Winlogon support functions, the GINA DLL must use the [**WLX\_DISPATCH\_VERSION\_1\_3**](/windows/desktop/api/Winwlx/ns-winwlx-wlx_dispatch_version_1_3) structure. In the GINA's [**WlxNegotiate**](/windows/desktop/api/Winwlx/nf-winwlx-wlxnegotiate) function, both parameters must be at least WLX\_VERSION\_1\_3.

 

 
