---
title: Accessing and Manipulating Data with ADSI
description: All objects have properties.
ms.assetid: 366a1fbc-3089-406a-9819-cf2ba7636c5f
ms.tgt_platform: multiple
keywords:
- ADSI ADSI , accessing and manipulating data
ms.topic: article
ms.date: 05/31/2018
---

# Accessing and Manipulating Data with ADSI

All objects have properties. All Active Directory Service Interface (ADSI) COM objects have one or more interfaces with methods that retrieve the properties of the directory object that the COM object represents. There are a number of ways you can read properties from an object:

-   Get a specific property by name: The [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface has two methods [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get) and [**IADs::GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) to read a specific property. Every ADSI COM object has an **IADs** interface.
-   Get a specified list of properties: The [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interface has the method [**IDirectoryObject::GetObjectAttributes**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-getobjectattributes) that allows you to specify a list containing the names of the properties to read and returns an array of structures containing the requested property values.
-   Enumerate all properties on the object: The [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist) interface allows you to enumerate all the properties on an object.
-   Get special properties: The Automation interfaces ([**IADs**](/windows/desktop/api/Iads/nn-iads-iads)\*) have property methods that allow you to get special properties that are not stored in an object. Or the property methods may allow you to get an object property in a data format that differs from the actual data type stored. For example, the **IADs** interface has property methods such as [**IADs::get\_Name**](iads-property-methods.md), which retrieves an object's relative distinguished name (RDN); **IADs::get\_Class**, which retrieves an object's class, and **IADs::get\_Parent**, which retrieves the ADsPath to the object's parent.

ADSI allows you to cache properties locally after they have been read from the directory server. This allows you a choice of reading the properties from the local property cache or retrieving the properties directly from the directory server. ADSI also has methods to update the cache as well as specifying whether all properties for an object are cached or just those you have specified.

After you have retrieved a property, you read its value. The data type of a property depends on the definition of the property (also known as an attribute) in the Active Directory schema. For each type of property that can exist in Active Directory, there is an **attributeSchema** object in the Active Directory schema. An **attributeSchema** object defines the characteristics of the attribute. One of these characteristics is the attribute's syntax, which determines the data type of the attribute's values. For more information, see [Characteristics of Attributes](/windows/desktop/AD/characteristics-of-attributes) and [Syntaxes for Active Directory Attributes](/windows/desktop/AD/syntaxes-for-attributes-in-active-directory-domain-services).

The Automation interfaces ([**IADs**](/windows/desktop/api/Iads/nn-iads-iads)\*) return a property value as a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) or a pointer to an Automation interface on a COM object that represents the property. The [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) and [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interfaces return a property as a pointer to a structure containing a typed property value or a pointer to a string of bytes. In addition, **IDirectoryObject** and **IDirectorySearch** retrieve properties directly from the directory server instead of using a local property cache.

This section describes the following topics:

-   [The IADs and IDirectoryObject Interfaces](the-iads-and-idirectoryobject-interfaces.md)
-   [Accessing Attributes with ADSI](accessing-attributes-with-adsi.md)
-   [Modifying Attributes with ADSI](modifying-attributes-with-adsi.md)
-   [Accessing the Property Cache Directly with the IADsProperty Interfaces](accessing-the-property-cache-directly-with-the-iadsproperty-interfaces.md)
-   [ADSI Attribute Syntax](adsi-attribute-syntax.md)

 

 