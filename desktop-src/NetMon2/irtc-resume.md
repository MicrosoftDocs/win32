---
description: IRTC::Resume method - The Resume method restarts a paused capture.
ms.assetid: 685dfdee-3bd0-44b3-ac4f-c9960cf77c5c
title: IRTC::Resume method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.Resume
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::Resume method

The **Resume** method restarts a paused capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Resume();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                | Description                                                                                                                   |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_NOT\_PAUSED**</dt> </dl> | The capture is not paused. Call [IRTC::Pause](irtc-pause.md) to pause the capture.<br/>                                |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>       | The NPP is not connected to the network. Call [IRTC::Connect](irtc-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_REALTIME**</dt> </dl>        | The NPP is connected to the network but not with the [IRTC::Connect](irtc-connect.md) method.<br/>                     |



 

## Remarks

While the capture is in a paused state, new data is not captured until a call to the [IRTC::Resume](idelaydc-resume.md) method restarts the capture.

When using the **Pause** and **Resume** methods to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) to the existing statistics for the current capture.

To stop the capture, call the [IRTC::Stop](irtc-stop.md) method.

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

[IRTC::Stop](irtc-stop.md)
</dt> </dl>

 

 




