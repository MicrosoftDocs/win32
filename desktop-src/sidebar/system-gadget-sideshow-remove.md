---
title: System.Gadget.SideShow.remove method
description: Removes an element specified by a content ID.
ms.assetid: 7eb937e6-8218-473b-b816-54a68cab405d
keywords:
- remove method Windows Sidebar
- remove method Windows Sidebar , System.Gadget.SideShow object
- System.Gadget.SideShow object Windows Sidebar , remove method
topic_type:
- apiref
api_name:
- System.Gadget.SideShow.remove
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

# System.Gadget.SideShow.remove method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Removes an element specified by a content ID.

## Syntax


```JScript
iRetVal = System.Gadget.SideShow.remove(
  intID
)
```



## Parameters

<dl> <dt>

*intID* \[in\]
</dt> <dd>

**Integer** that specifies the SideShow content ID.

</dd> </dl>

## Remarks

When calling [**addText**](system-gadget-sideshow-addtext.md) and [**addImage**](system-gadget-sideshow-addimage.md) repeatedly with the same ID, it is recommended that you call **remove** or [**removeAll**](system-gadget-sideshow-removeall.md) prior to updating the content for a given ID.

Verify that [**System.Gadget.SideShow.enabled**](system-gadget-sideshow-enabled.md) returns `true` before using other [**System.Gadget.SideShow**](system-gadget-sideshow.md) object members.

## Examples

The following example demonstrates how to remove specific elements from a SideShow gadget.


```JScript
//
// sideshow.js - Contains all Windows SideShow specific code.
//

sideshow =
{
    imageIdUp: 50,
    imageIdEqual: 51,
    imageIdDown: 52,
    
    // --------------------------------------------------------------------
    // initialize() - Initialize the SideShow portion of the gadget.
    // --------------------------------------------------------------------
    initialize: function()
    {
        // Ensure SideShow is enabled for this machine.
        if (!System.Gadget.SideShow.enabled())
        {
            // If it is not available, return without initializing anything.
            return;
        }
        
        System.Gadget.SideShow.setFriendlyName("Stocks");
        sideshow.clearContent();

        // Add images.
        System.Gadget.SideShow.addImage(sideshow.imageIdUp, System.Gadget.path + "\\images\\up.gif");
        System.Gadget.SideShow.addImage(sideshow.imageIdEqual, System.Gadget.path + "\\images\\equal.gif");
        System.Gadget.SideShow.addImage(sideshow.imageIdDown, System.Gadget.path + "\\images\\down.gif");
    },
    
    // --------------------------------------------------------------------
    // clearContent() - Removes all content from the device and puts in default text.
    // --------------------------------------------------------------------
    clearContent: function()
    {
        // Remove content from the device.
        System.Gadget.SideShow.remove(sideshow.imageIdUp);
        System.Gadget.SideShow.remove(sideshow.imageIdEqual);
        System.Gadget.SideShow.remove(sideshow.imageIdDown);
        System.Gadget.SideShow.addText(0, "ServiceIsUnavailable");    
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

[**System.Gadget.SideShow**](system-gadget-sideshow.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Windows SideShow: MSDN](http://msdn.microsoft.com/library/ms744202.aspx)
</dt> <dt>

[Windows SideShow: Windows Hardware Developer Central](http://www.microsoft.com/whdc/device/sideshow/default.mspx)
</dt> </dl>

 

 





