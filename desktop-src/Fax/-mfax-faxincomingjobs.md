---
Description: 'The FaxIncomingJobs collection is used by a fax client application to manage the inbound fax jobs in a fax server''s job queue. Each incoming job is represented by a FaxIncomingJob object.'
ms.assetid: '05b2ceec-d8e9-4ee8-be0c-e31bb12edfc8'
title: FaxIncomingJobs object
---

# FaxIncomingJobs object

The **FaxIncomingJobs** collection is used by a fax client application to manage the inbound fax jobs in a fax server's job queue. Each incoming job is represented by a [**FaxIncomingJob**](-mfax-faxincomingjob.md) object.

A **FaxIncomingJobs** object is accessed through a [**FaxIncomingQueue**](-mfax-faxincomingqueue.md) object.

![faxincomingqueue, faxincomingjobs, and faxincomingjob objects](images/faxincomingjobs.png)

## Members

The **FaxIncomingJobs** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxIncomingJobs** object has these properties.



| Property                                                   | Access type          | Description                                                                                                                                                                                                   |
|:-----------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxincomingjobs-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-faxincomingjobs-count-vb.md) property represents the number of objects in the **FaxIncomingJobs** collection. This is the total number of incoming jobs for the fax server.<br/> |
| [**Item**](-mfax-faxincomingjobs-item.md)<br/>      | Read-only<br/> | The [**Item**](-mfax-faxincomingjobs-item.md) property returns a [**FaxIncomingJob**](-mfax-faxincomingjob.md) object from the **FaxIncomingJobs** collection.<br/>                                   |



 

## Remarks

To create a **FaxIncomingJobs** object in Microsoft Visual Basic, call the [**GetJobs**](-mfax-faxincomingqueue-getjobs-vb.md) property of the [**FaxIncomingQueue**](-mfax-faxincomingqueue.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxIncomingJobs<br/>                                                       |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**FaxIncomingQueue**](-mfax-faxincomingqueue.md)
</dt> <dt>

[**IFaxIncomingJobs**](-mfax-faxincomingjobs-cpp.md)
</dt> </dl>

 

 




