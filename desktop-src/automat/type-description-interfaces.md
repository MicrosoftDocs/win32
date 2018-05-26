---
title: Type Description Interfaces
description: The automation type description interfaces provide a way to read and bind to the descriptions of objects in a type library. These descriptions are used by ActiveX clients when they browse, create, and manipulate ActiveX (Automation) objects.
ms.assetid: ab44422c-97d6-4a63-ade1-db919d53aae7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Type Description Interfaces

The automation type description interfaces provide a way to read and bind to the descriptions of objects in a type library. These descriptions are used by ActiveX clients when they browse, create, and manipulate ActiveX (Automation) objects.

A type library is accessed through the [**ITypeLib**](/windows/previous-versions/oaidl/nn-oaidl-itypelib?branch=master) interface. The **ITypeLib** interface provides access to information about the type description in a type library. The descriptions of individual objects are accessed through the [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master) interface.

The following table describes the type description interfaces:

## In this section



| Topic                                                 | Description                                                                                                                                                                          |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Type Descriptions](type-descriptions.md)<br/> | The information associated with an object described by [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master) can include a set of functions, a set of data members, and various type attributes.<br/> |
| [**ITypeComp**](/windows/previous-versions/oaidl/nn-oaidl-itypecomp?branch=master)<br/>             | The [**ITypeComp**](/windows/previous-versions/oaidl/nn-oaidl-itypecomp?branch=master) interface provides a fast way to access information that compilers need when binding to and instantiating structures and interfaces. <br/>  |
| [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master)<br/>             | Used for reading information about objects.<br/>                                                                                                                               |
| [**ITypeInfo2**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo2?branch=master)<br/>           | Used for reading information about objects.<br/>                                                                                                                               |
| [**ITypeLib**](/windows/previous-versions/oaidl/nn-oaidl-itypelib?branch=master)<br/>               | Represents a type library, the data that describes a set of objects.<br/>                                                                                                      |
| [**ITypeLib2**](/windows/previous-versions/oaidl/nn-oaidl-itypelib2?branch=master)<br/>             | Represents a type library, the data that describes a set of objects.<br/>                                                                                                      |



 

## Related topics

<dl> <dt>

[Type Description Functions](type-description-functions.md)
</dt> </dl>

 

 





