---
Description: 'Sets or retrieves the PauseServerQueue property for a FaxServer object. The PauseServerQueue property is a Boolean value that indicates whether the fax server has paused the fax job queue.'
ms.assetid: 'f4221461-127c-40a3-962a-3c7c69d736d7'
title: 'FaxServer.PauseServerQueue property'
---

# FaxServer.PauseServerQueue property

Sets or retrieves the **PauseServerQueue** property for a [FaxServer](-mfax-faxserver-client.md) object. The **PauseServerQueue** property is a Boolean value that indicates whether the fax server has paused the fax job queue.

This property is read/write.

## Syntax


```VB
Property PauseServerQueue As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax server has paused the outbound fax job queue. If this value is **True**, the queue has been paused. If this value is **False**, the queue is active.

## Remarks

An administrator might pause the fax job queue for various reasons. For example, the administrator may need to perform queue management, or free a fax device for an inbound reception or for another application's use.

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

 

 




