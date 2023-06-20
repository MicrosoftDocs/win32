---
title: DRM_OPL_OUTPUT_IDS structure (Wmdrmsdk.h)
description: The DRM\_OPL\_OUTPUT\_IDS structure holds a number of output protection level (OPL) output identifiers.
ms.assetid: 3627f2a7-1cea-400b-82e7-678898ccc386
keywords:
- DRM_OPL_OUTPUT_IDS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_OPL_OUTPUT_IDS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_OPL\_OUTPUT\_IDS structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_OPL\_OUTPUT\_IDS** structure holds a number of output protection level (OPL) output identifiers.

## Syntax


```C++
typedef struct DRM_OPL_OUTPUT_IDS {
  WORD cIds;
  GUID *rgIds;
} ;
```



## Members

<dl> <dt>

**cIds**
</dt> <dd>

Number of identifiers in the array referenced by **rgIds**.

</dd> <dt>

**rgIds**
</dt> <dd>

Address of an array of GUIDs. Each member of the array contains an OPL output identifier.

</dd> </dl>

## Remarks

This structure is used as a member of the [**DRM\_COPY\_OPL**](drmdrm-copy-opl.md) and [**DRM\_PLAY\_OPL**](drmdrm-play-opl.md) structures to identify groups of output identifiers.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





