---
description: IRTC::GetControlState method - The GetControlState method retrieves the state of the capture, which indicates if the capture is running or paused.
ms.assetid: ae0cf869-bf5b-4c23-a924-014554053c92
title: IRTC::GetControlState method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.GetControlState
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::GetControlState method

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



| Return code                                                                                          | Description                                                                                                                   |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network. Call [IRTC::Connect](irtc-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_REALTIME**</dt> </dl>  | The NPP is connected to the network but not with the [IRTC::Connect](irtc-connect.md) method.<br/>                     |



 

## Remarks

This method can be called any time the NPP is connected to the network. You can use this method to find out if a capture is running, if the capture is paused, or if the capture has been stopped but the NPP is still connected.

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

[IRTC::Pause](irtc-pause.md)
</dt> <dt>

[IRTC::Start](irtc-start.md)
</dt> <dt>

[IRTC::Stop](irtc-stop.md)
</dt> </dl>

 

 




