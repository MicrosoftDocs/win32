---
description: IDelaydC::Resume method - The Resume method restarts a paused capture.
ms.assetid: 4fa47220-d323-407b-9dae-704969f66bdd
title: IDelaydC::Resume method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.Resume
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::Resume method

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



| Return code                                                                                                | Description                                                                                                                               |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_NOT\_PAUSED**</dt> </dl> | The capture is not paused. Call [**IDelaydC::Pause**](idelaydc-pause.md) to pause the capture.<br/>                                |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>       | The NPP is not connected to the network. Call [**IDelaydC::Connect**](idelaydc-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_DELAYED**</dt> </dl>         | The NPP is connected to the network but not with the [**IDelaydC::Connect**](idelaydc-connect.md) method.<br/>                     |



 

## Remarks

While the capture is paused, new data is not added to the current [*capture file*](c.md) until the **IDelaydC::Resume** method is called to restart the capture. When [**Pause**](idelaydc-pause.md) and **Resume** are used to stop and restart the capture, all captured information is put in the same capture file.

When using [**Pause**](idelaydc-pause.md) and **Resume** to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) to the existing statistics for the current capture.

To stop the capture, call [**IDelaydC::Stop**](idelaydc-stop.md).

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

[**IDelaydC::Connect**](idelaydc-connect.md)
</dt> <dt>

[**IDelaydC::Pause**](idelaydc-pause.md)
</dt> <dt>

[**IDelaydC::Stop**](idelaydc-stop.md)
</dt> </dl>

 

 




