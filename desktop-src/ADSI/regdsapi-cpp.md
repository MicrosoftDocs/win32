---
title: REGDSAPI.CPP
description: In the example provider component, functions that represent an API that directly accesses the native operating system are in Regdsapi.cpp.
ms.assetid: dc5ab286-5c70-43a3-90a1-f3f8a1c61c43
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# REGDSAPI.CPP

In the example provider component, functions that represent an API that directly accesses the native operating system are in Regdsapi.cpp. The example provider component implements its directory service in the registry. To write a provider that accesses your own directory service, create your own implementations of this API. Supported functions are listed in the following table.



| Method                             | Description                                                                                                                                                                                    |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SampleDSOpenObject**             | Open this object by name. If the schema class type parameter is **NULL**, fill in the type found. Retrieve a handle on the object.                                                             |
| **SampleDSCloseObject**            | Use the handle retrieved by **SampleDSOpenObject**.                                                                                                                                            |
| **SampleDSRDNEnum**                | Retrieve the handle on an enumerator object to manage the enumeration of relative distinguished names (RDNs) from a container object.                                                          |
| **SampleDSNextRDN**                | Using the handle retrieved by **SampleDSRDNEnum**, get the next relative distinguished name from this container object.                                                                        |
| **SampleDSFreeEnum**               | Free the enumerator object allocated in **SampleDSRDNEnum**.                                                                                                                                   |
| **SampleDSModifyObject**           | Modify properties of an object in the directory service given the handle of the object and a list of attributes and their values.                                                              |
| **SampleDSReadObject**             | Read the properties of the object from the directory service. Map the syntax from the native storage to the appropriate ADS syntax values. Handle properties with multiple values accordingly. |
| **SampleDSGetPropertyDefinition**  | In the schema, look up all property definitions and their attributes for this type of schema class object.                                                                                     |
| **SampleDSGetPropertyDefinition**  | In the schema, look up this property and its attributes by name.                                                                                                                               |
| **SampleDSFreePropertyDefinition** | Free memory allocated by **GetPropertyDefinition**.                                                                                                                                            |
| **SampleDSGetTypeText**            | Get the schema class type of an object in text format.                                                                                                                                         |
| **SampleDSGetType**                | Get the schema class type of an object.                                                                                                                                                        |
| **SampleDSGetPropertyInfo**        | Given a handle on the schema class object and a property name, retrieve the property information, like syntax, and so on.                                                                      |
| **FreeList**                       | Free the memory used by a LPWSTR\_LIST.                                                                                                                                                        |
| **SampleDSGetClassDefinition**     | Retrieve the set of all schema class definitions and their associated data from the schema.                                                                                                    |
| **SampleDSGetClassDefinition**     | Retrieve data about a particular schema class in the schema.                                                                                                                                   |
| **SampleDSGetClassInfo**           | Given the name of a schema class, look up its associated data, like mandatory properties.                                                                                                      |
| **SampleDSAddObject**              | Add an object in the directory service.                                                                                                                                                        |
| **SampleDSRemoveObject**           | Remove an object from the directory service.                                                                                                                                                   |
| **SampleDSCreateBuffer**           | Create a memory buffer for attribute data and operation data.                                                                                                                                  |
| **SampleDSFreeBuffer**             | Free the buffer created in **SampleDSCreateBuffer**.                                                                                                                                           |



 

 

 




