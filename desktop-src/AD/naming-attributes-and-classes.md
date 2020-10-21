---
title: Naming Attributes and Classes
description: This topic includes guidelines for naming attributes and classes.
ms.assetid: ccbc2859-332f-4ded-9125-5bf507cad960
ms.tgt_platform: multiple
keywords:
- Naming Attributes and Classes
ms.topic: article
ms.date: 05/31/2018
---

# Naming Attributes and Classes

This topic includes guidelines for naming attributes and classes.

To create a new class or attribute, adhere to the following naming rules:

-   Use the same name for both the **cn** and **lDAPDisplayName** properties of a new **attributeSchema** or **classSchema** object.
-   Identify the company with a lower-case prefix in the first section of the name. This prefix can be a DNS name, acronym, or other string that uniquely identifies the company. The prefix ensures that all attributes and classes for a specific company are displayed consecutively when browsing the schema.
-   If you are developing a schema extension as an independent software vendor, add an abbreviation of the product name of the prefix. This adds distinction between multiple products that contain LDAP schema extensions.
-   Use a hyphen as the next character after the prefix.
-   Specify an attribute or class name that is unique within the company's attributes after the hyphen. This part of the common-name should be descriptive. Do not use illogical names that are meaningless to developers and viewers of the schema.

For example, if the fictitious Fabrikam company extended the schema by adding an attribute for storing a voice-mail identifier, the **cn** and **lDAPDisplayName** of the new attribute could be "fabrikam-VoiceMailID".

If the **lDAPDisplayName** of an attribute or class is not specified, the system uses the **cn** to generate one. However, the system algorithm for generating the name may result in name collisions or names that are difficult to read. To avoid these problems, it is recommended that an **lDAPDisplayName** be explicitly specified for all attributes and classes.

For development and testing purposes, it may be desirable to append a version suffix to the **cn** and **lDAPDisplayName**, for example, "fabrikam-VoiceMailID-001". In a distributed development/test environment, a version suffix enables developers to run multiple versions of their software simultaneously. After testing is complete, rename the attribute or class to remove the suffix.

It is not possible to delete defunct versions of a schema extensions, but it is possible to disable them and rename them with obscure names. For more information, see [Disabling Existing Classes and Attributes](disabling-existing-classes-and-attributes.md).

 

 




