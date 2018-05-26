---
Description: This topic describes how to retrieve fax file data in the Component Object Model (COM) implementation environment.
ms.assetid: 8e14ae44-b712-4ebf-bff7-54afe58c0d39
title: Retrieving Fax File Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Fax File Data

This functionality is currently available only in the Component Object Model (COM) implementation environment. It is not available in the Microsoft Win32 environment.

The fax service converts files it processes to the Tagged Image File Format Class F (TIFF Class F) for facsimile. The service embeds custom Tagged Image File Format (TIFF) tags in the file to store information about the fax transmission. A fax client application can use the [FaxTiff](-mfax-faxtiff.md) object to retrieve information about a file the fax service has sent or received. For more information, see [Fax Image Format](-mfax-fax-image-format.md).

An application can query the properties of a [FaxTiff](-mfax-faxtiff.md) object. Properties include device and station identifiers, the fax number, and sender and recipient names. You do not need to create a FaxServer object before you create an instance of a FaxTiff object.

If you are writing a C/C++ application, after you create a [FaxTiff](-mfax-faxtiff.md) object for a fax file, you can call [**IFaxTiff**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxtiff?branch=master) interface methods to query the properties of the file. For information about the steps required to create a FaxTiff object, and for a list of properties and methods, see **IFaxTiff**.

If you are writing a Microsoft Visual Basic application, after you create a [FaxTiff](-mfax-faxtiff.md) object for a specified fax file, you can retrieve multiple properties of the object. See [**FaxTiff object (Visual Basic)**](-mfax-faxtiff-object-visual-basic-.md) for more information about the steps required to create the object, and for a list of properties and methods of the object.

 

 



