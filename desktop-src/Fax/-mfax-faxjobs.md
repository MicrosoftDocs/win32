---
Description: 'The FaxJobs object represents a collection of FaxJob objects.'
ms.assetid: '7a8ad6e7-8db6-49ba-98de-da583907a54e'
title: FaxJobs
---

# FaxJobs

The FaxJobs object represents a collection of [FaxJob](-mfax-faxjob.md) objects. The FaxJobs object permits a fax client application to create FaxJob objects and to enumerate the fax jobs associated with a connected fax server.

A FaxJobs object is created by a [**FaxServer**](-mfax-faxserver.md) object. FaxJob objects are created by FaxJobs objects.

A fax client application must create an instance of a [FaxServer](-mfax-faxserver-client.md) object before accessing most other objects that begin with Fax. (A fax server connection is not required to access a [FaxTiff](-mfax-faxtiff.md) object.)

## C/C++

-   Create by calling the [**IFaxServer::GetJobs**](-mfax-ifaxserver-client-mfax-ifaxserver-getjobs-cpp.md) method.
-   Supports the [**IFaxJobs**](-mfax-ifaxjobs.md) interface.

For more information about creating an instance of a FaxJobs object, and for a list of the object's properties and methods, see [**IFaxJobs**](-mfax-ifaxjobs.md).

## Visual Basic

Create by calling the [**GetJobs**](-mfax-faxserver-object-visual-basic-.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object.

For more information about creating a FaxJobs object, and for a list of the properties and methods of the object, see [**FaxJobs object (Visual Basic)**](-mfax-faxjobs-object-visual-basic-.md).

 

 



