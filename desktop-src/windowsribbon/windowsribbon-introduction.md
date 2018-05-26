---
title: Introducing the Windows Ribbon Framework
description: The Windows Ribbon framework is a rich command presentation system that provides a modern alternative to the layered menus, toolbars, and task panes of traditional Windows applications.
ms.assetid: bc19d5eb-e3a4-4022-8051-512cb3a3e065
keywords:
- Windows Ribbon,framework
- Ribbon,framework
- Windows Ribbon,about
- Ribbon,about
- Windows Ribbon,components
- Ribbon,components
- Windows Ribbon,views
- Ribbon,views
- Windows Ribbon,architecture
- Ribbon,architecture
- Windows Ribbon,APIs
- Ribbon,APIs
- Windows Ribbon,security
- Ribbon,security
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Introducing the Windows Ribbon Framework

The Windows Ribbon framework is a rich command presentation system that provides a modern alternative to the layered menus, toolbars, and task panes of traditional Windows applications.

-   [A New Command Paradigm](#a-new-command-paradigm)
-   [Views](#views)
    -   [The Ribbon View](#the-ribbon-view)
    -   [The ContextPopup View](#the-contextpopup-view)
-   [Ribbon Architecture](#ribbon-architecture)
    -   [The Ribbon APIs](#the-ribbon-apis)
    -   [Security and Privacy](#security-and-privacy)
    -   [Accessibility and Localization](#accessibility-and-localization)
-   [Conclusion](#conclusion)
-   [Related topics](#related-topics)

## A New Command Paradigm

The Ribbon framework is a collection of Microsoft Win32 APIs that support a host of new UI capabilities for Windows developers.

This rich, modern UI command framework offers:

-   Easy implementation for brand new Ribbon framework applications and straightforward migration of existing Win32 applications.
-   Consistent appearance and behavior across Ribbon applications.
-   Adherence to Windows UI guidelines for a first-class Windows experience through accessibility standards, visual style (theming) support, automatic high contrast adjustments, and high dots per inch (dpi) awareness.

The Ribbon framework consists of two primary UI components:

-   The ribbon command bar, which is composed of the Quick Access Toolbar (QAT) that exposes and highlights various ribbon commands as specified by the user or the application, and a tab row that contains the application menu, standard or contextual tabs, and a help button.
-   A rich context menu system.

A combination of declarative XML and native COM interfaces is used to decouple the presentation and functionality of these components.

## Views

The primary UI components of the Ribbon framework, the ribbon command bar and the context menu system, are differentiated structurally through *Views*. The framework supports two Views: the [**Ribbon**](windowsribbon-element-ribbon.md) View and the [**ContextPopup**](windowsribbon-element-contextpopup.md) View.

### The Ribbon View

The UI of the [**Ribbon**](windowsribbon-element-ribbon.md) View is the primary feature of the Ribbon framework and provides the next-generation user experience for presenting commands in Windows applications.

The ribbon is a command bar that exposes the major features of an application through a series of tabs at the top of an application window. It is similar in functionality and appearance to the Microsoft Office 2007 Fluent UI. The ribbon provides an intuitive counterpoint to the trial-and-error process of command discovery that is typical of standard Windows menu systems. Optimized for efficiency and discoverability, the ribbon facilitates finding, understanding, and using commands with minimum mouse clicks and keystrokes through a system of standard controls, galleries, and live previewing.

The following image illustrates the Ribbon framework implementation in Paint for Windows 7.

![screen shot showing the ribbon implementation in paint for windows 7.](images/overviews/screenshot-paint-win7transparency-mirror.png)

### The ContextPopup View

The [**ContextPopup**](windowsribbon-element-contextpopup.md) View, through the [Context Popup](windowsribbon-controls-contextpopup.md) control, provides a richer context menu system than is available with earlier Windows applications. A Context Popup can only be deployed in support of a ribbon, a standalone Context Popup is not supported by the Ribbon framework.

## Ribbon Architecture

In contrast to the traditional control-based Windows UI development model, Windows Ribbon framework UI development is based on the more abstract concept of Commands. By focusing on the Commands that are associated with controls, rather than the controls themselves, the framework is able to automatically adjust the UI as required in response to Command execution state retrieved from the Ribbon host application.

An application that uses the Ribbon framework exposes Commands without being encumbered with the details of how that Command is represented in the UI. This is sometimes referred to as an intent-based UI model. The [**Command type**](https://msdn.microsoft.com/library/windows/desktop/dd371556), its properties, and its resources define the intent of the Command for the application. For example, mouse input, keyboard input, or even shaking a gyroscopic device can result in the execution of the same Command the application is only concerned with executing the Command, not with how it was invoked.

The Ribbon framework provides this flexibility by separating functionality from presentation with two distinct development structures: an Extensible Application Markup Language (XAML)-based markup language to declare controls and the visual layout of a Ribbon implementation, and C++ COM-based interfaces to initialize the framework and handle events at run time. This distinction enables UI developers and designers to be solely responsible for the appearance of a Ribbon application, while core functionality remains the domain of software engineers.

For more information, see [Understanding Commands and Controls](windowsribbon-commandscontrols.md).

### The Ribbon APIs

The Ribbon APIs provide the necessary connections between a View and the Ribbon host application. These APIs consist of the following interfaces and property keys:

-   A set of COM interfaces implemented by the Ribbon framework to perform UI services.

    

    | Interface                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    |----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [****IUIContextualUI****](https://msdn.microsoft.com/library/windows/desktop/dd371482)           | Defines the methods for the core functionality of the [**ContextPopup**](windowsribbon-element-contextpopup.md) View.                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | [****IUIFramework****](https://msdn.microsoft.com/library/windows/desktop/dd371467)                 | Defines the methods that support the core functionality of the [**Ribbon**](windowsribbon-element-ribbon.md) and [**ContextPopup**](windowsribbon-element-contextpopup.md) Views.                                                                                                                                                                                                                                                                                                                                                     |
    | [****IUIRibbon****](https://msdn.microsoft.com/library/windows/desktop/dd371360)                       | Defines the methods for specifying settings and properties for a [**Ribbon**](windowsribbon-element-ribbon.md) View.                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | [****IUISimplePropertySet****](https://msdn.microsoft.com/library/windows/desktop/dd371358) | Defines a method for retrieving the value identified by a property key. This interface is implemented by the Ribbon framework and is also implemented by the host application for each item in the [**IUICollection**](https://msdn.microsoft.com/library/windows/desktop/dd371519) object of an item gallery.<br/> When implemented by the host application, the method defined by this interface is used to retrieve a property key value for the selected item in the [**IUICollection**](https://msdn.microsoft.com/library/windows/desktop/dd371519).<br/> |
    | [****IUICollection****](https://msdn.microsoft.com/library/windows/desktop/dd371519)               | Defines the methods for dynamically manipulating collection-based controls, such as the Ribbon QAT and collection-based [galleries](ribbon-controls-galleries.md), at run time.                                                                                                                                                                                                                                                                                                                                                        |
    | [****IUIImage****](https://msdn.microsoft.com/library/windows/desktop/dd371367)                         | Defines the method for retrieving an image for display in the Ribbon UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | [****IUIImageFromBitmap****](https://msdn.microsoft.com/library/windows/desktop/dd371365)     | Defines the factory method for creating an [**IUIImage**](https://msdn.microsoft.com/library/windows/desktop/dd371367) object.                                                                                                                                                                                                                                                                                                                                                                                                                                 |

    

     

-   A set of COM interfaces implemented by the Ribbon host application that the framework calls in response to UI changes.

    

    | Interface                                                                                  | Description                                                                                                  |
    |--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
    | [****IUIApplication****](https://msdn.microsoft.com/library/windows/desktop/dd371528)                       | Defines the application callback entry-point methods for the Ribbon framework.                               |
    | [****IUICommandHandler****](https://msdn.microsoft.com/library/windows/desktop/dd371491)                 | Defines the methods for gathering Command information and handling Command events from the Ribbon framework. |
    | [****IUICollectionChangedEvent****](https://msdn.microsoft.com/library/windows/desktop/dd371499) | Defines the method required to handle changes to a collection at run time.                                   |

    

     

-   A set of property keys that define which UI properties the application has programmatic control over.

    

    | Property Key Type                                                  | Description                                              |
    |--------------------------------------------------------------------|----------------------------------------------------------|
    | [Collection](windowsribbon-reference-properties-collection.md)    | Defines properties for Ribbon collection-based controls. |
    | [Color Picker](windowsribbon-reference-properties-colorpicker.md) | Defines properties for Ribbon color picker controls.     |
    | [Font](windowsribbon-reference-properties-fontcontrol.md)         | Defines properties for the Ribbon FontControl.           |
    | [Global](windowsribbon-reference-properties-framework.md)         | Defines global properties for the Ribbon framework.      |
    | [Resource](windowsribbon-reference-properties-resource.md)        | Defines Ribbon resource properties.                      |
    | [Ribbon](windowsribbon-reference-properties-ribbon.md)            | Defines Ribbon View properties.                          |
    | [State](windowsribbon-reference-properties-state.md)              | Defines properties for Ribbon control state or context.  |

    

     

### Security and Privacy

The Ribbon framework DLL (uiribbon.dll) runs in-process and has the same privileges as the host application. The Ribbon accepts only what the host application provides as input or user input from tightly constrained controls such as the spinner and editable combo box.

In addition, the framework does not permanently store any information except what is provided by the host application or collected (as authorized by the end user) through the opt-in Windows Customer Experience Program.

### Accessibility and Localization

To provide a highly accessible UI, the Ribbon framework implements Microsoft Active Accessibility. By automatically populating relevant Microsoft Active Accessibility properties with valid and helpful information, the framework significantly reduces the burden on developers to provide an inclusive experience for all users.

For more information on accessibility in the Ribbon framework, see [Working with Active Accessibility in the 2007 Office Fluent User Interface](http://go.microsoft.com/fwlink/p/?linkid=157256).

In addition, the Ribbon framework is a Windows feature and, as such, is localized for all languages that Windows supports. Developers, however, are responsible for localizing their own specific application resources.

## Conclusion

The Ribbon is a new and engaging form of command presentation that application developers, architects, and designers should consider when designing and building new applications or updating existing ones.

The [Windows Ribbon Development Forum](http://go.microsoft.com/fwlink/p/?linkid=156613) is available to discuss topics and ask questions related to developing applications that implement the Windows Ribbon framework.

## Related topics

<dl> <dt>

[Declaring Commands and Controls with Ribbon Markup](windowsribbon-schema.md)
</dt> <dt>

[Ribbon User Experience Guidelines](http://go.microsoft.com/fwlink/p/?linkid=129233)
</dt> <dt>

[Ribbon Design Process](http://go.microsoft.com/fwlink/p/?linkid=129234)
</dt> </dl>

 

 





