---
description: Disconnects the NPP from the network.
ms.assetid: 01ff8fc2-aa27-4df8-a499-c7b00c1fa2e8
title: IStats::Disconnect method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.Disconnect
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::Disconnect method

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



| Return code                                                                                            | Description                                                                                                                 |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>        | The NPP is currently capturing data. You cannot disconnect from the network while a data capture is in progress.<br/> |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>   | The NPP is not connected to the network.<br/>                                                                         |
| <dl> <dt>**NMERR\_NOT\_STATS\_ONLY**</dt> </dl> | The NPP is connected to the network, but not with the [**IStats::Connect**](istats-connect.md) method.<br/>          |



 

## Remarks

This method cannot be called when the NPP is capturing data. Call the **IStats::Disconnect** method first and then call [**IStats::Stop**](istats-stop.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[**IStats**](istats.md)
</dt> <dt>

[**IStats::Connect**](istats-connect.md)
</dt> <dt>

[**IStats::Stop**](istats-stop.md)
</dt> </dl>

 

 




