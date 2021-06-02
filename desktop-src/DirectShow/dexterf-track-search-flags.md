---
description: The DEXTERF\_TRACK\_SEARCH\_FLAGS enumeration specifies the boundary conditions on a search for an object in the timeline.
ms.assetid: 9a66ea17-5c2c-41fd-8a7b-c9918b10c8c9
title: DEXTERF_TRACK_SEARCH_FLAGS enumeration (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DEXTERF_TRACK_SEARCH_FLAGS
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# DEXTERF\_TRACK\_SEARCH\_FLAGS enumeration

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `DEXTERF_TRACK_SEARCH_FLAGS` enumeration specifies the boundary conditions on a search for an object in the timeline.

## Syntax


```C++
typedef enum  { 
  DEXTERF_BOUNDING    = -1,
  DEXTERF_EXACTLY_AT  = 0,
  DEXTERF_FORWARDS    = 1
} DEXTERF_TRACK_SEARCH_FLAGS;
```



## Constants

<dl> <dt>

<span id="DEXTERF_BOUNDING"></span><span id="dexterf_bounding"></span>**DEXTERF\_BOUNDING**
</dt> <dd>

Search for an object that spans the specified time.

</dd> <dt>

<span id="DEXTERF_EXACTLY_AT"></span><span id="dexterf_exactly_at"></span>**DEXTERF\_EXACTLY\_AT**
</dt> <dd>

Search for an object that starts exactly at the specified time.

</dd> <dt>

<span id="DEXTERF_FORWARDS"></span><span id="dexterf_forwards"></span>**DEXTERF\_FORWARDS**
</dt> <dd>

Search for an object that starts at the specified time or later.

</dd> </dl>

## Remarks

These boundary conditions are summarized in the following table.



| Enumeration value    | Boundary condition                        |
|----------------------|-------------------------------------------|
| DEXTERF\_BOUNDING    | Start <= TimeStop > Time<br/> |
| DEXTERF\_EXACTLY\_AT | Start == Time                             |
| DEXTERF\_FORWARDS    | Start >= Time                          |



 

-   Start: start time of the retrieved object.
-   Stop: stop time of the retrieved object.
-   Time: specified search time.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineTrack::GetSrcAtTime**](iamtimelinetrack-getsrcattime.md)
</dt> </dl>

 

 




