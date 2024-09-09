---
title: DRM_LicenseState_PlaylistBurn
description: The DRM\_LicenseState\_PlaylistBurn property contains a WM\_LICENSE\_STATE\_DATA structure that contains details about how this right has been applied to the content.
ms.assetid: 21d2a284-1f0c-499a-94fd-f66d6437bd49
keywords:
- DRM_LicenseState_PlaylistBurn windows Media Format
topic_type:
- apiref
api_name:
- DRM_LicenseState_PlaylistBurn
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_LicenseState\_PlaylistBurn

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_LicenseState\_PlaylistBurn** property contains a [**WM\_LICENSE\_STATE\_DATA**](/previous-versions/windows/desktop/legacy/dd757942(v=vs.85)) structure that contains details about how this right has been applied to the content.

## Global Constant

g\_wszWMDRM\_LicenseState\_PlaylistBurn

## Data Type

**WMT\_TYPE\_BINARY**

## Remarks

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 