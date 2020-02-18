---
title: DRM_Level
description: DRM\_Level is a license attribute that the Windows Media Format SDK sets when it creates a local license for files protected with DRM version 1.
ms.assetid: 05357378-4d73-48df-a3b5-bdb2c543ec66
keywords:
- DRM_Level windows Media Format
topic_type:
- apiref
api_name:
- DRM_Level
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_Level

**DRM\_Level** is a license attribute that the Windows Media Format SDK sets when it creates a local license for files protected with DRM version 1. It contains the security level that the calling application must have to access the content in the file. The default value is 150.

## Global Constant

g\_wszWMDRM\_Level

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

An application's DRM security level is determined by the particular wmstubdrm library that it links to at compile time. For more information on these security levels, see [Obtaining the Required DRM Library](obtaining-the-required-drm-library.md). Use [**IWMHeaderInfo::SetAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-setattribute) to set this property when protecting ASF files with DRM version 1.

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




