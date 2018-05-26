---
title: Property.SubTypeMax property
description: Retrieves the maximum valid Property value.
ms.assetid: ee22dec8-7673-4d9d-9ad5-913a1bd5aac5
keywords:
- SubTypeMax property WIA Automation
- SubTypeMax property WIA Automation , Property object
- Property object WIA Automation , SubTypeMax property
topic_type:
- apiref
api_name:
- Property.SubTypeMax
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Property.SubTypeMax property

Retrieves the maximum valid [**Property**](-wiaaut-property.md) value.

This property is read-only.

## Syntax


```VB
Property SubTypeMax( _
)
```



## Property value

Returns the maximum valid [**Property**](-wiaaut-property.md) value if the SubType is [**RangeSubType**](-wiaaut-wiasubtype.md), otherwise generates an error.

## Remarks

For example code, see [Display Detailed Property Information](-wiaaut-shared-samples.md#display-detailed-property-information) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Property**](-wiaaut-property.md)
</dt> </dl>

 

 





