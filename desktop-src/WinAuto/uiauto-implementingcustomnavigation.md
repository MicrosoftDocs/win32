---
title: CustomNavigation Control Pattern
description: Describes guidelines and conventions for implementing the ICustomNavigationProvider interface, including information about properties and methods.
ms.assetid: 428540BB-5CC0-4F49-8384-0FFC130FBB38
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**CachedLevel**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement4-get_cachedlevel?branch=master)                   | Property    | Located on [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master) interface. |
| [**CachedPositionInSet**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement4-get_cachedpositioninset?branch=master)   | Property    | Located on [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master) interface. |
| [**CachedSizeOfSet**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement4-get_cachedsizeofset?branch=master)           | Property    | Located on [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master) interface. |
| [**CurrentLevel**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement4-get_currentlevel?branch=master)                 | Property    | Located on [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master) interface. |
| [**CurrentPositionInSet**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement4-get_currentpositioninset?branch=master) | Property    | Located on [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master) interface. |
| [**CurrentSizeOfSet**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement4-get_currentsizeofset?branch=master)         | Property    | Located on [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master) interface. |
| [**Navigate**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-navigate?branch=master)                   | Method      | None                                                                                |



 

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

 

 




