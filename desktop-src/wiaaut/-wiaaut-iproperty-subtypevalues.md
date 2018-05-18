---
title: Property.SubTypeValues property
description: Retrieves a Vector of valid Property values or valid flag values.
ms.assetid: '464d9cb2-15a7-4671-aab2-8c063ae80037'
keywords: ["SubTypeValues property WIA Automation", "SubTypeValues property WIA Automation , Property object", "Property object WIA Automation , SubTypeValues property"]
topic_type:
- apiref
api_name:
- Property.SubTypeValues
api_location:
- Wiaaut.h
api_type:
- COM
---

# Property.SubTypeValues property

Retrieves a [**Vector**](-wiaaut-vector.md) of valid [**Property**](-wiaaut-property.md) values or valid flag values.

This property is read-only.

## Syntax


```VB
Property SubTypeValues( _
)
```



## Property value

Returns a [**Vector**](-wiaaut-vector.md) of valid [**Property**](-wiaaut-property.md) values if the SubType is [**ListSubType**](-wiaaut-wiasubtype.md), or it returns valid flag values that can be combined using the OR operation if the SubType is **FlagSubType**, otherwise generates an error.

## Remarks

For example code, see [Display Detailed Property Information](-wiaaut-shared-samples.md#display-detailed-property-information) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Property**](-wiaaut-property.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**ARGBData**](-wiaaut-iimagefile-argbdata.md)
</dt> <dt>

[**FileData**](-wiaaut-iimagefile-filedata.md)
</dt> </dl>

 

 





