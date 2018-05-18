---
Description: 'Sets or retrieves the RetryDelay property for a FaxServer object. The RetryDelay property is a value that represents the time interval, in minutes, the fax server waits before attempting to retransmit an outbound fax job.'
ms.assetid: '999ec37f-7516-49f6-b3ab-626a33dee65f'
title: 'FaxServer.RetryDelay property'
---

# FaxServer.RetryDelay property

Sets or retrieves the **RetryDelay** property for a [FaxServer](-mfax-faxserver-client.md) object. The **RetryDelay** property is a value that represents the time interval, in minutes, the fax server waits before attempting to retransmit an outbound fax job.

This property is read/write.

## Syntax


```VB
Property RetryDelay As Long
```



## Property value

A **Long** that specifies or receives the number of minutes the fax server waits before attempting to retransmit an outbound fax job. If this property is equal to zero, the fax server will attempt to retransmit the fax job immediately.

## Remarks

A transmission might not be sent on the first attempt for various reasons. For example, the sending device may receive a busy signal.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxServer](-mfax-faxserver-client.md)
</dt> </dl>

 

 




