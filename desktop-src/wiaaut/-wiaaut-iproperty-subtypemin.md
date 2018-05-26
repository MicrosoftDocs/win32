---
title: Property.SubTypeMin property
description: Retrieves the minimum valid Property value.
ms.assetid: 97d7db69-e7d7-4ff3-8f2d-f2d68963c4c4
keywords:
- SubTypeMin property WIA Automation
- SubTypeMin property WIA Automation , Property object
- Property object WIA Automation , SubTypeMin property
topic_type:
- apiref
api_name:
- Property.SubTypeMin
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

# Property.SubTypeMin property

Retrieves the minimum valid [**Property**](-wiaaut-property.md) value.

This property is read-only.

## Syntax


```VB
Property SubTypeMin( _
)
```



## Property value

Returns the minimum valid [**Property**](-wiaaut-property.md) value if the SubType is [**RangeSubType**](-wiaaut-wiasubtype.md), otherwise generates an error.

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

 

 





