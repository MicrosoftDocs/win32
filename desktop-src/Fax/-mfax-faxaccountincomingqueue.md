---
Description: Used by a fax client application to retrieve the inbound fax jobs (FaxIncomingJobs object) in the job queue of a particular fax account.
ms.assetid: dd0ba850-d2d0-4ba3-a36c-a0947ab44c28
title: FaxAccountIncomingQueue object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxAccountIncomingQueue object

Used by a fax client application to retrieve the inbound fax jobs ([**FaxIncomingJobs**](-mfax-faxincomingjobs.md) object) in the job queue of a particular fax account.

A **FaxAccountIncomingQueue** object is accessed through a [**FaxAccountFolders**](-mfax-faxaccountfolders.md) object.

![faxaccountfolders, faxaccountincomingqueue, and faxincomingjob](images/faxaccountincomingqueue.png)

## Members

The **FaxAccountIncomingQueue** object has these types of members:

-   [Methods](#methods)

### Methods

The **FaxAccountIncomingQueue** object has these methods.



| Method                                                      | Description                                                                                                   |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**GetJob**](-mfax-faxaccountincomingqueue-getjob-vb.md)   | Returns an incoming fax job in the job queue of the current fax account according to the job's ID.<br/> |
| [**GetJobs**](-mfax-faxaccountincomingqueue-getjobs-vb.md) | Returns the collection of inbound fax jobs in the queue for the current fax account.<br/>               |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxAccountIncomingQueue<br/>                                               |



## See also

<dl> <dt>

[**FaxAccountFolders**](-mfax-faxaccountfolders.md)
</dt> <dt>

[**IFaxAccountIncomingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountincomingqueue)
</dt> </dl>

 

 




