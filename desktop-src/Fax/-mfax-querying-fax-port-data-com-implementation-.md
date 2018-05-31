---
Description: This topic describes how to query fax port data in the Component Object Model (COM) implementation environment.
ms.assetid: 6e977654-2776-4881-8e85-a32a82ac384e
title: Querying Fax Port Data (COM Implementation)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying Fax Port Data (COM Implementation)

The [FaxPort](-mfax-faxport.md) object is available for a fax client application to query the permanent line identifier of a port and the port's current status. You can also retrieve the transmission priority assigned to the port, the number of rings an incoming fax call should wait before the port answers the call, and whether transmission and reception of faxes are currently enabled on the port.

After you create an instance of a [FaxPort](-mfax-faxport.md) object, call the [**IFaxPort::GetStatus**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getstatus) method (the **Status** method of the FaxPort object in Microsoft Visual Basic) to create a [FaxStatus](-mfax-faxstatus.md) object. Use the FaxStatus object to retrieve real-time status information about the parent FaxPort object.

You can call the [**IFaxPort::GetRoutingMethods**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getroutingmethods) method (the **GetRoutingMethods** method of the [FaxPort](-mfax-faxport.md) object in Visual Basic) to create a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object. You can then use this object to create an instance of a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object. Use the FaxRoutingMethod object to retrieve fax routing configuration information for a fax port on a connected fax server. For more information, see [Managing Fax Routing Data](-mfax-managing-fax-routing-data.md).

If you are writing a C/C++ application, after you create a [FaxPort](-mfax-faxport.md) object for a specified fax port, you can call the [**IFaxPort**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxport) interface methods to retrieve the properties of the port. For information about the steps required to create a FaxPort object, and for a list of properties and methods, see **IFaxPort**.

If you are writing a Visual Basic application, after you create a [FaxPort](-mfax-faxport.md) object for a specified fax port, you can retrieve multiple properties of the object. See [**FaxPort**](-mfax-faxport-object-visual-basic-.md)) for more information about the steps required to create the object, and for a list of properties and methods of the object.

 

 



