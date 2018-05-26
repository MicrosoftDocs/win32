---
Description: The FaxOutgoingJobs messaging collection is used by a fax client application to manage the outbound fax jobs in a fax servers job queue. Each outbound job is represented by a FaxOutgoingJob object.
ms.assetid: cfd8e842-838e-41d7-97c0-e75be908c5a0
title: FaxOutgoingJobs object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJobs object

The **FaxOutgoingJobs** messaging collection is used by a fax client application to manage the outbound fax jobs in a fax server's job queue. Each outbound job is represented by a [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) object.

## Members

The **FaxOutgoingJobs** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxOutgoingJobs** object has these properties.



| Property                                                   | Access type          | Description                                                                                                                                                                                                   |
|:-----------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxoutgoingjobs-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-faxoutgoingjobs-count-vb.md) property represents the number of objects in the **FaxOutgoingJobs** collection. This is the total number of outgoing jobs for the fax server.<br/> |
| [**Item**](-mfax-faxoutgoingjobs-item.md)<br/>      | Read-only<br/> | The [**Item**](-mfax-faxoutgoingjobs-item.md) property returns a [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) object from the **FaxOutgoingJobs** collection.<br/>                                   |



 

## Remarks

A **FaxOutgoingJobs** object is accessed through a [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md) object.

![faxoutgoingqueue and faxoutgoingjobs objects](images/faxoutgoingjobs.png)

To create a **FaxOutgoingJobs** object in Microsoft Visual Basic, call the [**GetJobs**](-mfax-faxoutgoingqueue-getjobs-vb.md) method of the [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md) object.

To create a **FaxOutgoingJobs** object in C++, call the [**GetJobs**](-mfax-faxoutgoingqueue-getjobs-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxOutgoingJobs<br/>                                                       |



 

 




