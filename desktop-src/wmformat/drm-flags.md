---
title: DRM_Flags
description: The DRM\_Flags property is used with DRM version 1 content only to specify the rights that will be contained in the local license.
ms.assetid: d9a776d3-da22-4111-b1ed-e3607a5576ef
keywords:
- DRM_Flags windows Media Format
topic_type:
- apiref
api_name:
- DRM_Flags
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_Flags

The **DRM\_Flags** property is used with DRM version 1 content only to specify the rights that will be contained in the local license. Rights are specified with values defined by the **WMT\_RIGHTS** enumeration type. More than one value can be selected by combining them with the bitwise **OR** operator.

## Global Constant

g\_wszWMDRM\_Flags

## Data Type

**WMT\_TYPE\_DWORD**

## Remarks

When accessing the **IWMHeaderInfo3** interface of the writer object, you can add or change this value. In other objects (metadata editor, reader, and synchronous reader), this value is read-only. Use [**IWMHeaderInfo::SetAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-setattribute) to set this property when creating DRM version 1 content.

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




