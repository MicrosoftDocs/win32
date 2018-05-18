---
Description: 'When Terminal Services are enabled, the GINA must call Winlogon support functions to complete the setup for each user, to query the credentials of a Terminal Services client session, and to disconnect from a Terminal Services network session.Note   GINA DLLs are ignored in Windows Vista. '
ms.assetid: '70b55b99-b350-4638-84ba-e5580d9d992f'
title: Terminal Services GINA Functions
---

# Terminal Services GINA Functions

When Terminal Services are enabled, the [*GINA*](security.g_gly#-security-gina-gly) must call [*Winlogon*](security.w_gly#-security-winlogon-gly) support functions to complete the setup for each user, to query the [*credentials*](security.c_gly#-security-credentials-gly) of a Terminal Services client session, and to disconnect from a Terminal Services network session.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

These support functions include the following.



| Function                                                                     | Description                                                                                         |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WlxWin31Migrate**](wlxwin31migrate.md)                                   | Completes the setup of the user.                                                                    |
| [**WlxQueryClientCredentials**](wlxqueryclientcredentials.md)               | Called to query the credentials of remote clients that are not using an Internet connector license. |
| [**WlxQueryInetConnectorCredentials**](wlxqueryinetconnectorcredentials.md) | Called to query the credentials of remote clients that are using an Internet connector license.     |
| [**WlxQueryTerminalServicesData**](wlxqueryterminalservicesdata.md)         | Called to retrieve Terminal Services user configuration information.                                |
| [**WlxDisconnect**](wlxdisconnect.md)                                       | Called to disconnect from a Terminal Services network session.                                      |



 

In order to access these Winlogon support functions, the GINA DLL must use the [**WLX\_DISPATCH\_VERSION\_1\_3**](wlx-dispatch-version-1-3.md) structure. In the GINA's [**WlxNegotiate**](wlxnegotiate.md) function, both parameters must be at least WLX\_VERSION\_1\_3.

 

 



