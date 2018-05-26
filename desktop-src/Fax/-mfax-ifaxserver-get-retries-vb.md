---
Description: Sets or retrieves the Retries property for a FaxServer object. The Retries property is a value that represents the number of times the fax server attempts to retransmit an outgoing fax when the initial transmission fails.
ms.assetid: 8fe0debc-f54c-421b-bfef-9e3c7bbf072c
title: FaxServer.Retries property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.Retries property

Sets or retrieves the **Retries** property for a [FaxServer](-mfax-faxserver-client.md) object. The **Retries** property is a value that represents the number of times the fax server attempts to retransmit an outgoing fax when the initial transmission fails.

This property is read/write.

## Syntax


```VB
Property Retries As Long
```



## Property value

A **Long** that specifies or receives the number of times the fax server attempts to retransmit an outgoing fax when the initial transmission fails. A value of zero indicates that the fax server should not attempt to retransmit an outbound job if the first transmission fails.

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

 

 




