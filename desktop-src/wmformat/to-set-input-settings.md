---
title: To Set Input Settings
description: To Set Input Settings
ms.assetid: 288801a7-793f-43bd-9c5a-f9e1bd86ecc3
keywords:
- Advanced Systems Format (ASF),input settings
- ASF (Advanced Systems Format),input settings
- profiles,input settings
- codecs,input settings
- streams,input settings
ms.topic: article
ms.date: 05/31/2018
---

# To Set Input Settings

The basic properties of input media and stream media are defined by the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure. For input formats, the media type information is set by your application. For stream formats, the media type information is set in the profile you assign to the writer. Some properties are independent of media type and must be set for an input before writing begins. These properties are codec and writer features that are independent of stream type, and must be set after the profile is assigned in the writer but before writing begins.

Setting an input setting requires a call to [**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting). You can also check the current value of a setting with a call to [**IWMWriterAdvanced2::GetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-getinputsetting).

## Related topics

<dl> <dt>

[**To Use Profiles with the Writer**](to-use-profiles-with-the-writer.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> <dt>

[**Writing Image Streams**](writing-image-streams.md)
</dt> </dl>

 

 




