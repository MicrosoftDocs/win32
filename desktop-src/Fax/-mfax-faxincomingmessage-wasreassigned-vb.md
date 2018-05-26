---
Description: Indicates if the fax has been reassigned.
ms.assetid: 1b1d47a6-022b-4ecf-879b-d0a228c8ca8e
title: FaxIncomingMessage.WasReAssigned property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessage.WasReAssigned property

Indicates if the fax has been reassigned.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read-only.

## Syntax


```VB
Property WasReAssigned As Boolean
```



## Property value

A **Boolean** that receives a flag indicating whether the inbound fax message has been reassigned.

## Remarks

This property is always VARIANT\_FALSE when the fax arrives at the server. If it is reassigned by a [routing assistant](-mfax-glossary.md), the fax service sets it to VARIANT\_TRUE.

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

 

 




