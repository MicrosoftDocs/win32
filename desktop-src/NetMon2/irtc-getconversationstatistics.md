---
description: IRTC::GetConversationStatistics method - The GetConversationStatistics method retrieves session and station information about the current capture.
ms.assetid: 27f364cd-fee9-4262-b181-c5f15fb12e51
title: IRTC::GetConversationStatistics method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.GetConversationStatistics
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::GetConversationStatistics method

The **GetConversationStatistics** method retrieves [*session*](s.md) and [*station information*](s.md) about the current capture.

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

Pointer to a DWORD that contains the number of [*sessions*](s.md) recorded for the current capture.

</dd> <dt>

*lpSessionStats* \[out\]
</dt> <dd>

Pointer to a [SESSIONSTATS](sessionstats.md) structure.

</dd> <dt>

*nStations* \[out\]
</dt> <dd>

Pointer to a DWORD that contains the number of [*stations*](s.md) recorded for the current capture.

</dd> <dt>

*lpStationStats* \[out\]
</dt> <dd>

Pointer to a [STATIONSTATS](stationstats.md) structure.

</dd> <dt>

*fClearAfterReading* \[in\]
</dt> <dd>

Flag used to tell Network Monitor to clear out the internal storage of the [SESSIONSTATS](sessionstats.md) and [STATIONSTATS](stationstats.md) structures after it retrieves the current information.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                   | Description                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>          | The NPP is not connected to the network. Call [IRTC::Connect](irtc-connect.md) to connect the NPP to the network.<br/>                                                                                                      |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>          | The NPP is not capturing data. Call [IRTC::Start](irtc-start.md) to start the capture.<br/>                                                                                                                                 |
| <dl> <dt>**NMERR\_NOT\_REALTIME**</dt> </dl>           | The NPP is connected to the network but not with the [IRTC::Connect](irtc-connect.md) method.<br/>                                                                                                                          |
| <dl> <dt>**NMERR\_NO\_CONVERSATION\_STATS**</dt> </dl> | The configuration for this connection is set to not save conversation statistics. To save conversation statistics, stop the capture, set NoConversationStats = YES in the configuration BLOB, then restart the capture.<br/> |



 

## Remarks

This method can only be called while you are capturing data; if you call this method while the current capture is paused, the method will not succeed. To start a capture, call the [IRTC::Start](irtc-start.md) method.

To retrieve other types of statistics, call the [IRTC::GetTotalStatistics](irtc-gettotalstatistics.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IRTC](irtc.md)
</dt> <dt>

[IRTC::Connect](irtc-connect.md)
</dt> <dt>

[IRTC::GetTotalStatistics](irtc-gettotalstatistics.md)
</dt> <dt>

[IRTC::Start](irtc-start.md)
</dt> <dt>

[SESSIONSTATS](sessionstats.md)
</dt> <dt>

[STATIONSTATS](stationstats.md)
</dt> </dl>

 

 




