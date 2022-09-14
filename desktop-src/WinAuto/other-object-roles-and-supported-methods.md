---
title: Other Object Roles and Supported Methods (MSAA UI Element Reference)
description: This topic provides information about object roles that are not included in the previous topics for UI elements.
ms.assetid: 0c3a3ccf-f02a-4aca-9380-a13774598a19
ms.topic: article
ms.date: 05/31/2018
---

# Other Object Roles and Supported Methods (MSAA UI Element Reference)

This topic provides information about object roles that are not included in the previous topics for UI elements. Each object role includes a list of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods and properties that are supported for the object role. While other topics document supported **IAccessible** methods and properties for UI elements, this topic lists the methods and properties you can expect to be supported for a particular object role. Many of the UI elements which might have one of the roles listed here are typically seen in browsers.

> [!Note]  
> Use this topic as a guideline. We strongly suggest that you use Microsoft Active Accessibility tools to verify expected behavior for an individual object role.

 

The following table lists additional object roles which Oleacc.dll supports.



| &nbsp; |  &nbsp; |
|-------------------------------------------------------------------------|-----------------------------------------------------------|
| [**ROLE\_SYSTEM\_ALERT**](/windows)                           | [**ROLE\_SYSTEM\_DROPLIST**](/windows)       |
| [**ROLE\_SYSTEM\_APPLICATION**](/windows)               | [**ROLE\_SYSTEM\_EQUATION**](/windows)       |
| [**ROLE\_SYSTEM\_BORDER**](/windows)                         | [**ROLE\_SYSTEM\_GRAPHIC**](/windows)         |
| [**ROLE\_SYSTEM\_BUTTONDROPDOWN**](/windows)         | [**ROLE\_SYSTEM\_HELPBALLOON**](/windows) |
| [**ROLE\_SYSTEM\_BUTTONDROPDOWNGRID**](/windows) | [**ROLE\_SYSTEM\_IPADDRESS**](/windows)     |
| [**ROLE\_SYSTEM\_BUTTONMENU**](/windows)                 | [**ROLE\_SYSTEM\_LINK**](/windows)               |
| [**ROLE\_SYSTEM\_CELL**](/windows)                             | [**ROLE\_SYSTEM\_PANE**](/windows)               |
| [**ROLE\_SYSTEM\_CHARACTER**](/windows)                   | [**ROLE\_SYSTEM\_ROW**](/windows)                 |
| [**ROLE\_SYSTEM\_CHART**](/windows)                           | [**ROLE\_SYSTEM\_ROWHEADER**](/windows)     |
| [**ROLE\_SYSTEM\_CLOCK**](/windows)                           | [**ROLE\_SYSTEM\_SEPARATOR**](/windows)     |
| [**ROLE\_SYSTEM\_COLUMN**](/windows)                         | [**ROLE\_SYSTEM\_SOUND**](/windows)             |
| [**ROLE\_SYSTEM\_DIAGRAM**](/windows)                       | [**ROLE\_SYSTEM\_SPLITBUTTON**](/windows) |
| [**ROLE\_SYSTEM\_DIAL**](/windows)                             | [**ROLE\_SYSTEM\_TABLE**](/windows)             |
| [**ROLE\_SYSTEM\_DOCUMENT**](/windows)                     | [**ROLE\_SYSTEM\_WHITESPACE**](/windows)   |



 

## ROLE\_SYSTEM\_ALERT

For more information on this role, see [**ROLE\_SYSTEM\_ALERT**](object-roles.md).

**Supported Properties and Methods**

-   get\_accName
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_APPLICATION

For more information on this role, see [**ROLE\_SYSTEM\_APPLICATION**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_BORDER

For more information on this role, see [**ROLE\_SYSTEM\_BORDER**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_BUTTONDROPDOWN

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONDROPDOWN**](object-roles.md).

**Supported Properties and Methods**

-   accDoDefaultAction
-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accDefaultAction
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_BUTTONDROPDOWNGRID

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONDROPDOWNGRID**](object-roles.md).

**Supported Properties and Methods**

