---
title: Schema Implementation
description: In Active Directory Domain Services, class and attribute definitions are stored in the directory as instances of the classSchema and attributeSchema classes, respectively.
ms.assetid: 917f8e65-df2c-457e-bfd8-3f1ce0d0fbae
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Schema Implementation

In Active Directory Domain Services, class and attribute definitions are stored in the directory as instances of the [**classSchema**](/windows/desktop/ADSchema/c-classschema) and [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) classes, respectively. **classSchema** and **attributeSchema** are classes defined in the schema. To manipulate the Active Directory schema, use the same LDAP operations used to manipulate other object. Because the schema is a key part of the directory that affects the entire forest, special restrictions apply to schema extensions. For more information about restrictions, see [Restrictions on Schema Extensions](restrictions-on-schema-extension.md).

To summarize the schema implementation:

-   Instances of the [**classSchema**](/windows/desktop/ADSchema/c-classschema) class define every object class supported by Active Directory Domain Services. The attributes of a **classSchema** object, for example, its [**mayContain**](/windows/desktop/ADSchema/a-maycontain) and [**mustContain**](/windows/desktop/ADSchema/a-mustcontain) attributes, describe an object class, the same way that the attributes of a user object, for example, its [**userPrincipalName**](/windows/desktop/ADSchema/a-userprincipalname) and [**telephoneNumber**](/windows/desktop/ADSchema/a-telephonenumber) attributes, describe that user. For more information, see [Characteristics of Object Classes](characteristics-of-object-classes.md).
-   Instances of the [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) class are used to define every attribute supported by Active Directory Domain Services. The attributes of an **attributeSchema** object, for example, its **attributeSyntax** and **isSingleValued** attributes, describe an attribute, the same way the attributes of a user object describe that user. For more information, see [Characteristics of Attributes](characteristics-of-attributes.md).
-   Instances of the [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) and [**classSchema**](/windows/desktop/ADSchema/c-classschema) classes are stored in a well-known place in the directory, the schema container. The schema container always has a distinguished name of the form:

    ```C++
    CN=Schema,CN=Configuration,<DC=forestroot>
    ```

    

    where "&lt;DC=forestroot&gt;" is the distinguished name of the root of the forest, for example, "DC=Fabrikam,DC=Com".

    To get the distinguished name of the schema container, read the **schemaNamingContext** attribute of rootDSE. For more information about rootDSE and its attributes, see [Serverless Binding and RootDSE](serverless-binding-and-rootdse.md).

When thinking about the schema, remember:

-   Schema changes are global. There is a single schema for an entire forest. The schema is globally replicated: a copy of the schema exists on every domain controller in the forest. When you extend the schema, you do so for the entire forest.
-   Schema additions are not reversible. When a new class or attribute is added to the schema, it cannot be removed. An existing attribute or class can be disabled, but not removed. For more information, see [Disabling Existing Classes and Attributes](disabling-existing-classes-and-attributes.md).
-   Disabling a class or attribute does not affect existing instances of the class or attribute, but it prevents new instances from being created. You cannot disable an attribute if it is included in any class that is not disabled.

 

 