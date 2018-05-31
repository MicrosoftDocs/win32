---
Description: The Retries property is a value that indicates the number of times that the fax service attempted to transmit an outgoing fax after the initial transmission attempt failed.
ms.assetid: b1306219-273f-4119-886c-e595b3b405cb
title: FaxOutgoingMessage.Retries property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingMessage.Retries property

The **Retries** property is a value that indicates the number of times that the fax service attempted to transmit an outgoing fax after the initial transmission attempt failed.

This property is read-only.

## Syntax


```VB
Property Retries As Long
```



## Property value

A **Long** that receives the number of times that the fax service attempted to transmit the fax message after the initial transmission attempt failed.

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

 

 




