---
title: DO_DOWNLOAD_ENUM_CATEGORY structure
description: Used by **IDOManager::EnumDownloads** to filter the downloads enumeration by the specific property's value.
keywords:
- DO_DOWNLOAD_ENUM_CATEGORY structure
topic_type:
- apiref
api_name:
- DO_DOWNLOAD_ENUM_CATEGORY
api_location:
- do.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/03/2019
---

# DO_DOWNLOAD_ENUM_CATEGORY structure

The **DO_DOWNLOAD_ENUM_CATEGORY** structure is used by **IDOManager::EnumDownloads** to filter the downloads enumeration by the specific property's value.

## Syntax
```cpp
typedef struct _DO_DOWNLOAD_ENUM_CATEGORY
{
  DODownloadProperty Property;
  LPCWSTR Value;
} DO_DOWNLOAD_ENUM_CATEGORY;
```

## Members

`Property`

The property name to be used for the download enumeration. These properties are supported for enumeration purposes.
- **DODownloadProperty_Id**
- **DODownloadProperty_Uri**
- **DODownloadProperty_ContentId**
- **DODownloadProperty_DisplayName**
- **DODownloadProperty_LocalPath**

`Value`

The property's value.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
