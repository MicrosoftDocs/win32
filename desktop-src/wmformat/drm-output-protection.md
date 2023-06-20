---
title: DRM_OUTPUT_PROTECTION structure (Wmdrmsdk.h)
description: The DRM\_OUTPUT\_PROTECTION structure holds information about an output protection technology.
ms.assetid: e458013d-b77e-4e03-bff9-e3ecfc72ebdb
keywords:
- DRM_OUTPUT_PROTECTION structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_OUTPUT_PROTECTION
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_OUTPUT\_PROTECTION structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_OUTPUT\_PROTECTION** structure holds information about an output protection technology.

## Syntax


```C++
typedef struct DRM_OUTPUT_PROTECTION {
  GUID guidId;
  BYTE bConfigData;
} ;
```



## Members

<dl> <dt>

**guidId**
</dt> <dd>

GUID identifying the output protection technology.

</dd> <dt>

**bConfigData**
</dt> <dd>

Configuration data for the technology.

</dd> </dl>

## Remarks

**DRM\_AUDIO\_OUTPUT\_PROTECTION** and **DRM\_VIDEO\_OUTPUT\_PROTECTION** are both defined as **DRM\_OUTPUT\_PROTECTION** in **typedef** statements.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_OUTPUT\_PROTECTION\_EX**](drm-output-protection-ex.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





