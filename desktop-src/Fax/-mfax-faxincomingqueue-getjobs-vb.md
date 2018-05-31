---
Description: The GetJobs method returns the collection of inbound fax jobs in the queue.
ms.assetid: 3ffa4607-c4d4-43a2-9a81-6f75ac6ffd5a
title: FaxIncomingQueue.GetJobs method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingQueue.GetJobs method

The **GetJobs** method returns the collection of inbound fax jobs in the queue.

## Syntax


```VB
FaxIncomingQueue.GetJobs() As IFaxIncomingJobs
```



## Parameters

This method has no parameters.

## Return value

Type: **[**IFaxIncomingJobs**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjobs)\*\***

A [**FaxIncomingJobs**](-mfax-faxincomingjobs.md) object.

## Remarks

To use this method, a user must have the [**farQUERY\_JOBS**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) and [**farSUBMIT\_LOW**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access rights.

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

[**FaxIncomingQueue**](-mfax-faxincomingqueue.md)
</dt> <dt>

[**IFaxIncomingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingqueue)
</dt> </dl>

 

 




