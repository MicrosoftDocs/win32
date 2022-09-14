---
title: Using UI Automation for Automated Testing
description: This overview describes how Microsoft UI Automation can be useful as a framework for programmatic access in automated testing scenarios.
ms.assetid: 192162f9-55bf-4111-9f15-c0d3b5af2ab7
keywords:
- clients,UI Automation automated testing
- clients,automated testing
- clients,testing
- clients,tools for automated testing
- clients,UI Automation tools for automated testing
- clients,UI Automation testing
- UI Automation,automated testing
- UI Automation,testing
- UI Automation,tools for automated testing
- automated testing
- tools for automated testing
ms.topic: article
ms.date: 05/31/2018
---

# Using UI Automation for Automated Testing

This overview describes how Microsoft UI Automation can be useful as a framework for programmatic access in automated testing scenarios.

UI Automation provides a unified object model that enables all UI frameworks to expose complex and rich functionality in an accessible and easily automated manner.

UI Automation was developed as a successor to Microsoft Active Accessibility, a framework designed to provide a solution for making controls and applications accessible. Microsoft Active Accessibility was not designed with test automation in mind, although it evolved into that role because of the similar requirements of accessibility and automation. UI Automation is specifically designed to provide robust functionality for automated testing, in addition to providing more refined solutions for accessibility. For example, Microsoft Active Accessibility relies on a single interface to expose information about the UI and to collect the information needed by assistive technology products; UI Automation separates the two models.

Both a provider and a client are required to implement UI Automation for it to be useful as an automated test tool. UI Automation providers are applications, such as Microsoft Word, Microsoft Excel, and other third-party applications or controls based on the Windows operating system. UI Automation clients include automated test scripts and assistive technology applications.

This topic contains the following sections.

-   [UI Automation in Providers](#ui-automation-in-providers)
-   [UI Automation in Clients](#ui-automation-in-clients)
    -   [Programmatic Access](#programmatic-access)
-   [Key Properties for Test Automation](#key-properties-for-test-automation)
-   [Related Tools and Technologies](#related-tools-and-technologies)
-   [Related topics](#related-topics)

## UI Automation in Providers

To automate an element of the user interface, the developer must look at what actions an end user can perform on the UI object by using standard keyboard and mouse interaction. After these key actions have been identified, the UI Automation control patterns that mirror the functionality and behavior of the UI element should be implemented on the control. For example, user interaction with a combo box control typically involves expanding and collapsing the combo box to display or hide a list of items, selecting an item from the list, or adding a new value through keyboard input.

With other accessibility models, developers must gather information directly from individual buttons, menus, or other controls. Every control type comes in dozens of minor variations. In other words, even though 10 variations of a pushbutton work the same way and perform the same function, they must all be treated as unique controls. There is no way to know that these controls are functionally equivalent. UI Automation control patterns were developed to represent these common control behaviors. For more information, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).

Without the unified model of control patterns provided by UI Automation, test tools and developers must have framework-specific information to expose properties and control behaviors in that framework. Because several different UI frameworks can be present at the same time in Windows operating systems, including Microsoft Win32, Windows Forms, and Windows Presentation Foundation (WPF), it can be a daunting task to test multiple applications with controls that seem similar. For example, the following table lists the framework-specific property names required to retrieve the name or text associated with a button control and shows the equivalent UI Automation property.



| Control type | UI framework | Framework-specific property | UI Automation property |
|--------------|--------------|-----------------------------|------------------------|
| Button       | WPF          | Content                     | Name property          |
| Button       | Win32        | Caption                     | Name property          |
| Image        | HTML         | alt                         | Name property          |



 

UI Automation providers are responsible for mapping the framework-specific properties of their controls to the equivalent UI Automation properties. For information on implementing UI Automation in a provider, see [UI Automation Provider Programmer's Guide](uiauto-providerportal.md). For information on implementing control patterns, see [Implementing UI Automation Control Patterns](uiauto-implementinguiautocontrolpatterns.md).

## UI Automation in Clients

The goal of automated test tools and scenarios is the consistent and repeatable manipulation of the UI. For example, this can involve unit testing specific controls, and recording and running test scripts that iterate through a series of generic actions on a group of controls.

A complication in automated applications is the difficulty of synchronizing a test with a dynamic target, for example, a list box control, such as Windows Task Manager, that displays a list of currently running applications. Because the items in the list box are dynamically updated outside the control of the test application, an attempt to repeat selecting a specific item in the list box with any consistency is impossible. Similar issues can arise when attempting to repeat simple focus changes in a UI that is outside the control of the test application.

### Programmatic Access

Programmatic access provides the ability to imitate, through code, any interaction and experience exposed by traditional mouse and keyboard input. UI Automation enables programmatic access through five components:

-   The UI Automation tree facilitates navigation through the structure of the UI. The tree is built from the collection of **HWND**s. For more information, see [UI Automation Tree Overview](uiauto-treeoverview.md).
-   Automation elements are individual components in the UI. These can often be more granular than an **HWND**.
-   Automation properties provide specific information about UI elements. For more information, see [UI Automation Properties Overview](uiauto-propertiesoverview.md).
-   Control patterns define a particular aspect of a control's functionality; they can consist of property, method, event, and structure information. For more information, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).
-   Automation events provide event notifications and information. For more information, see [UI Automation Events Overview](uiauto-eventsoverview.md).

## Key Properties for Test Automation

The ability to uniquely identify and subsequently locate any control in the UI provides the basis for automated test applications to operate on that UI. UI Automation properties used by clients and providers to identify and locate controls are described in the following table.



| Property     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutomationId | Uniquely distinguishes an automation element from its siblings. Support for the AutomationId property is not required. When it is available, the AutomationId property of an element is the same in any instance of the application, regardless of the local language. Although the AutomationId property is unique among sibling elements, it may not be unique across the entire desktop. For example, multiple instances of an application, or multiple folder views in Microsoft Windows Explorer, may contain elements with the same AutomationIdProperty, such as "SystemMenuBar". Clients should make no assumptions regarding the AutomationIds exposed by other applications. AutomationId is not guaranteed to be stable across different releases or builds of an application. |
| ControlType  | Identifies the type of control represented by an automation element. Significant information can be inferred from knowledge of the control type. For more information, see [UI Automation Control Types Overview](uiauto-controltypesoverview.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Name         | A text string that identifies or explains the purpose of an automation element. It should be used with caution because it can be localized. The Name property is not a unique identifier among siblings. For test automation, clients should use the AutomationId property or RuntimeId property instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RuntimeId    | An array of integers that represent an identifier for an automation element. The identifier is unique on the desktop, but is guaranteed to be unique only to the UI of the desktop on which it was generated. Identifiers can be reused over time. Use [**IUIAutomation::CompareElements**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-compareelements) to determine if the element that currently has a particular runtime ID is the same element that previously had that ID. Also, the format of the RuntimeId property may change. It should be treated as an opaque value and used only for comparison; for example, to determine whether an automation element is in the cache.                                                                                                                       |



 

## Related Tools and Technologies

[Inspect](inspect-objects.md) (Inspect.exe) is a Windows-based tool that you can use to gather UI Automation information for provider and client development and debugging. Inspect is included in the Windows Software Development Kit (SDK).

## Related topics

<dl> <dt>

[UI Automation Security Considerations](uiauto-securityoverview.md)
</dt> </dl>

 

 




