---
title: Predefined List Attributes (TsAttrid.h)
description: The following values identify list attributes obtained with the ITfContext GetAppProperty method. The data format and contents of each property type are included.
ms.assetid: 9a9e1912-51c0-40e0-9e3a-b84ea7077dbe
keywords:
- Predefined List Attributes Text Services Framework
topic_type:
- apiref
api_name:
- Predefined List Attributes
api_location:
- TsAttrid.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Predefined List Attributes

The following values identify list attributes obtained with the [ITfContext::GetAppProperty](/windows/desktop/api/msctf/nf-msctf-itfcontext-getappproperty) method. The data format and contents of each property type are included.

## Properties



| Property                          | Description                                                                                     |
|-----------------------------------|-------------------------------------------------------------------------------------------------|
| TSATTRID\_List                    | Not used.                                                                                       |
| TSATTRID\_List\_LevelIndel        | Contains the index level of the list. 1 is the outermost level, 2 is the next level, and so on. |
| TSATTRID\_List\_Type              | Not used.                                                                                       |
| TSATTRID\_List\_Type\_Arabic      | Contains a nonzero value if the list is an arabic numeral list or zero otherwise.               |
| TSATTRID\_List\_Type\_Bullet      | Contains a nonzero value if the list is a bulleted list or zero otherwise.                      |
| TSATTRID\_List\_Type\_LowerLetter | Contains a nonzero value if the list is a lowercase lettered list or zero otherwise.            |
| TSATTRID\_List\_Type\_LowerRoman  | Contains a nonzero value if the list is a lowercase roman numeral list or zero otherwise.       |
| TSATTRID\_List\_Type\_UpperLetter | Contains a nonzero value if the list is an upper-case lettered list or zero otherwise.          |
| TSATTRID\_List\_Type\_UpperRoman  | Contains a nonzero value if the list is an uppercase roman numeral list or zero otherwise.      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                       |
| Header<br/>                   | <dl> <dt>TsAttrid.h</dt> </dl> |



## See also

<dl> <dt>

[ITfContext::GetAppProperty](/windows/desktop/api/msctf/nf-msctf-itfcontext-getappproperty)
</dt> </dl>

 

