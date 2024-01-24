---
title: DRM_ATTR_DATATYPE enumeration (Wmdrmsdk.h)
description: The DRM\_ATTR\_DATATYPE enumeration defines the data types used for DRM attributes and properties.
ms.assetid: ccad16e2-475d-4cc7-b773-f17038d2754a
keywords:
- DRM_ATTR_DATATYPE enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- DRM_ATTR_DATATYPE
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_ATTR\_DATATYPE enumeration

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_ATTR\_DATATYPE** enumeration defines the data types used for DRM attributes and properties.

## Syntax


```C++
typedef enum DRM_ATTR_DATATYPE { 
  DRM_TYPE_DWORD   = 0,
  DRM_TYPE_STRING  = 1,
  DRM_TYPE_BINARY  = 2,
  DRM_TYPE_BOOL    = 3,
  DRM_TYPE_QWORD   = 4,
  DRM_TYPE_WORD    = 5,
  DRM_TYPE_GUID    = 6
} ;
```



## Constants

<dl> <dt>

<span id="DRM_TYPE_DWORD"></span><span id="drm_type_dword"></span>**DRM\_TYPE\_DWORD**
</dt> <dd>

The property is a 4-byte **DWORD** value.

</dd> <dt>

<span id="DRM_TYPE_STRING"></span><span id="drm_type_string"></span>**DRM\_TYPE\_STRING**
</dt> <dd>

The property is a null-terminated Unicode string.

</dd> <dt>

<span id="DRM_TYPE_BINARY"></span><span id="drm_type_binary"></span>**DRM\_TYPE\_BINARY**
</dt> <dd>

The property is an array of bytes.

</dd> <dt>

<span id="DRM_TYPE_BOOL"></span><span id="drm_type_bool"></span>**DRM\_TYPE\_BOOL**
</dt> <dd>

The property is a 4-byte Boolean value.

</dd> <dt>

<span id="DRM_TYPE_QWORD"></span><span id="drm_type_qword"></span>**DRM\_TYPE\_QWORD**
</dt> <dd>

The property is an 8-byte **QWORD** value.

</dd> <dt>

<span id="DRM_TYPE_WORD"></span><span id="drm_type_word"></span>**DRM\_TYPE\_WORD**
</dt> <dd>

The property is a 2-byte **WORD** value.

</dd> <dt>

<span id="DRM_TYPE_GUID"></span><span id="drm_type_guid"></span>**DRM\_TYPE\_GUID**
</dt> <dd>

The property is a 128-bit (6-byte) GUID value.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](drm-enumeration-types.md)
</dt> </dl>

 

 





