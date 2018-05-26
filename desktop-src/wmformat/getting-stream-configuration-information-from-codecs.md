---
title: Getting Stream Configuration Information from Codecs
description: Getting Stream Configuration Information from Codecs
ms.assetid: 76c734a1-6fe4-4958-8773-a65f5ced80c6
keywords:
- streams,configurations from codecs
- codecs,getting stream configurations from
- streams,codec formats
- codecs,formats
- streams,IWMCodecInfo interface
- IWMCodecInfo,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Stream Configuration Information from Codecs

For audio and video streams that use the Windows Media Audio and Video codecs, you should get the values for the stream configuration structures from the codec you want to use. While it is possible to set these values yourself, using the codecs ensures that the values are accurate. You should not alter the values in these structures unless the documentation specifically recommends a particular change.

Information from the codecs comes in the form of codec formats. Each codec format is a single stream format supported by the codec. For more information about stream formats, see [Formats](formats.md).

You can request information from the Windows Media codecs using the [**IWMCodecInfo**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmcodecinfo?branch=master), [**IWMCodecInfo2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmcodecinfo2?branch=master), and [**IWMCodecInfo3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmcodecinfo3?branch=master) interfaces of the profile manager object. To get the [**IWMProfileManager**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofilemanager?branch=master) interface of a profile manager object, call the [**WMCreateProfileManager**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager?branch=master) function. Call **QueryInterface** on **IWMProfileManager** to get **IWMCodecInfo3**.

The following sections describe how to get the information you need.



| Section                                                                                                | Description                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [To Enumerate All Installed Windows Media Codecs](to-enumerate-all-installed-windows-media-codecs.md) | Describes how to use the methods of the **IWMCodecInfo** and **IWMCodecInfo2** interfaces to retrieve the name and codec index of each Windows Media codec installed. |
| [To Enumerate Codec Formats](to-enumerate-codec-formats.md)                                           | Describes how to get stream configuration objects from codecs for use in your profiles.                                                                               |



 

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> </dl>

 

 




