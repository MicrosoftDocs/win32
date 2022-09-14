---
title: Choosing the Content for Descriptive Properties
description: While the content of some properties is specific, the content for other properties consists of descriptive text that is left to the server developer to provide.
ms.assetid: 3f399451-e9c5-4901-9b6e-198aa0c2deab
ms.topic: article
ms.date: 05/31/2018
---

# Choosing the Content for Descriptive Properties

While the content of some properties is specific, the content for other properties consists of descriptive text that is left to the server developer to provide. Additionally, the type of information for each property varies depending on the object. The following table provides suggestions for choosing the content of these descriptive properties.



| Property                                        | Content suggestion                                                                                                                                                                                                                                                    |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Name**](name-property.md)                   | A label that briefly describes and identifies the object within its container, such as the text in a push button, the name of a menu item, or a label displayed next to an edit control.                                                                              |
| [**DefaultAction**](defaultaction-property.md) | The default interaction with the object. The string returned by this property is either a single verb, such as "Press" for a toolbar button, or a short phrase that begins with a verb.                                                                               |
| [**Value**](value-property.md)                 | Information contained in the object, such as the text in an edit control or the file name of an HTML link. The contents of the [**Value**](value-property.md) property can change, whereas the contents of the [**Name**](name-property.md) property do not change. |
| [**Description**](description-property.md)     | Describes the object's appearance.                                                                                                                                                                                                                                    |
| [**Help**](help-property.md)                   | Tooltip or balloon-style information used either to describe what the object does or how to use it.                                                                                                                                                                   |
| [**HelpTopic**](helptopic-property.md)         | A context identifier of a [WinHelp](/windows/win32/api/winuser/nf-winuser-winhelpa) topic that documents the object.                                                                                                                                                 |



 

Use one of the predefined [object role](object-roles.md) values for the [**Role**](role-property.md) and the appropriate combination of [object state constants](object-state-constants.md) for the [**State**](state-property.md).

The content of the properties for custom controls must match the content of the properties for the system-provided controls that the custom controls emulate. For information about the properties supported by system-provided controls, see [Appendix A: Supported User Interface Elements Reference](appendix-a--supported-user-interface-elements-reference.md).

 

 