---
Description: The FaxIncomingQueue configuration object is used by a fax client application to manage the inbound fax jobs (FaxIncomingJobs object) in the job queue. The object also includes a method to block inbound faxes from the fax job queue.
ms.assetid: 769e4fc5-5607-4fd6-8f78-59b190c94787
title: FaxIncomingQueue object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingQueue object

The **FaxIncomingQueue** configuration object is used by a fax client application to manage the inbound fax jobs ([**FaxIncomingJobs**](-mfax-faxincomingjobs.md) object) in the job queue. The object also includes a method to block inbound faxes from the fax job queue.

A **FaxIncomingQueue** object is accessed through a [**FaxFolders**](-mfax-faxfolders.md) object.

![faxfolders, faxincomingqueue, faxincomingjobs, and faxincomingjob objects](images/faxincomingqueue.png)

> [!Note]  
> Changes made to the **FaxIncomingQueue** object will not be saved until you call the [**Save**](-mfax-faxincomingqueue-save-vb.md) method.

 

## Members

The **FaxIncomingQueue** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxIncomingQueue** object has these methods.



| Method                                               | Description                                                                                                                                                                                                                                                                                                 |
|:-----------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetJob**](-mfax-faxincomingqueue-getjob-vb.md)   | The [**GetJob**](-mfax-faxincomingqueue-getjob-vb.md) method returns an incoming fax job in the job queue according to its ID.<br/>                                                                                                                                                                  |
| [**GetJobs**](-mfax-faxincomingqueue-getjobs-vb.md) | The [**GetJobs**](-mfax-faxincomingqueue-getjobs-vb.md) method returns the collection of inbound fax jobs in the queue.<br/>                                                                                                                                                                         |
| [**Refresh**](-mfax-faxincomingqueue-refresh-vb.md) | The [**Refresh**](-mfax-faxincomingqueue-refresh-vb.md) method refreshes **FaxIncomingQueue** object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxincomingqueue-save-vb.md) method call are lost.<br/> |
| [**Save**](-mfax-faxincomingqueue-save-vb.md)       | The [**Save**](-mfax-faxincomingqueue-save-vb.md) method saves the **FaxIncomingQueue** object's data.<br/>                                                                                                                                                                                          |



 

### Properties

The **FaxIncomingQueue** object has these properties.



| Property                                                        | Access type           | Description                                                                                                                                                          |
|:----------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Blocked**](-mfax-faxincomingqueue-blocked-vb.md)<br/> | Read/write<br/> | The [**Blocked**](-mfax-faxincomingqueue-blocked-vb.md) property is a Boolean value that indicates whether the job queue for incoming faxes is blocked. <br/> |



 

## Remarks

To create a **FaxIncomingQueue** object in Microsoft Visual Basic, call the [**IncomingQueue**](-mfax-faxfolders-incomingqueue-vb.md) method of the [**FaxFolders**](-mfax-faxfolders.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxIncomingQueue<br/>                                                      |



## See also

<dl> <dt>

[Fax Service Extended COM Object Model](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**FaxFolders**](-mfax-faxfolders.md)
</dt> <dt>

[**IFaxIncomingQueue**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingqueue?branch=master)
</dt> </dl>

 

 




