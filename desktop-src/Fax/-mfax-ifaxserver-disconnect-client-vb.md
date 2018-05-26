---
Description: The Disconnect method terminates a fax client applications connection to a fax server.
ms.assetid: 669a0120-ed0d-4078-a4c0-e41ef4917162
title: FaxServer.Disconnect method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.Disconnect method

The **Disconnect** method terminates a fax client application's connection to a fax server.

## Syntax


```VB
FaxServer.Disconnect() As Long
```



## Parameters

This method has no parameters.

## Remarks

A call to the **Disconnect** method attempts to terminate a server connection made by a previous call to the [**Connect**](-mfax-ifaxserver-connect-client-vb.md) method.

In addition to calling the **Disconnect** method, an application must also call the [IUnknown::Release](http://msdn.microsoft.com/en-us/library/ms682317.aspx) method to allow each object to deallocate itself.

For more information, see [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md) and [Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md).

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
</dt> <dt>

[**Connect**](-mfax-ifaxserver-connect-client-vb.md)
</dt> <dt>

[IUnknown::Release](http://msdn.microsoft.com/en-us/library/ms682317.aspx)
</dt> <dt>

[Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md)
</dt> <dt>

[Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md)
</dt> </dl>

 

 




