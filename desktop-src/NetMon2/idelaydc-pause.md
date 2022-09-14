---
description: IDelaydC::Pause method - The Pause method pauses the current capture.
ms.assetid: 9d5e11d1-8c45-4cf5-9fea-10c9e7a6fe86
title: IDelaydC::Pause method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.Pause
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::Pause method

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



| Return code                                                                                           | Description                                                                                                                           |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_PAUSED**</dt> </dl> | The capture is already in a paused state.<br/>                                                                                  |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>  | The NPP is not capturing data. Call [IDelaydC::Start](idelaydc-start.md) to start the capture.<br/>                            |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>  | The NPP is not connected to the network. Call [IDelaydC::Connect](idelaydc-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_DELAYED**</dt> </dl>    | The NPP is connected to the network but not with the [IDelaydC::Connect](idelaydc-connect.md) method.<br/>                     |



 

## Remarks

While the capture is in a paused state, new data is not added to the current [*capture file*](c.md) until the **IDelaydC::Resume** method is called to restart the capture. When **Pause** and **Resume** are used to stop and restart the capture, all captured information is put in the same capture file.

When using **IDelaydC::Pause** and **IDelaydC::Resume** to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) whenever the capture is running.

To restart the capture, call [IDelaydC::Resume](idelaydc-resume.md).

To stop the capture, call [IDelaydC::Stop](idelaydc-stop.md).

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

[IDelaydC::Resume](idelaydc-resume.md)
</dt> <dt>

[IDelaydC::Start](idelaydc-start.md)
</dt> <dt>

[IDelaydC::Stop](idelaydc-stop.md)
</dt> </dl>

 

 




