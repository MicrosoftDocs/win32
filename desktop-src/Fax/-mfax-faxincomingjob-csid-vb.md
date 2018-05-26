---
Description: The CSID property is a null-terminated string that contains the called station identifier (CSID) for the job.
ms.assetid: 14813440-53fe-4c3f-a872-70312d660805
title: FaxIncomingJob.CSID property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingJob.CSID property

The **CSID** property is a null-terminated string that contains the called station identifier (CSID) for the job.

This property is read-only.

## Syntax


```VB
Property CSID As String
```



## Property value

A **String** that receives the CSID for the inbound fax job.

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

 

 




