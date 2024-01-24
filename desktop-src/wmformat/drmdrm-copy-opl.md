---
title: DRM_COPY_OPL structure (Wmdrmsdk.h)
description: The DRM\_COPY\_OPL structure holds information about the output protection levels (OPLs) specified in a license for copy actions.
ms.assetid: 439cbd56-05c1-46f8-86b9-ac1341902a40
keywords:
- DRM_COPY_OPL structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_COPY_OPL
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_COPY\_OPL structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_COPY\_OPL** structure holds information about the output protection levels (OPLs) specified in a license for copy actions.

## Syntax


```C++
typedef struct DRM_COPY_OPL {
  WORD               wMinimumCopyLevel;
  DRM_OPL_OUTPUT_IDS oplIdIncludes;
  DRM_OPL_OUTPUT_IDS oplIdExcludes;
} ;
```



## Members

<dl> <dt>

**wMinimumCopyLevel**
</dt> <dd>

Minimum OPL for copy actions.

</dd> <dt>

**oplIdIncludes**
</dt> <dd>

[**DRM\_OPL\_OUTPUT\_IDS**](drmdrm-opl-output-ids.md) structure containing the identifiers of technologies to allow. This member is used for output technologies that are assigned OPLs lower than the minimum copy level, but to which the content may be copied.

</dd> <dt>

**oplIdExcludes**
</dt> <dd>

[**DRM\_OPL\_OUTPUT\_IDS**](drmdrm-opl-output-ids.md) structure containing the output identifiers of technologies to restrict. This member is used for output technologies that are assigned OPLs that exceed the minimum copy level, but that the license issuer does not grant rights for copying to.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_PLAY\_OPL**](drmdrm-play-opl.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





