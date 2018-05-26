---
Description: The FaxStatus object permits a fax client application to retrieve status information for a specific port on a connected fax server.
ms.assetid: 88f02cb1-df32-4fb8-9fe7-6c3abe1948dc
title: FaxStatus
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxStatus

The FaxStatus object permits a fax client application to retrieve status information for a specific port on a connected fax server. You can use the object to provide real-time status information about a [FaxPort](-mfax-faxport.md) object.

A FaxStatus object is created by a FaxPort object.

A fax client application must create an instance of a [FaxServer](-mfax-faxserver-client.md) object before accessing most other objects that begin with Fax. (A fax server connection is not required to access a [FaxTiff](-mfax-faxtiff.md) object.)

## C/C++

-   Create by calling the [**IFaxPort::GetStatus**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxport-getstatus?branch=master) method.
-   Supports the [**IFaxStatus**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxstatus?branch=master) interface.

For more information about creating an instance of a FaxStatus object, and for a list of the object's properties and methods, see [**IFaxStatus**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxstatus?branch=master).

## Visual Basic

Create by calling the [**GetStatus**](-mfax-faxport-object-visual-basic-.md) method of the [**FaxPort**](-mfax-faxport-object-visual-basic-.md) object.

For more information about creating a FaxStatus object, and for a list of the properties and methods of the object, see [**FaxStatus object (Visual Basic)**](-mfax-faxstatus-object-visual-basic-.md).

 

 



