---
description: IDelaydC::Stop method - The Stop method stops the current capture.
ms.assetid: 1b627137-e72d-4425-98d9-e296fb07e509
title: IDelaydC::Stop method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.Stop
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::Stop method

The **Stop** method stops the current capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Stop(
  [out] LPSTATISTICS lpStats
);
```



## Parameters

<dl> <dt>

*lpStats* \[out\]
</dt> <dd>

Pointer to a [STATISTICS](statistics.md) structure that contains network statistics such as total frames and total bytes captured.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                          | Description                                                                                                                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network. Call [IDelaydC::Connect](idelaydc-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl> | The NPP is not capturing data. Call [IDelaydC::Start](idelaydc-start.md) to start the capture.<br/>                            |
| <dl> <dt>**NMERR\_NOT\_DELAYED**</dt> </dl>   | The NPP is connected to the network but not with the [IDelaydC::Connect](idelaydc-connect.md) method.<br/>                     |



 

## Remarks

When **IDelaydC::Stop** is called, Network Monitor stops capturing data and closes the [*capture file*](c.md). (The name of the capture file was returned when [IDelaydC::Start](idelaydc-start.md) was called). You can now look at the contents of the capture file.

When you stop and start the capture, make sure you call the [IDelaydC::Configure](idelaydc-configure.md) method each time you call [IDelaydC::Start](idelaydc-start.md) to restart the capture.

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

[IDelaydC::Configure](idelaydc-configure.md)
</dt> <dt>

[IDelaydC::Start](idelaydc-start.md)
</dt> <dt>

[STATISTICS](statistics.md)
</dt> </dl>

 

 




