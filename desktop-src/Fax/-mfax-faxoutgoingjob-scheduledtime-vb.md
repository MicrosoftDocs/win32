---
Description: The ScheduledTime property indicates the time to submit the fax for processing to the fax service.
ms.assetid: 31a21a6f-587e-40d4-864d-43c834b91d1b
title: FaxOutgoingJob.ScheduledTime property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.ScheduledTime property

The **ScheduledTime** property indicates the time to submit the fax for processing to the fax service.

This property is read-only.

## Syntax


```VB
Property ScheduledTime As Date
```



## Property value

**Date** value. An 8-byte floating-point number that contains the time, expressed in local system time, to submit the fax for processing. If the time specified has passed, the fax service sends the fax as soon as a device is available.

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

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob)
</dt> </dl>

 

 




