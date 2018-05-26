---
Description: The CSID property is a null-terminated string that contains the called station identifier (CSID) for the inbound fax message.
ms.assetid: 464f15b6-0b52-4b6c-8a33-c1667ba36f13
title: FaxIncomingMessage.CSID property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessage.CSID property

The **CSID** property is a null-terminated string that contains the called station identifier (CSID) for the inbound fax message.

This property is read-only.

## Syntax


```VB
Property CSID As String
```



## Property value

A **String** that receives the CSID for the inbound fax message.

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

 

 




