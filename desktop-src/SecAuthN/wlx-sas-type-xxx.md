---
description: Values define a specific SAS type.
ms.assetid: c0a1269b-f9d4-49e1-89ca-526fef148134
title: WLX_SAS_TYPE_XXX (Winwlx.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WLX\_SAS\_TYPE\_XXX

\[The WLX\_SAS\_TYPE\_XXX constant is no longer available for use as of Windows Server 2008 and Windows Vista.\]

The **WLX\_SAS\_TYPE\_XXX** values define a specific SAS type.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

All values from zero to 127 are reserved for Microsoft-defined types. Values above 127 are available for customer-defined types. The following types are passed to functions that have a *dwSasType* parameter.



| Constant                                                                                                                                                                                                         | Description                                                                                                                                              |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WLX_SAS_TYPE_CTRL_ALT_DEL"></span><span id="wlx_sas_type_ctrl_alt_del"></span><dl> <dt>**WLX\_SAS\_TYPE\_CTRL\_ALT\_DEL**</dt> </dl>            | Indicates a user has typed the standard CTRL+ALT+DEL SAS.<br/>                                                                                     |
| <span id="WLX_SAS_TYPE_SC_INSERT"></span><span id="wlx_sas_type_sc_insert"></span><dl> <dt>**WLX\_SAS\_TYPE\_SC\_INSERT**</dt> </dl>                      | Indicates that a [*smart card*](../secgloss/s-gly.md) has been inserted into a compatible device.<br/> |
| <span id="WLX_SAS_TYPE_SC_REMOVE"></span><span id="wlx_sas_type_sc_remove"></span><dl> <dt>**WLX\_SAS\_TYPE\_SC\_REMOVE**</dt> </dl>                      | Indicates that a smart card has been removed from a compatible device.<br/>                                                                        |
| <span id="WLX_SAS_TYPE_SCRNSVR_ACTIVITY"></span><span id="wlx_sas_type_scrnsvr_activity"></span><dl> <dt>**WLX\_SAS\_TYPE\_SCRNSVR\_ACTIVITY**</dt> </dl> | Indicates that keyboard or mouse activity occurred while a secure screen saver was active.<br/>                                                    |
| <span id="WLX_SAS_TYPE_SCRNSVR_TIMEOUT"></span><span id="wlx_sas_type_scrnsvr_timeout"></span><dl> <dt>**WLX\_SAS\_TYPE\_SCRNSVR\_TIMEOUT**</dt> </dl>    | Indicates that screen saver activation has occurred due to keyboard and mouse inactivity.<br/>                                                     |
| <span id="WLX_SAS_TYPE_TIMEOUT"></span><span id="wlx_sas_type_timeout"></span><dl> <dt>**WLX\_SAS\_TYPE\_TIMEOUT**</dt> </dl>                             | Indicates that no user input was received within the specified time-out period.<br/>                                                               |
| <span id="WLX_SAS_TYPE_USER_LOGOFF"></span><span id="wlx_sas_type_user_logoff"></span><dl> <dt>**WLX\_SAS\_TYPE\_USER\_LOGOFF**</dt> </dl>                | Indicates the user is being logged off the system.<br/>                                                                                            |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| End of client support<br/>    | Windows XP<br/>                                                               |
| End of server support<br/>    | Windows Server 2003<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winwlx.h</dt> </dl> |



 

 
