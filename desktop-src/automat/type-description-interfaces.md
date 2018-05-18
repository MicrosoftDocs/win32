---
title: Type Description Interfaces
description: The automation type description interfaces provide a way to read and bind to the descriptions of objects in a type library. These descriptions are used by ActiveX clients when they browse, create, and manipulate ActiveX (Automation) objects.
ms.assetid: 'ab44422c-97d6-4a63-ade1-db919d53aae7'
---

# Type Description Interfaces

The automation type description interfaces provide a way to read and bind to the descriptions of objects in a type library. These descriptions are used by ActiveX clients when they browse, create, and manipulate ActiveX (Automation) objects.

A type library is accessed through the [**ITypeLib**](itypelib.md) interface. The **ITypeLib** interface provides access to information about the type description in a type library. The descriptions of individual objects are accessed through the [**ITypeInfo**](itypeinfo.md) interface.

The following table describes the type description interfaces:

## In this section



| Topic                                                 | Description                                                                                                                                                                          |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Type Descriptions](type-descriptions.md)<br/> | The information associated with an object described by [**ITypeInfo**](itypeinfo.md) can include a set of functions, a set of data members, and various type attributes.<br/> |
| [**ITypeComp**](itypecomp.md)<br/>             | The [**ITypeComp**](itypecomp.md) interface provides a fast way to access information that compilers need when binding to and instantiating structures and interfaces. <br/>  |
| [**ITypeInfo**](itypeinfo.md)<br/>             | Used for reading information about objects.<br/>                                                                                                                               |
| [**ITypeInfo2**](itypeinfo2.md)<br/>           | Used for reading information about objects.<br/>                                                                                                                               |
| [**ITypeLib**](itypelib.md)<br/>               | Represents a type library, the data that describes a set of objects.<br/>                                                                                                      |
| [**ITypeLib2**](itypelib2.md)<br/>             | Represents a type library, the data that describes a set of objects.<br/>                                                                                                      |



 

## Related topics

<dl> <dt>

[Type Description Functions](type-description-functions.md)
</dt> </dl>

 

 





