---
title: Single vs. Multiple Value Attributes
description: The attributes that can exist in a directory are typically defined in the schema for the directory.
ms.assetid: ea06ca66-6407-448f-8238-c8de5353663b
ms.tgt_platform: multiple
keywords:
- single vs. multiple value attributes ADSI
- attributes ADSI , single vs. multiple value attributes
ms.topic: article
ms.date: 05/31/2018
---

# Single vs. Multiple Value Attributes

The attributes that can exist in a directory are typically defined in the schema for the directory. The schema definition of an attribute specifies a number of characteristics of the attribute, such as the data type and whether an instance of the attribute can have multiple values.

An instance of a single-valued attribute can contain a single value. An instance of a multivalued attribute can contain either a single value or multiple values. Active Directory does not create attributes with empty values—either the attribute contains a valid value or it does not exist on the object.

> [!Note]  
> In Active Directory and most other LDAP servers, the order of values in a multi-valued attribute is undefined. Also, each value of a multi-valued attribute must be unique.

 

ADSI normally loads schema data if your directory supports a schema, as Active Directory does. Because ADSI knows the syntax of attributes in the schema, you are not required to specify the attribute type when accessing it. ADSI marshals attribute values to the appropriate data type as defined in the schema.

If your directory has no schema, supply the data type when accessing an attribute.

> [!Note]  
> Active Directory, Exchange, Windows NT 4.0, and Site Server all have a schema. In addition, Active Directory has an extensible schema.

 

 

 




