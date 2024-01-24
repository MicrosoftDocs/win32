---
description: Provides a list of all computers currently using Network Monitor to capture network data.
ms.assetid: 57e7b8e1-99b8-4194-b6dc-401235be4ef4
title: IRTC::QueryStations method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.QueryStations
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::QueryStations method

The **QueryStations** method provides a list of all computers currently using Network Monitor to capture network data.

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

A pointer to a [**QUERYTABLE**](querytable.md) structure. On input, this structure must contain the maximum number of computers you want Network Monitor to return and an array of [**STATIONQUERY**](stationquery.md) structures.

On output, this structure returns the number of computers capturing data and a [**STATIONQUERY**](stationquery.md) structure for each computer found. Be aware that this may include computers using versions of Network Monitor that predate version 2.0.

</dd> </dl>

## Return value

If the method is successful, the return value is **NMERR\_SUCCESS**.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                           | Description                                                          |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**NMERR\_OUT\_OF\_MEMORY**</dt> </dl> | The memory required to process this query is unavailable.<br/> |



 

## Remarks

This method can be called at any time after the [**CreateNPPInterface**](createnppinterface.md) method is called. A call to this method is a synchronous call, which may take several seconds to complete while Network Monitor waits for remote computers to respond to the query. Only computers on the local subnet can be queried.

The user must allocate the memory for the [**QUERYTABLE**](querytable.md) structure and free that memory after the table is no longer required. This requirement includes memory needed for the [**STATIONQUERY**](stationquery.md) array used in **QUERYTABLE**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[**IRTC**](irtc.md)
</dt> <dt>

[**QUERYTABLE**](querytable.md)
</dt> <dt>

[**STATIONQUERY**](stationquery.md)
</dt> </dl>

 

 




