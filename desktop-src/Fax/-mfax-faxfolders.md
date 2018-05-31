---
Description: The FaxFolders configuration object is used by a fax client application to access the folders, queued jobs, and archived messages on a fax server.
ms.assetid: 283c75e3-e596-403c-b4ea-b62bf0c744f3
title: FaxFolders object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxFolders object

The **FaxFolders** configuration object is used by a fax client application to access the folders, queued jobs, and archived messages on a fax server.

## Members

The **FaxFolders** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxFolders** object has these properties.



| Property                                                                  | Access type          | Description                                                                                                                      |
|:--------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| [**IncomingArchive**](-mfax-faxfolders-incomingarchive-vb.md)<br/> | Read-only<br/> | The [**IncomingArchive**](-mfax-faxfolders-incomingarchive-vb.md) property represents the archive of incoming faxes.<br/> |
| [**IncomingQueue**](-mfax-faxfolders-incomingqueue-vb.md)<br/>     | Read-only<br/> | The [**IncomingQueue**](-mfax-faxfolders-incomingqueue-vb.md) property represents the queue of incoming faxes.<br/>       |
| [**OutgoingArchive**](-mfax-faxfolders-outgoingarchive-vb.md)<br/> | Read-only<br/> | The [**OutgoingArchive**](-mfax-faxfolders-outgoingarchive-vb.md) property represents the archive of outgoing faxes.<br/> |
| [**OutgoingQueue**](-mfax-faxfolders-outgoingqueue-vb.md)<br/>     | Read-only<br/> | The [**OutgoingQueue**](-mfax-faxfolders-outgoingqueue-vb.md) property represents the queue of outgoing faxes.<br/>       |



 

## Remarks

Use the FaxFolders object to create and access the following objects:

-   [**FaxIncomingArchive**](-mfax-faxincomingarchive.md), which is the archive of inbound fax messages received successfully by the fax service
-   [**FaxIncomingQueue**](-mfax-faxincomingqueue.md), which is the queue of inbound fax jobs
-   [**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md), which is the archive of outbound fax messages sent successfully by the fax service
-   [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md), which is the queue of outbound fax jobs

A **FaxFolders** object is accessed through a [**FaxServer**](-mfax-faxserver.md) object.

![faxserver, faxfolders, and subordinate objects to faxfolders](images/faxfolders.png)

To create a **FaxFolders** object in Microsoft Visual Basic, call the [**Folders**](-mfax-faxserver-folders.md) property of the [**FaxServer**](-mfax-faxserver.md) object.

To create a **FaxFolders** object in C++, call the [**Folders**](-mfax-faxserver-folders.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxFolders<br/>                                                            |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxFolders**](-mfax-faxfolders-cpp.md)
</dt> </dl>

 

 




