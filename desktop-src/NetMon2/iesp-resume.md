---
description: IESP::Resume method - The Resume method restarts a paused capture.
ms.assetid: 047ea5f8-de3d-40db-ada3-fc0ef4deccef
title: IESP::Resume method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP.Resume
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP::Resume method

The **Resume** method restarts a paused capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Resume();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                | Description                                                                                                               |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_NOT\_PAUSED**</dt> </dl> | The capture is not paused. Call [**IESP::Pause**](iesp-pause.md) to pause the capture.<br/>                        |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>       | The NPP is not connected to the network. Call [**IESP::Connect**](iesp-connect.md) to connect to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_ESP**</dt> </dl>             | The NPP is connected to the network, but not with the [**IESP::Connect**](iesp-connect.md) method.<br/>            |



 

## Remarks

While the capture is in a paused state, new data is not added to the current [*capture file*](c.md) until **IESP::Resume** is called to restart the capture. When **Pause** and **Resume** are used to stop and restart the capture, all captured information is put in the same capture file.

When using **Pause** and **Resume** to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) to the existing statistics for the current capture.

To stop the capture, call [**IESP::Stop**](iesp-stop.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IESP](iesp.md)
</dt> <dt>

[**IESP::Connect**](iesp-connect.md)
</dt> <dt>

[**IESP::Pause**](iesp-pause.md)
</dt> <dt>

[**IESP::Stop**](iesp-stop.md)
</dt> </dl>

 

 




