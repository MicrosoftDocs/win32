---
Description: The Connect method connects a fax client application to the specified fax server.
ms.assetid: f3f4ff8a-4546-46a6-b5d8-ae351235b608
title: FaxServer.Connect method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.Connect method

The **Connect** method connects a fax client application to the specified fax server. Before accessing most interfaces that begin with **IFax**, the application must call this method to initiate a connection with an active fax server. A fax server connection is not required to access an [**IFaxTiff**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxtiff) interface.

## Syntax


```VB
FaxServer.Connect( _
  ByVal ServerName As String _
) As Long
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the name of the target fax server. If this parameter is **Null**, the method connects the application to the fax server on the local computer. See [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md) for limitations on connecting to remote servers.

</dd> </dl>

## Remarks

The fax client application must call the [**Disconnect**](-mfax-ifaxserver-disconnect-client-vb.md) method to disconnect from the fax server.

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

[**Disconnect**](-mfax-ifaxserver-disconnect-client-vb.md)
</dt> <dt>

[Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md)
</dt> <dt>

[Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md)
</dt> </dl>

 

 




