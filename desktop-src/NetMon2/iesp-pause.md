---
description: IESP::Pause method - The Pause method pauses the current capture.
ms.assetid: efbc8947-b9fe-4dbd-8097-375b5f99845e
title: IESP::Pause method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP.Pause
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP::Pause method

The **Pause** method pauses the current capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Pause(
   LPSTATISTICS lpStats
);
```



## Parameters

<dl> <dt>

*lpStats* 
</dt> <dd>

Obsolete.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                           | Description                                                                                                                   |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_PAUSED**</dt> </dl> | The capture is already paused.<br/>                                                                                     |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>  | The NPP is not capturing data. Call [IESP::Start](iesp-start.md) to start the capture.<br/>                            |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>  | The NPP is not connected to the network. Call [IESP::Connect](iesp-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_ESP**</dt> </dl>        | The NPP is connected to the network but not with the [IESP::Connect](iesp-connect.md) method.<br/>                     |



 

## Remarks

While the capture is in a paused state, new data is not added to the current [*capture file*](c.md) until you call the [IESP::Resume](iesp-resume.md) method to restart the capture. When **Pause** and **Resume** are used to stop and restart the capture, all captured information is put in the same capture file.

When you use the **IESP::Pause** and **IESP::Resume** methods to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) whenever the capture is running.

To restart the capture, call [IESP::Resume](iesp-resume.md). To stop the capture, call [IESP::Stop](iesp-stop.md).

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

[IESP::Connect](iesp-connect.md)
</dt> <dt>

[IESP::Resume](iesp-resume.md)
</dt> <dt>

[IESP::Start](iesp-start.md)
</dt> <dt>

[IESP::Stop](iesp-stop.md)
</dt> </dl>

 

 




