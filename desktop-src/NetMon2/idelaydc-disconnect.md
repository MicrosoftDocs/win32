---
description: IDelaydC::Disconnect method - The Disconnect method disconnects the NPP from the network.
ms.assetid: 476bbce4-2e3c-448f-b85e-6adac424fb0d
title: IDelaydC::Disconnect method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.Disconnect
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::Disconnect method

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



| Return code                                                                                          | Description                                                                                                       |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>      | The NPP is capturing data. You cannot disconnect the NPP from the network during a capture.<br/>            |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl> | The NPP is not connected to the network.<br/>                                                               |
| <dl> <dt>**NMERR\_NOT\_DELAYED**</dt> </dl>   | The NPP is connected to the network but not with the [IDelaydC::Connect](idelaydc-connect.md) method.<br/> |



 

## Remarks

This method cannot be called when the NPP is capturing data. You must call the **IDelaydC::Stop** method before calling **Disconnect**.

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

[IDelaydC::Stop](idelaydc-stop.md)
</dt> </dl>

 

 




