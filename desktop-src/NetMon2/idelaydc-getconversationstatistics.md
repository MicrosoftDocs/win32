---
description: IDelaydC::GetConversationStatistics method - The GetConversationStatistics method retrieves session and station information about the current capture.
ms.assetid: 0164fa0e-90f2-4b97-be9d-55d172f8112d
title: IDelaydC::GetConversationStatistics method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.GetConversationStatistics
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::GetConversationStatistics method

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



| Return code                                                                                                   | Description                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>          | The NPP is not connected to the network. Call [IDelaydC::Connect](idelaydc-connect.md) to connect the NPP to the network.<br/>                                                                                                  |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>          | The NPP is not capturing data. Call [IDelaydC::Start](idelaydc-start.md) to start the capture.<br/>                                                                                                                             |
| <dl> <dt>**NMERR\_NOT\_DELAYED**</dt> </dl>            | The NPP is connected to the network but not with the [IDelaydC::Connect](idelaydc-connect.md) method.<br/>                                                                                                                      |
| <dl> <dt>**NMERR\_NO\_CONVERSATION\_STATS**</dt> </dl> | The configuration for this connection is set to not save conversation statistics. To save conversation statistics, stop the capture, set NoConversationStats = YES in the configuration BLOB, and then restart the capture.<br/> |



 

## Remarks

This method can only be called only while data capture is in progress; when the current capture is paused, calls to this method will not succeed. To start a capture, call the [IDelaydC::Start](idelaydc-start.md) method.

To retrieve other types of statistics, call [IDelaydC::GetTotalStatistics](idelaydc-gettotalstatistics.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IDelaydC](idelaydc.md)
</dt> <dt>

[IDelaydC::Connect](idelaydc-connect.md)
</dt> <dt>

[IDelaydC::GetTotalStatistics](idelaydc-gettotalstatistics.md)
</dt> <dt>

[IDelaydC::Start](idelaydc-start.md)
</dt> <dt>

[SESSIONSTATS](sessionstats.md)
</dt> <dt>

[STATIONSTATS](stationstats.md)
</dt> </dl>

 

 




