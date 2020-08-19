---
title: Declaring Commands and Controls with Ribbon Markup
description: The Windows Ribbon framework uses a markup language based on Extensible Application Markup Language (XAML) to declaratively implement the appearance of a Ribbon application.
ms.assetid: 76bacfb3-ecaf-47b3-be97-afa5e7e52330
keywords:
- Windows Ribbon,markup structure
- Ribbon,markup structure
- Windows Ribbon,separating presentation from command logic
- Ribbon,separating presentation from command logic
- Windows Ribbon,components
- Ribbon,components
- command system for Windows Ribbon
- controls for Windows Ribbon
ms.topic: article
ms.date: 05/31/2018
---

# Declaring Commands and Controls with Ribbon Markup

The Windows Ribbon framework uses a markup language based on Extensible Application Markup Language (XAML) to declaratively implement the appearance of a Ribbon application.

-   [Separating Presentation from Command Logic](#separating-presentation-from-command-logic)
-   [Markup Structure](#markup-structure)
-   [Ribbon Components](#ribbon-components)
-   [Related topics](#related-topics)

## Separating Presentation from Command Logic

The separation of presentation and visual attributes from command logic in the Ribbon framework is accomplished through two distinct, but dependent, development platforms. Control layouts, scaling behaviors, Command declarations, and resource specifications are the design time domain of a declarative markup syntax based on the [Extensible Application Markup Language (XAML)](/dotnet/framework/wpf/advanced/xaml-in-wpf) specification. Low level functionality, application hooks, and Command handlers are defined in Component Object Model (COM)-based interface implementations.

This separation of presentation and logic provides the following benefits:

-   A more efficient application development cycle which allows UI developers and designers to implement the GUI of the Ribbon application independently from the core application functionality. This core functionality can be left to dedicated software developers.
-   Less costly maintenance because changes to the GUI are possible without changes to core functionality (and vice versa).
-   Simple specification of string and image resources through markup.
-   Ease of prototyping.

## Markup Structure

Two distinct branches exist within the structure of Ribbon framework markup.

The first branch contains a manifest of Command and resource declarations (strings and images). Each Command entry is used by the framework to bind a Ribbon control, through a Command ID, to a Command handler defined in the application code.

The second branch contains the actual control declarations. Each control is associated with a Command through a *CommandName* attribute that maps to a *Name* attribute specified in each Command declaration.

## Ribbon Components

Ribbon framework UI functionality is exposed through [Views](windowsribbon-reference-elements-view.md). A View is essentially a container, such as the [**Ribbon**](windowsribbon-element-ribbon.md) and [**ContextPopup**](windowsribbon-element-contextpopup.md), that is used to present framework controls and the Commands they are bound to.

The [**Ribbon**](windowsribbon-element-ribbon.md) View is composed of several components that include an [Application Menu](windowsribbon-controls-applicationmenu.md), the [Quick Access Toolbar (QAT)](windowsribbon-controls-quickaccesstoolbar.md) for displaying commonly used Commands from the ribbon UI, core and contextual [tabs](windowsribbon-controls-tab.md) that contain [groups](windowsribbon-controls-group.md) of controls, and the rich context menu system of the [**ContextPopup**](windowsribbon-element-contextpopup.md).

All Ribbon components are declared in a standalone markup file that:

-   Specifies the basic properties for each element.
-   Shows hierarchical relationships clearly.
-   Supplies layout preferences and scaling hints. For more information on Ribbon framework layout templates, see [Customizing a Ribbon Through Size Definitions and Scaling Policies](windowsribbon-templates.md).
-   Provides a way to define resources such as images and labels. For more information on image resources, see [Specifying Ribbon Image Resources](windowsribbon-imageformats.md).

The following two Ribbon markup examples demonstrate how a set of Ribbon Application Menu items are each associated with a Command name and ID.

1.  This section shows the Command declarations required for an Application Menu with basic commands such as New, Open, and Save.
    ```XML
    <!-- Command declarations for the Application Menu. -->
    <Command Name="cmdFileMenu"
             Symbol="ID_FILE_MENU"
             Id="25000" />
    <!-- Command declaration for most recently used items. -->
    <Command Name="cmdMRUItems"
             Symbol="ID_FILE_MRUITEMS"
             Id="25050"/>
    <!-- Command declarations for Application Menu items. -->
    <Command Name="cmdNew"
             Symbol="ID_FILE_NEW"
             Comment="New"
             Id="25001"
             LabelTitle="&amp;New"/>
    <Command Name="cmdOpen"
             Symbol="ID_FILE_OPEN"
             Comment="Open"
             Id="25002"
             LabelTitle="&amp;&amp;Open"/>
    <Command>
      <Command.Name>cmdSave</Command.Name>
      <Command.Symbol>ID_FILE_SAVE</Command.Symbol>
      <Command.Comment>Save</Command.Comment>
      <Command.Id>25003</Command.Id>
      <Command.LabelTitle>
        <String>
          <String.Content>Label for Save</String.Content>
          <String.Id>59999</String.Id>
          <String.Symbol>strSave</String.Symbol>
        </String>
      </Command.LabelTitle>
      <Command.TooltipTitle>Tooltip title with &amp;&amp; for Save Command</Command.TooltipTitle>
      <Command.TooltipDescription>Tooltip description for Save Command.</Command.TooltipDescription>
      <Command.Keytip>s1</Command.Keytip>
    </Command>
    <Command Name="cmdPrint"
             Symbol="ID_FILE_PRINT"
             Comment="Save"
             Id="25004"
             LabelTitle="Print" />
    <Command Name="cmdExit"
             Symbol="ID_FILE_EXIT"
             Comment="Exit"
             Id="25005"
             LabelTitle="Exit" />
    ```

    

2.  This section shows the associated Control declarations.
    ```XML
    <!-- Control declarations for Application Menu items. -->
    <Ribbon.ApplicationMenu>
      <ApplicationMenu CommandName="cmdFileMenu">
        <!-- Most recently used items collection. -->
        <ApplicationMenu.RecentItems>
          <RecentItems CommandName="cmdMRUItems"/>
        </ApplicationMenu.RecentItems>
        <!-- Menu items collection. -->
        <MenuGroup>
          <Button CommandName="cmdNew" />
          <Button CommandName="cmdOpen" />
          <Button CommandName="cmdSave" />
        </MenuGroup>
        <MenuGroup>
          <Button CommandName="cmdPrint" />
          <Button CommandName="cmdExit" />
        </MenuGroup>
      </ApplicationMenu>
    </Ribbon.ApplicationMenu>
    ```

    

When the markup is compiled with the UI Command Compiler (UICC) tool, the Command names and IDs are placed into a header file used by the Ribbon host application.

The following is an example of a header file generated by UICC.


```
// *****************************************************************************
// * This is an automatically generated header file for UI Element definition  *
// * resource symbols and values. Please do not modify manually.               *
// *****************************************************************************

#pragma once

#define cmdFileMenu 25000 
#define cmdNew 22001  /* New */ 
#define cmdNew_LabelTitle_RESID 60005
#define cmdOpen 22002  /* Open */ 
#define cmdOpen_LabelTitle_RESID 60006
#define cmdSave 22003  /* Save */ 
#define cmdSave_LabelTitle_RESID 60007
#define cmdSave_TooltipTitle_RESID 60008
#define cmdSave_TooltipDescription_RESID 60009
```



## Related topics

<dl> <dt>

[Extensible Application Markup Language (XAML)](/dotnet/framework/wpf/advanced/xaml-in-wpf)
</dt> <dt>

[Compiling Ribbon Markup](windowsribbon-intentcl.md)
</dt> </dl>

 

 