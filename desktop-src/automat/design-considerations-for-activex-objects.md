---
title: Design Considerations for ActiveX Objects
description: Provides guidance for designing an Automation application.
ms.assetid: 10ad9099-3810-4c74-8962-f7ecd7ae3b50
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Design Considerations for ActiveX Objects

When you expose objects to Automation, you need to decide which interfaces to implement and how to organize your objects. You should also create a type library. This section provides information to guide you in designing an Automation application.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Creating the Programmable Interface](creating-the-programmable-interface.md)<br/>         | An object's programmable interface comprises the properties, methods, and events that it defines.<br/>                                                                         |
| [Creating the IUnknown Interface](creating-the-iunknown-interface.md)<br/>                 | The **IUnknown** interface defines three member functions that must be implemented for each object that is exposed.<br/>                                                       |
| [Creating the IDispatch Interface](creating-the-idispatch-interface.md)<br/>               | The [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface provides a [late-bound](glossary.md) mechanism to access and retrieve information about an object's methods and properties.<br/> |
| [Implementing Dual Interfaces](implementing-dual-interfaces.md)<br/>                       | It is recommended that you implement dual interfaces because of the advantages in doing so.<br/>                                                                               |
| [Registering Interfaces](registering-interfaces.md)<br/>                                   | Applications that add interfaces need to register the interfaces so OLE can find the appropriate remoting code for interprocess communication.<br/>                            |
| [Creating Class Identifiers](creating-class-identifiers.md)<br/>                           | CLSIDs are universally unique identifiers (UUIDs, also called globally unique identifiers, or GUIDs) that identify class objects to OLE.<br/>                                  |
| [Passing Formatted Data](passing-formatted-data.md)<br/>                                   | When handling formatted data, the application should pass an object that implements the OLE **IDataObject** interface.<br/>                                                    |
| [Implementing the IEnumVARIANT Interface](implementing-the-ienumvariant-interface.md)<br/> | Automation defines the [**IEnumVARIANT**](/windows/previous-versions/oaidl/nn-oaidl-ienumvariant?branch=master) interface to provide a standard way for ActiveX clients to iterate over collection objects.<br/>                   |
| [Implementing the \_NewEnum Property](implementing-the--newenum-property.md)<br/>          | The **\_NewEnum** property identifies an object as supporting iteration through the [**IEnumVARIANT**](/windows/previous-versions/oaidl/nn-oaidl-ienumvariant?branch=master) interface.<br/>                                       |



 

 

 





