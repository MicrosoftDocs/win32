---
Description: The CallerId property is a null-terminated string that identifies the calling device associated with the inbound fax message.
ms.assetid: 1cc5a3cb-af22-4f22-8031-ab93c75c62c3
title: FaxIncomingMessage.CallerId property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.CallerId property

The **CallerId** property is a null-terminated string that identifies the calling device associated with the inbound fax message.

This property is read-only.

## Syntax


```VB
Property CallerId As String
```



## Property value

A **String** that receives the caller ID for the inbound fax message. The string identifies the calling device that sent the inbound fax.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingMessage**](-mfax-faxincomingmessage.md)
</dt> <dt>

[**IFaxIncomingMessage**](-mfax-faxincomingmessage-cpp.md)
</dt> </dl>

 

 




