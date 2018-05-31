---
Description: The SubmissionId property is a null-terminated string that contains the unique identifier assigned to the fax job during the submission process.
ms.assetid: a8849369-88a6-451a-8d2a-91f8c7a8673b
title: FaxOutgoingJob.SubmissionId property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.SubmissionId property

The **SubmissionId** property is a null-terminated string that contains the unique identifier assigned to the fax job during the submission process.

This property is read-only.

## Syntax


```VB
Property SubmissionId As String
```



## Property value

A **String** that receives the unique submission ID assigned to the outbound fax job.

## Remarks

All fax jobs created by the same submission process share the same unique submission ID. When you submit a fax to be sent to more than one recipient, separate fax jobs will be created, but as part of the same fax broadcast, they will share the same **SubmissionID**.

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

[**IFaxOutgoingJob**](-mfax-faxoutgoingjob-cpp.md)
</dt> </dl>

 

 




