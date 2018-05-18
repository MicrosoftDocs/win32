---
title: System.Network.Wireless.ssid property
description: Gets the Service Set Identifier (SSID) of the wireless network connection.
ms.assetid: '450b440c-7ea0-4ed4-9a5d-3574a0d6a3ee'
keywords: ["ssid property Windows Sidebar", "ssid property Windows Sidebar , System.Network.Wireless object", "System.Network.Wireless object Windows Sidebar , ssid property"]
topic_type:
- apiref
api_name:
- System.Network.Wireless.ssid
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Network.Wireless.ssid property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Service Set Identifier (SSID) of the wireless network connection.

This property is read-only.

## Syntax


```JScript
strssid = System.Network.Wireless.ssid
```



## Property value

A **String** that receives the SSID.

## Remarks

The SSID is also referred to as the "Network Name".

## Examples

The following example demonstrates how to listen for the [**connectionChanged**](system-network-wireless-connectionchanged.md) event.


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



 

 