-   accDoDefaultAction
-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accDefaultAction
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_BUTTONMENU

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONMENU**](object-roles.md).

**Supported Properties and Methods**

-   accDoDefaultAction
-   accHitTest
-   accLocation
-   accNavigate
-   get\_accDefaultAction
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_CELL

For more information on this role, see [**ROLE\_SYSTEM\_CELL**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   accSelect
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_CHARACTER

For more information on this role, see [**ROLE\_SYSTEM\_CHARACTER**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accDescription
-   get\_accFocus
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_CHART

For more information on this role, see [**ROLE\_SYSTEM\_CHART**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_CLOCK

For more information on this role, see [**ROLE\_SYSTEM\_CLOCK**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_COLUMN

For more information on this role, see [**ROLE\_SYSTEM\_COLUMN**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   accSelect
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_DIAGRAM

For more information on this role, see [**ROLE\_SYSTEM\_DIAGRAM**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_DIAL

For more information on this role, see [**ROLE\_SYSTEM\_DIAL**](object-roles.md).

**Supported Properties and Methods**

-   accDoDefaultAction
-   accHitTest
-   accLocation
-   accNavigate
-   get\_accDefaultAction
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_DOCUMENT

For more information on this role, see [**ROLE\_SYSTEM\_DOCUMENT**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   accSelect
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_DROPLIST

For more information on this role, see [**ROLE\_SYSTEM\_DROPLIST**](object-roles.md).

**Supported Properties and Methods**

-   accDoDefaultAction
-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accDefaultAction
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_EQUATION

For more information on this role, see [**ROLE\_SYSTEM\_EQUATION**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accFocus
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_GRAPHIC

For more information on this role, see [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_HELPBALLOON

For more information on this role, see [**ROLE\_SYSTEM\_HELPBALLOON**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accDefaultAction
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_IPADDRESS

For more information on this role, see [**ROLE\_SYSTEM\_IPADDRESS**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_LINK

For more information on this role, see [**ROLE\_SYSTEM\_LINK**](object-roles.md).

**Supported Properties and Methods**

-   accDoDefaultAction
-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accDefaultAction
-   get\_accDescription
-   get\_accFocus
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_PANE

For more information on this role, see [**ROLE\_SYSTEM\_PANE**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accChild
-   get\_accChildCount
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_ROW

For more information on this role, see [**ROLE\_SYSTEM\_ROW**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   accSelect
-   get\_accChild
-   get\_accChildCount
-   get\_accDescription
-   get\_accFocus
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_ROWHEADER

For more information on this role, see [**ROLE\_SYSTEM\_ROWHEADER**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   accSelect
-   get\_accChild
-   get\_accChildCount
-   get\_accDefaultAction
-   get\_accDescription
-   get\_accFocus
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState
-   get\_accValue

## ROLE\_SYSTEM\_SEPARATOR

For more information on this role, see [**ROLE\_SYSTEM\_SEPARATOR**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   get\_accChild
-   get\_accChildCount
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_SOUND

For more information on this role, see [**ROLE\_SYSTEM\_SOUND**](object-roles.md).

**Supported Properties and Methods**

-   get\_accDescription
-   get\_accName
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_SPLITBUTTON

For more information on this role, see [**ROLE\_SYSTEM\_SPLITBUTTON**](object-roles.md).

**Supported Properties and Methods**

-   accDoDefaultAction
-   accHitTest
-   accLocation
-   accNavigate
-   get\_accDefaultAction
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_TABLE

For more information on this role, see [**ROLE\_SYSTEM\_TABLE**](object-roles.md).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   accSelect
-   get\_accChild
-   get\_accChildCount
-   get\_accDescription
-   get\_accFocus
-   get\_accHelp
-   get\_accHelpTopic
-   get\_accKeyboardShortcut
-   get\_accName
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_WHITESPACE

For more information on this role, see [**ROLE\_SYSTEM\_WHITESPACE**](object-roles.md).

**Supported Properties and Methods**

-   accLocation
-   accSelect
-   get\_accParent
-   get\_accRole
-   get\_accState

 

 