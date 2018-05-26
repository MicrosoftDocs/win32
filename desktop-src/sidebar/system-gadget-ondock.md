---
title: System.Gadget.onDock event
description: Event fired when the gadget is docked on the Windows Sidebar.
ms.assetid: be909ef7-aa72-4329-b78a-228e56d49bc9
keywords:
- onDock event Windows Sidebar
- onDock event Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , onDock event
topic_type:
- apiref
api_name:
- System.Gadget.onDock
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

# System.Gadget.onDock event

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the gadget is docked on the Windows Sidebar.

> [!Note]  
> For Windows 7, because there is no Sidebar associated with the Gadget Platform, the **onDock** and [**onUndock**](system-gadget-onundock.md) event listeners are linked to a new gadget icon ("Larger size" or "Smaller size"). Clicking this icon resizes the gadget and raises the dock ("Smaller size") or undock ("Larger size") event.

 

## Syntax


```JScript
iRetVal = System.Gadget.onDock(
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

This event is fired either when the gadget is initialized or through user interaction after initialization.

This event updates the gadget [**docked**](system-gadget-docked.md) property.

Docked gadgets must be at least 60 pixels high (the height of the gadget toolbar including the **Settings** icon) and anywhere from 25 pixels to 130 pixels wide to fit within the maximum width of the Sidebar. Oversized gadgets are **not** clipped at the bounds of the Sidebar. Undocked gadgets have no maximum size constraints.

## Examples

The following example demonstrates how to modify the appearance of a gadget based on its dock state.


```JScript
// Gadget width and height.
var gadgetWidth = 130;
var gadgetHeight = 108;

// Amount to scale gadget when docked or undocked.
var scaleDocked = 1;
var scaleUndocked = 2;

// Amount of time desired to perform transition (in seconds).
var timeTransition = 2;

// Declare the dock and undock event handlers.
System.Gadget.onDock = CheckDockState;
System.Gadget.onUndock = CheckDockState;

// --------------------------------------------------------------------
// Check the gadget dock state; set the gadget style.
// imgBackground is the value of the 'id' attribute for the 
// g:background element.
// --------------------------------------------------------------------
function CheckDockState()
{
    var oBackground = document.getElementById("imgBackground");
            
    // Set the width of the background element to 0.
    // This forces the image to be refreshed appropriately.
    oBackground.style.width = 0;

    System.Gadget.beginTransition();
    
    var oBody = document.body.style;
    if (System.Gadget.docked)
    {
        oBody.width = gadgetWidth*scaleDocked;
        oBody.height = gadgetHeight*scaleDocked;
        
        oBackground.src = "url(../images/bg_docked.png)";
        
        txtDocked.className = 'gadgetDocked';
        txtDocked.innerText = 'Docked';
    }
    else
    {
        oBody.width = gadgetWidth*scaleUndocked;
        oBody.height = gadgetHeight*scaleUndocked;  
        
        oBackground.src = "url(../images/bg_undocked.png)";
        
        txtDocked.className = 'gadgetUndocked';
        txtDocked.innerText = 'Undocked';
    }
    System.Gadget.endTransition(System.Gadget.TransitionType.morph, timeTransition);
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

 

 





