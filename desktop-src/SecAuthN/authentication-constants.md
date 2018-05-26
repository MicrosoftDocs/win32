---
Description: Lists the constants used for Microsoft authentication APIs.
ms.assetid: 3e5b7fd8-01bf-4090-b68f-006b7e2228a9
title: Authentication Constants
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Authentication Constants

## Credentials Management Constants

Credentials Management uses the following constants to specify maximum string sizes.



| Constant                                        | Description                                                                                                                   |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| CREDUI\_MAX\_MESSAGE\_LENGTH<br/>         | Maximum number of characters for the **pszMessageText** member of a [**CREDUI\_INFO**](/windows/win32/WinCred/ns-wincred-_credui_infoa?branch=master) structure.<br/> |
| CREDUI\_MAX\_CAPTION\_LENGTH<br/>         | Maximum number of characters for the **pszCaptionText** member of a [**CREDUI\_INFO**](/windows/win32/WinCred/ns-wincred-_credui_infoa?branch=master) structure.<br/> |
| CREDUI\_MAX\_GENERIC\_TARGET\_LENGTH<br/> | Maximum number of characters in a string that specifies a target name.<br/>                                             |
| CREDUI\_MAX\_DOMAIN\_TARGET\_LENGTH<br/>  | Maximum number of characters in a string that specifies a domain name.<br/>                                             |
| CREDUI\_MAX\_USERNAME\_LENGTH<br/>        | Maximum number of characters in a string that specifies a user account name.<br/>                                       |
| CREDUI\_MAX\_PASSWORD\_LENGTH<br/>        | Maximum number of characters in a string that specifies a password.<br/>                                                |



 

## Gina Defined Values

[*GINA*](https://msdn.microsoft.com/library/windows/desktop/ms721584#-security-gina-gly) interface functions and [*Winlogon*](https://msdn.microsoft.com/library/windows/desktop/ms721635#-security-winlogon-gly) support functions use the following defined values.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 



| Value                                                              | Description                                                                                                                          |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**WLX\_LOGON\_OPTION\_XXX**](wlx-logon-option-xxx.md)<br/> | Contains predefined logon options. It is used by the *dwOptions* parameter of [**WlxLoggedOutSAS**](/windows/win32/Winwlx/nf-winwlx-wlxloggedoutsas?branch=master).<br/> |
| [**WLX\_SAS\_TYPE\_XXX**](wlx-sas-type-xxx.md)<br/>         | Defines a specific SAS type.<br/>                                                                                              |



 

 

 




