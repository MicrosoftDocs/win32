---
Description: The TransmissionStart property indicates the time that the fax inbound job began transmitting.
ms.assetid: f36377b7-da89-49a9-9834-aa04030252c8
title: FaxIncomingJob.TransmissionStart property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.TransmissionStart property

The **TransmissionStart** property indicates the time that the fax inbound job began transmitting.

This property is read-only.

## Syntax


```VB
Property TransmissionStart As Date
```



## Property value

A **Date** that receives the hour and minute, expressed in local system time, at which the fax began transmitting. **Date** is an 8-byte floating-point number.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-queue.md)
</dt> <dt>

[**FaxIncomingJob**](-mfax-faxincomingjob.md)
</dt> <dt>

[**IFaxIncomingJob**](-mfax-faxincomingjob-cpp.md)
</dt> </dl>

 

 




