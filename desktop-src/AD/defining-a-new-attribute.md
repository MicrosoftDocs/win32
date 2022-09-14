---
title: Defining a New Attribute
description: This topic shows how to define a new attribute when extending the Active Directory schema.
ms.assetid: b8ac69ba-3b75-4e55-bf80-dabf2e80288a
ms.tgt_platform: multiple
keywords:
- Defining a New Attribute AD
ms.topic: article
ms.date: 05/31/2018
---

# Defining a New Attribute

This topic shows how to define a new attribute when extending the Active Directory schema.

Consider the following when defining a new attribute:

-   Use existing attributes when possible.
-   Always use the **cn** ("common name") property as the naming (relative distinguished name) attribute. This is the default for most classes, including those derived directly from Top. The **cn** property is an indexed property and will make searching for objects by name more efficient.
-   Large multi-valued attributes are costly to store and retrieve and should be avoided. Active Directory Domain Services implement an LDAP extension to enable incremental read of large properties with multiple values, but not all LDAP clients will recognize this extension.
-   Remember that attributes are flat, that is there is no implied substructure to an attribute. All attributes in a given class should relate directly to instances of that class.

## Creating a New Attribute

To create a new attribute:

-   Choose a name for the attribute. The name will be contained in the **cn** and **lDAPDisplayName** attributes. For more information about composing a name for a new attribute, see [Naming Attributes and Classes](naming-attributes-and-classes.md).
-   Obtain an object identifier (OID) for the attribute. For more information, see [Obtaining a Root Object Identifier](obtaining-an-object-identifier.md).
-   Choose a syntax for the attribute. The syntax is determined by the combination of the **oMSyntax** and **oMObjectClass** attributes. For more information, see [Choosing a Syntax](choosing-a-syntax.md).
-   Decide if the attribute is single or multi-valued. The **isSingleValued** attribute determines if the attribute is single or multi-valued.
-   Decide if the attribute should be indexed by default. For more information, see [Indexed Attributes](indexed-attributes.md).
-   Decide if the attribute should be in the global catalog by default. For more information, see [Attributes Included in the Global Catalog](attributes-included-in-the-global-catalog.md).
-   If the attribute is an integer or string, decide if a range limit is required. The **rangeLower** and **rangeUpper** attributes are used to specify the range limit.
-   If the attribute is DN-valued, decide if the attribute should be linked with another attribute. If so, the [**linkID**](/windows/desktop/ADSchema/a-linkid) attribute must be set appropriately on each attribute; one attribute must be a forward link, the other a back link. For more information about linked attributes, see [Linked Attributes](linked-attributes.md).
-   Create a new **attributeSchema** object in the schema container and set the appropriate attributes for the object. There are a large number of attributes that can be set for an **attributeSchema** object, but the attributes listed in the following table below are critical to the definition of a new attribute. The values of these attributes are determined by the previous steps. For more information about these attributes, see [Characteristics of Attributes](characteristics-of-attributes.md).

    | Attribute                                    | Comment                                              |
    |----------------------------------------------|------------------------------------------------------|
    | **cn**<br/>                            | Required.<br/>                                 |
    | **lDAPDisplayName**<br/>               | Required.<br/>                                 |
    | **adminDisplayName**<br/>              | Required.<br/>                                 |
    | **attributeSyntax**<br/>               | Required.<br/>                                 |
    | **oMSyntax**<br/>                      | Required.<br/>                                 |
    | **oMObjectClass**<br/>                 | Required.<br/>                                 |
    | **schemaIDGUID**<br/>                  | Required.<br/>                                 |
    | **attributeID**<br/>                   | Required.<br/>                                 |
    | **isSingleValued**<br/>                | Required.<br/>                                 |
    | **searchFlags**<br/>                   | Required.<br/>                                 |
    | **isMemberOfPartialAttributeSet**<br/> | Required.<br/>                                 |
    | **rangeLower**<br/>                    | Optional.<br/>                                 |
    | **rangeUpper**<br/>                    | Optional.<br/>                                 |
    | **linkID**<br/>                        | Optional. Required for linked attributes.<br/> |
    | **description**<br/>                   | Optional.<br/>                                 |

    

     

-   Commit the new **attributeSchema** object to the schema container.
-   Update the schema cache, if necessary. For more information, see [Updating the Schema Cache](updating-the-schema-cache.md).

 

