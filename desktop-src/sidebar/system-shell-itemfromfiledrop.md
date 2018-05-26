---
title: System.Shell.itemFromFileDrop method
description: Retrieves an System.Shell.Item from the Items collection that represents the object(s) dropped on a gadget during a drag-and-drop operation (copying or moving).
ms.assetid: 5bb3ab91-3ad7-4ee5-ac92-4dc5ca083597
keywords:
- itemFromFileDrop method Windows Sidebar
- itemFromFileDrop method Windows Sidebar , System.Shell object
- System.Shell object Windows Sidebar , itemFromFileDrop method
topic_type:
- apiref
api_name:
- System.Shell.itemFromFileDrop
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

# System.Shell.itemFromFileDrop method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves an [**System.Shell.Item**](system-shell-item.md) from the [**Items**](system-shell-folder-items.md) collection that represents the object(s) dropped on a gadget during a drag-and-drop operation (copying or moving).

## Syntax


```JScript
retVal = System.Shell.itemFromFileDrop(
  oEvent,
  intIndex
)
```



## Parameters

<dl> <dt>

*oEvent* \[in\]
</dt> <dd>

**Object** that specifies the event.dataTransfer object.

</dd> <dt>

*intIndex* \[in\]
</dt> <dd>

**Integer** that specifies the index of the [**System.Shell.Item**](system-shell-item.md) of interest in the [**Items**](system-shell-folder-items.md) collection.

</dd> </dl>

## Return value

[**System.Shell.Item**](system-shell-item.md) object that represents the specified item, or null if the item cannot be determined.

## Remarks

To enable listening for the drag and drop event, both `ondragenter` and `ondragover` events must be disabled in the `<body>` tag of the gadget HTML file (see example).

## Examples

The following example demonstrates how to display the names of files dropped on the gadget.


```JScript
<!-- Gadget HTML file. -->
<body onload="Init();" 
ondragenter="event.returnValue = false"
ondragover="event.returnValue = false"
ondrop="GetItemFromDrop()">
    <div id="gadgetContent">
        <span id="spFeedback">Nothing to report.</span>
    </div>
</body>
</html>

<!-- Gadget script file. -->
// --------------------------------------------------------------------
// Display the names of objects dropped on the gadget.
// --------------------------------------------------------------------
function GetItemFromDrop()
{
    spFeedback.innerHTML = "File(s) dropped.<br/>";
    var intIndex = 0;
    var oItem;
    while(oItem = System.Shell.itemFromFileDrop(event.dataTransfer, intIndex))
    {
        // Display the current item property and increment the index.
        spFeedback.innerHTML += oItem.name + "<br/>";        
        intIndex++;
    }
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

[**System.Shell**](system-shell.md)
</dt> <dt>

[**System.Shell.Drive**](system-shell-drive.md)
</dt> </dl>

 

 





