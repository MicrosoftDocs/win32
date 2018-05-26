---
title: background.opacity property
description: Gets or sets the opacity of the g background element.
ms.assetid: c7fbdb06-6342-44af-b6a1-7a06f1d50df8
keywords:
- opacity property Windows Sidebar
- opacity property Windows Sidebar , background object
- background object Windows Sidebar , opacity property
topic_type:
- apiref
api_name:
- background.opacity
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

# background.opacity property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the opacity of the [**g:background**](background-element.md) element.

This property is read/write.

## Syntax


```JScript
iopacity = background.opacity
background.opacity = iopacity
```



## Property value

An **Integer** that specifies or receives the opacity of the target element. The value ranges from `0` to `100`.

<dt>



 (0)


</dt> <dd>

The target element is completely transparent.

</dd> <dt>



 (100)


</dt> <dd>

Default. The target element is completely opaque.

</dd> </dl>

## Remarks

The opacity can be specified in the gadget HTML and script files.

## Examples

The following example demonstrates how to set the opacity of the [**g:background**](background-element.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
imgBackground.opacity = 0;
```



The following example demonstrates how to set the opacity of the [**g:background**](background-element.md) element in the gadget HTML file.


```JScript
<g:background 
        id="imgBackground" 
        src="images/background.png" 
        opacity="100">
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

 

 





