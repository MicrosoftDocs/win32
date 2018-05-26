---
Description: The TSID property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the fax inbound job.
ms.assetid: 019edad7-63c6-4ed4-81d7-c3759b72e63b
title: FaxIncomingJob.TSID property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingJob.TSID property

The **TSID** property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the fax inbound job.

This property is read-only.

## Syntax


```VB
Property TSID As String
```



## Property value

A **String** that receives the TSID associated with the inbound fax job.

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

 

 




