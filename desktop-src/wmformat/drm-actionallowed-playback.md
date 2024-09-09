---
title: DRM_ActionAllowed_Playback
description: The DRM\_ActionAllowed\_Playback attribute indicates whether playback of the content is allowed.
ms.assetid: 7c8d7631-7edc-482d-afdb-758c4a0ecc22
keywords:
- DRM_ActionAllowed_Playback windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_Playback
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_ActionAllowed\_Playback

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_ActionAllowed\_Playback** attribute indicates whether playback of the content is allowed.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_Playback

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




