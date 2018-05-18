---
title: System.Shell.RecycleBin.onRecycleBinChanged event
description: Event fired when the content of the Recycle Bin is modified.
ms.assetid: '4afc138a-a731-46f5-bad2-7ed0d7c9be6c'
keywords: ["onRecycleBinChanged event Windows Sidebar", "onRecycleBinChanged event Windows Sidebar , System.Shell.RecycleBin object", "System.Shell.RecycleBin object Windows Sidebar , onRecycleBinChanged event"]
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin.onRecycleBinChanged
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.RecycleBin.onRecycleBinChanged event

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the content of the **Recycle Bin** is modified.

## Syntax


```JScript
iRetVal = System.Shell.RecycleBin.onRecycleBinChanged(
  handler
)
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

The name of the function to call when the event is fired.

</dd> </dl>

## Remarks

This event is triggered when [**fileCount**](system-shell-recyclebin-filecount.md) or [**folderCount**](system-shell-recyclebin-foldercount.md) changes.

The **Recycle Bin** must be open for this event to be fired.

This event may be triggered multiple times; this will require some management depending on gadget functionality.

## Examples

The following example demonstrates how to display user feedback when the Recycling Bin contents are modified.


```JScript
// Member variables.
var intRecycleBinFileCount = System.Shell.RecycleBin.fileCount;
var intRecycleBinFolderCount = System.Shell.RecycleBin.folderCount;
var bRecycleBinChangeHandled = false;

// Recycle Bin event handler.
System.Shell.RecycleBin.onRecycleBinChanged = function RecycleBinChanged()
{
    // Manage multiple events.
    setTimeout("RecycleBinChangedFeedback()",1000);
    bRecycleBinChangeHandled = false;
};

// --------------------------------------------------------------------
// Provide feedback on Recycle Bin content changes.
// --------------------------------------------------------------------
function RecycleBinChangedFeedback()
{
    if (bRecycleBinChangeHandled == false)
    {
        //
        // Display feedback to user.
        //
        
        // Manage multiple events.
        bRecycleBinChangeHandled = true;
    }
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





