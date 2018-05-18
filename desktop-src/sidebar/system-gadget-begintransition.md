---
title: System.Gadget.beginTransition method
description: Suspends all gadget updates, animations, and effects until a docking or undocking transition has completed.
ms.assetid: '82e37cff-cab8-49d1-ac25-7dd039eab454'
keywords: ["beginTransition method Windows Sidebar", "beginTransition method Windows Sidebar , System.Gadget object", "System.Gadget object Windows Sidebar , beginTransition method"]
topic_type:
- apiref
api_name:
- System.Gadget.beginTransition
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.beginTransition method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Suspends all gadget updates, animations, and effects until a docking or undocking transition has completed.

> [!Note]  
> For Windows 7, calls to the System.Gadget.beginTransition and System.Gadget.endTransition methods are ignored.

 

## Syntax


```JScript
System.Gadget.beginTransition()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

**beginTransition** and [**endTransition**](system-gadget-endtransition.md) enclose the code that defines the visual effects to execute during gadget docking and undocking transitions.

Use [**endTransition**](system-gadget-endtransition.md) to resume updates and refresh the gadget view once the docking or undocking transition has completed.

## Examples

The following example demonstrates how to use **beginTransition** and [**endTransition**](system-gadget-endtransition.md) with the "morph" transition type.


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

 

 





