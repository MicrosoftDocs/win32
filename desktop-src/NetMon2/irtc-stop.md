---
description: IRTC::Stop method - The Stop method stops the current capture.
ms.assetid: 64a80ff1-5a48-4be8-835d-a3d304ebb324
title: IRTC::Stop method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.Stop
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::Stop method

The **Stop** method stops the current capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Stop();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                          | Description                                                                                                                   |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network. Call [IRTC::Connect](irtc-connect.md) to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl> | The NPP is not capturing data. Call [IRTC::Start](irtc-start.md) to start the capture.<br/>                            |
| <dl> <dt>**NMERR\_NOT\_REALTIME**</dt> </dl>  | The NPP is connected to the network but not with the [IRTC::Connect](irtc-connect.md) method.<br/>                     |



 

## Remarks

When you restart the capture after calling the **IRTC::Stop** method, make sure to call [IRTC::Configure](irtc-configure.md) each time you call [IRTC::Start](irtc-start.md) to restart the capture.

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

[IRTC::Configure](irtc-configure.md)
</dt> <dt>

[IRTC::Start](irtc-start.md)
</dt> </dl>

 

 




