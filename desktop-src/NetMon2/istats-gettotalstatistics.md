---
description: IStats::GetTotalStatistics method - The GetTotalStatistics method retrieves the total statistics for the current capture.
ms.assetid: 494634f6-a9b3-4a50-8920-2387be9ba30f
title: IStats::GetTotalStatistics method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.GetTotalStatistics
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::GetTotalStatistics method

The **GetTotalStatistics** method retrieves the [*total statistics*](t.md) for the current [*capture*](c.md).

## Syntax


```C++
HRESULT STDMETHODCALLTYPE GetTotalStatistics(
  [out] LPSTATISTICS lpStats,
  [in]  BOOL         fClearAfterReading
);
```



## Parameters

<dl> <dt>

*lpStats* \[out\]
</dt> <dd>

Pointer to a [STATISTICS](statistics.md)structure that provides the total statistics for the capture. It is the caller's responsibility to allocate and free the memory used by the **STATISTICS** structure.

</dd> <dt>

*fClearAfterReading* \[in\]
</dt> <dd>

Flag used to tell Network Monitor how to handle the internal storage of the total statistics. A setting of TRUE tells Network Monitor to clear out the internal storage of the total statistics after the current information is retrieved.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                            | Description                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>   | The NPP is not connected to the network. Call the [IStats::Connect](istats-connect.md) method to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_STATS\_ONLY**</dt> </dl> | The NPP is connected to the network but not with the [IStats::Connect](istats-connect.md) method.<br/>                                |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>   | The NPP is not capturing data. Call the [IStats::Start](istats-start.md) method to start capturing data.<br/>                         |



 

## Remarks

This method returns data only while a capture is in progress, including while the capture is paused.

Network Monitor also stores [*conversation statistics*](c.md), which can be retrieved by calling the [IStats::GetConversationStatistics](istats-getconversationstatistics.md) method.

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

[IStats::Connect](istats-connect.md)
</dt> <dt>

[IStats::GetConversationStatistics](istats-getconversationstatistics.md)
</dt> <dt>

[IStats::Start,](istats-start.md)
</dt> <dt>

[STATISTICS](statistics.md)
</dt> </dl>

 

 




