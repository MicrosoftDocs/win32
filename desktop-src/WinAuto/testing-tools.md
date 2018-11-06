---
title: Testing Tools
description: Describes tools for testing the accessibility implementation of your application to ensure that the UI is fully accessible to client applications, and to users who access your application though the keyboard.
ms.assetid: abacbec4-6ccd-4853-afcd-a92a6656f393
keywords:
- accessibility testing tools
- testing tools,accessibility
- accessibility testing
- UIA
- MSAA
ms.topic: article
ms.date: 05/31/2018
---

# Testing Tools

Programmatic access and keyboard access to your application are two critical requirements for accessibility. Without adequate access, many users of assistive technology (AT), such as screen reader and on-screen keyboard users, would be unable to use your application. It is important to thoroughly test your application to ensure that it provides adequate information about its UI elements, and that all of your application scenarios can be accomplished with only the keyboard.

This section describes tools for testing the accessibility implementation of your application to ensure that the UI is fully accessible to client applications, and to users who access your application though the keyboard. It describes the available tools for testing Microsoft UI Automation (UIA) and Microsoft Active Accessibility (MSAA) implementations.

In addition to verifying the programmatic access, some of the tools can help you assess the implementation of your application's keyboard access. However, tools alone are not enough. It is important to manually verify that all scenarios can be accomplished with only the keyboard.

For programmatic and keyboard requirements, there is no one tool that can verify your full implementation. Try to use a variety of tools to verify your implementation and, when possible, find users of assistive technologies, such as screen readers, to use your UI.

> [!Note]  
> The **Accessible Explorer** and **UI Spy** tools are obsolete and no longer available. Developers should use [**Inspect**](inspect-objects.md) or [**AccScope**](accscope.md) instead.

 

### In this section

The Windows SDK contains several tools that are useful to help create accessible products and services. These tools include the following:

-   [**Accessible Event Watcher**](accessible-event-watcher.md): The Accessible Event Watcher (AccEvent) tool examines accessibility data to help validate application UI elements, to ensure the UI elements raise proper Microsoft Active Accessibility and UI Automation events when UI changes occur. AccEvent is usually used to debug issues and to validate that custom and extended controls are working correctly.

-   [**Inspect**](inspect-objects.md): Inspect allows you to view the accessibility data in any UI element. It is especially useful, when extending a common control or creating a custom control, to ensure properties and control patterns are set correctly.

-   [**AccScope**](accscope.md): The AccScope tool allows developers to visually evaluate the accessibility of their application during the early design and development phases. AccScope helps visualize how a screen reader uses UI Automation information that an app provides. It can show areas where adding information or support to your application can improve its accessibility.

-   [**UI Accessibility Checker**](ui-accessibility-checker.md): The UI Accessibility Checker (AccChecker) tool verifies that key UI accessibility requirements are met. AccChecker includes verification checks for UI Automation, Microsoft Active Accessibility, and Accessible Rich Internet Applications (ARIA). It can provide a static check looking for errors such as missing names, tree issues and more. It helps verify programmatic access and has advanced features to support automating accessibility testing.

-   [**UI Automation Verify**](ui-automation-verify.md): UI Automation Verify (UIA Verify) is a testing framework for manual and automated testing of a control's or application's implementation of UI Automation. It can also log the test results. You can integrate your application into the test code and conduct regular, automated testing or spot checks of your UI Automation scenarios. This tool is useful to verify that changes to applications with established features do not have new issues or regressions in areas beyond the new features.

## Related topics

<dl> <dt>

[Accessibility Developer Hub](https://developer.microsoft.com/windows/accessible-apps)
</dt> <dt>

[Microsoft accessibility](http://go.microsoft.com/fwlink/p/?LinkId=320802)
</dt> </dl>

 

 




