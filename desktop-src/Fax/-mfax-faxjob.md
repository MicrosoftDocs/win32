---
Description: 'The FaxJob object permits a fax client application to access the job status of incoming and outgoing fax transmissions, and to pause, resume, cancel or restart a fax job.'
ms.assetid: '4c8376a4-dded-489e-a361-ce6edd0e17af'
title: FaxJob
---

# FaxJob

The FaxJob object permits a fax client application to access the job status of incoming and outgoing fax transmissions, and to pause, resume, cancel or restart a fax job. You can also use the object to retrieve the properties of fax jobs.

A FaxJob object is created by a [FaxJobs](-mfax-faxjobs.md) object.

A fax client application must create an instance of a [FaxServer](-mfax-faxserver-client.md) object before accessing most other objects that begin with Fax. (A fax server connection is not required to access a [FaxTiff](-mfax-faxtiff.md) object.)

## C/C++

-   Create by calling the [**IFaxJobs::get\_Item**](-mfax-ifaxjobs-get-item.md) method.
-   Supports the [**IFaxJob**](-mfax-ifaxjob.md) interface.

For more information about creating an instance of a FaxJob object, and for a list of the object's properties and methods, see [**IFaxJob**](-mfax-ifaxjob.md).

## Visual Basic

Create by retrieving the [**Item**](-mfax-faxjobs-object-visual-basic-.md) property of the [**FaxJobs**](-mfax-faxjobs-object-visual-basic-.md) object.

For more information about creating a FaxJob object, and for a list of the properties and methods of the object, see [**FaxJob object (Visual Basic)**](-mfax-faxjob-object-visual-basic-.md).

 

 



