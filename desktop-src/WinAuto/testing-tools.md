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

Programmatic access and keyboard access are critical requirements for supporting accessibility in your application. Without adequate access, many users of assistive technology (AT), such as screen reader and on-screen keyboard users, would be unable to use your application. Ensure that you thoroughly test the accessibility implementation of your application to confirm that it provides adequate information about its UI elements, and that all of your application scenarios can be accomplished with only the keyboard.

In addition to verifying the programmatic access, some of the tools can help you assess the implementation of your application's keyboard access. However, tools alone are not enough. It is important to manually verify that all scenarios can be accomplished with only the keyboard.

For programmatic and keyboard requirements, there is no one tool that can verify your full implementation. Try to use a variety of tools to verify your implementation and, when possible, find users of assistive technologies, such as screen readers, to use your UI.

This section describes the available tools for testing Microsoft UI Automation (UIA) and Microsoft Active Accessibility (MSAA) implementations.

## Tools

[Accessibility Insights](https://accessibilityinsights.io/) - Helps developers find and fix accessibility issues in both websites and Windows applications.

- [Accessibility Insights for Web](https://accessibilityinsights.io/docs/web/overview) is an extension for Chrome and [Microsoft Edge Insider](https://www.microsoftedgeinsider.com) that helps developers find and fix accessibility issues in web apps and sites. It supports two primary scenarios:
  - **FastPass** - a lightweight, two-step process that helps developers identify common, high-impact accessibility issues in less than five minutes.  
  - **Assessment** - lets anyone verify that a web site is 100% compliant with accessibility standards and guidelines. [Accessibility Insights](https://accessibilityinsights.io/) also lets you review UI Automation elements, properties, control patterns, and events (similar to the [Inspect](/windows/desktop/winauto/inspect-objects) and [AccEvent](/windows/desktop/winauto/accessible-event-watcher) legacy tools described in the following section).

- [Accessibility Insights for Windows](https://accessibilityinsights.io/docs/windows/overview) helps developers find and fix accessibility issues in Windows apps. The tool supports three primary scenarios:
  - **Live Inspect** lets developers verify that an element in an app has the right UI Automation properties simply by hovering over the element or setting keyboard focus on it.
  - **FastPass** - a lightweight, two-step process that helps developers identify common, high-impact accessibility issues in less than five minutes.
  - **Troubleshooting** allows you to diagnose and fix specific accessibility issues.

### Legacy testing tools

The following tools are still available in the Windows SDK and are documented here for continued support, but we recommend transitioning to [Accessibility Insights](https://accessibilityinsights.io/).

- [**Accessible Event Watcher**](accessible-event-watcher.md): The Accessible Event Watcher (AccEvent) tool examines accessibility data to help validate application UI elements, to ensure the UI elements raise proper Microsoft Active Accessibility and UI Automation events when UI changes occur. AccEvent is usually used to debug issues and to validate that custom and extended controls are working correctly.

- [**Inspect**](inspect-objects.md): Inspect allows you to view the accessibility data in any UI element. It is especially useful, when extending a common control or creating a custom control, to ensure properties and control patterns are set correctly.

- [**AccScope**](accscope.md): The AccScope tool allows developers to visually evaluate the accessibility of their application during the early design and development phases. AccScope helps visualize how a screen reader uses UI Automation information that an app provides. It can show areas where adding information or support to your application can improve its accessibility.

- [**UI Accessibility Checker**](ui-accessibility-checker.md): The UI Accessibility Checker (AccChecker) tool verifies that key UI accessibility requirements are met. AccChecker includes verification checks for UI Automation, Microsoft Active Accessibility, and Accessible Rich Internet Applications (ARIA). It can provide a static check looking for errors such as missing names, tree issues and more. It helps verify programmatic access and has advanced features to support automating accessibility testing.

- [**UI Automation Verify**](ui-automation-verify.md): UI Automation Verify (UIA Verify) is a testing framework for manual and automated testing of a control's or application's implementation of UI Automation. It can also log the test results. You can integrate your application into the test code and conduct regular, automated testing or spot checks of your UI Automation scenarios. This tool is useful to verify that changes to applications with established features do not have new issues or regressions in areas beyond the new features.

### Obsolete tools

The **Accessible Explorer** and **UI Spy** tools are obsolete and no longer available. Use [**Inspect**](inspect-objects.md) or [**AccScope**](accscope.md) instead.

## Related topics

- [Accessibility Developer Hub](https://developer.microsoft.com/windows/accessible-apps)
- [Microsoft accessibility](https://www.microsoft.com/accessibility/)