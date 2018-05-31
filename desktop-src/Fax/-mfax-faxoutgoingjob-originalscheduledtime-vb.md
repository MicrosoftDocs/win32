---
Description: The OriginalScheduledTime property specifies the time that the fax job was originally scheduled for transmission.
ms.assetid: 0c3f44da-c4e6-4d65-943a-412a220417f4
title: FaxOutgoingJob.OriginalScheduledTime property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.OriginalScheduledTime property

The **OriginalScheduledTime** property specifies the time that the fax job was originally scheduled for transmission.

This property is read-only.

## Syntax


```VB
Property OriginalScheduledTime As Date
```



## Property value

A **Date** value that represents the date and time that the fax was originally scheduled for processing. **OriginalScheduledTime** is expressed in local system time.

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

[**IFaxOutgoingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob)
</dt> </dl>

 

 




