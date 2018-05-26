---
Description: The GetJobs method returns a collection of the outbound fax jobs in the job queue.
ms.assetid: 3581ffc9-d8d0-4734-a88c-367e335234ca
title: FaxOutgoingQueue.GetJobs method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

To use this method, a user must have the [****farSUBMIT\_LOW****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) or [****farQUERY\_JOBS****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

With the [****farSUBMIT\_LOW****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right, users can use this method only for their own faxes. With the [****farQUERY\_JOBS****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right, users can use this method for all faxes on the server.

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

[**IFaxOutgoingQueue**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingqueue?branch=master)
</dt> <dt>

[Managing Outgoing Jobs](-mfax-managing-outgoing-jobs.md)
</dt> </dl>

 

 




