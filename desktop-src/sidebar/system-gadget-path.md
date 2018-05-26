---
title: System.Gadget.path property
description: Gets the Universal Naming Convention (UNC) location of the gadget source files.
ms.assetid: a57a0f18-0c10-4fa7-bc2b-355f2549a761
keywords:
- path property Windows Sidebar
- path property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , path property
topic_type:
- apiref
api_name:
- System.Gadget.path
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

# System.Gadget.path property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Universal Naming Convention (UNC) location of the gadget source files.

This property is read-only.

## Syntax


```JScript
strpath = System.Gadget.path
```



## Property value

A **String** that receives the UNC location.

## Remarks

Useful for referring to files within the gadget file structure.

## Examples

The following example demonstrates how to play an ASX file from a gadget.


```JScript
// mediaPlayer is the id of the Media Player object.
function StartPlayer()
{
    mediaPlayer.url = System.Gadget.path + "\\mediafile.asx"; 
    mediaPlayer.controls.play();
}

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

[**System.Gadget**](system-gadget.md)
</dt> </dl>

 

 





