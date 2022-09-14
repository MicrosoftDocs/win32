---
title: Bluetooth Structures
description: This section provides definitions for structures used for managing Bluetooth devices and services.
ms.assetid: bab27f5c-04c1-4fdc-91ff-249d1bfaef24
keywords:
- Bluetooth, reference, structures
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth Structures

This section provides definitions for structures used for managing Bluetooth devices and services.

Bluetooth is also supported by using the Windows Sockets programming interface. For more information about programming Bluetooth by using the Windows Sockets interface, see [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md).



| Section                                                                                       | Content                                                                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**BLUETOOTH\_ADDRESS**](/windows/win32/api/bluetoothapis/ns-bluetoothapis-bluetooth_address_struct)                                               | Contains the address of a Bluetooth device.                                                                                      |
| [**BLUETOOTH\_AUTHENTICATE\_CALLBACK\_PARAMS**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_authentication_callback_params) | Contains specific configuration information about the Bluetooth device responding to an authentication request.                  |
| [**BLUETOOTH\_AUTHENTICATE\_RESPONSE**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_authenticate_response)                  | Contains information passed in response to a BTH\_REMOTE\_AUTHENTICATE\_REQUEST event.                                           |
| [**BLUETOOTH\_COD\_PAIRS**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_cod_pairs)                                          | Provides for specification and retrieval of Bluetooth Class Of Device (COD) information.                                         |
| [**BLUETOOTH\_DEVICE\_INFO**](/windows/win32/api/bluetoothapis/ns-bluetoothapis-bluetooth_device_info_struct)                                      | Provides information about a Bluetooth device.                                                                                   |
| [**BLUETOOTH\_DEVICE\_SEARCH\_PARAMS**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_device_search_params)                   | Specifies search criteria for Bluetooth device searches.                                                                         |
| [**BLUETOOTH\_FIND\_RADIO\_PARAMS**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_find_radio_params)                         | Facilitates the enumeration of installed Bluetooth radios.                                                                       |
| [**BLUETOOTH\_LOCAL\_SERVICE\_INFO**](/windows/win32/api/bluetoothapis/ns-bluetoothapis-bluetooth_local_service_info_struct)                       | Contains local service information for a Bluetooth radio.                                                                        |
| [**BLUETOOTH\_NUMERIC\_COMPARISON\_INFO**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_numeric_comparison_info)             | Contains the numeric value used for authentication via numeric comparison.                                                       |
| [**BLUETOOTH\_OOB\_DATA\_INFO**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_oob_data_info)                                 | Contains data used to authenticate prior to establishing an Out-of-Band device pairing.                                          |
| [**BLUETOOTH\_PASSKEY\_INFO**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_passkey_info)                                    | Contains the passkey used for authentication via passkey.                                                                        |
| [**BLUETOOTH\_PIN\_INFO**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_pin_info)                                            | Contains information used for authentication via PIN.                                                                            |
| [**BLUETOOTH\_RADIO\_INFO**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_radio_info)                                        | Contains information about a Bluetooth radio.                                                                                    |
| [**BLUETOOTH\_SELECT\_DEVICE\_PARAMS**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-bluetooth_select_device_params)                   | Facilitates and manages the visibility, authentication, and selection of Bluetooth devices and services.                         |
| [**BTH\_DEVICE\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_device_info)                                                  | Stores information about a Bluetooth device.                                                                                     |
| [**BTH\_HCI\_EVENT\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_hci_event_info)                                           | Used in connection with obtaining WM\_DEVICECHANGE messages for Bluetooth.                                                       |
| [**BTH\_L2CAP\_EVENT\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_l2cap_event_info)                                       | Contains data about the events that are associated with an L2CAP channel.                                                        |
| [**BTH\_QUERY\_DEVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_device)                                                | Used when querying for the presence of a Bluetooth device.                                                                       |
| [**BTH\_QUERY\_SERVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_service)                                              | Used to query a Bluetooth service.                                                                                               |
| [**BTH\_RADIO\_IN\_RANGE**](/windows/desktop/api/Bthdef/ns-bthdef-bth_radio_in_range)                                           | Stores data about the Bluetooth devices that are within communication range.                                                     |
| [**BTH\_SET\_SERVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_set_service)                                                  | Provides service information for the specified Bluetooth service.                                                                |
| [**SDP\_ELEMENT\_DATA**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-sdp_element_data)                                                | Stores SDP element data.                                                                                                         |
| [**SDP\_STRING\_TYPE\_DATA**](/windows/desktop/api/BluetoothAPIs/ns-bluetoothapis-sdp_string_type_data)                                       | Stores information about SDP string types.                                                                                       |
| [**SdpAttributeRange**](/windows/desktop/api/Bthsdpdef/ns-bthsdpdef-sdpattributerange)                                                | Used in a Bluetooth query to constrain the set of attributes to return in the query.                                             |
| [**SdpQueryUuid**](/windows/desktop/api/Bthsdpdef/ns-bthsdpdef-sdpqueryuuid)                                                          | Facilitates searching for UUIDs.                                                                                                 |
| [**SdpQueryUuidUnion**](/windows/desktop/api/Bthsdpdef/ns-bthsdpdef-sdpqueryuuidunion)                                                | Contains the UUID on which to perform an SDP query. Used in conjunction with the [**SdpQueryUuid**](/windows/desktop/api/Bthsdpdef/ns-bthsdpdef-sdpqueryuuid) structure. |
| [**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth)                                                         | Used in conjunction with Bluetooth socket operations as defined by the AF\_BTH address family.                                   |



 

 

 




