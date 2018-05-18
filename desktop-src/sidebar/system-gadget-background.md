---
title: System.Gadget.background property
description: Gets or sets the file path for the gadget background image.
ms.assetid: '8a14bd7f-5f25-4b7e-aae2-d41a38fc3aa6'
keywords: ["background property Windows Sidebar", "background property Windows Sidebar , System.Gadget object", "System.Gadget object Windows Sidebar , background property"]
topic_type:
- apiref
api_name:
- System.Gadget.background
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.background property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the file path for the gadget background image.

This property is read/write.

## Syntax


```JScript
strbackground = System.Gadget.background
System.Gadget.background = strbackground
```



## Property value

A **String** that specifies or receives a UNC path or a URI.

## Remarks

The **background** property is initialized by the [**g:background**](background-element.md) element in the gadget HTML file.

The **background** property should be modified after the gadget has finished loading.

> [!Note]  
> It is recommended that the [**src**](src-attribute-gbackground.md) property be used instead of the **background** property if the script is located within the `body` tags of the gadget HTML file. The System.Gadget object is not guaranteed to exist in these cases.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

[**System.Gadget**](system-gadget.md)
</dt> </dl>

 

 





