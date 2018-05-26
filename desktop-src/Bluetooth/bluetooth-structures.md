---
title: Bluetooth Structures
description: This section provides definitions for structures used for managing Bluetooth devices and services.
ms.assetid: bab27f5c-04c1-4fdc-91ff-249d1bfaef24
keywords:
- Bluetooth, reference, structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bluetooth Structures

This section provides definitions for structures used for managing Bluetooth devices and services.

Bluetooth is also supported by using the Windows Sockets programming interface. For more information about programming Bluetooth by using the Windows Sockets interface, see [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md).



| Section                                                                                       | Content                                                                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**BLUETOOTH\_ADDRESS**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_address?branch=master)                                               | Contains the address of a Bluetooth device.                                                                                      |
| [**BLUETOOTH\_AUTHENTICATE\_CALLBACK\_PARAMS**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_authentication_callback_params?branch=master) | Contains specific configuration information about the Bluetooth device responding to an authentication request.                  |
| [**BLUETOOTH\_AUTHENTICATE\_RESPONSE**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_authenticate_response?branch=master)                  | Contains information passed in response to a BTH\_REMOTE\_AUTHENTICATE\_REQUEST event.                                           |
| [**BLUETOOTH\_COD\_PAIRS**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_cod_pairs?branch=master)                                          | Provides for specification and retrieval of Bluetooth Class Of Device (COD) information.                                         |
| [**BLUETOOTH\_DEVICE\_INFO**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_device_info?branch=master)                                      | Provides information about a Bluetooth device.                                                                                   |
| [**BLUETOOTH\_DEVICE\_SEARCH\_PARAMS**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_device_search_params?branch=master)                   | Specifies search criteria for Bluetooth device searches.                                                                         |
| [**BLUETOOTH\_FIND\_RADIO\_PARAMS**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_find_radio_params?branch=master)                         | Facilitates the enumeration of installed Bluetooth radios.                                                                       |
| [**BLUETOOTH\_LOCAL\_SERVICE\_INFO**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_local_service_info?branch=master)                       | Contains local service information for a Bluetooth radio.                                                                        |
| [**BLUETOOTH\_NUMERIC\_COMPARISON\_INFO**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_numeric_comparison_info?branch=master)             | Contains the numeric value used for authentication via numeric comparison.                                                       |
| [**BLUETOOTH\_OOB\_DATA\_INFO**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_oob_data_info?branch=master)                                 | Contains data used to authenticate prior to establishing an Out-of-Band device pairing.                                          |
| [**BLUETOOTH\_PASSKEY\_INFO**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_passkey_info?branch=master)                                    | Contains the passkey used for authentication via passkey.                                                                        |
| [**BLUETOOTH\_PIN\_INFO**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_pin_info?branch=master)                                            | Contains information used for authentication via PIN.                                                                            |
| [**BLUETOOTH\_RADIO\_INFO**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_radio_info?branch=master)                                        | Contains information about a Bluetooth radio.                                                                                    |
| [**BLUETOOTH\_SELECT\_DEVICE\_PARAMS**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_bluetooth_select_device_params?branch=master)                   | Facilitates and manages the visibility, authentication, and selection of Bluetooth devices and services.                         |
| [**BTH\_DEVICE\_INFO**](/windows/win32/Bthdef/ns-bthdef-_bth_device_info?branch=master)                                                  | Stores information about a Bluetooth device.                                                                                     |
| [**BTH\_HCI\_EVENT\_INFO**](/windows/win32/Bthdef/ns-bthdef-_bth_hci_event_info?branch=master)                                           | Used in connection with obtaining WM\_DEVICECHANGE messages for Bluetooth.                                                       |
| [**BTH\_L2CAP\_EVENT\_INFO**](/windows/win32/Bthdef/ns-bthdef-_bth_l2cap_event_info?branch=master)                                       | Contains data about the events that are associated with an L2CAP channel.                                                        |
| [**BTH\_QUERY\_DEVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_device?branch=master)                                                | Used when querying for the presence of a Bluetooth device.                                                                       |
| [**BTH\_QUERY\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_service?branch=master)                                              | Used to query a Bluetooth service.                                                                                               |
| [**BTH\_RADIO\_IN\_RANGE**](/windows/win32/Bthdef/ns-bthdef-_bth_radio_in_range?branch=master)                                           | Stores data about the Bluetooth devices that are within communication range.                                                     |
| [**BTH\_SET\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_set_service?branch=master)                                                  | Provides service information for the specified Bluetooth service.                                                                |
| [**SDP\_ELEMENT\_DATA**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_sdp_element_data?branch=master)                                                | Stores SDP element data.                                                                                                         |
| [**SDP\_STRING\_TYPE\_DATA**](/windows/win32/BluetoothAPIs/ns-bluetoothapis-_sdp_string_type_data?branch=master)                                       | Stores information about SDP string types.                                                                                       |
| [**SdpAttributeRange**](/windows/win32/Bthsdpdef/ns-bthsdpdef-_sdpattributerange?branch=master)                                                | Used in a Bluetooth query to constrain the set of attributes to return in the query.                                             |
| [**SdpQueryUuid**](/windows/win32/Bthsdpdef/ns-bthsdpdef-_sdpqueryuuid?branch=master)                                                          | Facilitates searching for UUIDs.                                                                                                 |
| [**SdpQueryUuidUnion**](/windows/win32/Bthsdpdef/ns-bthsdpdef-sdpqueryuuidunion?branch=master)                                                | Contains the UUID on which to perform an SDP query. Used in conjunction with the [**SdpQueryUuid**](/windows/win32/Bthsdpdef/ns-bthsdpdef-_sdpqueryuuid?branch=master) structure. |
| [**SOCKADDR\_BTH**](/windows/win32/Ws2bth/ns-ws2bth-_sockaddr_bth?branch=master)                                                         | Used in conjunction with Bluetooth socket operations as defined by the AF\_BTH address family.                                   |



 

 

 




