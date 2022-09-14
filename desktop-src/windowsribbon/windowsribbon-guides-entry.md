---
title: Windows Ribbon Framework Developer Guides
description: The topics contained in this section describe specific aspects of the Windows Ribbon framework.
ms.assetid: 87434a15-ba13-4c6f-a814-49ae2349bfa2
keywords:
- Windows Ribbon,framework
- Ribbon,framework
- Windows Ribbon,developer guides
- Ribbon,developer guides
- developer guides for Windows Ribbon
ms.topic: article
ms.date: 05/31/2018
---

# Windows Ribbon Framework Developer Guides

The topics contained in this section describe specific aspects of the Windows Ribbon framework.

## Basics

[Creating a Ribbon Application](windowsribbon-stepbystep.md)

For the Windows Ribbon framework to consume the Ribbon markup file, the markup file must be compiled into a binary format resource file. A dedicated Ribbon markup compiler, the UI Command Compiler (UICC), is included with the Microsoft Windows Software Development Kit (SDK) (7.0 or later) for this purpose. In addition to compiling the binary version of the Ribbon markup, the UICC generates an ID definition header (.h) file that exposes all markup elements to the Ribbon host application and a resource (.rc) file that is used to link image and string resources to the host application at build time.

[Migrating to the Windows Ribbon Framework](ribbon-migration.md)

An application that relies on traditional menus, toolbars, and dialogs can be migrated to the rich, dynamic, and context-driven user interface (UI) of the Ribbon framework Command system. This is an easy and effective way to modernize and revitalize the application while also improving the accessibility, usability, and discoverability of its functionality.

[Understanding Commands and Controls](windowsribbon-commandscontrols.md)

The separation of logic from presentation is the design philosophy that inspires the command presentation system of the Ribbon framework—a system that is based on a design pattern where functionality and behavior are implemented independently from the controls that expose this functionality.

## User Interface

[Specifying Ribbon Image Resources](windowsribbon-imageformats.md)

As a rich command presentation system, the Ribbon framework is designed to support image resources extensively throughout the Ribbon user interface (UI). All image resources are declared in [Ribbon markup](windowsribbon-schema.md) or queried from a Ribbon host application.

For Windows 8 and later, the Ribbon framework supports the following graphics formats: 32-bit ARGB bitmap (BMP) files and Portable Network Graphics (PNG) files with transparency.

For Windows 7 and earlier, image resources must conform to the standard BMP graphics format used in Windows.

[Customizing a Ribbon Through Size Definitions and Scaling Policies](windowsribbon-templates.md)

Controls hosted in the ribbon Command bar are subject to layout rules that are enforced by the Ribbon framework and based on a combination of default behaviors and layout templates (both framework-defined and custom) as declared in the Ribbon markup. These rules define the adaptive layout behaviors of the Ribbon framework that influence how controls in the Command bar adapt to various ribbon sizes at run time.

[Working with Galleries](ribbon-controls-galleries.md)

The Ribbon framework provides developers with a robust and consistent model for managing dynamic content across a variety of collection-based controls. By adapting and reconfiguring the Ribbon user interface (UI), these dynamic controls allow the framework to respond to user interaction in both the host application and Ribbon itself, and provide the flexibility to handle various run time environments.

[Displaying Contextual Tabs](ribbon-contextualtabs.md)

In a Ribbon framework application, a contextual tab is a hidden [Tab](windowsribbon-controls-tab.md) control that is displayed in the tab row when an object in the application workspace, such as an image, is selected or highlighted.

[Reconfiguring the Ribbon with Application Modes](ribbon-applicationmodes.md)

The Ribbon framework supports the dynamic reconfiguring and exposing of core elements of the Ribbon user interface (UI) at run time, based on the application's state (also referred to as context). Declared and associated with specific elements in markup, the various states supported by an application are referred to as application modes.

[Customizing Ribbon Colors](ribbon-color.md)

The Ribbon framework exposes a set of color properties that allow an application to customize the appearance of various Ribbon user interface (UI) elements at run time.

[Displaying the Ribbon](ribbon-visibility.md)

The Ribbon framework exposes a set of properties that allow an application to specify how the Ribbon user interface (UI) is displayed at run time.

## Management

[Persisting Ribbon State](ribbon-statepersistence.md)

The Windows Ribon framework (Ribbon) provides the ability to preserve the state of a variety of user settings and preferences across application sessions.

[Listening for Ribbon Events](listening-for-ribbon-events.md)

The Ribbon framework uses the [Event Tracing for Windows (ETW)](../etw/event-tracing-portal.md) infrastructure to enable developers to learn how users are interacting with their application's ribbon.

## Markup Compiler

[Compiling Ribbon Markup](windowsribbon-intentcl.md)

For the Ribbon framework to consume the [Ribbon markup](windowsribbon-schema.md) file, the markup file must be compiled into a binary format resource file. A dedicated markup compiler, the UI Command Compiler (UICC), is included with the Microsoft Windows Software Development Kit (SDK) (7.0 or later) for this purpose. In addition to compiling the binary version of the markup, the UICC generates an ID definition header (.h) file that exposes all markup elements to the Ribbon host application and a resource (.rc) file that is used to link image and string resources to the host application at build time.

[Understanding Markup Compiler Messages](windowsribbon-compilationerrors.md)

The Windows Ribbon framework (Ribbon) markup compiler, UI Command Compiler (UICC.exe), validates the Ribbon markup against both the Ribbon schema and an additional set of rules defined by the Ribbon framework.

 

 