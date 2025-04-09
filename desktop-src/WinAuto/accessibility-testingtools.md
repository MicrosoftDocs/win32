---
description: Overview of how to use UI Automation and other tools to test your apps.
title: Testing for accessibility
ms.topic: concept-article
ms.date: 10/18/2023
---

# Testing for accessibility

Testing the accessibility of your Windows applications, assistive technology (AT) tools, and UI frameworks is crucial to ensuring a successful user experience for people with various disabilities (including vision, learning, dexterity/mobility, and language/communication), situational constraints, or those who simply prefer using a keyboard.

Both programmatic access and keyboard access are crucial for supporting accessibility. You should ensure that your application provides adequate programmatic access to and information about all UI elements, and that all of your application scenarios can be accomplished using only keyboard focus and navigation.

In addition to verifying the programmatic access, some of the tools listed here can also help assess your application's support for keyboard access and navigation. However, it is also important to, when possible, verify your implementation with users of assistive technologies, such as screen readers.

The following describes the various tools that can be used to test the accessibility implementation of both Windows and web applications.

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
