---
description: The QueryStations method provides a list of all computers who are currently capturing data using Network Monitor.
ms.assetid: feebcb28-914b-450e-95d4-10a60cbf1438
title: IStats::QueryStations method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.QueryStations
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::QueryStations method

The **QueryStations** method provides a list of all computers who are currently capturing data using Network Monitor.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE QueryStations(
  [in, out] QUERYTABLE *lpQueryTable
);
```



## Parameters

<dl> <dt>

*lpQueryTable* \[in, out\]
</dt> <dd>

Pointer to a [QUERYTABLE](querytable.md) structure. On input, this structure must contain the maximum number of computers you want Network Monitor to return and an array of [STATIONQUERY](stationquery.md) structures.

On output, this structure returns the number of computers that are capturing data and a [STATIONQUERY](stationquery.md) structure for each computer found. Note that this information may include computers using versions of Network Monitor that predate version 2.0.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is the following error code:



| Return code                                                                                           | Description                                                           |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**NMERR\_OUT\_OF\_MEMORY**</dt> </dl> | The memory required to process this query was unavailable.<br/> |



 

## Remarks

This method can be called at any time after [CreateNPPInterface](createnppinterface.md) is called. A call to this method is a synchronous call, which may take several seconds to complete as Network Monitor waits for remote computers to respond to the query. Only computers on the local subnet can be queried.

It is your responsibility to allocate the memory for the [QUERYTABLE](querytable.md) structure and free that memory after the table is no longer needed. This requirement includes the memory needed for the [STATIONQUERY](stationquery.md) array used in QUERYTABLE.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IStats](istats.md)
</dt> <dt>

[QUERYTABLE](querytable.md)
</dt> <dt>

[STATIONQUERY](stationquery.md)
</dt> </dl>

 

 




