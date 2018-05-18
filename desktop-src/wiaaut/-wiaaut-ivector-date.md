---
title: Vector.Date property
description: Sets or retrieves the Vector of integers from a date.
ms.assetid: '0059cee2-c60d-438c-ab03-67a99cec7e09'
keywords: ["Date property WIA Automation", "Date property WIA Automation , Vector object", "Vector object WIA Automation , Date property"]
topic_type:
- apiref
api_name:
- Vector.Date
api_location:
- Wiaaut.h
api_type:
- COM
---

# Vector.Date property

Sets or retrieves the [**Vector**](-wiaaut-vector.md) of integers from a date.

This property is read/write.

## Syntax


```VB
Property Date( _
)
```



## Property value

Date value.

## Remarks

Several [**Device**](-wiaaut-device.md) and [**Item**](-wiaaut-item.md) objects have properties that contain dates and times stored as a [**Vector**](-wiaaut-vector.md) of unsigned integers containing eight elements. Since this is very common, the Windows Image Acquisition (WIA) Automation Library provides the Date property on a **Item** so the Microsoft Visual Basic Programmer can access these special vectors as date types.

For example code, see [Enumerate Root Level Items and Display Their Names](-wiaaut-shared-samples.md#enumerate-root-level-items-and-display-their-names) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> </dl>

 

 





