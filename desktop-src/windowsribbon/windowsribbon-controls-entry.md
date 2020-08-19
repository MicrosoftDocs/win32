---
title: Windows Ribbon Framework Control Library
description: The topics contained in this section describe the set of controls that are included with the Windows Ribbon framework. The controls listed here are the UI objects in a ribbon that expose Command functionality.
ms.assetid: bda13e51-7e5f-4600-a6bd-9388bffd6ce2
ms.topic: article
ms.date: 05/31/2018
---

# Windows Ribbon Framework Control Library

The topics contained in this section describe the set of controls that are included with the Windows Ribbon framework. The controls listed here are the UI objects in a ribbon that expose Command functionality.

-   [Introduction](#introduction)
-   [The Controls](#windows-ribbon-framework-control-library)
    -   [Basic Controls](#basic-controls)
    -   [Container Controls](#container-controls)
    -   [Specialized Controls](#specialized-controls)
-   [Related topics](#related-topics)

## Introduction

The Ribbon framework is composed of components such as [Tabs](windowsribbon-controls-tab.md) and the [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md), that work together to deliver a rich UI experience. Individually, these components expose different types of Commands to give customers an organized, predictable experience across Ribbon applications. For example, each Tab exposes Commands related to creating and acting on specific parts of the content within the application workspace, whereas the [Application Menu](windowsribbon-controls-applicationmenu.md) exposes functionality related to a complete project, such as an entire document, picture, or movie.

This topic provides a comprehensive list of Ribbon controls and includes a brief description for each control, with links to more detailed documentation where available.

## The Controls

The Ribbon framework is composed of two [Views](windowsribbon-reference-elements-view.md): the [**Ribbon**](windowsribbon-element-ribbon.md) View and the [**ContextPopup**](windowsribbon-element-contextpopup.md) View. Each View can host several components that act as presentation containers for all controls that are rendered and managed by the framework.

The [**Ribbon**](windowsribbon-element-ribbon.md) View hosts the [**ApplicationMenu**](windowsribbon-element-applicationmenu.md) element, [**QuickAccessToolbar**](windowsribbon-element-quickaccesstoolbar.md) element, and ribbon command bar while the [**ContextPopup**](windowsribbon-element-contextpopup.md) View hosts a [**ContextMenu**](windowsribbon-element-contextmenu.md) element, a [**MiniToolbar**](windowsribbon-element-minitoolbar.md) element, or both.

Each framework control is distinguished by the functionality associated with its [**Command type**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_commandtype).

### Basic Controls

Basic controls consist of one or more buttons that can be invoked by a single mouse click to perform a simple action.

> [!Note]  
> The [**Spinner**](windowsribbon-element-spinner.md) is an exception as it contains an edit control.

 

The following table lists the basic controls in the Ribbon framework.



| Control                                                  | Markup Element                                             |
|----------------------------------------------------------|------------------------------------------------------------|
| [Button](windowsribbon-controls-button.md)              | [**Button**](windowsribbon-element-button.md)             |
| [Check Box](windowsribbon-controls-checkbox.md)         | [**CheckBox**](windowsribbon-element-checkbox.md)         |
| [Help Button](windowsribbon-controls-helpbutton.md)     | [**HelpButton**](windowsribbon-element-helpbutton.md)     |
| [Spinner](windowsribbon-controls-spinner.md)            | [**Spinner**](windowsribbon-element-spinner.md)           |
| [Toggle Button](windowsribbon-controls-togglebutton.md) | [**ToggleButton**](windowsribbon-element-togglebutton.md) |



 

### Container Controls

Container controls are composed of groups of controls, menus, lists, or item and Command collections.

The framework distinguishes between two types of containers, static and dynamic.

### Static Containers

Static containers are declared and populated, along with all associated resources, in the Ribbon markup file. These controls cannot be modified at run time.

The advantages of static controls include the following:

-   Rapid prototyping. Static controls make it possible to quickly build a Ribbon mock-up resembling a final Ribbon design that requires no complicated code.
-   Easy modifications. Most elements, attributes, resources, and layouts of static controls can be modified in markup.
-   Consistent UI. Well-designed applications provide a consistent and stable UI that avoids changes to menus and lists at run time.

The following table describes the static container controls in the Ribbon framework.



| Control                                                        | Markup Element                                                   |
|----------------------------------------------------------------|------------------------------------------------------------------|
| [Application Menu](windowsribbon-controls-applicationmenu.md) | [**ApplicationMenu**](windowsribbon-element-applicationmenu.md) |
| [Context Popup](windowsribbon-controls-contextpopup.md)       | [**ContextPopup**](windowsribbon-element-contextpopup.md)       |
| [Drop-Down Button](windowsribbon-controls-dropdownbutton.md)  | [**DropDownButton**](windowsribbon-element-dropdownbutton.md)   |
| [Group](windowsribbon-controls-group.md)                      | [**Group**](windowsribbon-element-group.md)                     |
| [Menu Group](windowsribbon-controls-menugroup.md)             | [**MenuGroup**](windowsribbon-element-menugroup.md)             |
| [Split Button](windowsribbon-controls-splitbutton.md)         | [**SplitButton**](windowsribbon-element-splitbutton.md)         |
| [Tab](windowsribbon-controls-tab.md)                          | [**Tab**](windowsribbon-element-tab.md)                         |
| [Tab Group](windowsribbon-controls-tabgroup.md)               | [**TabGroup**](windowsribbon-element-tabgroup.md)               |



 

### Dynamic Containers

Dynamic containers are declared in the Ribbon markup file. They feature a group of items or Commands that are created or modified at run time.

A subclass of dynamic containers, called galleries, are distinguished by their implementation of the [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) interface. This interface allows a control to expose its item or Command list as a collection, and to support updates based on both user interaction and run-time conditions. For more information, see [Working with Galleries](ribbon-controls-galleries.md).

The following table lists the dynamic container controls in the Ribbon framework.



| Control                                                               | Markup Element                                                         |
|-----------------------------------------------------------------------|------------------------------------------------------------------------|
| [Combo Box](windowsribbon-controls-combobox.md)                      | [**ComboBox**](windowsribbon-element-combobox.md)                     |
| [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md)       | [**DropDownGallery**](windowsribbon-element-dropdowngallery.md)       |
| [In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md)       | [**InRibbonGallery**](windowsribbon-element-inribbongallery.md)       |
| [Quick Access Toolbar](windowsribbon-controls-quickaccesstoolbar.md) | [**QuickAccessToolbar**](windowsribbon-element-quickaccesstoolbar.md) |
| [Recent Items](windowsribbon-controls-recentitems.md)                | [**RecentItems**](windowsribbon-element-recentitems.md)               |
| [Split Button Gallery](windowsribbon-controls-splitbuttongallery.md) | [**SplitButtonGallery**](windowsribbon-element-splitbuttongallery.md) |



 

### Specialized Controls

The Ribbon framework contains a number of specialized controls for specific UI functionality.

The following table lists the specialized controls in the Ribbon framework.



| Control                                                                  | Markup Element                                                           |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [Drop-Down Color Picker](windowsribbon-controls-dropdowncolorpicker.md) | [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) |
| [Font Control](windowsribbon-controls-fontcontrol.md)                   | [**FontControl**](windowsribbon-element-fontcontrol.md)                 |



 

## Related topics

<dl> <dt>

[Understanding Commands and Controls](windowsribbon-commandscontrols.md)
</dt> </dl>

 

 