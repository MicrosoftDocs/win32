---
title: Implementing Network Functionality
description: Implementing Network Functionality
ms.assetid: 908e269b-63be-4666-a364-a894f6dcd86f
keywords:
- Windows Media Format SDK,implementing network functionality
- Windows Media Format SDK,network functionality
- Advanced Systems Format (ASF),implementing network functionality
- ASF (Advanced Systems Format),implementing network functionality
- Advanced Systems Format (ASF),network functionality
- ASF (Advanced Systems Format),network functionality
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Implementing Network Functionality

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to use the networking features available through the Windows Media Format SDK. An application can use these features to read ASF streams from a network, broadcast ASF streams to a network, or push ASF streams to a publishing point on a server running Windows Media Services.

The following sections describe the networking features of this SDK.



| Section                                                                    | Description                                                                                                          |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Overview of Networking Interfaces](overview-of-networking-interfaces.md) | Names and describes each interface that supports networking methods.                                                 |
| [Reading ASF Data Over a Network](reading-asf-data-over-a-network.md)     | Describes how to play files from a network source and how to configure the network settings on the reader object.    |
| [Sending ASF Data Over a Network](sending-asf-data-over-a-network.md)     | Describes how to broadcast ASF data over a network or send ASF data to a publishing point on a Windows Media server. |
| [Default Networking Settings](default-networking-settings.md)             | Provides a quick reference for the default settings used by the SDK.                                                 |



 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




