---
Description: The FaxServer object permits a fax client application to connect to and disconnect from an active fax server.
ms.assetid: e3169385-6a7f-4b2d-ad70-6d4d323becb8
title: FaxServer
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer

The FaxServer object permits a fax client application to connect to and disconnect from an active fax server. After you obtain a connection, you can create other objects you need; for example, [FaxDoc](-mfax-faxdoc.md), [FaxJobs](-mfax-faxjobs.md) and [FaxPorts](-mfax-faxports.md) objects. You can also use the FaxServer object to set and retrieve information relative to the connected fax server.

[FaxDoc](-mfax-faxdoc.md), [FaxJobs](-mfax-faxjobs.md) and [FaxPorts](-mfax-faxports.md) objects are created by FaxServer objects.

A fax client application must create an instance of a FaxServer object before accessing most other objects that begin with Fax. (A fax server connection is not required to access a [FaxTiff](-mfax-faxtiff.md) object.)

## C/C++

-   Create by calling the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function.
-   Supports the [**IFaxServer**](/windows/previous-versions/faxcom/nn-faxcom-ifaxserver?branch=master) interface.

For more information about creating an instance of a FaxServer object, and for a list of the object's properties and methods, see [**IFaxServer**](/windows/previous-versions/faxcom/nn-faxcom-ifaxserver?branch=master).

## Visual Basic

Create a [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object by calling the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function.

For more information about creating a FaxServer object, and for a list of the properties and methods of the object, see [**FaxServer object (Visual Basic)**](-mfax-faxserver-object-visual-basic-.md).

 

 



