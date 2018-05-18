---
Description: 'The GetJobs method returns a collection of the outbound fax jobs in the job queue.'
ms.assetid: '3581ffc9-d8d0-4734-a88c-367e335234ca'
title: 'FaxOutgoingQueue.GetJobs method'
---

# FaxOutgoingQueue.GetJobs method

The **GetJobs** method returns a collection of the outbound fax jobs in the job queue.

## Syntax


```VB
FaxOutgoingQueue.GetJobs() As FaxOutgoingJobs
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FaxOutgoingJobs**](-mfax-faxoutgoingjobs.md)\*\***

A [**FaxOutgoingJobs**](-mfax-faxoutgoingjobs.md) object.

## Remarks

To use this method, a user must have the [****farSUBMIT\_LOW****](-mfax-fax-access-rights-enum.md) or [****farQUERY\_JOBS****](-mfax-fax-access-rights-enum.md) access right.

With the [****farSUBMIT\_LOW****](-mfax-fax-access-rights-enum.md) access right, users can use this method only for their own faxes. With the [****farQUERY\_JOBS****](-mfax-fax-access-rights-enum.md) access right, users can use this method for all faxes on the server.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md)
</dt> <dt>

[**IFaxOutgoingQueue**](-mfax-faxoutgoingqueue-cpp.md)
</dt> <dt>

[Managing Outgoing Jobs](-mfax-managing-outgoing-jobs.md)
</dt> </dl>

 

 




