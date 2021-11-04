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
ms.date: 05/31/2018
---

# DRM\_SAPLEVEL (deprecated)

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

 

 





