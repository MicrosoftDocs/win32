---
title: Vector.String property
description: Retrieves a Vector of bytes as a String.
ms.assetid: e5ca70d1-1b50-4e48-9a0f-3678d4f2971d
keywords:
- String property WIA Automation
- String property WIA Automation , Vector object
- Vector object WIA Automation , String property
topic_type:
- apiref
api_name:
- Vector.String
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

# Vector.String property

Retrieves a [**Vector**](-wiaaut-vector.md) of bytes as a **String**.

This property is read-only.

## Syntax


```VB
Property String( _
  [ ByVal Unicode As VARIANT_BOOL ] _
)
```



## Property value

## Remarks

Because [**Vector**](-wiaaut-vector.md)s of bytes can actually be strings in either Unicode or ANSI form, this property provides an easy way to access the contents of **Vector**s that otherwise might be difficult to access or maintain.

For more information (and a common programming pitfall) about how to create a [**Vector**](-wiaaut-vector.md) of bytes, see the Remarks section of [**SetFromString**](-wiaaut-ivector-setfromstring.md).

For example code, see [Display Detailed Image Information](-wiaaut-shared-samples.md#display-detailed-image-information) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> </dl>

 

 





