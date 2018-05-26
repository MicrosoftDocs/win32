---
Description: The TSID property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the inbound fax message.
ms.assetid: 37291276-8b59-45cc-b05a-45325ddaf06e
title: FaxIncomingMessage.TSID property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessage.TSID property

The **TSID** property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the inbound fax message.

This property is read-only.

## Syntax


```VB
Property TSID As String
```



## Property value

A **String** that receives the tsid associated with the inbound fax message.

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

[**IFaxIncomingMessage**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingmessage?branch=master)
</dt> </dl>

 

 




