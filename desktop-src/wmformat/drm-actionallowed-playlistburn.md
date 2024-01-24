---
title: DRM_ActionAllowed_PlaylistBurn
description: The DRM\_ActionAllowed\_PlaylistBurn attribute indicates whether the content is allowed to be copied to CD as part of a playlist.
ms.assetid: 9e078c02-a2ab-484f-a695-790eebb05837
keywords:
- DRM_ActionAllowed_PlaylistBurn windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_PlaylistBurn
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_ActionAllowed\_PlaylistBurn

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_ActionAllowed\_PlaylistBurn** attribute indicates whether the content is allowed to be copied to CD as part of a playlist.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_PlaylistBurn

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




