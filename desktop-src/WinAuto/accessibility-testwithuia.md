---
description: Overview of how to use UI Automation and other tools to test your apps.
title: Testing for accessibility
ms.topic: article
ms.date: 04/18/2019
---

# Testing for accessibility

Programmatic access and keyboard access are critical requirements for supporting accessibility in your application. Testing the accessibility of your Windows applications, assistive technology (AT) tools, and UI frameworks is crucial to ensure a successful user experience for people with various disabilities and limitations (including vision, learning, dexterity/mobility, and language/communication disabilities), or those who simply prefer using a keyboard.

Without adequate access through AT such as screen-readers and on-screen keyboards, users with vision, learning, dexterity/mobility, and language/communication disabilities or limitations (and users who just prefer using the keyboard) would be unable to use your application.

This section describes the various tools that can be used to test the accessibility implementation of both Windows and web applications.

> [!NOTE]
> It is also important to do manual testing to verify keyboard access to your application.

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

- [Inspect](/windows/desktop/winauto/inspect-objects): Lets you view the accessibility data of any UI element. It is especially useful for ensuring properties and control patterns are set correctly when extending a common control or creating a custom control.
- [Accessible Event Watcher (AccEvent)](/windows/desktop/winauto/accessible-event-watcher): Examines accessibility data to validate application UI elements and ensure UI elements raise proper Microsoft Active Accessibility and UI Automation events on UI events. AccEvent is typically used to debug issues and to validate that custom and extended controls are working correctly.
- [AccScope](/windows/desktop/winauto/accscope): Enables visual evaluation of an application's accessibility during the early design and development phases. AccScope helps visualize how a screen reader uses UI Automation information provided by an app, and shows where adding information or support to your application can improve its accessibility.
- [UI Accessibility Checker](/windows/desktop/winauto/ui-accessibility-checker): Verifies that key UI accessibility requirements in an application are achieved. AccChecker includes verification checks for UI Automation, Microsoft Active Accessibility, and Accessible Rich Internet Applications (ARIA). It can provide a static check for errors such as missing names, tree issues and more. It helps verify programmatic access and includes advanced features for automating accessibility testing.
- [UI Automation Verify](/windows/desktop/winauto/ui-automation-verify): A framework for manual and automated testing of the UI Automation implementation in a control or application (results can be logged). You can integrate your application into the test code and conduct regular, automated testing or spot checks of your UI Automation scenarios. This tool is useful for verifying that changes to applications with established features do not have new issues or regressions in areas beyond the new features.
