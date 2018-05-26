---
Description: The TSID property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the fax outbound message.
ms.assetid: 162128b8-8121-44cf-bb7c-394bdd01dff9
title: FaxOutgoingMessage.TSID property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessage.TSID property

The **TSID** property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the fax outbound message.

This property is read-only.

## Syntax


```VB
Property TSID As String
```



## Property value

A **String** that receives the TSID associated with the outbound fax message.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)
</dt> <dt>

[**IFaxOutgoingMessage**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingmessage?branch=master)
</dt> </dl>

 

 




