---
title: Use\_DRM
description: The Use\_DRM attribute instructs the writer object to apply DRM version 1 protection to the current file.
ms.assetid: ad959e4a-faf7-4b61-9988-6878afcf3a90
keywords:
- Use_DRM windows Media Format
topic_type:
- apiref
api_name:
- Use_DRM
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Use\_DRM

The **Use\_DRM** attribute instructs the writer object to apply DRM version 1 protection to the current file.

## Global Constant

g\_wszWMUse\_DRM

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

Use [**IWMHeaderInfo::SetAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-setattribute?branch=master) to set this property to **TRUE** when creating DRM version 1 content. This property is not accessible from the reader object.

## See also

<dl> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




