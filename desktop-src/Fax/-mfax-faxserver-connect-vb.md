---
Description: The Connect method connects a fax client application to the specified fax server.
ms.assetid: 561024ba-f15e-4339-877e-b8cc8e9f0234
title: FaxServer.Connect method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.Connect method

The **Connect** method connects a fax client application to the specified fax server.

## Syntax


```VB
FaxServer.Connect( _
  ByVal bstrServerName As String _
) As Long
```



## Parameters

<dl> <dt>

*bstrServerName* 
</dt> <dd>

Type: **String**

A null-terminated string that specifies the name of the target fax server, such as "computername". If this parameter is **Null** or an empty string, the method connects the application to the fax server on the local computer.

</dd> </dl>

## Remarks

Before accessing most of the objects of the fax extended Component Object Model (COM), the application must call this method to initiate a connection with an active fax server. A fax server connection is not required for you to access a [**FaxDocument**](-mfax-faxdocument.md) object. The method fails if the client is not connected to an active fax server.

To connect to the local server, set the *bstrServerName* parameter to **Null** or an empty string. For usage examples, see [Connecting to the Fax Server](-mfax-connecting-to-the-fax-server.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-retrieving-server-properties.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](-mfax-faxserver-cpp.md)
</dt> </dl>

 

 




