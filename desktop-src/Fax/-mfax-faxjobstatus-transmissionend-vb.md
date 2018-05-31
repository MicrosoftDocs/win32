---
Description: The TransmissionEnd property indicates the time that the fax job completed transmission.
ms.assetid: bae23bc4-c26f-4651-8227-94a12d11125b
title: FaxJobStatus.TransmissionEnd property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.TransmissionEnd property

The **TransmissionEnd** property indicates the time that the fax job completed transmission.

This property is read-only.

## Syntax


```VB
Property TransmissionEnd As Date
```



## Property value

A **Date** that receives the hour and minute, expressed in local system time, that the fax completed transmission. **Date** is an 8-byte floating-point number.

## Remarks

The property is not valid as long as the fax is still being received by the fax device.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-registering-for-fax-events.md)
</dt> <dt>

[**FaxJobStatus**](-mfax-faxjobstatus.md)
</dt> <dt>

[**IFaxJobStatus**](-mfax-faxjobstatus-cpp.md)
</dt> </dl>

 

 




