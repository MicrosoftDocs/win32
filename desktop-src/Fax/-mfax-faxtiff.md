---
Description: The FaxTiff object permits a fax client application to retrieve the properties of a file that the fax service has transmitted or received.
ms.assetid: 70acd518-4058-4146-bbdf-50108d0c7e3f
title: FaxTiff
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxTiff

The FaxTiff object permits a fax client application to retrieve the properties of a file that the fax service has transmitted or received. These files are Tagged Image File Format Class F (TIFF Class F) files. A fax server connection is not required to access a FaxTiff object.

The FaxTiff object is a standalone object. You do not need to create a [FaxServer](-mfax-faxserver-client.md) object before you create an instance of a FaxTiff object.

## C/C++

-   Create by calling the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function.
-   Supports the [**IFaxTiff**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxtiff?branch=master) interface.

For more information about creating an instance of a FaxTiff object, and for a list of the object's properties and methods, see [**IFaxTiff**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxtiff?branch=master).

## Visual Basic

Create by calling the Microsoft Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function.

For more information about creating a FaxTiff object, and for a list of the properties and methods of the object, see [**FaxTiff object (Visual Basic)**](-mfax-faxtiff-object-visual-basic-.md).

 

 



