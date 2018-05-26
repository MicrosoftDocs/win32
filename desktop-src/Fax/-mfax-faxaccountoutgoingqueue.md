---
Description: Used by a fax client application to get the outbound fax jobs (FaxOutgoingJobs object) in the outbound job queue of a particular fax account.
ms.assetid: a1012b13-e629-4449-9b7c-c182dad56a9b
title: FaxAccountOutgoingQueue object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccountOutgoingQueue object

Used by a fax client application to get the outbound fax jobs ([**FaxOutgoingJobs**](-mfax-faxoutgoingjobs.md) object) in the outbound job queue of a particular fax account.

A **FaxAccountOutgoingQueue** object is accessed through a [**FaxAccountFolders**](-mfax-faxaccountfolders.md) object.

![faxaccountfolders, faxaccountoutgoingqueue, and faxoutgoingjobs](images/faxaccountoutgoingqueue.png)

## Members

The **FaxAccountOutgoingQueue** object has these types of members:

-   [Methods](#methods)

### Methods

The **FaxAccountOutgoingQueue** object has these methods.



| Method                                                      | Description                                                                                                   |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**GetJob**](-mfax-faxaccountoutgoingqueue-getjob-vb.md)   | Returns an outgoing fax job in the job queue of the current fax account according to the job's ID.<br/> |
| [**GetJobs**](-mfax-faxaccountoutgoingqueue-getjobs-vb.md) | Returns the collection of outbound fax jobs in the queue for the current fax account.<br/>              |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxAccountOutgoingQueue<br/>                                               |



## See also

<dl> <dt>

[**FaxAccountFolders**](-mfax-faxaccountfolders.md)
</dt> <dt>

[**IFaxAccountOutgoingQueue**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccountoutgoingqueue?branch=master)
</dt> </dl>

 

 




