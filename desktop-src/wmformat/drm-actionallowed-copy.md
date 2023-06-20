---
title: DRM_ActionAllowed_Copy
description: The DRM\_ActionAllowed\_Copy attribute indicates whether the content is allowed to be copied to a device, such as a portable player.
ms.assetid: 3a391a14-ccbb-43c6-b362-0db53d93ab79
keywords:
- DRM_ActionAllowed_Copy windows Media Format
topic_type:
- apiref
api_name:
- DRM_ActionAllowed_Copy
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_ActionAllowed\_Copy

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_ActionAllowed\_Copy** attribute indicates whether the content is allowed to be copied to a device, such as a portable player.

## Global Constant

g\_wszWMDRM\_ActionAllowed\_Copy

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

In Windows Media DRM 10, all copy operations are restricted using the Copy action.

This is a read-only property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty).

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




