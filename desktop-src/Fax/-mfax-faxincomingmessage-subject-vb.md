---
Description: The Subject property contains the subject associated with the inbound fax message. This property is a null-terminated string.
ms.assetid: d13605b5-ad30-4729-9cb9-76af0492124b
title: FaxIncomingMessage.Subject property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessage.Subject property

The **Subject** property contains the subject associated with the inbound fax message. This property is a null-terminated string.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property Subject As String
```



## Property value

Pointer to the subject associated with the inbound fax message.

## Remarks

A received message starts with a null value for the subject when it arrives. It can be given a subject by a [routing assistant](-mfax-glossary.md) when it is reassigned.

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

[**IFaxIncomingMessage2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingmessage2?branch=master)
</dt> </dl>

 

 




