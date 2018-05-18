---
title: CustomNavigation Control Pattern
description: Describes guidelines and conventions for implementing the ICustomNavigationProvider interface, including information about properties and methods.
ms.assetid: '428540BB-5CC0-4F49-8384-0FFC130FBB38'
---

# CustomNavigation Control Pattern

Describes guidelines and conventions for implementing the **ICustomNavigationProvider** interface, including information about properties and methods. The **CustomNavigation** control pattern is used to enable custom navigation between controls in hierarchy-like structures such as list items, bulleted lists, numbered lists and headings. This enables providers to describe structures or define the navigable relationships using the element alone and not just the containing control.

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ICustomNavigationProvider**](#required-members-for-icustomnavigationprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **CustomNavigation** provider, note the following guidelines and conventions:

-   Property values for **PositionInSet**, **SizeOfSet**, and **Level** are one-based integer values.
-   **ICustomNavigationProvider** does not provide for active manipulation of the control such as moving positions, adding and removing items, or promoting and demoting levels.
-   Controls that implement **ICustomNavigationProvider** typically have a hierarchical structure, but can skip levels by using the **Navigate** method. The properties **PositionInSet**, **SizeOfSet**, and **Level** are required on the pattern.

## Required Members for **ICustomNavigationProvider**

The following properties are required for implementing the **ICustomNavigationProvider** interface.



| Required members                                                                  | Member type | Notes                                                                               |
|-----------------------------------------------------------------------------------|-------------|-------------------------------------------------------------------------------------|
| [**CachedLevel**](uiauto-iuiautomationelement4-cachedlevel.md)                   | Property    | Located on [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md) interface. |
| [**CachedPositionInSet**](uiauto-iuiautomationelement4-cachedpositioninset.md)   | Property    | Located on [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md) interface. |
| [**CachedSizeOfSet**](uiauto-iuiautomationelement4-cachedsizeofset.md)           | Property    | Located on [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md) interface. |
| [**CurrentLevel**](uiauto-iuiautomationelement4-currentlevel.md)                 | Property    | Located on [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md) interface. |
| [**CurrentPositionInSet**](uiauto-iuiautomationelement4-currentpositioninset.md) | Property    | Located on [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md) interface. |
| [**CurrentSizeOfSet**](uiauto-iuiautomationelement4-currentsizeofset.md)         | Property    | Located on [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md) interface. |
| [**Navigate**](uiauto-irawelementproviderfragment-navigate.md)                   | Method      | None                                                                                |



 

This control pattern has no associated methods or events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[ListItem Control](uiauto-supportlistitemcontroltype.md)
</dt> <dt>

[HeaderItem Control](uiauto-supportheaderitemcontroltype.md)
</dt> <dt>

[DataItem Control](uiauto-supportdataitemcontroltype.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> </dl>

 

 




