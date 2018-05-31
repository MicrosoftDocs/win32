---
Description: A flag that indicates whether the fax has a cover page.
ms.assetid: f84b39d6-3e41-44fc-8450-0a97b888cc9a
title: FaxIncomingMessage.HasCoverPage property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.HasCoverPage property

A flag that indicates whether the fax has a cover page.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property HasCoverPage As Boolean
```



## Property value

A flag indicating whether the inbound fax message has a cover page.

## Remarks

A received message has a VARIANT\_FALSE value when it arrives. A [routing assistant](-mfax-glossary.md) application can set this to VARIANT\_TRUE when it is reassigned.

A change to this value is not committed to the server until [**Save**](-mfax-faxincomingmessage-save-vb.md) is called.

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

 

 




