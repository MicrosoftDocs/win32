---
description: IESP::Stop method - The Stop method stops the current capture.
ms.assetid: d2d4e51a-c6a4-4aec-a805-929af621ffb3
title: IESP::Stop method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP.Stop
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP::Stop method

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



| Return code                                                                                          | Description                                                                                                                   |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network. Call [IESP::Connect](iesp-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl> | The NPP is not capturing data. Call [IESP::Start](iesp-start.md) to start the capture.<br/>                            |
| <dl> <dt>**NMERR\_NOT\_ESP**</dt> </dl>       | The NPP is connected to the network but not with the [IESP::Connect](iesp-connect.md) method.<br/>                     |



 

## Remarks

When the **IESP::Stop** method is called, Network Monitor stops capturing data and closes the [*capture file.*](c.md) (The name of the capture file was returned when [IESP::Start](iesp-start.md) was called.) You can now look at the contents of the capture file.

When you stop and restart the capture, make sure to call the [IESP::Configure](iesp-configure.md) method each time you call [IESP::Start](iesp-start.md) to restart the capture.

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

[IESP::Start](iesp-start.md)
</dt> <dt>

[STATISTICS](statistics.md)
</dt> </dl>

 

 




