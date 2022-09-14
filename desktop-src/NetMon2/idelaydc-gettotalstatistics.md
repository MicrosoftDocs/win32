---
description: IDelaydC::GetTotalStatistics method - The GetTotalStatistics method retrieves the total statistics for the current capture.
ms.assetid: 904c7496-5603-41b9-8481-06fa31f6f112
title: IDelaydC::GetTotalStatistics method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.GetTotalStatistics
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::GetTotalStatistics method

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

Flag used to tell Network Monitor how to handle the internal storage of the total statistics. A setting of **TRUE** tells Network Monitor to clear out the internal storage of the total statistics after the current information is retrieved.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                          | Description                                                                                                                   |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network. Call [IDelaydC::Connect](idelaydc-connect.md) to connect to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_DELAYED**</dt> </dl>   | The NPP is connected to the network but not with the [IDelaydC::Connect](idelaydc-connect.md) method.<br/>             |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl> | The NPP is not capturing data. Call [IDelaydC::Start](idelaydc-start.md) to start capturing data.<br/>                 |



 

## Remarks

This method returns data only while a capture is in progress; when the capture is paused, calls to this method will not succeed.

Network Monitor also stores [*conversation statistics*](c.md), which can be retrieved by calling the [IDelaydC::GetConversationStatistics](idelaydc-getconversationstatistics.md) method.

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

[IDelaydC::GetConversationStatistics](idelaydc-getconversationstatistics.md)
</dt> <dt>

[IDelaydC::Start](idelaydc-start.md)
</dt> <dt>

[STATISTICS](statistics.md)
</dt> </dl>

 

 




