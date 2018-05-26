---
title: ImageFile.FileData property
description: Retrieves the raw image file as a Vector of bytes.
ms.assetid: 41fa23a3-5d50-41d9-b166-227f5671a1f3
keywords:
- FileData property WIA Automation
- FileData property WIA Automation , ImageFile object
- ImageFile object WIA Automation , FileData property
topic_type:
- apiref
api_name:
- ImageFile.FileData
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

# ImageFile.FileData property

Retrieves the raw image file as a [**Vector**](-wiaaut-vector.md) of bytes.

This property is read-only.

## Syntax


```VB
Property FileData( _
)
```



## Property value

[**Vector**](-wiaaut-vector.md) value.

## Remarks

This property copies the file into the [**Vector**](-wiaaut-vector.md). The [**ActiveFrame**](-wiaaut-iimagefile-activeframe.md) property has no effect on the copy of the file.

For example code, see [Download New Items as They are Created](-wiaaut-shared-samples.md#download-new-items-as-they-are-created) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ImageFile**](-wiaaut-imagefile.md)
</dt> <dt>

[**ARGBData**](-wiaaut-iimagefile-argbdata.md)
</dt> <dt>

[**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md)
</dt> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> </dl>

 

 





