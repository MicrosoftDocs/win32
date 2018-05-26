---
Description: The FaxRoutingMethods object represents a collection of FaxRoutingMethod objects.
ms.assetid: 8f164bc0-647c-4495-be67-2f208770c28d
title: FaxRoutingMethods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxRoutingMethods

The FaxRoutingMethods object represents a collection of [FaxRoutingMethod](-mfax-faxroutingmethod.md) objects. The FaxRoutingMethods object permits a fax client application to enumerate the fax routing methods associated with a specific fax port, and to create FaxRoutingMethod objects for those routing methods.

A FaxRoutingMethods object is created by a [FaxPort](-mfax-faxport.md) object. FaxRoutingMethod objects are created by FaxRoutingMethods objects.

A fax client application must create an instance of a [FaxServer](-mfax-faxserver-client.md) object before accessing most other objects that begin with Fax. (A fax server connection is not required to access a [FaxTiff](-mfax-faxtiff.md) object.)

## C/C++

-   Create by calling the [**IFaxPort::GetRoutingMethods**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxport-getroutingmethods?branch=master) method.
-   Supports the [**IFaxRoutingMethods**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxroutingmethods?branch=master) interface.

For more information about creating an instance of a FaxRoutingMethods object, and for a list of the object's properties and methods, see [**IFaxRoutingMethods**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxroutingmethods?branch=master).

## Visual Basic

Create by calling the [**GetRoutingMethods**](-mfax-faxport-object-visual-basic-.md) method of the [**FaxPort**](-mfax-faxport-object-visual-basic-.md) object.

For more information about creating a FaxRoutingMethods object, and for a list of the properties and methods of the object, see [**FaxRoutingMethods object (Visual Basic)**](-mfax-faxroutingmethods-object-visual-basic-.md).

 

 



