---
title: Microsoft Active Accessibility and UI Automation Compared
description: This topic provides summarizes the main differences between Microsoft Active Accessibility and UI Automation.
ms.assetid: ba963e53-6fb8-4bc1-8883-62547f52b0e2
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Active Accessibility and UI Automation Compared

The Windows Automation API consists of two technologies—Microsoft Active Accessibility and Microsoft UI Automation. Microsoft Active Accessibility is the legacy accessibility technology that was introduced as a platform add-in for Windows 95, while UI Automation is a newer, more capable technology that overcomes the limitations inherent in Microsoft Active Accessibility.

This topic provides summarizes the main differences between Microsoft Active Accessibility and UI Automation. It includes the following sections:

-   [Basic Design Principles](#basic-design-principles)
-   [Properties and Control Patterns](#properties-and-control-patterns)
-   [MSAA Roles and UI Automation Control Patterns](#msaa-roles-and-ui-automation-control-patterns)
-   [Object Model Navigation](#object-model-navigation)
-   [Object Model Extensibility](#object-model-extensibility)
-   [Transitioning from MSAA](#transitioning-from-msaa)
-   [Choosing Microsoft Active Accessibility, UI Automation, or IAccessibleEx](#choosing-microsoft-active-accessibility-ui-automation-or-iaccessibleex)
    -   [New Applications and Controls](#new-applications-and-controls)
    -   [Existing Microsoft Active Accessibility Implementations](#existing-microsoft-active-accessibility-implementations)
-   [Related topics](#related-topics)

## Basic Design Principles

Although Microsoft Active Accessibility and UI Automation are two different technologies, the basic design principles are similar. The purpose of both technologies is to expose rich information about the UI elements used in Windows applications. Developers of accessibility tools can use this information to create software that makes applications running on Windows more accessible to people with vision, hearing, or motion disabilities.

Both Microsoft Active Accessibility and UI Automation expose the UI object model as a hierarchical tree, rooted at the desktop. Microsoft Active Accessibility represents individual UI elements as *accessible objects*, and UI Automation represents them as *automation elements*. Both refer to the accessibility tool or software automation program as the *client*. However, Microsoft Active Accessibility refers to the application or control offering the UI for accessibility as the *server*, while UI Automation refers to this as the *provider*.

## Properties and Control Patterns

Microsoft Active Accessibility offers a single Component Object Model (COM) interface with a fixed, small set of properties. UI Automation offers a richer set of properties, as well as a set of extended interfaces called *control patterns* to manipulate accessible objects in ways Microsoft Active Accessibility cannot.

For more information, see [UI Automation Properties Overview](uiauto-propertiesoverview.md) and [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).

## MSAA Roles and UI Automation Control Patterns

Microsoft designed the Microsoft Active Accessibility object model at about the same time as Windows 95 was released. The model is based on "roles" defined a decade ago, and you cannot support new UI behaviors or merge two or more roles together. There is no text object model, for example, to help assistive technologies deal with complex web content. UI Automation overcomes these limitations by introducing control patterns that enable objects to support more than one role, and the UI Automation [Text](uiauto-implementingtextandtextrange.md) control pattern offers a full-fledged text object model.

## Object Model Navigation

Another limitation of Microsoft Active Accessibility involves navigating the object model. Microsoft Active Accessibility represents the UI as a hierarchy of accessible objects. Clients navigate from one accessible object to another using interfaces and methods available from the accessible object. Servers can expose the children of an accessible object with properties of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface, or with the standard [IEnumVARIANT](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) COM interface. Clients, however, must be able to deal with both approaches for any server. This ambiguity means extra work for client implementers, and broken accessible object models for server implementers.

UI Automation represents the UI as a hierarchical tree of automation elements, and provides a single interface for navigating the tree. Clients can customize the view of elements in the tree by scoping and filtering.

## Object Model Extensibility

Microsoft Active Accessibility properties and functions cannot be extended without breaking or changing the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) COM interface specification. The result is that new control behavior cannot be exposed through the object model; it tends to be static.

With UI Automation, as new UI elements are created, application developers can introduce custom properties, control patterns, and events to describe the new elements. For more information, see [Custom Properties, Events, and Control Patterns](uiauto-custompropertieseventscontrolpatterns.md).

## Transitioning from MSAA

The Windows Automation API framework provides support for transitioning from Microsoft Active Accessibility servers to UI Automation providers. The [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) interface enables support for specific UI Automation properties and control patterns to be added to legacy Microsoft Active Accessibility servers without needing to rewrite the entire implementation. The **IAccessibleEx** interface also allows in-process Microsoft Active Accessibility clients to access UI Automation provider interfaces directly, rather than through UI Automation client interfaces. For more information, see [The IAccessibleEx Interface](iaccessibleex.md).

## Choosing Microsoft Active Accessibility, UI Automation, or IAccessibleEx

This section helps you determine which Windows Automation API solution to use to implement an assistive technology product or to make your application accessible to assistive technology products.

### New Applications and Controls

If you are developing a new application or control, Microsoft recommends using UI Automation. Although Microsoft Active Accessibility can be easier to implement in the short term, the limitations inherent in this technology, such as its aging object model and inability to support new UI behaviors or merge roles, makes it more difficult and costly over the long term. These limitations become especially apparent when introducing new controls.

The UI Automation object model is easier to use and is more flexible than that of Microsoft Active Accessibility. The UI automation elements reflect the evolution of user interfaces, and developers can define custom UI Automation control patterns, properties, and events.

Microsoft Active Accessibility tends to run slowly for clients that run out of process. To improve performance, developers of accessibility tool programs often choose to hook into and run their programs in the target application process: an extremely difficult and risky approach. UI Automation is much easier to implement for out-of-process clients, and offers much better performance and reliability.

### Existing Microsoft Active Accessibility Implementations

If you are updating an existing application or control that is based on Microsoft Active Accessibility, consider adding support for UI Automation by implementing the [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) interface. First, ensure that your application or control meets the following requirements:

-   The baseline Microsoft Active Accessibility server's hierarchy of accessible objects must be well organized and error free. [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) cannot fix problems with existing accessible object hierarchies.
-   Your [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation must comply with both the Microsoft Active Accessibility specification, and the UI Automation Specification. Microsoft provides a set of tools for validating compliance with both specifications. For more information, see [Testing Tools](testing-tools.md).

If either of these requirements is not met, consider implementing UI Automation natively. You can keep legacy Microsoft Active Accessibility server implementations for backward compatibility if it is necessary. From a UI Automation client perspective, there is no difference between UI Automation providers and Microsoft Active Accessibility servers that implement [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) correctly.

For more information, see [The IAccessibleEx Interface](iaccessibleex.md).

## Related topics

<dl> <dt>

[Windows Automation API Overview](windows-automation-api-overview.md)
</dt> <dt>

[Microsoft Active Accessibility](microsoft-active-accessibility.md)
</dt> <dt>

[UI Automation](entry-uiauto-win32.md)
</dt> <dt>

[The IAccessibleEx Interface](iaccessibleex.md)
</dt> </dl>

 

 