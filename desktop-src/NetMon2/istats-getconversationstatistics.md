---
description: Retrieves session and station information about the current capture.
ms.assetid: 7fc436fc-b569-402d-a1ea-c1bb65de8a9e
title: IStats::GetConversationStatistics method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.GetConversationStatistics
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::GetConversationStatistics method

The **GetConversationStatistics** method retrieves session and station information about the current capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE GetConversationStatistics(
  [out] DWORD          *nSessions,
  [out] LPSESSIONSTATS lpSessionStats,
  [out] DWORD          *nStations,
  [out] LPSTATIONSTATS lpStationStats,
  [in]  BOOL           fClearAfterReading
);
```



## Parameters

<dl> <dt>

*nSessions* \[out\]
</dt> <dd>

A pointer to a DWORD that contains the number of [*sessions*](s.md) recorded for the current capture.

</dd> <dt>

*lpSessionStats* \[out\]
</dt> <dd>

A pointer to a [**SESSIONSTATS**](sessionstats.md) structure.

</dd> <dt>

*nStations* \[out\]
</dt> <dd>

A pointer to a DWORD that contains the number of [*stations*](s.md) recorded for the current capture.

</dd> <dt>

*lpStationStats* \[out\]
</dt> <dd>

A pointer to a [**STATIONSTATS**](stationstats.md) structure.

</dd> <dt>

*fClearAfterReading* \[in\]
</dt> <dd>

Flag used to instruct Network Monitor to clear the internal storage of the [**SESSIONSTATS**](sessionstats.md) and [**STATIONSTATS**](stationstats.md) structures after the current data is retrieved.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                   | Description                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>          | The NPP is not connected to the network. Call [**IStats::Connect**](istats-connect.md) to connect the NPP to the network.<br/>                                                                                                      |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>          | The NPP is not capturing data. Call [**IStats::Start**](istats-start.md) to start the capture.<br/>                                                                                                                                 |
| <dl> <dt>**NMERR\_NOT\_STATS\_ONLY**</dt> </dl>        | The NPP is connected to the network, but not with the [**IStats::Connect**](istats-connect.md) method.<br/>                                                                                                                         |
| <dl> <dt>**NMERR\_NO\_CONVERSATION\_STATS**</dt> </dl> | The configuration for this connection is set to not save conversation statistics. To save conversation statistics, stop the capture, set **NoConversationStats = YES** in the configuration BLOB, and then restart the capture.<br/> |



 

## Remarks

This method can be called only while data capture is in progress; when the current capture is paused, a call to this method will not succeed.

To start a capture, call the [**IStats::Start**](istats-start.md) method. To retrieve other types of statistics, call [**IStats::GetTotalStatistics**](istats-gettotalstatistics.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[**IStats**](istats.md)
</dt> <dt>

[**IStats::GetTotalStatistics**](istats-gettotalstatistics.md)
</dt> <dt>

[**IStats::Start**](istats-start.md)
</dt> <dt>

[**IStats::Connect**](istats-connect.md)
</dt> <dt>

[**SESSIONSTATS**](sessionstats.md)
</dt> <dt>

[**STATIONSTATS**](stationstats.md)
</dt> </dl>

 

 




