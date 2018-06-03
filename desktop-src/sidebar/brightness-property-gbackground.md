---
title: background.brightness property
description: Gets or sets the brightness of the g background element.
ms.assetid: 0f0a2dc8-4ebb-4bb5-830d-6bc41c598941
keywords:
- brightness property Windows Sidebar
- brightness property Windows Sidebar , background object
- background object Windows Sidebar , brightness property
topic_type:
- apiref
api_name:
- background.brightness
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# background.brightness property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the brightness of the [**g:background**](background-element.md) element.

This property is read/write.

## Syntax


```JScript
brightness = background.brightness
background.brightness = brightness
```



## Property value

A **Floating-point** that specifies or receives the "white" level applied to the target element. The value ranges from `0.0` to `100.0`.

<dt>



 (0.0)


</dt> <dd>

Default. No brightness effect applied. The target element is not modified.

</dd> <dt>



 (1.0)


</dt> <dd>

Brightness effect of 100%. The target element has no detail, color, or contrast; it is opaque but effectively blank (white).

</dd> <dt>



 (100.0)


</dt> <dd>

Brightness effect of 1%.

</dd> </dl>

## Remarks

The brightness effect can be specified in the gadget HTML and script files.

The opacity of the [**g:background**](background-element.md) element must be set to a value of at least 1 for the brightness effect to be visible.

## Examples

The following example demonstrates how to add a brightness effect to the [**g:background**](background-element.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
imgBackground.brightness = 1.0;
```



The following example demonstrates how to add a brightness effect to the [**g:background**](background-element.md) element in the gadget HTML file.


```JScript
<g:background 
        id="imgBackground" 
        src="images/background.png" 
        opacity="100" brightness="1.0">
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

 

 





