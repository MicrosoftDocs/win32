---
title: Rights Constants
description: Rights Constants
ms.assetid: fb20dc57-25da-4613-a324-e081ba87df73
keywords:
- Windows Media Format SDK,constants
- digital rights management (DRM),constants
- DRM (digital rights management),constants
- DRM Client Extended APIs,constants
- Client Extended APIs,constants
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Rights Constants

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The constants listed in the following table are used to identify DRM actions and to build lists of actions.



| Constant                                        | Description                                                                                                                                                                                                                                                    |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| g\_wszWMDRM\_ACTIONLIST\_TAG                    | Defines the XML element name for an action list.                                                                                                                                                                                                               |
| g\_wszWMDRM\_ACTION\_TAG                        | Defines the XML element name for an entry in an action list.                                                                                                                                                                                                   |
| g\_wszWMDRM\_RIGHT\_PLAYBACK                    | Defines the string for the right to play content.                                                                                                                                                                                                              |
| g\_wszWMDRM\_RIGHT\_COPY                        | Defines the string for the right to copy content.                                                                                                                                                                                                              |
| g\_wszWMDRM\_RIGHT\_PLAYLIST\_BURN              | Defines the string for the right to burn content to CD as part of a playlist.                                                                                                                                                                                  |
| g\_wszWMDRM\_RIGHT\_CREATE\_THUMBNAIL\_IMAGE    | Defines the string for the right to create a thumbnail image from video content.                                                                                                                                                                               |
| g\_wszWMDRM\_RIGHT\_COPY\_TO\_CD                | Defines the string for the right to copy content to a CD. New licenses should not use this right. Instead, all rights granting permission to copy content should be covered by the copy right and the playlist burn right.                                     |
| g\_wszWMDRM\_RIGHT\_COPY\_TO\_SDMI\_DEVICE      | Defines the string for the right to copy content to a device that conforms to the Secure Digital Music Initiative (SDMI). New licenses should not use this right. Instead, all rights granting permission to copy content should be covered by the copy right. |
| g\_wszWMDRM\_RIGHT\_COPY\_TO\_NON\_SDMI\_DEVICE | Defines the string for the right to copy to a device that does not conform to the Secure Digital Music Initiative (SDMI). New licenses should not use this right. Instead, all rights granting permission to copy content should be covered by the copy right. |
| g\_wszWMDRM\_RIGHT\_BACKUP                      | Defines the string for the right to backup the license.                                                                                                                                                                                                        |
| g\_wszWMDRM\_RIGHT\_COLLABORATIVE\_PLAY         | Defines the string for the right to play content over a network as part of a shared playlist.                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[**Constants**](constants.md)
</dt> </dl>

 

 




