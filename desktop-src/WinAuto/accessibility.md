---
description: The Windows accessibility and automation documentation provides information for developers seeking to create and test accessible Windows apps that can be used by as many people as possible, including those with impairments or disabilities.
title: Accessible Windows apps
ms.topic: reference
ms.date: 10/17/2023
---

# Accessibility and automation for Windows developers

This section contains documentation for Windows developers designing accessible applications, assistive technology developers building tools such as screen readers and magnifiers, and software test engineers creating automated scripts for testing Windows applications.

The resources provided here can help you build Windows applications for as many people as possible, including those with disabilities, personal preferences, environmental considerations, and specific work styles.

## In this section

<table>
    <tr>
        <th>Topic</th>
        <th>Description</th>
    </tr>
        <td><a href="accessibility-appdev.md">Developing accessible applications for Windows</a></td>
        <td>Each Windows application framework supports numerous accessibility features that make it easier for users with disabilities, personal preferences, or specific work styles to successfully use any Windows device they choose</td>
    <tr>
        <td><a href="accessibility-uiframeworkdev.md">Developing accessible UI frameworks for Windows</a></td>
        <td>To be usable by as many people as possible, UI frameworks built for the Windows platform should support accessibility features that make it easier for those with disabilities, personal preferences, or specific work styles to use their Windows devices successfully.</td>
    </tr>
    <tr>
        <td><a href="accessibility-atdev.md">Developing assistive technology for Windows</a></td>
        <td>Third-party assistive technology products—such as screen readers, magnifiers and specialty hardware—are essential tools for many users of Windows (and other Microsoft products).</td>
    </tr>
    <tr>
        <td><a href="accessibility-testwithuia.md">Testing with UI Automation and other tools</a></td>
        <td>Testing the accessibility of your Windows applications, assistive technology tools, and UI frameworks is a critical step in ensuring successful user experiences for people with disabilities and other limitations, as well as users who prefer keyboard interactions.</td>
    </tr>
    <tr>
        <td><a href="uiauto-securityoverview.md">Security considerations for assistive technologies</a></td>
        <td>Assistive technology applications typically need access to the protected system UI elements, or to other processes that might be running at a higher privilege level. Therefore, assistive technology applications must be trusted by the system, and must run with special privileges.</td>
    </tr>
    <tr>
        <td valign="top">Accessibility settings<p>Each accessibility parameter and each built-in accessibility feature corresponds to a system parameter that can be set or queried with the <a href="/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa">SystemParametersInfo</a> function.
</td>
        <td>There are two types of settings available to users (through the Ease of Access Center in Control Panel) that are also exposed to developers.
        <ul><li><a href="accessibility-parameters.md">Accessibility parameters</a>. When set, these parameters indicate that applications should change their default behavior. Applications can check the state of an accessibility parameter to determine whether the user wants special behavior that can be provided in an application-specific manner. For example, the ShowSounds parameter indicates that an application that typically uses sound to convey important information should also provide the information visually.</li>
        <li><a href="built-in-accessibility-features.md">Built-in accessibility features</a>. These features are built into the system or are provided as an extension to the system. They affect how the user provides keyboard and mouse input to the computer. When enabled, their functionality is available regardless of which applications are running. An example is a keyboard filter that makes it easier for users with movement impairments to type key combinations such as CTRL+ALT+DEL.</li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><a href="accessibility-legacy.md">Legacy accessibility and automation technology - MSAA to UI Automation</a></td>
        <td>Windows accessibility and automation consist of two technologies—Microsoft Active Accessibility (MSAA) and Microsoft UI Automation. MSAA is a legacy technology introduced with Windows 95, while UI Automation is a newer, more capable technology that addresses the limitations of MSAA.</td>
    </tr>
</table>

## Related topics
