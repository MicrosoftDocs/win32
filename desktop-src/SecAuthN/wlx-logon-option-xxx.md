---
description: Values are used by the dwOptions parameter of WlxLoggedOutSAS.
ms.assetid: a146427b-f3f1-4221-b2eb-ee7da451314a
title: WLX_LOGON_OPTION_XXX (Winwlx.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WLX\_LOGON\_OPTION\_XXX

\[The WLX\_LOGON\_OPTION\_XXX constant is no longer available for use as of Windows Server 2008 and Windows Vista.\]

The **WLX\_LOGON\_OPTION\_XXX** values are used by the *dwOptions* parameter of [**WlxLoggedOutSAS**](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedoutsas).

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

Upon a successful logon, your GINA DLL can use this value to specify the following option.



| Constant                                                                                                                                                                                          | Description                                                                                                                                                                      |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WLX_LOGON_OPT_NO_PROFILE"></span><span id="wlx_logon_opt_no_profile"></span><dl> <dt>**WLX\_LOGON\_OPT\_NO\_PROFILE**</dt> </dl> | Specifies that Winlogon must not load a profile for the logged-on user. In this case, either your GINA DLL will load the profile or the user does not need a profile.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| End of client support<br/>    | Windows XP<br/>                                                               |
| End of server support<br/>    | Windows Server 2003<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winwlx.h</dt> </dl> |



 

 




