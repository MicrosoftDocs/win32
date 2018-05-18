---
Description: Rob Haverty
ms.assetid: '3f64f51f-24fe-411a-8354-f446810de023'
title: New Accessibility Model for Microsoft Windows and Cross Platform Development
---

# New Accessibility Model for Microsoft Windows and Cross Platform Development

Rob Haverty

Microsoft Corporation

September 2005

Summary: Microsoft Windows User Interface (UI) Automation is an accessibility framework for Microsoft Windows that will ultimately replace Microsoft Active Accessibility (MSAA). UI Automation is intended to address the needs of assistive technology products and automated testing frameworks by providing programmatic access to information about the user interface. UI Automation is fully supported on Microsoft Windows XP and the next version of the Windows desktop operating system, Windows Vista (support will continue for MSAA in the Windows Vista time frame as well). It is also available for cross platform development through a royalty-free license.

-   [Introduction](#introduction)
-   [UI Automation Namespaces](#ui-automation-namespaces)
-   [UI Automation Tree](#ui-automation-tree)
    -   [Views of the Automation Tree](#views-of-the-automation-tree)
    -   [Raw View](#raw-view)
    -   [Control View](#control-view)
    -   [Content View](#content-view)
    -   [Custom View](#custom-view)
    -   [Automation Tree Structure Example](#automation-tree-structure-example)
-   [UI Automation Control Patterns](#ui-automation-control-patterns)
    -   [Control Pattern Components](#control-pattern-components)
    -   [Standard UI Controls and Their Control Patterns](#standard-ui-controls-and-their-control-patterns)
    -   [Control Patterns](#standard-ui-controls-and-their-control-patterns)
-   [UI Automation Properties](#ui-automation-properties)
-   [UI Automation Events](#ui-automation-events)
-   [Conclusions](#conclusions)
-   [References](#references)

## Introduction

In 2003, Microsoft Corporation commissioned Forrester Research, Inc., to conduct a study to measure the potential market of people in the United States who are most likely to benefit from the use of accessible technology for computers (for more information, see [Research About Accessibility](http://go.microsoft.com/fwlink/p/?linkid=208695)). Accessible technology enables individuals to adjust their computers to meet their visual, hearing, dexterity, cognitive, and speech needs. It includes both accessibility options built into products as well as specialty hardware and software products ([assistive technology products](http://go.microsoft.com/fwlink/p/?linkid=208696)) that help individuals interact with a computer. Overall results show that 57% (74.2 million)of computer users in the United States are likely or very likely to benefit from the use of accessible technology due to experiencing mild to severe difficulties or impairments.

With the current technology, assistive technology vendors (ATVs) are required to use many different approaches to obtain and present information about the UI to the end user, thus spending an inordinate amount of time and resources on providing this basic information. With such a large percentage of users needing accessible information, it is becoming increasingly important to make it easier for an ATV to programmatically obtain information about the UI.

The new accessibility model for Windows, UI Automation, is designed to provide a single reliable source of UI information to assistive technology products and automated test scripts. It provides programmatic access that allows automated tests to interact with the UI and allows assistive technology products to provide information about the user interface to their end users. UI Automation also provides means for manipulating the UI.

UI Automation has two main audiences: UI Automation providers and UI Automation clients. UI Automation providers are applications such as Microsoft Word, or third-party applications. UI Automation clients are assistive technology applications, such as screen readers, screen enlargers, or others. Automated test scripts can use UI Automation for automated testing and are also considered clients in the UI Automation framework.

This document includes information on the namespaces that the UI Automation framework uses, as well as information on the following UI Automation features: automation tree, control patterns, properties, events, and input.

## UI Automation Namespaces

Namespaces are used as an organizational system — a way of presenting program components that are exposed to other programs and applications. The following table lists the namespaces used in the UI Automation framework, as well as the audience that uses each namespace.

**Table 1. UI Automation Namespaces and related audiences**



| Namespace                                                                      | Audience used by                                                                                   |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**System.Windows.Automation**](frlrfSystemWindowsAutomation)                  | Clients for finding automation elements, registering for events and working with control patterns. |
| [**System.Windows.Automation.Provider**](frlrfSystemWindowsAutomationProvider) | Providers for implementing UI Automation on controls or applications.                              |



 

## UI Automation Tree

Standard Windows programming has always exposed the relationship between elements in the user interface in a parent/child relational structure. UI Automation clients view the UI elements on the desktop (a UI element would be, for example, the OK button) as a set of automation elements that are arranged in a tree structure. Automation elements are referenced through a common object ([**AutomationElement**](frlrfSystemWindowsAutomationAutomationElementClassTopic) to enable consistent information, interaction, and a navigation model. UI Automation unifies disparate UI Frameworks so that code can be written against one API rather than several.

Within the automation tree there is a root automation element that represents the current desktop and whose children represent application windows on the desktop. Each of these child elements can contain automation elements representing the UI elements that make up their UI, such as menus, buttons, toolbars, and others. Each piece of UI can contain automation elements representing their content, such as menu items or list items. Even a button, which does not contain any items, may have children automation elements that represent the basic UI components that make up the button, such as text and rectangles.

It is important to note that the automation tree is not a fixed structure. For performance reasons it is built on demand starting with an automation element that the client specifies.

### Views of the Automation Tree

The automation tree can be filtered to create customized views of the tree that contain only those automation elements that are relevant for a particular client. This approach allows clients to customize the structure presented through UI Automation to their particular needs. Default views are provided by the UI Automation framework, but clients can also define custom views.

### Raw View

The raw view of the automation tree is the full tree of elements for which the desktop is the root. The raw view closely follows the native programmatic structure of an application and therefore is the most detailed view that is available. It is also the base on which the other views of the tree are built. Because this view depends on the underlying UI framework, the raw view of a button from one framework will have a different view than a button from another framework.

### Control View

The control view of the automation tree simplifies the assistive technology product's task of describing the UI to the end user and helping that end user interact with the application because it closely maps to the UI structure perceived by an end user.

The control view includes all elements from the raw view that an end user would understand as interactive or contributing to the logical structure of the control in the UI. Examples of elements that contribute to the logical structure of the UI but are not interactive themselves are item containers such as list view headers, toolbars, menus, and the status bar. Non-interactive elements used simply for layout or decorative purposes will not be seen in the control view. An example is a panel that was used only to layout the controls in a dialog box but does not itself contain any information. Non-interactive elements that will be seen in the control view are graphics with information and static text in a dialog box.

### Content View

The content view of the automation tree contains elements that convey the true information in a user interface. For example, the values in a combo box will appear in the content view because they represent the information being used by an end user. In the content view, a combo box and list box are both represented as a collection of items where one or more items can be selected. The fact that one is always open and one can expand and collapse is irrelevant in the content view, because it is designed to show the data, or content, that is being presented to the user.

### Custom View

The UI Automation framework also allows a client to create a custom view of the automation tree by specifying the desired match conditions and scoping information. This also allows clients to build their own interaction models for the application using just the data that they need.

### Automation Tree Structure Example

The following example compares the control view and content view of the automation tree for the same application:

**Table 2. Comparison of two Automation Tree structures**



|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Automation Tree (Control View)**<br/> The Control view of WordPad shown from the Desktop has the following structure:<br/> Desktop<br/> Window "Notepad"<br/> TitleBar "Notepad"<br/> SystemBar<br/> MenuItem<br/> Button AutomationId = "Minimize"<br/> Button AutomationId = "Maximize"<br/> Button AutomationId = "Close"<br/> MenuBar ""<br/> MenuItem "File"<br/> MenuItem "Edit"<br/> ToolBar ""<br/> Button "New"<br/> Button "Open"<br/> Text ""<br/> StatusBar<br/> Edit<br/> Edit<br/> | **Automation Tree (Content View)**<br/> The Content view of WordPad shown from the Desktop has the following structure:<br/> Desktop<br/> Window "Notepad"<br/> MenuBar ""<br/> MenuItem "File"<br/> MenuItem "Edit"<br/> ToolBar ""<br/> Button "New"<br/> Button "Open"<br/> Text ""<br/> StatusBar<br/> Edit<br/> Edit<br/> |



 

## UI Automation Control Patterns

UI Automation uses control patterns to express the functionality contained in each control. UI Automation differentiates between what a user would call the control and what can be programmatically done with the control by using control patterns to express only functionality, separate from the type or name of that control.

Providers implement control pattern interfaces on UI elements. Control pattern interfaces are found in the [**System.Windows.Automation.Provider**](frlrfSystemWindowsAutomationProvider) namespace and have names that include the suffix "Provider" (for example, [**IScrollProvider**](frlrfSystemWindowsAutomationProviderIScrollProviderClassTopic) and [**IInvokeProvider**](frlrfSystemWindowsAutomationProviderIInvokeProviderClassTopic)).

Clients access methods and properties of control pattern classes and use them to access information about a UI element, or to manipulate the UI. These control patterns classes are found in the [**System.Windows.Automation**](frlrfSystemWindowsAutomation)namespace and have names that include the suffix "Pattern" (for example, [**InvokePattern**](frlrfSystemWindowsAutomationInvokePatternClassTopic) and [**SelectionPattern**](frlrfSystemWindowsAutomationSelectionPatternClassTopic)).

### Control Pattern Components

Control patterns may define the structure, methods, properties, and events supported by a control:

The structure includes the parent, child, and sibling relationships of elements for that control pattern.

The methods provide the ability to programmatically manipulate the control.

The properties and events provide rich information and notifications relevant for that control.

Control patterns relate to UI as interfaces relate to COM objects. In COM, you can query an object to ask what interfaces it supports, and then use those interfaces to access functionality. In UI Automation, clients can ask a control which patterns it supports and then interact with the control through the properties, methods, events, and structure of the supported control patterns. For example, providers implement [**IScrollProvider**](frlrfSystemWindowsAutomationProviderIScrollProviderClassTopic) for a multi-line edit box. When a client detects that a UI element supports [**ScrollPattern**](frlrfSystemWindowsAutomationScrollPatternClassTopic), it can use the properties, methods, and events from that class to gather scroll-specific information or programmatically scroll its content to a new position.

### Standard UI Controls and Their Control Patterns

Controls can support zero or more control patterns. For example:

The image control does not support any control patterns.

The button control supports [**InvokePattern**](frlrfSystemWindowsAutomationInvokePatternClassTopic) to correspond to the functionality that it can be clicked.

To define the full set of functionality for a control, providers implement multiple control patterns. The following table shows more examples of standard controls and the control patterns they support.

**Table 3. Controls and Their Control Patterns**



| Control Type | Relevant Control Patterns     |
|--------------|-------------------------------|
| Button       | Invoke or Toggle              |
| CheckBox     | Toggle                        |
| ComboBox     | ExpandCollapse, Selection     |
| Edit         | Value, Text                   |
| List         | Selection                     |
| ListItem     | SelectionItem                 |
| Tree         | Selection                     |
| TreeItem     | SelectionItem, ExpandCollapse |



 

### Control Patterns

The following table lists some of the key control patterns and their classes and interfaces.

**Table 4. Control Patterns and Their Classes and Interfaces**



| Control Pattern | Client-Side Class                                                                        | Provider-Side Interfaces                                                                             |
|-----------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Dock            | [**DockPattern**](frlrfSystemWindowsAutomationDockPatternClassTopic)                     | [**IDockProvider**](frlrfSystemWindowsAutomationProviderIDockProviderClassTopic)                     |
| ExpandCollapse  | [**ExpandCollapsePattern**](frlrfSystemWindowsAutomationExpandCollapsePatternClassTopic) | [**IExpandCollapseProvider**](frlrfSystemWindowsAutomationProviderIExpandCollapseProviderClassTopic) |
| Grid            | [**GridPattern**](frlrfSystemWindowsAutomationGridPatternClassTopic)                     | [**IGridProvider**](frlrfSystemWindowsAutomationProviderIGridProviderClassTopic)                     |
| Invoke          | [**InvokePattern**](frlrfSystemWindowsAutomationInvokePatternClassTopic)                 | [**IInvokeProvider**](frlrfSystemWindowsAutomationProviderIInvokeProviderClassTopic)                 |
| Multiple View.  | [**MultipleViewPattern**](frlrfSystemWindowsAutomationMultipleViewPatternClassTopic)     | [**IMultipleViewProvider**](frlrfSystemWindowsAutomationProviderIMultipleViewProviderClassTopic)     |
| RangeValue      | [**RangeValuePattern**](frlrfSystemWindowsAutomationRangeValuePatternClassTopic)         | [**IRangeValueProvider**](frlrfSystemWindowsAutomationProviderIRangeValueProviderClassTopic)         |
| Scroll          | [**ScrollPattern**](frlrfSystemWindowsAutomationScrollPatternClassTopic)                 | [**IScrollProvider**](frlrfSystemWindowsAutomationProviderIScrollProviderClassTopic)                 |
| ScrollItem      | [**ScrollItemPattern**](frlrfSystemWindowsAutomationScrollItemPatternClassTopic)         | [**IScrollItemProvider**](frlrfSystemWindowsAutomationProviderIScrollItemProviderClassTopic)         |
| Selection       | [**SelectionPattern**](frlrfSystemWindowsAutomationSelectionPatternClassTopic)           | [**ISelectionProvider**](frlrfSystemWindowsAutomationProviderISelectionProviderClassTopic)           |
| SelectionItem   | [**SelectionItemPattern**](frlrfSystemWindowsAutomationSelectionItemPatternClassTopic)   | [**ISelectionItemProvider**](frlrfSystemWindowsAutomationProviderISelectionItemProviderClassTopic)   |
| Table           | [**TablePattern**](frlrfSystemWindowsAutomationTablePatternClassTopic)                   | [**ITableProvider**](frlrfSystemWindowsAutomationProviderITableProviderClassTopic)                   |
| TableItem       | [**TableItem**](frlrfSystemWindowsAutomationTableItemPatternClassTopic)                  | [**ITableItemProvider**](frlrfSystemWindowsAutomationProviderITableItemProviderClassTopic)           |
| Text            | [**TextPattern**](frlrfSystemWindowsAutomationTextPatternClassTopic)                     | [**ITextProvider**](frlrfSystemWindowsAutomationProviderITextProviderClassTopic)                     |
| Toggle          | [**TogglePattern**](frlrfSystemWindowsAutomationTogglePatternClassTopic)                 | [**IToggleProvider**](frlrfSystemWindowsAutomationProviderIToggleProviderClassTopic)                 |
| Transform       | [**TransformPattern**](frlrfSystemWindowsAutomationTransformPatternClassTopic)           | [**ITransformProvider**](frlrfSystemWindowsAutomationProviderITransformProviderClassTopic)           |
| Value           | [**ValuePattern**](frlrfSystemWindowsAutomationValuePatternClassTopic)                   | [**IValueProvider**](frlrfSystemWindowsAutomationProviderIValueProviderClassTopic)                   |
| Window          | [**WindowPattern**](frlrfSystemWindowsAutomationWindowPatternClassTopic)                 | [**IWindowProvider**](frlrfSystemWindowsAutomationProviderIWindowProviderClassTopic)                 |



 

## UI Automation Properties

UI Automation properties are a set of standard properties that expose information that is important to assistive technologies. Frequently, this information is exposed differently for each UI framework.

The following table shows how one standard UI Automation property maps to multiple property names in other UI frameworks.

**Table 5. Mapping UI Automation Properties to Other UI Frameworks**



| UI Automation Control Type | UI Framework | Framework Property | UI Automation Property |
|----------------------------|--------------|--------------------|------------------------|
| Button                     | Win32        | Caption            | NameProperty           |
| Image                      | Trident/HTML | ALT                | NameProperty           |



 

By implementing UI Automation, providers map unique UI framework properties to standard UI Automation properties. When this done, it allows clients to query for property information using one API call for a UI Automation property.

## UI Automation Events

UI Automation offers an event mechanism similar to WinEvents in the current Windows platform. However, unlike WinEvents, UI Automation's events are not based on a broadcast mechanism. Clients register for specific event notifications and can request that specific UI Automation properties and control pattern information be passed into their event handler. This provides a much more powerful mechanism than WinEvents because clients make fewer calls to retrieve the information they require, which results in fewer cross-process calls, and therefore better performance. UI Automation provides event notifications for logical structure changes, control pattern changes, focus changes, property changes, and multimedia events.

## Conclusions

UI Automation is a key part of the new accessibility model for Windows, gathering information about and interacting with the UI. Adoption of this technology will improve product quality for Windows applications and reduce the time to market for assistive technology products. Additionally, by implementing UI Automation, ATVs reduce the resources invested in obtaining UI information allowing them to improve and expand on the products that they offer.

## References

[.NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=180690)

[Microsoft research results](http://go.microsoft.com/fwlink/p/?linkid=208695)

[Microsoft Accessibility home page](http://go.microsoft.com/fwlink/p/?linkid=202420)

 

 




