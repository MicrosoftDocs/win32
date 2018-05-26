---
title: System.Network.Wireless.signalStrengthChanged event
description: Event fired when the signal strength of a wireless connection changes.
ms.assetid: b5175c2a-e509-40b0-ac81-bd80eca46070
keywords:
- signalStrengthChanged event Windows Sidebar
- signalStrengthChanged event Windows Sidebar , System.Network.Wireless object
- System.Network.Wireless object Windows Sidebar , signalStrengthChanged event
topic_type:
- apiref
api_name:
- System.Network.Wireless.signalStrengthChanged
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

# System.Network.Wireless.signalStrengthChanged event

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the signal strength of a wireless connection changes.

## Syntax


```JScript
iRetVal = System.Network.Wireless.signalStrengthChanged(
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

This event updates the [**signalStrength**](system-network-wireless-signalstrength.md) property.

## Examples

The following example demonstrates how to listen for the **signalStrengthChanged** event.


```JScript
var oGadgetDocument = System.Gadget.document;
System.Network.Wireless.signalStrengthChanged = SignalChanged;

// --------------------------------------------------------------------
// Display the network SSID.
// --------------------------------------------------------------------
function SignalChanged()
{
    oGadgetDocument.getElementById("strFeedback").innerText = "Signal Strengh: " + System.Network.Wireless.signalStrength;
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



 

 





