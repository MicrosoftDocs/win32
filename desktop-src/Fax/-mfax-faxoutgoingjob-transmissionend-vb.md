---
Description: The TransmissionEnd property indicates the time that the outbound fax job completed transmission.
ms.assetid: c27e4e56-23de-4f9d-af94-39b81432c676
title: FaxOutgoingJob.TransmissionEnd property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJob.TransmissionEnd property

The **TransmissionEnd** property indicates the time that the outbound fax job completed transmission.

This property is read-only.

## Syntax


```VB
Property TransmissionEnd As Date
```



## Property value

**Date** value. An 8-byte floating-point number that contains the time, expressed in local system time, that the fax completed transmission.

For more information about the **Date** data type, see the *Microsoft Visual C++ Programmer's Guide*.

## Remarks

The property is not valid as long as the fax is still being sent by the fax device. It will have a value only after the transmission has ended. In the case of an individual fax, once the transmission has ended, the fax will be moved to the outgoing archive, and you will not be able to retrieve this value. You can instead retrieve the value of the [**TransmissionEnd**](-mfax-faxincomingjob-transmissionend-vb.md) property. In the case of a broadcast, each fax of the broadcast remains in the outgoing queue until the entire broadcast has been completed, and you can retrieve the value for the **TransmissionEnd** property.

In the case of a failed fax, this property will be assigned a value of zero. If you try to retrieve the property for a failed fax, you will receive an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outgoing-jobs.md)
</dt> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingjob?branch=master)
</dt> </dl>

 

 




