---
description: IRTC::Pause method - The Pause method pauses the current capture.
ms.assetid: 8c7b310e-de04-4bd8-9c96-3c5948e610be
title: IRTC::Pause method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.Pause
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::Pause method

The **Pause** method pauses the current capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Pause();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                           | Description                                                                                                                   |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_PAUSED**</dt> </dl> | The capture is already paused.<br/>                                                                                     |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>  | The NPP is not capturing data. Call [IRTC::Start](irtc-start.md) to start the capture.<br/>                            |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>  | The NPP is not connected to the network. Call [IRTC::Connect](irtc-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_REALTIME**</dt> </dl>   | The NPP is connected to the network but not with the [IRTC::Connect](irtc-connect.md) method.<br/>                     |



 

## Remarks

While the capture is in a paused state, new frames are not captured until the [IRTC::Resume](irtc-resume.md) method is called to restart the capture.

When you use the **IRTC::Pause** and **IRTC::Resume** methods to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) whenever the capture is running.

To restart the capture call [IRTC::Resume](irtc-resume.md). To stop the capture, call [IRTC::Stop](irtc-stop.md).

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

[IRTC::Resume](irtc-resume.md)
</dt> <dt>

[IRTC::Start](irtc-start.md)
</dt> <dt>

[IRTC::Stop](irtc-stop.md)
</dt> </dl>

 

 




