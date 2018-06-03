---
title: Other Object Roles and Supported Methods (MSAA UI Element Reference)
description: This topic provides information about object roles that are not included in the previous topics for UI elements.
ms.assetid: 0c3a3ccf-f02a-4aca-9380-a13774598a19
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Other Object Roles and Supported Methods (MSAA UI Element Reference)

This topic provides information about object roles that are not included in the previous topics for UI elements. Each object role includes a list of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods and properties that are supported for the object role. While other topics document supported **IAccessible** methods and properties for UI elements, this topic lists the methods and properties you can expect to be supported for a particular object role. Many of the UI elements which might have one of the roles listed here are typically seen in browsers.

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

For more information on this role, see [**ROLE\_SYSTEM\_ALERT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_ALERT**).

**Supported Properties and Methods**

-   get\_accName
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_APPLICATION

For more information on this role, see [**ROLE\_SYSTEM\_APPLICATION**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_APPLICATION**).

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

For more information on this role, see [**ROLE\_SYSTEM\_BORDER**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_BORDER**).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   accNavigate
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_BUTTONDROPDOWN

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONDROPDOWN**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_BUTTONDROPDOWN**).

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

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONDROPDOWNGRID**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_BUTTONDROPDOWNGRID**).

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

For more information on this role, see [**ROLE\_SYSTEM\_BUTTONMENU**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_BUTTONMENU**).

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

For more information on this role, see [**ROLE\_SYSTEM\_CELL**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CELL**).

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

For more information on this role, see [**ROLE\_SYSTEM\_CHARACTER**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CHARACTER**).

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

For more information on this role, see [**ROLE\_SYSTEM\_CHART**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CHART**).

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

For more information on this role, see [**ROLE\_SYSTEM\_CLOCK**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CLOCK**).

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

For more information on this role, see [**ROLE\_SYSTEM\_COLUMN**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_COLUMN**).

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

For more information on this role, see [**ROLE\_SYSTEM\_DIAGRAM**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_DIAGRAM**).

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

For more information on this role, see [**ROLE\_SYSTEM\_DIAL**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_DIAL**).

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

For more information on this role, see [**ROLE\_SYSTEM\_DOCUMENT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_DOCUMENT**).

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

For more information on this role, see [**ROLE\_SYSTEM\_DROPLIST**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_DROPLIST**).

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

For more information on this role, see [**ROLE\_SYSTEM\_EQUATION**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_EQUATION**).

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

For more information on this role, see [**ROLE\_SYSTEM\_GRAPHIC**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_GRAPHIC**).

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

For more information on this role, see [**ROLE\_SYSTEM\_HELPBALLOON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_HELPBALLOON**).

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

For more information on this role, see [**ROLE\_SYSTEM\_IPADDRESS**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_IPADDRESS**).

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

For more information on this role, see [**ROLE\_SYSTEM\_LINK**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LINK**).

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

For more information on this role, see [**ROLE\_SYSTEM\_PANE**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PANE**).

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

For more information on this role, see [**ROLE\_SYSTEM\_ROW**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_ROW**).

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

For more information on this role, see [**ROLE\_SYSTEM\_ROWHEADER**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_ROWHEADER**).

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

For more information on this role, see [**ROLE\_SYSTEM\_SEPARATOR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SEPARATOR**).

**Supported Properties and Methods**

-   accHitTest
-   accLocation
-   get\_accChild
-   get\_accChildCount
-   get\_accParent
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_SOUND

For more information on this role, see [**ROLE\_SYSTEM\_SOUND**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SOUND**).

**Supported Properties and Methods**

-   get\_accDescription
-   get\_accName
-   get\_accRole
-   get\_accState

## ROLE\_SYSTEM\_SPLITBUTTON

For more information on this role, see [**ROLE\_SYSTEM\_SPLITBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SPLITBUTTON**).

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

For more information on this role, see [**ROLE\_SYSTEM\_TABLE**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_TABLE**).

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

For more information on this role, see [**ROLE\_SYSTEM\_WHITESPACE**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_WHITESPACE**).

**Supported Properties and Methods**

-   accLocation
-   accSelect
-   get\_accParent
-   get\_accRole
-   get\_accState

 

 




