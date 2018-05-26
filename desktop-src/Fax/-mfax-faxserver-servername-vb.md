---
Description: The ServerName property retrieves the name of the active fax server to which the fax client is connected.
ms.assetid: b07d1885-ba7a-438b-8692-833683ba4775
title: FaxServer.ServerName property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.ServerName property

The **ServerName** property retrieves the name of the active fax server to which the fax client is connected.

This property is read-only.

## Syntax


```VB
Property ServerName As String
```



## Property value

A **String** that receives the name of the active fax server to which the fax client is connected. If the method returns an empty string, it indicates that the object is connected to a fax server on the local computer.

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

[**IFaxServer**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver?branch=master)
</dt> </dl>

 

 




