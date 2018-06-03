---
title: Type Description Interfaces
description: The automation type description interfaces provide a way to read and bind to the descriptions of objects in a type library. These descriptions are used by ActiveX clients when they browse, create, and manipulate ActiveX (Automation) objects.
ms.assetid: ab44422c-97d6-4a63-ade1-db919d53aae7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Type Description Interfaces

The automation type description interfaces provide a way to read and bind to the descriptions of objects in a type library. These descriptions are used by ActiveX clients when they browse, create, and manipulate ActiveX (Automation) objects.

A type library is accessed through the [**ITypeLib**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypelib) interface. The **ITypeLib** interface provides access to information about the type description in a type library. The descriptions of individual objects are accessed through the [**ITypeInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypeinfo) interface.

The following table describes the type description interfaces:

## In this section



| Topic                                                 | Description                                                                                                                                                                          |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Type Descriptions](type-descriptions.md)<br/> | The information associated with an object described by [**ITypeInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypeinfo) can include a set of functions, a set of data members, and various type attributes.<br/> |
| [**ITypeComp**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypecomp)<br/>             | The [**ITypeComp**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypecomp) interface provides a fast way to access information that compilers need when binding to and instantiating structures and interfaces. <br/>  |
| [**ITypeInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypeinfo)<br/>             | Used for reading information about objects.<br/>                                                                                                                               |
| [**ITypeInfo2**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypeinfo2)<br/>           | Used for reading information about objects.<br/>                                                                                                                               |
| [**ITypeLib**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypelib)<br/>               | Represents a type library, the data that describes a set of objects.<br/>                                                                                                      |
| [**ITypeLib2**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypelib2)<br/>             | Represents a type library, the data that describes a set of objects.<br/>                                                                                                      |



 

## Related topics

<dl> <dt>

[Type Description Functions](type-description-functions.md)
</dt> </dl>

 

 





