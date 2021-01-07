---
description: Lists the constants used for Microsoft authentication APIs.
ms.assetid: 3e5b7fd8-01bf-4090-b68f-006b7e2228a9
title: Authentication Constants (Authentication)
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Constants (Authentication)

## Credentials Management Constants

Credentials Management uses the following constants to specify maximum string sizes.



| Constant                                        | Description                                                                                                                   |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| CREDUI\_MAX\_MESSAGE\_LENGTH<br/>         | Maximum number of characters for the **pszMessageText** member of a [**CREDUI\_INFO**](/windows/desktop/api/WinCred/ns-wincred-credui_infoa) structure.<br/> |
| CREDUI\_MAX\_CAPTION\_LENGTH<br/>         | Maximum number of characters for the **pszCaptionText** member of a [**CREDUI\_INFO**](/windows/desktop/api/WinCred/ns-wincred-credui_infoa) structure.<br/> |
| CREDUI\_MAX\_GENERIC\_TARGET\_LENGTH<br/> | Maximum number of characters in a string that specifies a target name.<br/>                                             |
| CREDUI\_MAX\_DOMAIN\_TARGET\_LENGTH<br/>  | Maximum number of characters in a string that specifies a domain name.<br/>                                             |
| CREDUI\_MAX\_USERNAME\_LENGTH<br/>        | Maximum number of characters in a string that specifies a user account name.<br/>                                       |
| CREDUI\_MAX\_PASSWORD\_LENGTH<br/>        | Maximum number of characters in a string that specifies a password.<br/>                                                |



 

## Gina Defined Values

[*GINA*](/windows/desktop/SecGloss/g-gly) interface functions and [*Winlogon*](/windows/desktop/SecGloss/w-gly) support functions use the following defined values.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 



| Value                                                              | Description                                                                                                                          |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**WLX\_LOGON\_OPTION\_XXX**](wlx-logon-option-xxx.md)<br/> | Contains predefined logon options. It is used by the *dwOptions* parameter of [**WlxLoggedOutSAS**](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedoutsas).<br/> |
| [**WLX\_SAS\_TYPE\_XXX**](wlx-sas-type-xxx.md)<br/>         | Defines a specific SAS type.<br/>                                                                                              |



 

 

