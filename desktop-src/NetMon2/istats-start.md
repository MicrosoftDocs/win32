---
description: IStats::Start method - The Start method starts a capture.
ms.assetid: d4086e30-e5ed-4f29-90f0-d65125d9af6d
title: IStats::Start method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.Start
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::Start method

The **Start** method starts a capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Start();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                            | Description                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_PAUSED**</dt> </dl>  | The capture has paused and must be stopped before it can be restarted. Call the [IStats::Stop](istats-stop.md) method to stop the capture.<br/> |
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>        | The capture has already started.<br/>                                                                                                            |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>   | The NPP is not connected to the network. Call the [IStats::Connect](istats-connect.md) method to connect the NPP to the network.<br/>           |
| <dl> <dt>**NMERR\_NOT\_STATS\_ONLY**</dt> </dl> | The NPP is connected to the network but not with the [IStats::Connect](istats-connect.md) method.<br/>                                          |



 

## Remarks

When restarting the capture by using the IStats::Start and [IStats::Stop](istats-stop.md) methods, you must call the [IStats::Configure](istats-configure.md) method to reconfigure the connection each time you call IStats::Start to restart the data capture.

> [!Note]  
> You can also start and stop the capture by using the [IStats::Pause](istats-pause.md) and [IStats::Resume](istats-resume.md) methods. When you use these methods, the captured data is stored in the same capture file.

 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IStats](istats.md)
</dt> <dt>

[IStats::Configure](istats-configure.md)
</dt> <dt>

[IStats::Connect](istats-connect.md)
</dt> <dt>

[IStats::Pause](istats-pause.md)
</dt> <dt>

[IStats::Resume](istats-resume.md)
</dt> <dt>

[IStats::Stop](istats-stop.md)
</dt> </dl>

 

 




