---
title: System.Shell.Item.invokeVerb method
description: Invokes a verb associated with the item.
ms.assetid: c44f0d49-1635-442c-b626-199789c59013
keywords:
- invokeVerb method Windows Sidebar
- invokeVerb method Windows Sidebar , System.Shell.Item object
- System.Shell.Item object Windows Sidebar , invokeVerb method
topic_type:
- apiref
api_name:
- System.Shell.Item.invokeVerb
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

# System.Shell.Item.invokeVerb method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Invokes a verb associated with the item.

## Syntax


```JScript
System.Shell.Item.invokeVerb(
  [ strVerb ]
)
```



## Parameters

<dl> <dt>

*strVerb* \[in, optional\]
</dt> <dd>

**String** that specifies a verb.

> [!Note]  
> The default verb is typically "open".

 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A verb is a string used to specify a particular action that an item supports. Invoking a verb is equivalent to selecting a command from an item's shortcut menu. Typically, invoking a verb launches a related application. For example, invoking the "open" verb on a .txt file opens the file with a text editor, usually Microsoft Notepad.

## Examples

The following example demonstrates how to invoke the "Properties" verb on an item, if requested.


```JScript
// --------------------------------------------------------------------
// Display the name of an object obtained from the UNC path and invoke
// an associated verb if requested.
// itemPath: the UNC path for the item.
// --------------------------------------------------------------------
function GetItemFromPath(itemPath)
{
    var oItem = System.Shell.itemFromPath(itemPath);
    // invoke: checkbox that indicates whether to invoke the verb.
    if (invoke.checked)
    {
        // Right-click and select from the list of available verbs 
        // for the item of interest.
        oItem.invokeVerb("Properties");
    }
    spFeedback.innerHTML = oItem.name + "<br/>";
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





