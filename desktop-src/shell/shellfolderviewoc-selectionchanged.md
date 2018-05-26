---
Description: Indicates that the selection state of one or more items in the view has changed.
title: ShellFolderViewOC.SelectionChanged event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ShellFolderViewOC.SelectionChanged event

Indicates that the selection state of one or more items in the view has changed.

## Syntax


```JScript
function EventHandler()
{
    // Code to handle the event.
}

// Set the event property to the handler.
ShellFolderViewOC.SelectionChanged = EventHandler;
```



## Parameters

This event handler has no parameters.

## Remarks

Provide event handling code for this event as shown here.


```
 
Private Sub object_SelectionChanged()
    'Event handling code
End Sub
                
```



## Requirements



|                                     |                                                                                                               |
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

 

 




