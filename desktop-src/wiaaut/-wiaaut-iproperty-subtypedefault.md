---
title: Property.SubTypeDefault property
description: Retrieves the default Property value.
ms.assetid: b42d319d-e5b5-4e19-b735-89e2c0c0f6ed
keywords:
- SubTypeDefault property WIA Automation
- SubTypeDefault property WIA Automation , Property object
- Property object WIA Automation , SubTypeDefault property
topic_type:
- apiref
api_name:
- Property.SubTypeDefault
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

# Property.SubTypeDefault property

Retrieves the default [**Property**](-wiaaut-property.md) value.

This property is read-only.

## Syntax


```VB
Property SubTypeDefault( _
)
```



## Property value

Returns the default [**Property**](-wiaaut-property.md) value if the SubType is not [**UnspecifiedSubType**](-wiaaut-wiasubtype.md), otherwise generates an error.

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

 

 





