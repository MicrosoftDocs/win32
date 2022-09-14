---
description: IStats::GetControlState method - The GetControlState method retrieves the state of the capture, which indicates if the capture is running or paused.
ms.assetid: 0faf2300-d9ff-4fe0-9d50-18beafd1daea
title: IStats::GetControlState method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.GetControlState
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::GetControlState method

The **GetControlState** method retrieves the state of the [*capture*](c.md), which indicates if the capture is running or paused.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE GetControlState(
  [out] BOOL *IsRunnning,
  [out] BOOL *IsPaused
);
```



## Parameters

<dl> <dt>

*IsRunnning* \[out\]
</dt> <dd>

Indicator that the current capture is running, including if the capture is paused.

</dd> <dt>

*IsPaused* \[out\]
</dt> <dd>

Indicator that the current capture is paused.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                            | Description                                                                                                                       |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>   | The NPP is not connected to the network. Call [IStats::Connect](istats-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_STATS\_ONLY**</dt> </dl> | The NPP is connected to the network but not with the [IStats::Connect](istats-connect.md) method.<br/>                     |



 

## Remarks

This method can be called any time the NPP is connected to the network. You can use this method to find out if a capture is running, if the capture is paused, or if the capture has been stopped but the NPP is not disconnected.

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

[IStats::Pause](istats-pause.md)
</dt> <dt>

[IStatsC::Start](istats-start.md)
</dt> <dt>

[IStatsC::Stop](istats-stop.md)
</dt> </dl>

 

 




