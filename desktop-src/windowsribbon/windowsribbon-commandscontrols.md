---
title: Understanding Commands and Controls
description: The separation of logic from presentation is the design philosophy that inspires the command presentation system of the Windows Ribbon framework \ 8212;a system that is based on a design pattern where functionality and behavior are implemented independently from the controls that expose this functionality.
ms.assetid: fdea0d70-c6e0-4d13-99bc-ff0c1dbff10d
keywords:
- Windows Ribbon,commands overview
- Ribbon,commands overview
- Windows Ribbon,controls overview
- Ribbon,controls overview
- command system for Windows Ribbon
- controls for Windows Ribbon
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Commands and Controls

The separation of logic from presentation is the design philosophy that inspires the command presentation system of the Windows Ribbon framework—a system that is based on a design pattern where functionality and behavior are implemented independently from the controls that expose this functionality.

-   [Introduction](#introduction)
-   [The Windows Ribbon Command System](#the-windows-ribbon-command-system)
    -   [Controls](#understanding-commands-and-controls)
    -   [Commands](#understanding-commands-and-controls)
    -   [The Command Experience In Action](#the-command-experience-in-action)
-   [Related topics](#related-topics)

## Introduction

This article discusses the design of the Ribbon framework command system. It describes the concepts of Commands and controls and explores how they work together to provide a rich command experience with a host of new UI capabilities.

## The Windows Ribbon Command System

In the Ribbon framework, Commands and controls are independent entities. A Command is an abstract structure, without presentation constraints, that represents a specific task or class of functionality. A control, on the other hand, is a concrete object that exposes Command functionality through the Ribbon UI.

This distinction provides the ability to define Commands that are free of UI details and able to execute on the intent of an action without the need to manage how the action was invoked.

### Controls

Controls are the UI objects required for Command presentation. They are rendered and managed at run time by the framework based on user interaction and a set of inherent properties and behaviors.

Known as adaptive layout, the framework-managed flexibility of the UI is one of the great strengths of the Ribbon. Ribbon controls can automatically reconfigure themselves through framework-dependent or developer-defined layout templates that are able to respond to various run time requirements, all without writing a single line of presentation code. For more information, see [Customizing a Ribbon Through Size Definitions and Scaling Policies](windowsribbon-templates.md).

Besides the benefits of adaptive layout, a number of complex Ribbon controls provide self-contained solutions for specific UI problem spaces. By offering a sophisticated interaction model, Ribbon controls, such as the FontControl or ColorPicker, provide the ability to manipulate data in more abstract terms through property bags of actual font or color attributes rather than through various sub-controls, enumerations, and index values of standard Windows controls.

### Commands

Loosely coupled to the Ribbon controls that expose their functionality, Command implementations are the domain of the host application and take the form of event listeners, Command handlers, and various Command properties.

Commands are declared in Ribbon markup with a unique ID, or assigned a markup compiler-generated ID at compilation. Commands are associated with controls through a Command name but, unlike controls, their actual functionality is defined in code where they are bound to specific Command handlers through the Command ID.

> [!Note]  
> At compilation, this ID is stored in an ID definition header file that exposes Commands to their corresponding Command handlers in the Ribbon host application.

 

Each Command has an underlying Command type itemized in the [**UI\_COMMANDTYPE**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_commandtype) enumeration.

### The Command Experience In Action

The capabilities of this command model are demonstrated by the Ribbon Quick Access Toolbar (QAT). The QAT provides end users with a way to easily define their own shortcuts for virtually any control in the Ribbon UI. A shortcut is added dynamically to the QAT at run time when the user right-clicks a Ribbon control and selects **Add to Quick Access Toolbar** from the context menu.

The following picture shows the **Paste** and **Paste from** Commands, represented by a [**SplitButton**](windowsribbon-element-splitbutton.md) control, in the Ribbon of Windows 7 Paint.

![picture of the paste splitbutton in the microsoft paint ribbon.](images/overviews/paint-paste-splitbutton-ribbon.png)

The following picture shows the same **Paste** and **Paste from** Commands, still represented by a [**SplitButton**](windowsribbon-element-splitbutton.md) control, in the Ribbon QAT of Windows 7 Paint.

![picture of the paste splitbutton in the microsoft paint qat.](images/overviews/paint-paste-splitbutton-qat.png)

When a control is hosted by the QAT, the new instance of the control maintains all the functionality of the original control without the need for additional event listeners and command handlers to support it. Both controls are bound to the same Ribbon Command handler through a shared Command identifier. In this way, the framework treats both controls as one, no matter which is invoked.

> [!Note]  
> The same benefits are realized when Commands are incorporated into a [**ContextPopup**](windowsribbon-element-contextpopup.md) at design time. In this case, the Paste Command handlers can be used whether the [**SplitButton**](windowsribbon-element-splitbutton.md) control appears in the Ribbon, the QAT, or the **ContextPopup**.

 

## Related topics

<dl> <dt>

[Introducing the Windows Ribbon Framework](windowsribbon-introduction.md)
</dt> <dt>

[Creating a Ribbon Application](windowsribbon-stepbystep.md)
</dt> <dt>

[Declaring Commands and Controls with Ribbon Markup](windowsribbon-schema.md)
</dt> </dl>

 

 