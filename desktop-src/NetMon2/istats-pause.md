---
description: The Pause method temporarily stops the current capture.
ms.assetid: 43176e9e-1502-484c-a8af-4e7bbf5f6474
title: IStats::Pause method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.Pause
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::Pause method

The **Pause** method temporarily stops the current capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Pause();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                            | Description                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURE\_PAUSED**</dt> </dl>  | The capture is already paused.<br/>                                                                                                    |
| <dl> <dt>**NMERR\_NOT\_CAPTURING**</dt> </dl>   | The NPP is not capturing data. Call the [IStats::Start](istats-start.md) method to start the capture.<br/>                            |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>   | The NPP is not connected to the network. Call the [IStats::Connect](istats-connect.md) method to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_STATS\_ONLY**</dt> </dl> | The NPP is connected to the network but not with the [IStats::Connect](istats-connect.md) method.<br/>                                |



 

## Remarks

While the capture is paused, new frames are not captured until a call to the [IStats::Resume](istats-resume.md) method restarts the capture.

When you use the **IStats::Pause** and **IStats::Resume** methods to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) whenever the capture is running.

To restart the capture call [IStats::Resume](istats-resume.md). To stop the capture, call [IStats::Stop](istats-stop.md).

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

[IStats::Connect](istats-connect.md)
</dt> <dt>

[IStats::Resume](istats-resume.md)
</dt> <dt>

[IStats::Start](istats-start.md)
</dt> <dt>

[IStats::Stop](istats-stop.md)
</dt> </dl>

 

 




