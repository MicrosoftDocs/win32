---
title: Device Extensions for Reporting Acquired Content
description: Device Extensions for Reporting Acquired Content
ms.assetid: 597d872e-9105-4edb-afa3-9f4407de0f73
keywords:
- Windows Media Player,device extensions
- Windows Media Player,extensions
- Windows Media Player,reporting acquired content
- device extensions,reporting acquired content
- extensions,reporting acquired content
- reporting acquired content
ms.topic: article
ms.date: 05/31/2018
---

# Device Extensions for Reporting Acquired Content

Windows Media Player 11 introduces new functionality that enables portable devices to notify the Player about content added to the device since the last synchronization. Windows Media Player 11 can use this information to copy newly acquired content from the device to the user's computer. Device manufacturers should note the following requirements for supporting this functionality:

-   This feature is supported only for MTP-enabled devices.
-   This feature works only with devices that have a partnership with Windows Media Player.
-   Devices must report only content that the device authored or downloaded. This includes photos taken by the device; voice recordings created by the device; voicemail recordings; downloads from a storage card; and downloads from the Internet. Content that was stored on the device as a result of synchronization with another device or a different partnership must not be reported.

The header file named wmpdevices.h, which is installed as part of the Windows Media Player SDK, defines the structures and constants needed to support Windows Media Player device extensions.

For a device to be recognized as supporting the reporting of acquired content through the Windows Media Player MTP device extension set, it must include the following information in the DeviceInfo dataset. (For more information about this dataset, see section 4.6.1 of the MTP specification.)



| Dataset field          | Field order | Data type  | Value                       |
|------------------------|-------------|------------|-----------------------------|
| VendorExtensionID      | 2           | **UINT32** | 0x00000006                  |
| VendorExtensionVersion | 3           | **UINT16** | 0x0064 (100)                |
| VendorExtensionDesc    | 4           | **String** | "microsoft.com/WMPPD: 11.0" |



 

The following table provides details about the MTP operation for reporting acquired content.



| Item                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Code        | 0x9202                                                                                                                                                                                                                          |
| Operation Parameter 1 | The transaction ID supplied by the device during the previous session. This value is zero for the first session.                                                                                                                |
| Operation Parameter 2 | Starting index. This value is always zero on the first call of a session. On subsequent calls within the same synchronization session, this value increases by the count of the items returned from the previous response data. |
| Operation Parameter 3 | 0x10000. This constant, defined in wmpdevices.h, is the maximum number of PUOIDs that can be returned in the response. Note that the value of this constant may be revised in future releases of this header file.              |
| Operation Parameter 4 | 0                                                                                                                                                                                                                               |
| Operation Parameter 5 | 0                                                                                                                                                                                                                               |
| Data                  | The device returns an MTP array containing PUOIDs that have been acquired. The array begins with a **DWORD** value indicating the count of items in the array, followed by the array of elements.                               |
| Data Direction        | R->I                                                                                                                                                                                                                         |
| Response Code Options | **MTP\_RESPONSE\_OK** (0x2001) or valid error response code.                                                                                                                                                                    |
| Response Parameter 1  | The current transaction ID.                                                                                                                                                                                                     |
| Response Parameter 2  | The number of PUOIDs that remain to be retrieved by future requests.                                                                                                                                                            |
| Response Parameter 3  | **DWORD** containing status information. Status is indicated in a bitwise fashion. See Remarks for information about flags to use.                                                                                              |
| Response Parameter 4  | 0                                                                                                                                                                                                                               |
| Response Parameter 5  | 0                                                                                                                                                                                                                               |



 

## Remarks

Status is indicated through Response Parameter 3 in a bitwise fashion by using the following flag.



| Flag                                              | Value | Description                                                                                                                                                                                                                             |
|---------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WMP\_MDRT\_FLAGS\_UNREPORTED\_ACQUIRED\_ITEMS** | 0x1   | The device contains some acquired items that cannot be returned in the list of PUOIDS. Note that this flag is not redundant with Response Parameter 2. Set this flag only when there are requested items that the device cannot return. |



 

Bits 1 through 31 are reserved for future use. These bits should be set to zero.

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 




