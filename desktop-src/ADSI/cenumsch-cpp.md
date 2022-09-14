---
title: CENUMSCH.CPP
description: In the example provider component, the enumeration of a schema object uses the methods, from cenumsch.cpp, listed in the following table.
ms.assetid: edad1ad1-16b9-40f3-b841-a70aa7fff5d9
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# CENUMSCH.CPP

In the example provider component, the enumeration of a schema object uses the methods, from cenumsch.cpp, listed in the following table.



| Method                                        | Description                                                                                                          |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **CSampleDSSchemaEnum::Create**               | Create an object to allow enumeration of an ADSI schema class object.                                                |
| **CSampleDSSchemaEnum::CSampleDSSchemaEnum**  | Standard constructor.                                                                                                |
| **CSampleDSSchemaEnum::~CSampleDSSchemaEnum** | Standard destructor.                                                                                                 |
| **CSampleDSSchemaEnum::Next**                 | Retrieve the specified number of elements from the schema object indicated.                                          |
| **CSampleDSSchemaEnum::EnumObjects**          | Manage retrieving the interfaces pointers to the objects of the object type indicated.                               |
| **CSampleDSSchemaEnum::EnumObjects**          | Manage retrieving the interface pointers to the objects of the default object type.                                  |
| **CSampleDSSchemaEnum::EnumClasses**          | Manage retrieving the interface pointers to only the schema class objects contained in this object.                  |
| **CSampleDSSchemaEnum::GetClassObject**       | Retrieve the next schema class definition; if found, create a schema class object, and return the interface pointer. |
| **CSampleDSSchemaEnum::EnumProperties**       | Manage retrieving the interface pointers to the property objects only contained in this object.                      |
| **CSampleDSSchemaEnum::GetPropertyObject**    | Retrieve the next property definition; if found, create a schema class object, and return the interface pointer.     |
| **CSampleDSSchemaEnum::EnumSyntaxes**         | Manage retrieving the interface pointers to the syntax objects only contained in this object.                        |
| **CSampleDSSchemaEnum::GetSyntaxObject**      | Retrieve the next syntax definition; if found, create a schema class object, and return the interface pointer.       |



 

 

 




