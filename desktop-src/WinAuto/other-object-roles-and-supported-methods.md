---
title: Other Object Roles and Supported Methods (MSAA UI Element Reference)
description: This topic provides information about object roles that are not included in the previous topics for UI elements.
ms.assetid: '0c3a3ccf-f02a-4aca-9380-a13774598a19'
---

# Other Object Roles and Supported Methods (MSAA UI Element Reference)

This topic provides information about object roles that are not included in the previous topics for UI elements. Each object role includes a list of the [**IAccessible**](iaccessible.md) methods and properties that are supported for the object role. While other topics document supported **IAccessible** methods and properties for UI elements, this topic lists the methods and properties you can expect to be supported for a particular object role. Many of the UI elements which might have one of the roles listed here are typically seen in browsers.

> [!Note]  
> Use this topic as a guideline. We strongly suggest that you use Microsoft Active Accessibility tools to verify expected behavior for an individual object role.

 

The following table lists additional object roles which Oleacc.dll supports.



|                                                                         |                                                           |
|-------------------------------------------------------------------------|-----------------------------------------------------------|
| [**ROLE\_SYSTEM\_ALERT**](#role-system-alert)                           | [**ROLE\_SYSTEM\_DROPLIST**](#role-system-droplist)       |
| [**ROLE\_SYSTEM\_APPLICATION**](#role-system-application)               | [**ROLE\_SYSTEM\_EQUATION**](#role-system-equation)       |
| [**ROLE\_SYSTEM\_BORDER**](#role-system-border)                         | [**ROLE\_SYSTEM\_GRAPHIC**](#role-system-graphic)         |
| [**ROLE\_SYSTEM\_BUTTONDROPDOWN**](#role-system-buttondropdown)         | [**ROLE\_SYSTEM\_HELPBALLOON**](#role-system-helpballoon) |
| [**ROLE\_SYSTEM\_BUTTONDROPDOWNGRID**](#role-system-buttondropdowngrid) | [**ROLE\_SYSTEM\_IPADDRESS**](#role-system-ipaddress)     |
| [**ROLE\_SYSTEM\_BUTTONMENU**](#role-system-buttonmenu)                 | [**ROLE\_SYSTEM\_LINK**](#role-system-link)               |
| [**ROLE\_SYSTEM\_CELL**](#role-system-cell)                             | [**ROLE\_SYSTEM\_PANE**](#role-system-pane)               |
| [**ROLE\_SYSTEM\_CHARACTER**](#role-system-character)                   | [**ROLE\_SYSTEM\_ROW**](#role-system-row)                 |
| [**ROLE\_SYSTEM\_CHART**](#role-system-chart)                           | [**ROLE\_SYSTEM\_ROWHEADER**](#role-system-rowheader)     |
| [**ROLE\_SYSTEM\_CLOCK**](#role-system-clock)                           | [**ROLE\_SYSTEM\_SEPARATOR**](#role-system-separator)     |
| [**ROLE\_SYSTEM\_COLUMN**](#role-system-column)                         | [**ROLE\_SYSTEM\_SOUND**](#role-system-sound)             |
| [**ROLE\_SYSTEM\_DIAGRAM**](#role-system-diagram)                       | [**ROLE\_SYSTEM\_SPLITBUTTON**](#role-system-splitbutton) |
| [**ROLE\_SYSTEM\_DIAL**](#role-system-dial)                             | [**ROLE\_SYSTEM\_TABLE**](#role-system-table)             |
| [**ROLE\_SYSTEM\_DOCUMENT**](#role-system-document)                     | [**ROLE\_SYSTEM\_WHITESPACE**](#role-system-whitespace)   |



 

## ROLE\_SYSTEM\_ALERT

For more information on this role, see [**ROLE\_SYSTEM\_ALERT**](object-roles.md#role-system-alert).

**Supported Properties and Methods**

-   get\_accName
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_APPLICATION

For more information on this role, see [**ROLE\_SYSTEM\_APPLICATION**](object-roles.md#role-system-application).

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

For more information on this role, see [**ROLE\_SYSTEM\_BORDER**](object-roles.md#role-system-border).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_BUTTONDROPDOWN

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONDROPDOWN**](object-roles.md#role-system-buttondropdown).

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

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONDROPDOWNGRID**](object-roles.md#role-system-buttondropdowngrid).

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

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONMENU**](object-roles.md#role-system-buttonmenu).

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

For more information on this role, see [**ROLE\_SYSTEM\_CELL**](object-roles.md#role-system-cell).

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

For more information on this role, see [**ROLE\_SYSTEM\_CHARACTER**](object-roles.md#role-system-character).

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

For more information on this role, see [**ROLE\_SYSTEM\_CHART**](object-roles.md#role-system-chart).

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

For more information on this role, see [**ROLE\_SYSTEM\_CLOCK**](object-roles.md#role-system-clock).

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

For more information on this role, see [**ROLE\_SYSTEM\_COLUMN**](object-roles.md#role-system-column).

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

For more information on this role, see [**ROLE\_SYSTEM\_DIAGRAM**](object-roles.md#role-system-diagram).

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

For more information on this role, see [**ROLE\_SYSTEM\_DIAL**](object-roles.md#role-system-dial).

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

For more information on this role, see [**ROLE\_SYSTEM\_DOCUMENT**](object-roles.md#role-system-document).

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

For more information on this role, see [**ROLE\_SYSTEM\_DROPLIST**](object-roles.md#role-system-droplist).

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

For more information on this role, see [**ROLE\_SYSTEM\_EQUATION**](object-roles.md#role-system-equation).

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

For more information on this role, see [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md#role-system-graphic).

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

For more information on this role, see [**ROLE\_SYSTEM\_HELPBALLOON**](object-roles.md#role-system-helpballoon).

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

For more information on this role, see [**ROLE\_SYSTEM\_IPADDRESS**](object-roles.md#role-system-ipaddress).

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

For more information on this role, see [**ROLE\_SYSTEM\_LINK**](object-roles.md#role-system-link).

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

For more information on this role, see [**ROLE\_SYSTEM\_PANE**](object-roles.md#role-system-pane).

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

For more information on this role, see [**ROLE\_SYSTEM\_ROW**](object-roles.md#role-system-row).

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

For more information on this role, see [**ROLE\_SYSTEM\_ROWHEADER**](object-roles.md#role-system-rowheader).

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

For more information on this role, see [**ROLE\_SYSTEM\_SEPARATOR**](object-roles.md#role-system-separator).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   get\_accChild
-   get\_accChildCount
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_SOUND

For more information on this role, see [**ROLE\_SYSTEM\_SOUND**](object-roles.md#role-system-sound).

**Supported Properties and Methods**

-   get\_accDescription
-   get\_accName
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_SPLITBUTTON

For more information on this role, see [**ROLE\_SYSTEM\_SPLITBUTTON**](object-roles.md#role-system-splitbutton).

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

For more information on this role, see [**ROLE\_SYSTEM\_TABLE**](object-roles.md#role-system-table).

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

For more information on this role, see [**ROLE\_SYSTEM\_WHITESPACE**](object-roles.md#role-system-whitespace).

**Supported Properties and Methods**

-   accLocation
-   accSelect
-   get\_accParent
-   get\_accRole
-   get\_accState

 

 




