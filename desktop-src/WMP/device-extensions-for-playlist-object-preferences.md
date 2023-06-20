---
title: Device Extensions for Playlist Object Preferences
description: Device Extensions for Playlist Object Preferences
ms.assetid: 33b3dd18-fda2-4bf9-a893-5d77cdde6b80
keywords:
- Windows Media Player,device extensions
- Windows Media Player,extensions
- Windows Media Player,Playlist object preferences
- device extensions,Playlist object preferences
- extensions,Playlist object preferences
- Playlist object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Extensions for Playlist Object Preferences

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

As part of the synchronization process, Windows Media Player 10 or later copies playlist objects to MTP-enabled portable devices. Windows Media Player 11 introduces new functionality that enables portable devices to limit the types of playlist objects copied. (Windows Media Player always synchronizes playlist content as specified by the synchronization rules. This feature affects only the synchronization of playlist objects.) Windows Media Player copies three types of playlist objects from the computer to the device:

-   **Ordinary playlists.** These are playlists that are visible in the **Library** feature of Windows Media Player. These include playlists created by the user, playlists added to the library by online stores, and sample playlists installed with the Player. Windows Media Player copies only these playlists to the device when the user has selected them for synchronization.
-   **Stock sync playlists.** These are special playlists that are installed with Windows Media Player and used only for synchronization. These playlists are visible only in the Windows Media Player Device Setup Wizard.
-   **Implicitly created playlists.** These playlists are created when the user drags and drops a category folder, such as **Artist** or **Album**, onto the pane that lists the items to be synchronized.

The header file named wmpdevices.h, which has been updated for this release, defines the structures and constants needed to support Windows Media Player device extensions.

For a device to be recognized as supporting playlist object preferences through the Windows Media Player MTP device extension set, it must include the following information in the DeviceInfo dataset. (For more information about this dataset, see section 4.6.1 of the MTP specification.)



| Dataset field          | Field order | Data type  | Value                       |
|------------------------|-------------|------------|-----------------------------|
| VendorExtensionID      | 2           | **UINT32** | 0x00000006                  |
| VendorExtensionVersion | 3           | **UINT16** | 0x0064 (100)                |
| VendorExtensionDesc    | 4           | **String** | "microsoft.com/WMPPD: 11.0" |



 

The following table provides details about the MTP operation for playlist object preferences.



| Item                  | Description                                                                                                                                                                                                                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Code        | 0x9203                                                                                                                                                                                                                                                                                          |
| Operation Parameter 1 | 0                                                                                                                                                                                                                                                                                               |
| Operation Parameter 2 | 0                                                                                                                                                                                                                                                                                               |
| Operation Parameter 3 | 0                                                                                                                                                                                                                                                                                               |
| Operation Parameter 4 | 0                                                                                                                                                                                                                                                                                               |
| Operation Parameter 5 | 0                                                                                                                                                                                                                                                                                               |
| Data                  | The device returns a value in Response Parameter 1 to indicate playlist object synchronization preference.                                                                                                                                                                                      |
| Data Direction        | R->I                                                                                                                                                                                                                                                                                         |
| Response Code Options | MTP\_RESPONSE\_OK (0x2001) or valid error response code.                                                                                                                                                                                                                                        |
| Response Parameter 1  | 0 or 1. A value of 0 indicates that Windows Media Player must synchronize only ordinary playlist objects. A value of 1 indicates that that Windows Media Player must synchronize ordinary playlist objects, stock, and implicitly-created sync playlist objects, which is the default behavior. |
| Response Parameter 2  | 0                                                                                                                                                                                                                                                                                               |
| Response Parameter 3  | 0                                                                                                                                                                                                                                                                                               |
| Response Parameter 4  | 0                                                                                                                                                                                                                                                                                               |
| Response Parameter 5  | 0                                                                                                                                                                                                                                                                                               |



 

## Remarks

Implementing this feature is optional for portable devices. Windows Media Player synchronizes ordinary playlist objects, stock sync playlist objects, and implicitly-created playlist objects by default.

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 




