---
description: IESP::Disconnect method - The Disconnect method disconnects the NPP from the network.
ms.assetid: 962e033d-a51c-47a2-83dc-cee1e7150ab8
title: IESP::Disconnect method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP.Disconnect
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP::Disconnect method

The **Disconnect** method disconnects the NPP from the network.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Disconnect();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                          | Description                                                                                                     |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>      | The NPP is capturing data. You cannot disconnect from the network while data capture is in progress.<br/> |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network.<br/>                                                             |
| <dl> <dt>**NMERR\_NOT\_ESP**</dt> </dl>       | The NPP is connected to the network but not with the [IESP::Connect](iesp-connect.md) method.<br/>       |



 

## Remarks

This method cannot be called when the NPP is capturing data. You must call the **IESP::Stop** method before calling **IESP::Disconnect**.

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

[IESP::Stop](iesp-stop.md)
</dt> </dl>

 

 




