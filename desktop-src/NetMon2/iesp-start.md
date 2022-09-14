---
description: IESP::Start method - The Start method starts a capture.
ms.assetid: 8bf8c0c7-20be-4404-8ea5-b28b4c658523
title: IESP::Start method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP.Start
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP::Start method

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



| Return code                                                                                           | Description                                                                                                                            |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_PAUSED**</dt> </dl> | The capture is paused and must be stopped before it can be restarted. Call [IESP::Stop](iesp-stop.md) to stop the capture.<br/> |
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>       | The capture is already started.<br/>                                                                                             |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>  | The NPP is not connected to the network. Call [IESP::Connect](iesp-connect.md) to connect the NPP to the network.<br/>          |
| <dl> <dt>**NMERR\_NOT\_ESP**</dt> </dl>        | The NPP is connected to the network but not with the [IESP::Connect](iesp-connect.md) method.<br/>                              |



 

## Remarks

The location of the [*capture file*](c.md) is specified in the Windows registry, but you can use Network Monitor to change the directory location.

When you restart the capture by using the IESP::Start and [IESP::Stop](iesp-stop.md) methods, you must call the [IESP::Configure](iesp-configure.md) method to reconfigure the connection each time you call IESP::Start to restart capturing data. When you start and stop the capture with these three methods, a new capture file is created each time the capture is started.

> [!Note]  
> You can also start and stop the capture by using the [IESP::Pause](iesp-pause.md) and [IESP::Resume](iesp-resume.md) methods. When these two methods are used, the captured data is stored in the same capture file.

 

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

[IESP::Configure](iesp-configure.md)
</dt> <dt>

[IESP::Connect](iesp-connect.md)
</dt> <dt>

[IESP::Pause](iesp-pause.md)
</dt> <dt>

[IESP::Resume](iesp-resume.md)
</dt> <dt>

[IESP::Stop](iesp-stop.md)
</dt> </dl>

 

 




