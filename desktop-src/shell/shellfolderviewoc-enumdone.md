---
description: Indicates that the ShellFolderView object has finished enumerating the folder's contents.
title: ShellFolderViewOC.EnumDone event (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumDone
api_type: 
- DllExport
api_location: 
- Shell32.dll
ms.assetid: 7baa5f58-62c2-406e-a81e-4ca9c446a756
api_name: 
 - EnumDone
api_type: 
 - DllExport
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# ShellFolderViewOC.EnumDone event

Indicates that the [**ShellFolderView**](shellfolderview.md) object has finished enumerating the folder's contents.

## Syntax


```JScript
function EventHandler()
{
    // Code to handle the event.
}

// Set the event property to the handler.
ShellFolderViewOC.EnumDone = EventHandler;
```



## Parameters

This event handler has no parameters.

## Remarks

The [**ShellFolderView**](shellfolderview.md) object must enumerate the contents of a folder before it can display it. With folders that are large or located on a remote system, this process can take as much as several minutes. During this time, an animated flashlight graphic is displayed to indicate to the user that processing is under way. Once the enumeration is complete, the **EnumDone** event is fired and the flashlight graphic is replaced by the contents of the folder.

Provide event handling code for this event as shown here.


```
 
Private Sub object_EnumDone()
    'Event handling code
End Sub
                
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**ShellFolderViewOC**](shellfolderviewoc-object.md)
</dt> </dl>

 

 




