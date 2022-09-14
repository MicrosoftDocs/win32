---
description: The QUERYTABLE structure provides a list of the computers that are currently using Network Monitor to capture network data.
ms.assetid: b701a6d5-df6d-4ee9-b008-a568a410dc14
title: QUERYTABLE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- QUERYTABLE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# QUERYTABLE structure

The **QUERYTABLE** structure provides a list of the computers that are currently using Network Monitor to capture network data.

## Syntax


```C++
typedef struct _QUERYTABLE {
  DWORD        nStationQueries;
  STATIONQUERY StationQuery[1];
} QUERYTABLE, *LPQUERYTABLE;
```



## Members

<dl> <dt>

**nStationQueries**
</dt> <dd>

On input, the maximum number of computers you want Network Monitor to return.

On output, the number of [STATIONQUERY](stationquery.md) structures returned by Network Monitor. Each **STATIONQUERY** structure represents a computer that is currently capturing data.

</dd> <dt>

**StationQuery**
</dt> <dd>

On input, an array of empty [STATIONQUERY](stationquery.md) structures that contains the number of elements specified in **nStationQueries**.

On output, a filled [STATIONQUERY](stationquery.md) structure for each computer that is capturing data. The number of filled elements is returned by **nStationQueries**.

</dd> </dl>

## Remarks

The memory for this structure and the [STATIONQUERY](stationquery.md) array must be allocated by the calling application and freed after the information is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[IDelaydC::QueryStations](idelaydc-querystations.md)
</dt> <dt>

[IESP::QueryStations](iesp-querystations.md)
</dt> <dt>

[IRTC::QueryStations](irtc-querystations.md)
</dt> <dt>

[IStats::QueryStations](istats-querystations.md)
</dt> <dt>

[STATIONQUERY](stationquery.md)
</dt> </dl>

 

 




