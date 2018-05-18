---
title: CCLSOBJ.CPP
description: In the example provider component, the functions for the schema class object are contained in cclsobj.cpp.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'e8cdef8e-c031-49e0-9496-871064aec8bd'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["CSampleDSClass"]
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
| Standard IADs methods.      | Standard [**IADs**](iads.md) interface methods included in this file.                                                                                                                                     |
| Standard IADsClass methods. | Standard [**IADsClass**](iadsclass.md) interface methods included in this file.                                                                                                                           |
| **CreatePropertyList**      | Create a list of properties associated with this schema class by calling **CreatePropertyEntry**.                                                                                                          |
| **CreatePropertyEntry**     | Create one property object in this schema class.                                                                                                                                                           |
| **FreePropertyEntry**       | Free the entry made in **CreatePropertyEntry**.                                                                                                                                                            |
| **MakeVariantFromPropList** | Create an array of VARIANTS from the property list created by **CreatePropertyList**. Can be used in the implementation of [**IADsClass::MandatoryAttributes**](iadsclass-property-methods.md) and so on. |



 

 

 




