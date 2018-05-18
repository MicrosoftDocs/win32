---
Description: 'This topic describes how to manage fax routing data for individual ports in a Component Object Model (COM) implementation environment.'
ms.assetid: 'e3faa8db-fe56-48fd-b2af-31c8b5de4c9b'
title: 'Managing Fax Routing Data for Individual Ports (COM Implementation)'
---

# Managing Fax Routing Data for Individual Ports (COM Implementation)

In addition to enabling or disabling a fax routing method on a specified fax port, a fax client application can retrieve data about the method. Data includes the name of the DLL that exports the fax routing method, the GUID and function name that uniquely identify the routing method, and the method's user-friendly name.

If you are writing a C/C++ application, after you create a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object for a fax routing method on a specified port, call [**IFaxRoutingMethod**](-mfax-ifaxroutingmethod.md) interface methods. These methods can retrieve properties of the routing method and enable or disable a routing method on the port. For information about the steps required to create a FaxRoutingMethod object, and for a list of its properties, see [**IFaxRoutingMethod**](-mfax-ifaxroutingmethod.md).

If you are writing a Microsoft Visual Basic application, after you create a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object for a fax routing method on a specified port, you can retrieve multiple properties of the object. You can also enable or disable a routing method on the port. For more information about the steps required to create the object, and for a list of properties and methods of the object, see [**FaxRoutingMethod object (Visual Basic)**](-mfax-faxroutingmethod-object-visual-basic-.md).

 

 



