---
title: WiaImageIntent enumeration
description: Helps specify what type of data the image is intended to represent.
ms.assetid: ef68ec41-7ee3-4be1-9d53-42e4966e7d25
keywords:
- WiaImageIntent enumeration WIA Automation
- WiaDeviceType enumeration WIA Automation
topic_type:
- apiref
api_name:
- WiaDeviceType
api_location:
- Wiaaut.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# WiaImageIntent enumeration

Helps specify what type of data the image is intended to represent.

## Members



| Member                | Description                                                             | Value |
|-----------------------|-------------------------------------------------------------------------|-------|
| **UnspecifiedIntent** | No intent specified.<br/>                                         | 0     |
| **ColorIntent**       | The image is a color illustration.<br/>                           | 1     |
| **GrayscaleIntent**   | The image is grayscale data.<br/>                                 | 2     |
| **TextIntent**        | The image is a text image such as a fax or scanned document.<br/> | 4     |



## Remarks

The Intent parameter for both the [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md) and [**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md) methods can have a value from the **WiaImageIntent** enumeration.

The following example shows how to call the [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md) method with the TextIntent value.


```
Dim Img 'As ImageFile

Set Img = CommonDialog1.ShowAcquireImage(UnspecifiedDeviceType, _
                                         TextIntent, _
                                         MaximizeQuality, _
                                         wiaFormatTIFF)
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





