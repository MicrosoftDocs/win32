---
Description: The TransmissionStart property indicates the time that the fax outbound message began transmitting.
ms.assetid: 1d7dbd88-343d-4876-8066-abfb95c5ef22
title: FaxOutgoingMessage.TransmissionStart property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessage.TransmissionStart property

The **TransmissionStart** property indicates the time that the fax outbound message began transmitting.

This property is read-only.

## Syntax


```VB
Property TransmissionStart As Date
```



## Property value

**Date** value. An 8-byte floating-point number that contains the time, expressed in local system time, that the fax message began transmitting.

For more information about the **Date** data type, see the *Microsoft Visual C++ Programmer's Guide*.

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

 

 




