---
title: Class and Attribute Display Names
description: This topic contains information about and guidelines for class and attribute display names.
ms.assetid: c85905b2-ed8b-4032-8c54-fd4de8b34ecf
ms.tgt_platform: multiple
keywords:
- display specifiers AD ,class and attribute display names
- class display names AD
- attribute display names AD
ms.topic: article
ms.date: 05/31/2018
---

# Class and Attribute Display Names

The display specifier for an object class contains the following attributes that can be used to specify the localized display names used in the UI for objects of that class:

-   The **classDisplayName** attribute is a single-value Unicode string that specifies the class display name.
-   The **attributeDisplayNames** attribute is a multi-value property that specifies the names to use in the UI for attributes of the object class.

The **attributeDisplayNames** values are Unicode strings; each element consists of a comma-delimited name pair:


```C++
<attribute name>,<display text>
```



In this example, "&lt;attribute name&gt;" is the **lDAPDisplayName** of the attribute and "&lt;display text&gt;" is the text to display as the name of that attribute in the user interface.

## Guidelines for Class and Attribute Display Names

Because many vendors may extend classes with new attributes or creating entirely new classes, it is important that the class and attribute display names are unambiguous and do not result in conflicts.

Each vendor should prefix the class display name with a unique friendly identifier based on the vendor name. For example, if the fictitious company, Fabrikam Inc., creates a new class derived from the "contact" class, they can have a unique class display name "Fabrikam Contact."

If a vendor extends an existing class with new attributes, they should again uniquely identify the attribute display name so that no conflicts occur with other attribute display names. Again, prefixing the attribute display name with unique friendly identifier based on the vendor name is good practice. For example, if the Fabrikam company extends the user class with a new HR attribute, they could uniquely display the attribute as "Fabrikam HR Information."

In addition, from a localization perspective, each vendor should localize the class and attribute display names into each language supported by Windows 2000.

## Adding a Value to the attributeDisplayNames Attribute

**To add a name mapping value to the **attributeDisplayNames** attribute**

1.  Determine if the name mapping value for the attribute exists. If a name mapping value is to be replaced, first deleted the existing value, using the [**IADs::PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) method, with the *lnControlCode* parameter set to **ADS\_PROPERTY\_DELETE** and the *vProp* parameter set to the value to be removed. Do not use **ADS\_PROPERTY\_CLEAR** or **ADS\_PROPERTY\_UPDATE** for *lnControlCode*.
2.  Create the string that represents the attribute display name. For an example, see the format above.
3.  Use the [**IADs::PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) method with the *lnControlCode* parameter set to **ADS\_PROPERTY\_APPEND** to add the new value.
4.  Call [**IADs::SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) to commit the changes to the directory.

For more information about naming new classes and attributes, see [Naming Attributes and Classes](naming-attributes-and-classes.md).

 

 