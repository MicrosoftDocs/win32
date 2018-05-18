---
title: System.Network.Wireless object
description: Defines the properties and events for determining wireless network connectivity and interface settings.
ms.assetid: '68b88729-e511-4eee-ad67-410bd5dea76f'
keywords: ["System.Network.Wireless object Windows Sidebar", "System.Network.Wireless object Windows Sidebar , described"]
topic_type:
- apiref
api_name:
- System.Network.Wireless
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Network.Wireless object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and events for determining wireless network connectivity and interface settings.

## Members

The **System.Network.Wireless** object has these types of members:

-   [Events](#events)
-   [Properties](#properties)

### Events

The **System.Network.Wireless** object has these events.



| Event                                                                          | Description                                                                        |
|:-------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**connectionChanged**](system-network-wireless-connectionchanged.md)         | Event fired when the network connection changes. <br/>                       |
| [**signalStrengthChanged**](system-network-wireless-signalstrengthchanged.md) | Event fired when the signal strength of a wireless connection changes. <br/> |



 

### Properties

The **System.Network.Wireless** object has these properties.



| Property                                                                          | Access type          | Description                                                                                |
|:----------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------|
| [**address**](system-network-wireless-address.md)<br/>                     | Read-only<br/> | Gets the IP address of the active network adapter. <br/>                             |
| [**ipv6Address**](system-network-wireless-ipv6address.md)<br/>             | Read-only<br/> | Gets the IPv6 address of the wireless network adapter. <br/>                         |
| [**primaryDNSAddress**](system-network-wireless-primarydnsaddress.md)<br/> | Read-only<br/> | Gets the IP address of the first available DNS server on the wireless network. <br/> |
| [**secureConnection**](system-network-wireless-secureconnection.md)<br/>   | Read-only<br/> | Gets whether the current connection is secure. <br/>                                 |
| [**signalStrength**](system-network-wireless-signalstrength.md)<br/>       | Read-only<br/> | Gets the signal strength of the wireless network connection. <br/>                   |
| [**ssid**](system-network-wireless-ssid.md)<br/>                           | Read-only<br/> | Gets the Service Set Identifier (SSID) of the wireless network connection. <br/>     |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





