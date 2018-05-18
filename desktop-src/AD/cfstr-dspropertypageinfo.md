---
title: CFSTR\_DSPROPERTYPAGEINFO
description: The CFSTR\_DSPROPERTYPAGEINFO clipboard format provides an HGLOBAL that contains a DSPROPERTYPAGEINFO structure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '84ed1322-fee3-44ee-873e-57586261ff62'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSPROPERTYPAGEINFO
api_location:
- DSClient.h
api_type:
- HeaderDef
---

# CFSTR\_DSPROPERTYPAGEINFO

<dl> <dt>

<span id="CFSTR_DSPROPERTYPAGEINFO"></span><span id="cfstr_dspropertypageinfo"></span>**CFSTR\_DSPROPERTYPAGEINFO**
</dt> <dd> <dl> <dt>

"DsPropPageInfo"
</dt> <dt>



The **CFSTR\_DSPROPERTYPAGEINFO** clipboard format provides an **HGLOBAL** that contains a [**DSPROPERTYPAGEINFO**](dspropertypageinfo.md) structure. The **DSPROPERTYPAGEINFO** structure contains the optional string that the extension added to the **adminPropertySheet** and/or **shellPropertySheet** parameter values when the extension was registered. For more information about how this string is set, see [Registering the Property Page COM Object in a Display Specifier](registering-the-property-page-com-object-in-a-display-specifier.md).


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>DSClient.h</dt> </dl> |



## See also

<dl> <dt>

[**DSPROPERTYPAGEINFO**](dspropertypageinfo.md)
</dt> <dt>

[Registering the Property Page COM Object in a Display Specifier](registering-the-property-page-com-object-in-a-display-specifier.md)
</dt> </dl>

 

 





