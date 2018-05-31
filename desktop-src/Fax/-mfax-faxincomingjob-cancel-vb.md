---
Description: The Cancel method cancels the incoming fax job.
ms.assetid: 36e3f4a3-4957-473b-895e-99e2c5b68785
title: FaxIncomingJob.Cancel method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.Cancel method

The **Cancel** method cancels the incoming fax job.

## Syntax


```VB
FaxIncomingJob.Cancel() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [**farMANAGE\_JOBS**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

 

 




