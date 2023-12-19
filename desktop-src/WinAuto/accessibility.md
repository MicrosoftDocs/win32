---
description: The Windows accessibility and automation documentation provides information for developers seeking to create and test accessible Windows apps that can be used by as many people as possible, including those with impairments or disabilities.
title: Accessible Windows apps
ms.topic: reference
ms.date: 10/17/2023
---

# Accessibility and automation for Windows developers

This topic provides links to documentation for Windows developers designing accessible applications, assistive technology developers building tools such as screen readers and magnifiers, and software test engineers creating automated scripts for testing Windows applications.

## Resources

The resources provided here can help you build Windows applications for as many people as possible, including those with disabilities, personal preferences, environmental considerations, and specific work styles.

:::row:::
    :::column span="2":::
        ### Accessibility and automation frameworks overview

        Windows accessibility and automation consist of two technologies—Microsoft Active Accessibility (MSAA) and Microsoft UI Automation. MSAA is a legacy technology introduced with Windows 95, while UI Automation is a newer, more capable technology that addresses the limitations of MSAA.

        - [Microsoft Active Accessibility and UI Automation Compared](/windows/desktop/winauto/microsoft-active-accessibility-and-ui-automation-compared)
        - [Microsoft Active Accessibility](/windows/desktop/winauto/microsoft-active-accessibility)
    :::column-end:::
:::row-end:::
:::row:::
    :::column:::
        ### Develop accessible applications for Windows

        Windows application frameworks support numerous accessibility features that you can incorporate into your application.

        - [Win32 apps](/windows/win32/winauto/windows-automation-api-portal)
        - [UWP apps](/windows/uwp/design/accessibility/accessibility)
        - [WinForms apps](/dotnet/framework/winforms/advanced/windows-forms-accessibility)
        - [WPF apps](/dotnet/framework/ui-automation/)        
        - [Web applications](/microsoft-edge/accessibility)
    :::column-end:::
    :::column:::
        ### Develop accessible UI frameworks for Windows

        UI frameworks built for the Windows platform should always support programmatic access and automation, keyboard navigation and commanding, color and theme options, and personalization through user settings.

        - [UI Automation for Win32](/windows/desktop/winauto/entry-uiauto-win32)
        - [Keyboard accessibility](/previous-versions/windows/desktop/dnacc/guidelines-for-keyboard-user-interface-design)
        - [Respecting High Contrast](/windows/desktop/w8cookbook/high-contrast-mode)
        - [User settings](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa)
        - [User settings blog post](https://devblogs.microsoft.com/oldnewthing/?p=36243)
    :::column-end:::
:::row-end:::
:::row:::
    :::column:::
        ### Develop assistive technology for Windows

        Build screen readers, magnifiers, speech recognizers, eye trackers, and other specialty hardware compatible with Microsoft products for people with vision, dexterity/mobility, learning, and language/communication disabilities.

        - [UI Automation for Win32](/windows/desktop/winauto/entry-uiauto-win32)
        - [UI Automation for .NET Framework](/dotnet/framework/ui-automation/ui-automation-overview)
        - [Security Considerations for Assistive Technologies](../winauto/uiauto-securityoverview.md)
        - [Ease of Access Assistive Technology Registration](/windows/desktop/winauto/ease-of-access---assistive-technology-registration)
        - [Magnification API](/previous-versions/windows/desktop/magapi/entry-magapi-sdk)
    :::column-end:::
    :::column:::
        ### Test for accessibility

        Testing the accessibility of your Windows applications, assistive technology (AT) tools, and UI frameworks ensures that your application provides adequate programmatic access to and information about all UI elements, and that all of your application scenarios can be accomplished using only keyboard focus and navigation.

        - [Test for accessibility](accessibility-testingtools.md)
    :::column-end:::
:::row-end:::
:::row:::
    :::column:::
        ### Security considerations for assistive technologies

        Assistive technology applications typically need access to protected system UI elements, or other processes that might be running at a higher privilege level, and must run with special privileges to be trusted by the system.

        - [Security Considerations for Assistive Technologies](uiauto-securityoverview.md)
    :::column-end:::
    :::column:::
        ### Accessibility best practices

        Accessibility best practices focus on UI design and implementation details for controls and applications.
        
        - [Accessibility best practices](accessibility-best-practices.md)
    :::column-end:::
:::row-end:::
:::row:::
    :::column span="2":::
        ### Accessibility settings

        Each accessibility parameter and each built-in accessibility feature corresponds to a system parameter that can be set or queried with the <a href="/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa">SystemParametersInfo</a> function.

        There are two types of settings available to users (through the Ease of Access Center in Control Panel) that are also exposed to developers.
        - [Accessibility parameters](accessibility-parameters.md). When set, these parameters indicate that applications should change their default behavior. Applications can check the state of an accessibility parameter to determine whether the user wants special behavior that can be provided in an application-specific manner. For example, the ShowSounds parameter indicates that an application that typically uses sound to convey important information should also provide the information visually.
        - [Built-in Accessibility Features](built-in-accessibility-features.md). These features are built into the system or are provided as an extension to the system. They affect how the user provides keyboard and mouse input to the computer. When enabled, their functionality is available regardless of which applications are running. An example is a keyboard filter that makes it easier for users with movement impairments to type key combinations such as CTRL+ALT+DEL.
    :::column-end:::
:::row-end:::

## Related topics

- [UI Automation WPF Framework Implementation sample](https://github.com/Microsoft/WPF-Samples/tree/main/Accessibility)
- [UI contrast and settings sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Windows%208%20app%20samples/%5BC%2B%2B%5D-Windows%208%20app%20samples/C%2B%2B/Windows%208%20app%20samples/UI%20contrast%20and%20settings%20sample%20(Windows%208))
