---
title: DRM_ActionAllowed_Backup
description: The DRM\_ActionAllowed\_Backup attribute indicates whether the license is allowed to be backed up.
ms.assetid: 49b503ff-a2ca-405c-a8ac-49653c62e13e
keywords:
- DRM_ActionAllowed_Backup windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_Backup
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_ActionAllowed\_Backup

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_ActionAllowed\_Backup** attribute indicates whether the license is allowed to be backed up.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_Backup

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




