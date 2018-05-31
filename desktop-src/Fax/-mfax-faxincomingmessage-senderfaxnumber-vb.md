---
Description: Contains the sender's fax number associated with the inbound fax message. This property is a null-terminated string.
ms.assetid: c16b3cee-5fd8-4ee3-a80c-08aedec56a64
title: FaxIncomingMessage.SenderFaxNumber property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.SenderFaxNumber property

Contains the sender's fax number associated with the inbound fax message. This property is a null-terminated string.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property SenderFaxNumber As String
```



## Property value

The fax number of the sender associated with the inbound fax message.

## Remarks

A received message starts with a null value for the sender's fax number when it arrives. A [routing assistant](-mfax-glossary.md) can specify the sender's fax number when the fax is reassigned.

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

 

 




