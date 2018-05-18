---
title: System.Shell.Item.metadata method
description: Retrieves the metadata value for a canonical property name key of the System.Shell.Item.
ms.assetid: 'b3947176-3a5c-4f0d-a358-570419a9f65c'
keywords: ["metadata method Windows Sidebar", "metadata method Windows Sidebar , System.Shell.Item object", "System.Shell.Item object Windows Sidebar , metadata method"]
topic_type:
- apiref
api_name:
- System.Shell.Item.metadata
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Item.metadata method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves the metadata value for a canonical property name key of the [**System.Shell.Item**](system-shell-item.md).

## Syntax


```JScript
objRetVal = System.Shell.Item.metadata(
  sMetadata
)
```



## Parameters

<dl> <dt>

*sMetadata* \[in\]
</dt> <dd>

**String** that specifies the metadata key.

</dd> </dl>

## Return value

The metadata value.

## Remarks

Metadata keys can be obtained from the **Details** tab of the **Properties** dialog for an item.

> [!Note]  
> The following list provides examples of metadata that can be retrieved for particular file types.
>
> -   Graphics
>
>     Width, Height, Resolution, Bit depth
>
> -   Video
>
>     Bit rate, Frame rate, Sample size
>
> -   Audio/Music
>
>     Artist, Album, Year, Track, Genre, Lyrics, Duration
>
> -   Documents
>
>     Author, Title, Subject, Owner
>
 

## Examples

The following example demonstrates how to retrieve the "Owner" of an object dropped on a gadget.


```JScript
// --------------------------------------------------------------------
// Display the names of objects dropped on the gadget.
// --------------------------------------------------------------------
function GetItemFromDrop()
{    
    spFeedback.innerHTML = "Item(s) dropped.<br/>";
    var intIndex = 0;
    var oItem;
    var sItem;
    while(oItem = System.Shell.itemFromFileDrop(event.dataTransfer, intIndex))
    {
        // Display object properties and increment the index.
        sItem = "Other: ";
        if (oItem.isFileSystem == true)
        {
            sItem = "File: ";
        }
        if (oItem.isFolder == true)
        {
            sItem = "Folder: ";
        }
        if (oItem.isLink == true)
        {
            oLinkItem = oItem.link;
            sItem = "Link (" + oLinkItem.path + "): ";
        }
        spFeedback.innerHTML += sItem;
        spFeedback.innerHTML += oItem.name + "<br/>"; 
        spFeedback.innerHTML += "metadata: " + oItem.metadata("Owner") + "<br/>";
        
        intIndex++;
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



 

 





