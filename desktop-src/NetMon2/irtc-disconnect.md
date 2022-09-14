---
description: IRTC::Disconnect method - The Disconnect method disconnects the NPP from the network.
ms.assetid: 47a0cce0-a50d-4bad-9787-672cc3d13d07
title: IRTC::Disconnect method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.Disconnect
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::Disconnect method

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



| Return code                                                                                          | Description                                                                                                         |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>      | The NPP is capturing data. You cannot disconnect from the network while the data capture is in progress.<br/> |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network.<br/>                                                                 |
| <dl> <dt>**NMERR\_NOT\_REALTIME**</dt> </dl>  | The NPP is connected to the network but not with the [IRTC::Connect](irtc-connect.md) method.<br/>           |



 

## Remarks

This method cannot be called when the NPP is capturing data. You must call the [IRTC::Stop](irtc-stop.md) method before calling IRTC::Disconnect.

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

[IRTC::Stop](irtc-stop.md)
</dt> </dl>

 

 




