---
title: Is\_Protected
description: The Is\_Protected attribute is a file-level attribute specifying whether the content in the file was protected using digital rights management (DRM).
ms.assetid: 6fe63d9b-67ec-47a8-ba20-657434c7a15b
keywords:
- Is_Protected windows Media Format
topic_type:
- apiref
api_name:
- Is_Protected
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Is\_Protected

The **Is\_Protected** attribute is a file-level attribute specifying whether the content in the file was protected using digital rights management (DRM).

## Global Constant

g\_wszWMProtected

## Data Type

**WMT\_TYPE\_BOOL**

## Remarks

This is a coded attribute. Retrieving this property provides the same information as calling [**WMIsContentProtected**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmiscontentprotected?branch=master).

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




