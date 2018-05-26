---
title: System.Gadget.endTransition method
description: Refreshes the gadget view and resumes updates, animations, and effects once a gadget docking or undocking transition has completed.
ms.assetid: b5f7ba34-4439-465e-b439-f74bb68565fd
keywords:
- endTransition method Windows Sidebar
- endTransition method Windows Sidebar , System.Gadget object
- System.Gadget object Windows Sidebar , endTransition method
topic_type:
- apiref
api_name:
- System.Gadget.endTransition
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

# System.Gadget.endTransition method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Refreshes the gadget view and resumes updates, animations, and effects once a gadget docking or undocking transition has completed.

> [!Note]  
> For Windows 7, calls to the System.Gadget.beginTransition and System.Gadget.endTransition methods are ignored.

 

## Syntax


```JScript
System.Gadget.endTransition(
  intTransition,
  fSeconds
)
```



## Parameters

<dl> <dt>

*intTransition* \[in\]
</dt> <dd>

The transition type or effect.

<dt>



 (0)


</dt> <dd>

None. No transition effect applied during gadget docking or undocking.

</dd> <dt>



 (1)


</dt> <dd>

Morph. The gadget's visual appearance "morphs" from one state to another during gadget docking or undocking.

</dd> </dl> </dd> <dt>

*fSeconds* \[in\]
</dt> <dd>

The number of seconds desired to complete the docking or undocking transition.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

[**beginTransition**](system-gadget-begintransition.md) and **endTransition** enclose the code that defines the visual effects to execute during gadget docking and undocking transitions.

Use [**beginTransition**](system-gadget-begintransition.md) to suspend all gadget updates, animations, and effects.

## Examples

The following example demonstrates how to use [**beginTransition**](system-gadget-begintransition.md) and **endTransition** with the 'morph' transition type.


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

 

 





