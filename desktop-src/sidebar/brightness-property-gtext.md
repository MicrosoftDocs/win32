---
title: text.brightness property
description: Gets or sets the brightness of the g text element.
ms.assetid: baa02afe-6cd8-499b-b8df-5f713f16b00c
keywords:
- brightness property Windows Sidebar
- brightness property Windows Sidebar , text object
- text object Windows Sidebar , brightness property
topic_type:
- apiref
api_name:
- text.brightness
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# text.brightness property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the brightness of the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
brightness = text.brightness
text.brightness = brightness
```



## Property value

A **Floating-point** that specifies or receives the "white" level applied to the target element. The value ranges from `0.0` to `100.0`.

<dt>



 (0.0)


</dt> <dd>

Default. No brightness effect applied. Text is not modified.

</dd> <dt>



 (1.0)


</dt> <dd>

Brightness effect of 100%. Text has no color, or contrast; it is opaque but effectively blank (white).

</dd> <dt>



 (100.0)


</dt> <dd>

Brightness effect of 1%.

</dd> </dl>

## Remarks

The opacity of the [**g:text**](gtext.md) element must be set to a value of at least 1 for the brightness effect to be visible.

## Examples

The following example demonstrates how to add a brightness effect to the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtBrightness = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtBrightness.brightness = 1.0;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**background**](background-element.md)
</dt> <dt>

[**image**](image-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





