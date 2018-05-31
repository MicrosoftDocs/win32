---
Description: This topic describes how to modify certain configuration data that applies to a fax port.
ms.assetid: 940d0d7c-e891-44a4-9f9f-febbd6e9b6d0
title: Modifying Fax Port Data
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Modifying Fax Port Data

A fax client application can modify certain configuration data that applies to a fax port. The data includes the transmission priority assigned to the port and the number of rings an incoming fax call should wait before the port answers the call. It also includes the current status and capability of the port, and the transmitting and called station identifiers.

## In the Win32 Environment

A fax client application can call the [**FaxSetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetporta) function to change the configuration of the fax ports associated with a fax server.

Note that an application must first call the [**FaxOpenPort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxopenport) function, specifying the PORT\_OPEN\_MODIFY port access level, to obtain a fax port handle before calling the [**FaxSetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetporta) function.

## In the COM Implementation Environment

After you create an instance of a [FaxPort](-mfax-faxport.md) object, call the [**IFaxPort::GetRoutingMethods**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getroutingmethods) method (the **GetRoutingMethods** method of the FaxPort object in Microsoft Visual Basic) to create a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object. This object can then be used to create an instance of a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object. Use the FaxRoutingMethod object to enable or disable a fax routing method on a specific fax port. For more information, see [Managing Fax Routing Data](-mfax-managing-fax-routing-data.md).

Note that before your application calls a method that modifies a [FaxPort](-mfax-faxport.md) property, you can call the [**IFaxPort::get\_CanModify**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-get_canmodify) method (retrieve the **CanModify** property of the FaxPort object in Visual Basic) to ensure that the client has access to modify the port's configuration.

If you are writing a C/C++ application, after you create a [FaxPort](-mfax-faxport.md) object for a specified fax port, you can call [**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport) interface methods to change properties of the port. For information about the steps required to create a FaxPort object, and for a list of properties and methods, see **IFaxPort**.

If you are writing a Visual Basic application, after you create a [FaxPort](-mfax-faxport.md) object for a specified fax port, you can retrieve multiple properties of the object. See [**FaxPort object (Visual Basic)**](-mfax-faxport-object-visual-basic-.md) for more information about the steps required to create the object, and for a list of properties and methods of the object.

 

 



