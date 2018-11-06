---
title: User Interface Extension for New Object Classes
description: Active Directory Domain Services and its administrative MMC snap-in user interface can be customized to adapt to the requirements of administrators and users.
ms.assetid: 38e3b800-20ad-4da8-ad40-4e90838acfb5
ms.tgt_platform: multiple
keywords:
- User Interface Extension for New Object Classes AD
- Object AD , User Interface Extension for New Object Classes
ms.topic: article
ms.date: 05/31/2018
---

# User Interface Extension for New Object Classes

Active Directory Domain Services and its administrative MMC snap-in user interface can be customized to adapt to the requirements of administrators and users. Active Directory Domain Services enable the schema to be modified by creating new classes and attributes, or modifying existing classes. Display specifiers for the classes can be modified to reflect the new user interface elements that schema modifications require.

The following table lists attributes can be used to modify how the administrative snap-ins will display objects of a particular class.



| Attribute                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **defaultHidingValue**     | The **defaultHidingValue** attribute is an attribute of a **classSchema** object. This attribute contains a Boolean value that, if TRUE, causes instances of the object class to be hidden in the administrative snap-ins and the Windows shell. This also means that a menu item for the new object class does not appear in the **New** context menu of the administrative snap-ins, even if the appropriate creation wizard properties are set on the new object class's **displaySpecifier** object.If this attribute is FALSE, instances of the class will be visible in the administrative snap-ins and the shell. This also causes a menu item to create a new object instance to be added to the **New** menu of the administrative snap-ins.<br/> If no value is set for this attribute, the default value is TRUE. This means that, by default, instances of the object are hidden.<br/>                                                                |
| **showInAdvancedViewOnly** | The **showInAdvancedViewOnly** attribute contains a Boolean value that, if TRUE, causes instances of the object class to appear in the Users and Computers snap-in in Advanced View only and do not appear in the Windows shell. If this property is FALSE, instances of the class will be visible in Normal view in the Users and Computers snap-in and the Windows shell.<br/> If no value is set for this attribute, the default value is TRUE.<br/> This attribute can be set on an individual object to override the value set on the object class. For example, the **Container** class has this attribute set to TRUE but the **User** container has this value set to FALSE. Because of this, the **User** container appears in the shell and in Normal view in the Users and Computers snap-in but other containers that do not have **showInAdvancedViewOnly** set to FALSE appear only in Advanced view in the Users and Computers snap-in.<br/> |



 

## Creating Display Specifiers for New Classes

To customize the user interface for a new class, create a display specifier object for the new class for each supported locale, then set the desired attributes for the display specifier.

## Inheriting Display Specifiers for Derived Classes

A new class that inherits from an existing class does not inherit the parent class display specifier. If the new class is to use some or all of the parent class display specifier properties, create a new display specifier for the new class and copy the properties from the parent class display specifier to the new object display specifier. This must be done for all locales for which the parent class display specifier properties apply.

Certain parts of the UI feature set, such as the menu items and creation wizard for the user class, are implemented internally and are not available for use by a derived object. In these instances it is better to extend an existing class than to use a derived class.

## Modifying Existing Classes

New attributes can be added to an existing class. New UI components (property pages, menu items, and attribute display names) can be added or the existing UI replaced. It is also possible to design new property pages that expose fewer attributes of a class and to create context menus with fewer actions. For more information, see [Property Pages for Use with Display Specifiers](property-pages-for-use-with-display-specifiers.md), [Context Menus for Use with Display Specifiers](context-menus-for-use-with-display-specifiers.md), and [Class and Attribute Display Names](class-and-attribute-display-names.md).

 

 





