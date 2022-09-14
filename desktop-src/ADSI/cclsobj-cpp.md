---
title: CCLSOBJ.CPP
description: In the example provider component, the functions for the schema class object are contained in cclsobj.cpp.
ms.assetid: e8cdef8e-c031-49e0-9496-871064aec8bd
ms.tgt_platform: multiple
keywords:
- CSampleDSClass
ms.topic: article
ms.date: 05/31/2018
---

# CCLSOBJ.CPP

In the example provider component, the functions for the schema class object are contained in cclsobj.cpp.

The **CSampleDSClass** class is defined in this file. **CSampleDSClass** is defined with methods and properties listed in the following table.



| Method                      | Description                                                                                                                                                                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CSampleDSClass**          | Standard constructor.                                                                                                                                                                                      |
| **~CSampleDSClass**         | Standard destructor.                                                                                                                                                                                       |
| **CreateClass**             | Create an ADs schema class object. Lookup attribute definitions by calling **SampleDSGetClassDefinition**.                                                                                                 |
| **CreateClass**             | Create a schema class object, given the attribute definitions, setting known attributes, such as those listed in [**IADsClass::MandatoryAttributes**](iadsclass-property-methods.md).                     |
| **AllocateClassObject**     | Create a schema class object and load its type data.                                                                                                                                                       |
| **QueryInterface**          | Return the requested interface pointer, if available.                                                                                                                                                      |
| Standard IADs methods.      | Standard [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface methods included in this file.                                                                                                                                     |
| Standard IADsClass methods. | Standard [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass) interface methods included in this file.                                                                                                                           |
| **CreatePropertyList**      | Create a list of properties associated with this schema class by calling **CreatePropertyEntry**.                                                                                                          |
| **CreatePropertyEntry**     | Create one property object in this schema class.                                                                                                                                                           |
| **FreePropertyEntry**       | Free the entry made in **CreatePropertyEntry**.                                                                                                                                                            |
| **MakeVariantFromPropList** | Create an array of VARIANTS from the property list created by **CreatePropertyList**. Can be used in the implementation of [**IADsClass::MandatoryAttributes**](iadsclass-property-methods.md) and so on. |



 

 

 




