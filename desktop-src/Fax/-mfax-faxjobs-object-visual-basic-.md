---
Description: The FaxJobs object represents a collection of FaxJob objects.
ms.assetid: 9df2f27f-b0a6-4ba5-920b-320dd83f6e40
title: FaxJobs object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxJobs object

The **FaxJobs** object represents a collection of [**FaxJob objects**](-mfax-faxjob-object-visual-basic-.md). The **FaxJobs** object permits a fax client Microsoft Visual Basic application to enumerate the fax jobs associated with a connected fax server, and to create **FaxJob** objects for fax jobs. There is one **FaxJob** object for each queued job associated with the server.

The **FaxJobs** object has the following properties:

-   A property to enumerate the number of jobs associated with a connected fax server.
-   A property to create a [**FaxJob object**](-mfax-faxjob-object-visual-basic-.md) for a specified fax job.

## Members

The **FaxJobs** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxJobs** object has these properties.



| Property                                                | Access type          | Description                                                                                                                                                                                                                   |
|:--------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-ifaxjobs-get-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-ifaxjobs-get-count-vb.md) property returns the number of queued fax jobs associated with the connected fax server.<br/>                                                                          |
| [**Item**](-mfax-ifaxjobs-get-item-vb.md)<br/>   | Read-only<br/> | The [**Item**](-mfax-ifaxjobs-get-item-vb.md) property creates a [FaxJob](-mfax-faxjob.md) object for a specified fax job. The object allows enumeration of the fax jobs associated with a connected fax server.<br/> |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxJobs** object's type library information in Visual Basic syntax.

### To create a FaxJobs object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object.
2.  Call the [**GetJobs**](-mfax-ifaxserver-getjobs-vb.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object to create a **FaxJobs** object on the connected fax server.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




