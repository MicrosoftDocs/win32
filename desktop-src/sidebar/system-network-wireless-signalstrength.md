---
title: System.Network.Wireless.signalStrength property
description: Gets the signal strength of the wireless network connection.
ms.assetid: 'c497c07b-ca60-4be0-929e-f7801082358a'
keywords: ["signalStrength property Windows Sidebar", "signalStrength property Windows Sidebar , System.Network.Wireless object", "System.Network.Wireless object Windows Sidebar , signalStrength property"]
topic_type:
- apiref
api_name:
- System.Network.Wireless.signalStrength
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Network.Wireless.signalStrength property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the signal strength of the wireless network connection.

This property is read-only.

## Syntax


```JScript
isignalStrength = System.Network.Wireless.signalStrength
```



## Property value

An **Integer** that receives the signal strength.

## Examples

The following example demonstrates how to listen for the [**signalStrengthChanged**](system-network-wireless-signalstrengthchanged.md) event.


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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





