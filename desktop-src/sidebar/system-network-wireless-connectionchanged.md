---
title: System.Network.Wireless.connectionChanged event
description: Event fired when the network connection changes.
ms.assetid: 'c3fd7450-0ebf-4148-8dd6-dba3ca6243e9'
keywords: ["connectionChanged event Windows Sidebar", "connectionChanged event Windows Sidebar , System.Network.Wireless object", "System.Network.Wireless object Windows Sidebar , connectionChanged event"]
topic_type:
- apiref
api_name:
- System.Network.Wireless.connectionChanged
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Network.Wireless.connectionChanged event

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the network connection changes.

## Syntax


```JScript
iRetVal = System.Network.Wireless.connectionChanged(
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

A network connection change is triggered if the network name, or Signal Set Identifier (SSID), changes.

This event updates the [**ssid**](system-network-wireless-ssid.md) property.

## Examples

The following example demonstrates how to listen for the **connectionChanged** event.


```JScript
var oGadgetDocument = System.Gadget.document;
System.Network.Wireless.connectionChanged = ConnectionChanged;

// --------------------------------------------------------------------
// Display the network SSID.
// --------------------------------------------------------------------
function ConnectionChanged()
{
    oGadgetDocument.getElementById("strFeedback").innerText = "SSID: " + System.Network.Wireless.ssid;
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



 

 





