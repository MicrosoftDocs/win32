---
title: Use\_Advanced\_DRM
description: The Use\_Advanced\_DRM attribute specifies whether DRM version 7 is used to protect the content.
ms.assetid: a385152f-d72e-473c-93a0-5697659df23c
keywords:
- Use_Advanced_DRM windows Media Format
topic_type:
- apiref
api_name:
- Use_Advanced_DRM
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Use\_Advanced\_DRM

The **Use\_Advanced\_DRM** attribute specifies whether DRM version 7 is used to protect the content.

## Global Constant

g\_wszWMUse\_Advanced\_DRM

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a read-write property that is retrieved using [**IWMDRMReader::GetDRMProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-getdrmproperty?branch=master) and set using [**IWMDRMWriter::SetDRMAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute?branch=master). This property is not accessible from the reader object.

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




