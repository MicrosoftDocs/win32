---
title: DRM_IsDRM
description: The DRM\_IsDRM property indicates whether a file is a DRM-protected file.
ms.assetid: 1d728135-25e9-4ab8-873d-b7df3e8cae83
keywords:
- DRM_IsDRM windows Media Format
topic_type:
- apiref
api_name:
- DRM_IsDRM
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_IsDRM

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_IsDRM** property indicates whether a file is a DRM-protected file.

## Global Constant

g\_wszWMDRM\_IsDRM

## Data Type

**WMT\_TYPE\_BOOL**

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




