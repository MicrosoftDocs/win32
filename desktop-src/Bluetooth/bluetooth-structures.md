---
title: Bluetooth Structures
description: This section provides definitions for structures used for managing Bluetooth devices and services.
ms.assetid: 'bab27f5c-04c1-4fdc-91ff-249d1bfaef24'
keywords: ["Bluetooth, reference, structures"]
---

# Bluetooth Structures

This section provides definitions for structures used for managing Bluetooth devices and services.

Bluetooth is also supported by using the Windows Sockets programming interface. For more information about programming Bluetooth by using the Windows Sockets interface, see [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md).



| Section                                                                                       | Content                                                                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**BLUETOOTH\_ADDRESS**](bluetooth-address.md)                                               | Contains the address of a Bluetooth device.                                                                                      |
| [**BLUETOOTH\_AUTHENTICATE\_CALLBACK\_PARAMS**](bluetooth-authentication-callback-params.md) | Contains specific configuration information about the Bluetooth device responding to an authentication request.                  |
| [**BLUETOOTH\_AUTHENTICATE\_RESPONSE**](bluetooth-authenticate-response.md)                  | Contains information passed in response to a BTH\_REMOTE\_AUTHENTICATE\_REQUEST event.                                           |
| [**BLUETOOTH\_COD\_PAIRS**](bluetooth-cod-pairs.md)                                          | Provides for specification and retrieval of Bluetooth Class Of Device (COD) information.                                         |
| [**BLUETOOTH\_DEVICE\_INFO**](bluetooth-device-info.md)                                      | Provides information about a Bluetooth device.                                                                                   |
| [**BLUETOOTH\_DEVICE\_SEARCH\_PARAMS**](bluetooth-device-search-params.md)                   | Specifies search criteria for Bluetooth device searches.                                                                         |
| [**BLUETOOTH\_FIND\_RADIO\_PARAMS**](bluetooth-find-radio-params.md)                         | Facilitates the enumeration of installed Bluetooth radios.                                                                       |
| [**BLUETOOTH\_LOCAL\_SERVICE\_INFO**](bluetooth-local-service-info.md)                       | Contains local service information for a Bluetooth radio.                                                                        |
| [**BLUETOOTH\_NUMERIC\_COMPARISON\_INFO**](bluetooth-numeric-comparison-info.md)             | Contains the numeric value used for authentication via numeric comparison.                                                       |
| [**BLUETOOTH\_OOB\_DATA\_INFO**](bluetooth-oob-data-info.md)                                 | Contains data used to authenticate prior to establishing an Out-of-Band device pairing.                                          |
| [**BLUETOOTH\_PASSKEY\_INFO**](bluetooth-passkey-info.md)                                    | Contains the passkey used for authentication via passkey.                                                                        |
| [**BLUETOOTH\_PIN\_INFO**](bluetooth-pin-info.md)                                            | Contains information used for authentication via PIN.                                                                            |
| [**BLUETOOTH\_RADIO\_INFO**](bluetooth-radio-info.md)                                        | Contains information about a Bluetooth radio.                                                                                    |
| [**BLUETOOTH\_SELECT\_DEVICE\_PARAMS**](bluetooth-select-device-params.md)                   | Facilitates and manages the visibility, authentication, and selection of Bluetooth devices and services.                         |
| [**BTH\_DEVICE\_INFO**](bth-device-info.md)                                                  | Stores information about a Bluetooth device.                                                                                     |
| [**BTH\_HCI\_EVENT\_INFO**](bth-hci-event-info.md)                                           | Used in connection with obtaining WM\_DEVICECHANGE messages for Bluetooth.                                                       |
| [**BTH\_L2CAP\_EVENT\_INFO**](bth-l2cap-event-info.md)                                       | Contains data about the events that are associated with an L2CAP channel.                                                        |
| [**BTH\_QUERY\_DEVICE**](bth-query-device.md)                                                | Used when querying for the presence of a Bluetooth device.                                                                       |
| [**BTH\_QUERY\_SERVICE**](bth-query-service.md)                                              | Used to query a Bluetooth service.                                                                                               |
| [**BTH\_RADIO\_IN\_RANGE**](bth-radio-in-range.md)                                           | Stores data about the Bluetooth devices that are within communication range.                                                     |
| [**BTH\_SET\_SERVICE**](bth-set-service.md)                                                  | Provides service information for the specified Bluetooth service.                                                                |
| [**SDP\_ELEMENT\_DATA**](sdp-element-data.md)                                                | Stores SDP element data.                                                                                                         |
| [**SDP\_STRING\_TYPE\_DATA**](sdp-string-type-data.md)                                       | Stores information about SDP string types.                                                                                       |
| [**SdpAttributeRange**](sdpattributerange.md)                                                | Used in a Bluetooth query to constrain the set of attributes to return in the query.                                             |
| [**SdpQueryUuid**](sdpqueryuuid.md)                                                          | Facilitates searching for UUIDs.                                                                                                 |
| [**SdpQueryUuidUnion**](sdpqueryuuidunion.md)                                                | Contains the UUID on which to perform an SDP query. Used in conjunction with the [**SdpQueryUuid**](sdpqueryuuid.md) structure. |
| [**SOCKADDR\_BTH**](sockaddr-bth.md)                                                         | Used in conjunction with Bluetooth socket operations as defined by the AF\_BTH address family.                                   |



 

 

 




