---
Description: The CSID property is a null-terminated string that contains the called station identifier (CSID) for the fax message.
ms.assetid: e8171711-ce85-4569-94bc-53d52b8d1c91
title: FaxOutgoingMessage.CSID property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingMessage.CSID property

The **CSID** property is a null-terminated string that contains the called station identifier (CSID) for the fax message.

This property is read-only.

## Syntax


```VB
Property CSID As String
```



## Property value

A **String** that receives the CSID for the outbound fax message.

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

[**IFaxOutgoingMessage**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingmessage)
</dt> </dl>

 

 




