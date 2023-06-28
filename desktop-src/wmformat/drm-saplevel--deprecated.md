---
title: DRM_SAPLEVEL (deprecated)
description: Specifies the secure audio path (SAP) level supported by your application.
ms.assetid: a2648083-f9ec-43c7-96c8-4d8b5f8285d1
keywords:
- DRM_SAPLEVEL (deprecated) windows Media Format
topic_type:
- apiref
api_name:
- DRM_SAPLEVEL (deprecated)
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_SAPLEVEL (deprecated)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[**DRM\_SAPLEVEL** is no longer available for use as of Windows Vista. Instead, use Protected User Mode Audio (PUMA) in the Media Foundation library. \]

The **DRM\_SAPLEVEL** property specifies the secure audio path (SAP) level supported by your application.

## Global Constant

g\_wszWMDRM\_SAPLEVEL

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This is a write-only property that is set by calling [**IWMDRMReader::SetDRMProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-setdrmproperty). The value is a wide-character string representation of the SAP level, such as L"200". Current supported values are 200 and 300.

## Requirements



| Requirement | Value |
|----------------------------------|--------------------------------|
| End of client support<br/> | Windows XP<br/>          |
| End of server support<br/> | Windows Server 2003<br/> |



## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 





