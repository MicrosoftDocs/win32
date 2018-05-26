---
Description: The Cancel method cancels the outbound fax job.
ms.assetid: 0d9e5a61-fde1-4527-89e8-c70abbc8aef5
title: FaxOutgoingJob.Cancel method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJob.Cancel method

The **Cancel** method cancels the outbound fax job.

## Syntax


```VB
FaxOutgoingJob.Cancel() As Long
```



## Parameters

This method has no parameters.

## Remarks

When you cancel a job that is not part of a broadcast or when you cancel an entire broadcast, the [**Count**](-mfax-faxoutgoingjobs-count-vb.md) property is updated to reflect the change in the number of outgoing jobs. However, if you cancel a single fax from a broadcast, the **Count** property does not reflect the change. The canceled fax remains in the outgoing queue, so that you can view the status of all faxes from the broadcast.

To use this method, a user must have the [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) or **farMANAGE\_JOBS** access right. With the **farSUBMIT\_LOW** access right, users will be able to use this method only for their own faxes. With the **farMANAGE\_JOBS** access right, users will be able to use this method for all faxes on the server.

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

 

 




