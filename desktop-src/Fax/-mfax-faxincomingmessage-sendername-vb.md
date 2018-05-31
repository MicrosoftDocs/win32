---
Description: Contains the name of the sender that is associated with the inbound fax message. This property is a null-terminated string.
ms.assetid: 1d29eab0-bb82-4d57-9ced-194dff25a995
title: FaxIncomingMessage.SenderName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.SenderName property

Contains the name of the sender that is associated with the inbound fax message. This property is a null-terminated string.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property SenderName As String
```



## Property value

The sender associated with the inbound fax message.

## Remarks

A received message starts with a null value for the sender when it arrives. A sender can be specified by a [routing assistant](-mfax-glossary.md) when it is re-assigned.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxIncomingMessage**](-mfax-faxincomingmessage.md)
</dt> <dt>

[**IFaxIncomingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingmessage2)
</dt> </dl>

 

 




