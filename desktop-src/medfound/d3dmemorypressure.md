---
description: Contains data for memory pressure reporting.
ms.assetid: 42cf0922-53cc-48b9-8359-b88583ef5f1c
title: D3DMEMORYPRESSURE structure (D3d9types.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DMEMORYPRESSURE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DMEMORYPRESSURE structure (D3d9types.h)

Contains data for memory pressure reporting.

## Syntax


```C++
typedef struct _D3DMEMORYPRESSURE {
  UINT64 BytesEvictedFromProcess;
  UINT64 SizeOfInefficientAllocation;
  DWORD  LevelOfEfficiency;
} D3DMEMORYPRESSURE;
```



## Members

<dl> <dt>

**BytesEvictedFromProcess**
</dt> <dd>

The number of bytes that were evicted by the process during the duration of the query.

</dd> <dt>

**SizeOfInefficientAllocation**
</dt> <dd>

The total number of bytes placed in nonoptimal memory segments, due to inadequate space within the preferred memory segments.

</dd> <dt>

**LevelOfEfficiency**
</dt> <dd>

The overall efficiency of the memory allocations that were placed in nonoptimal memory. The value is expressed as a percentage. For example, the value 95 indicates that the allocations placed in nonpreferred memory segments are 95% efficient. This number should not be considered an exact measurement.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>D3d9types.h (include D3d9.h)</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Structures](direct3d-video-structures.md)
</dt> <dt>

[Memory Pressure Reporting](memory-pressure-reporting.md)
</dt> </dl>

 

 




