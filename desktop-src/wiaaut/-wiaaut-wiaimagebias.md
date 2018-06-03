---
title: WiaImageBias enumeration
description: Helps specify what type of data the image is intended to represent.
ms.assetid: e592b98f-585e-4a71-bc63-96036703ab23
keywords:
- WiaImageBias enumeration WIA Automation
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

# WiaImageBias enumeration

Helps specify what type of data the image is intended to represent.

## Members



| Member              | Description                                                                                   | Value  |
|---------------------|-----------------------------------------------------------------------------------------------|--------|
| **MinimizeSize**    | Use a lower quality scan to minimize the size of the file that contains the image.<br/> | 65536  |
| **MaximizeQuality** | Use a higher quality scan to maximize the quality of the image.<br/>                    | 131072 |



## Remarks

The Bias parameter for both the [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md) and [**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md) methods can have a value from the **WiaImageBias** enumeration.

The following example shows how to call the [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md) method with the **MaximizeQuality** bias value.


```
Dim Img 'As ImageFile

Set Img = CommonDialog1.ShowAcquireImage(UnspecifiedDeviceType, _
                                         UnspecifiedIntent, _
                                         MaximizeQuality, _
                                         wiaFormatJPEG)
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





