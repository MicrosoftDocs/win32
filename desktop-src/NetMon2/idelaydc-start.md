---
description: IDelaydC::Start method - The Start method starts a capture.
ms.assetid: 92b25afc-d5d8-47e4-a155-4ed2a3571038
title: IDelaydC::Start method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.Start
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::Start method

The **Start** method starts a capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Start(
  [out] char *pFileName
);
```



## Parameters

<dl> <dt>

*pFileName* \[out\]
</dt> <dd>

Pointer to the name of the [*capture file*](c.md) used to store the network data. Be sure to cache this file name if it is needed for future reference.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                           | Description                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_PAUSED**</dt> </dl> | The capture is in a paused state and must be stopped before it can be restarted. Call [**IDelaydC::Stop**](idelaydc-stop.md) to stop the capture. For more information, see the Remarks section in this topic.<br/> |
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>       | The capture is already started.<br/>                                                                                                                                                                                 |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>  | The NPP is not connected to the network. Call [**IDelaydC::Connect**](idelaydc-connect.md) to connect to the network.<br/>                                                                                          |
| <dl> <dt>**NMERR\_NOT\_DELAYED**</dt> </dl>    | The NPP is connected to the network but not with the [**IDelaydC::Connect**](idelaydc-connect.md) method.<br/>                                                                                                      |



 

## Remarks

The location of the [*capture file*](c.md) is specified in your Windows registry, but you can use Network Monitor to change the file's location.

To restart the capture by using **IDelaydC::Start** and [**IDelaydC::Stop**](idelaydc-stop.md), you must call the [**IDelaydC::Configure**](idelaydc-configure.md) method to reconfigure the connection each time you call the **IDelaydC::Start** method to restart capturing data. When you start and stop the capture with these three methods, a new capture file is created each time the capture is started.

> [!Note]  
> You can also start and stop the capture by using the [**IDelaydC::Pause**](idelaydc-pause.md) and [**IDelaydC::Resume**](idelaydc-resume.md) methods. When you use these two methods, the captured data is stored in the same capture file.

 

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

[**IDelaydC::Configure**](idelaydc-configure.md)
</dt> <dt>

[**IDelaydC::Connect**](idelaydc-connect.md)
</dt> <dt>

[**IDelaydC::Pause**](idelaydc-pause.md)
</dt> <dt>

[**IDelaydC::Resume**](idelaydc-resume.md)
</dt> <dt>

[**IDelaydC::Stop**](idelaydc-stop.md)
</dt> </dl>

 

 




