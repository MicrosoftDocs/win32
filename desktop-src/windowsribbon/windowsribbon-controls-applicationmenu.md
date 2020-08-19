---
title: Application Menu
description: The Application Menu is the main menu for an application that implements the Windows Ribbon framework.
ms.assetid: 5be93a5b-277b-44c1-be24-a0598a140bfc
ms.topic: article
ms.date: 05/31/2018
---

# Application Menu

The Application Menu is the main menu for an application that implements the Windows Ribbon framework.

-   [Introduction](#introduction)
-   [Components of the Application Menu](#components-of-the-application-menu)
    -   [Application Menu MenuGroup](#application-menu-menugroup)
-   [Sizing the Application Menu](#sizing-the-application-menu)
-   [Application Menu Properties](#application-menu-properties)
-   [Related topics](#related-topics)

## Introduction

The Application Menu is composed of a drop-down button control that displays a menu containing Commands that expose functionality related to a complete project, such as an entire document, picture, or movie. Examples include the **New**, **Open**, **Save**, and **Exit** Commands.

The following screen shot illustrates the Application Menu.

![screen shot of the application menu and recent items list of the paint for windows 7 ribbon.](images/controls/recentitems.png)

## Components of the Application Menu

The Application Menu is a mandatory element in any Ribbon application. The entry point into the Application Menu is a distinctive button that appears as the first item in the [Tab](windowsribbon-controls-tab.md) row, as shown in the following screen shot.

> [!Note]  
> Windows 8 and newer: Application Menu button image changed to label: **File**. We recommend that you do not use File as the label for any of your own tabs.

 

![screen shot of the application menu button of wordpad for windows 7.](images/overviews/applicationmenu-button.png)

When clicked, this button displays the rich menu that is shown in the following screen shot (the Application Menu from WordPad for Windows 7).

![screen shot of the application menu menu of wordpad for windows 7.](images/overviews/applicationmenu-menu.png)

> [!Note]  
> There is no impact on the tab set when the Application Menu button is clicked; instead, the focus enters the menu.

 

The Application Menu contains two panes: a list of Commands represented by one or more [**MenuGroup**](windowsribbon-element-menugroup.md) elements, and a [Recent Items](windowsribbon-controls-recentitems.md) list represented by an [**ApplicationMenu.RecentItems**](windowsribbon-element-applicationmenu-recentitems.md) element.

### Application Menu MenuGroup

The [**ApplicationMenu**](windowsribbon-element-applicationmenu.md) element must contain at least one [**MenuGroup**](windowsribbon-element-menugroup.md) child element that exposes a list of application-level commands. If multiple **MenuGroup** elements are declared, a divider line is drawn between the groups, as shown in the following screen shot.

![screen shot of an application menu menugroup.](images/overviews/applicationmenu-menugroup.png)

The following is a list of constraints for a [**MenuGroup**](windowsribbon-element-menugroup.md) element of an Application Menu:

-   All [**MenuGroup**](windowsribbon-element-menugroup.md) items must be declared with a *Class* attribute value of `MajorItems`.
-   An Application Menu [**MenuGroup**](windowsribbon-element-menugroup.md) supports only the [Button](windowsribbon-controls-button.md), [Toggle Button](windowsribbon-controls-togglebutton.md), [Drop-Down Button](windowsribbon-controls-dropdownbutton.md), [Split Button](windowsribbon-controls-splitbutton.md), [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md), and [Split Button Gallery](windowsribbon-controls-splitbuttongallery.md) controls.
    > \[!Important\]  
    > Command galleries are the only type of gallery that are supported in the Application Menu. See [Working with Galleries](./ribbon-controls-galleries.md), for more information on gallery controls.

     

When a [Button](windowsribbon-controls-button.md) or [Toggle Button](windowsribbon-controls-togglebutton.md) is used in a [**MenuGroup**](windowsribbon-element-menugroup.md), the value of [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) is displayed in the menu and the values of [**Command.TooltipTitle**](windowsribbon-element-command-tooltiptitle.md) and [**Command.TooltipDescription**](windowsribbon-element-command-tooltipdescription.md) are displayed as the tooltip, as shown in the following screen shot.

![screen shot of a button control in an application menu.](images/overviews/applicationmenu-menubutton.png)

When a [Drop-Down Button](windowsribbon-controls-dropdownbutton.md), [Split Button](windowsribbon-controls-splitbutton.md), [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md), or [Split Button Gallery](windowsribbon-controls-splitbuttongallery.md) is used in the Application Menu, the menu portion is displayed as a flyout that covers and conceals the **Recent items** pane.

For [Split Button](windowsribbon-controls-splitbutton.md) and [Drop-Down Button](windowsribbon-controls-dropdownbutton.md) controls, the value of [**Command.LabelDescription**](windowsribbon-element-command-labeldescription.md) is shown inline in the flyout menu to visually assist users with discovering the Command functionality. The displayed value of **Command.LabelDescription** is programmatically broken over a two-line span, and an attempt is made to fit the value exactly over the **Recent items** pane beneath. If the **Command.LabelDescription** value does not fit, the flyout will expand to accommodate the longest [**Command.Comment**](windowsribbon-element-command-comment.md) value in the [**MenuGroup**](windowsribbon-element-menugroup.md).

The following screen shot illustrates these behaviors in a [Split Button](windowsribbon-controls-splitbutton.md) flyout.

![screen shot of a list control flyout in an application menu.](images/overviews/applicationmenu-menuflyout.png)

With a [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md) and a [Split Button Gallery](windowsribbon-controls-splitbuttongallery.md), only a label and an image are shown.

## Sizing the Application Menu

Sizing of the Application Menu is handled by the Ribbon framework. If very long strings are supplied for the value of [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md) or [**Command.LabelDescription**](windowsribbon-element-command-labeldescription.md), or a long list of Commands is used, the menu will adjust its size to accommodate the contents. Some forms of adjustment include expanding the size of flyouts or menu panes, and adding pan viewers when scrolling is required.

## Application Menu Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Application Menu control.

Typically, an Application Menu property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled and the property updates are defined by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed and the application is not queried for an updated property value until the property is required by the framework. For example, the framework requires the property when a tab is activated and a control is revealed in the ribbon UI, or when a tooltip is displayed.



| Property key                                                                                     | Notes                                     |
|--------------------------------------------------------------------------------------------------|-------------------------------------------|
| [UI\_PKEY\_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md) | Can only be updated through invalidation. |
| [UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)             | Can only be updated through invalidation. |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**ApplicationMenu markup element**](windowsribbon-element-applicationmenu.md)
</dt> </dl>

 

 