---
Description: The Id property is a null-terminated string that contains a unique ID for the inbound fax job.
ms.assetid: 94bcfac7-3011-4b4c-86a7-60abda46bb94
title: FaxIncomingJob.Id property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingJob.Id property

The **Id** property is a null-terminated string that contains a unique ID for the inbound fax job.

This property is read-only.

## Syntax


```VB
Property Id As String
```



## Property value

A **String** that receives a unique ID for the inbound fax job.

## Remarks

You can use the fax job's ID to retrieve the archived fax message after the job completes successfully.

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

[**IFaxIncomingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingjob?branch=master)
</dt> </dl>

 

 




