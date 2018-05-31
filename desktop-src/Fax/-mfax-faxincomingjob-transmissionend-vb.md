---
Description: The TransmissionEnd property indicates the time at which the inbound fax job completed transmission.
ms.assetid: 7b4ca28b-6787-4ba6-9ea7-7d0fc5b771dc
title: FaxIncomingJob.TransmissionEnd property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.TransmissionEnd property

The **TransmissionEnd** property indicates the time at which the inbound fax job completed transmission.

This property is read-only.

## Syntax


```VB
Property TransmissionEnd As Date
```



## Property value

A **Date** that receives the hour and minute, expressed in local system time, that the fax completed transmission. **Date** is an 8-byte floating-point number.

## Remarks

The **TransmissionEnd** property is not valid as long as the fax is still being received by the fax device. In the case of a fax that is still in progress, this property will be assigned a value of zero. If you try to retrieve the property for a fax that is still in progress you will receive an error.

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

[**IFaxIncomingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjob)
</dt> </dl>

 

 




