---
description: IStats::Resume method - The Resume method restarts a paused capture.
ms.assetid: 128e38c4-7459-4376-a3d7-2c6944fcf535
title: IStats::Resume method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.Resume
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::Resume method

The **Resume** method restarts a paused capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Resume();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                | Description                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>       | The NPP is not connected to the network.<br/>                                                                                          |
| <dl> <dt>**NMERR\_CAPTURE\_NOT\_PAUSED**</dt> </dl> | The capture is not paused. Call the [IStats::Pause](istats-pause.md) method to temporarily stop the capture.<br/>                     |
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>       | The NPP is not connected to the network. Call the [IStats::Connect](istats-connect.md) method to connect the NPP to the network.<br/> |
| <dl> <dt>**NMERR\_NOT\_STATS\_ONLY**</dt> </dl>     | The NPP is connected to the network but not with the [IStats::Connect](istats-connect.md) method.<br/>                                |



 

## Remarks

While the capture is in a paused state, new data is not captured until the IStats::Resume method is called to restart the capture.

When using the **Pause** and **Resume** methods to control the capture, Network Monitor continues to add [*conversation statistics*](c.md) to the existing statistics for the current capture.

To stop the capture, call [IStats::Stop](istats-stop.md).

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

[IStats::Pause](istats-pause.md)
</dt> <dt>

[IStats::Stop](istats-stop.md)
</dt> </dl>

 

 




