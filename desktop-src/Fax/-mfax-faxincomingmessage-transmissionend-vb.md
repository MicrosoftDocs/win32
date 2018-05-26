---
Description: The TransmissionEnd property indicates the time that the inbound fax message completed transmission.
ms.assetid: 0a1a89fa-520d-4fb1-b0ca-7d231d9d7ff6
title: FaxIncomingMessage.TransmissionEnd property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessage.TransmissionEnd property

The **TransmissionEnd** property indicates the time that the inbound fax message completed transmission.

This property is read-only.

## Syntax


```VB
Property TransmissionEnd As Date
```



## Property value

A **Date** that receives the hour and minute, expressed in local system time, that the fax completed transmission. **Date** is an 8-byte floating-point number.

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

 

 




