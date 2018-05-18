---
Description: 'The FaxPorts object represents a collection of FaxPort objects.'
ms.assetid: 'ac1e4c87-ba3b-4b49-887c-ed392ddab455'
title: FaxPorts
---

# FaxPorts

The FaxPorts object represents a collection of [FaxPort](-mfax-faxport.md) objects. The FaxPorts object permits a fax client application to enumerate the fax ports associated with a connected fax server, and to create FaxPort objects for those ports.

A FaxPorts object is created by a [**FaxServer**](-mfax-faxserver.md) object. FaxPort objects are created by FaxPorts objects.

A fax client application must create an instance of a [FaxServer](-mfax-faxserver-client.md) object before accessing most other objects that begin with Fax. (A fax server connection is not required to access a [FaxTiff](-mfax-faxtiff.md) object.)

## C/C++

-   Create by calling the [**IFaxServer::GetPorts**](-mfax-ifaxserver-client-mfax-ifaxserver-getports-cpp.md) method.
-   Supports the [**IFaxPorts**](-mfax-ifaxports.md) interface.

For more information about creating an instance of a FaxPorts object, and for a list of the object's properties and methods, see [**IFaxPorts**](-mfax-ifaxports.md).

## Visual Basic

Create by calling the [**GetPorts**](-mfax-faxserver-object-visual-basic-.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object.

For more information about creating a FaxPorts object, and for a list of the properties and methods of the object, see [**FaxPorts object (Visual Basic)**](-mfax-faxports-object-visual-basic-.md).

 

 



