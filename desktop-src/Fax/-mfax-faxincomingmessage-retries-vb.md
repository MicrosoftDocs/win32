---
Description: The Retries property is a value that indicates the number of times that the fax service attempted to route an inbound fax message after the initial routing attempt failed.
ms.assetid: 47c5c4ed-15ce-490e-8a49-28837ddc149a
title: FaxIncomingMessage.Retries property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.Retries property

The **Retries** property is a value that indicates the number of times that the fax service attempted to route an inbound fax message after the initial routing attempt failed.

This property is read-only.

## Syntax


```VB
Property Retries As Long
```



## Property value

A **Long** that receives the number of times that the fax service attempted to route the fax message after the initial routing attempt failed.

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

[**IFaxIncomingMessage**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingmessage)
</dt> </dl>

 

 




