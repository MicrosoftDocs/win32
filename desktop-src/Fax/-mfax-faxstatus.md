---
Description: The FaxStatus object permits a fax client application to retrieve status information for a specific port on a connected fax server.
ms.assetid: 88f02cb1-df32-4fb8-9fe7-6c3abe1948dc
title: FaxStatus
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus

The FaxStatus object permits a fax client application to retrieve status information for a specific port on a connected fax server. You can use the object to provide real-time status information about a [FaxPort](-mfax-faxport.md) object.

A FaxStatus object is created by a FaxPort object.

A fax client application must create an instance of a [FaxServer](-mfax-faxserver-client.md) object before accessing most other objects that begin with Fax. (A fax server connection is not required to access a [FaxTiff](-mfax-faxtiff.md) object.)

## C/C++

-   Create by calling the [**IFaxPort::GetStatus**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getstatus) method.
-   Supports the [**IFaxStatus**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxstatus) interface.

For more information about creating an instance of a FaxStatus object, and for a list of the object's properties and methods, see [**IFaxStatus**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxstatus).

## Visual Basic

Create by calling the [**GetStatus**](-mfax-faxport-object-visual-basic-.md) method of the [**FaxPort**](-mfax-faxport-object-visual-basic-.md) object.

For more information about creating a FaxStatus object, and for a list of the properties and methods of the object, see [**FaxStatus object (Visual Basic)**](-mfax-faxstatus-object-visual-basic-.md).

 

 



