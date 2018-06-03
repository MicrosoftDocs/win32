---
title: System.Gadget.docked property
description: Gets the dock state of the gadget in relation to the Windows Sidebar.
ms.assetid: a7e7c720-1f16-49a3-a4df-2c30e3ff7916
keywords:
- docked property Windows Sidebar
- docked property Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , docked property
topic_type:
- apiref
api_name:
- System.Gadget.docked
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

# System.Gadget.docked property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the dock state of the gadget in relation to the Windows Sidebar.

This property is read-only.

## Syntax


```JScript
bdocked = System.Gadget.docked
```



## Property value

A **Boolean** that receives the docked state of the gadget.

<dt>



 (TRUE)


</dt> <dd>

Gadget is docked in the Sidebar.

</dd> <dt>



 (FALSE)


</dt> <dd>

Gadget is undocked from the Sidebar.

</dd> </dl>

## Remarks

This property is updated by the [**onDock**](system-gadget-ondock.md) and [**onUndock**](system-gadget-onundock.md) events.

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

 

 





