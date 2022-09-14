---
description: Describes recent innovations and updates to Windows accessibility features, tools, documentation, and samples.
title: What's new in Windows accessibility for developers
ms.topic: article
ms.date: 04/18/2019
---

# New Windows accessibility features, tools, documentation, and samples for developers

The Windows platform is constantly being updated with new accessibility and automation features for developers.

[Install the tools and SDK](https://developer.microsoft.com/windows/downloads/#_blank) on Windows 10 and you’re ready to either create a new Universal Windows app or explore how you can use your existing app code on Windows.

For more info on the latest tools available for testing the accessibility implementation of your Windows and web applications, see [Testing for accessibility](accessibility-testwithuia.md).

## What's new for Windows 10 May 2019 Update (Version 1903)

The following features, tools, developer guidance, samples, and videos have been made available for the [Windows 10 May 2019 Update](https://blogs.windows.com/windowsexperience/2019/04/08/releasing-the-may-2019-update-to-the-release-preview-ring/#oTrOrMWFFgWJuCqO.97).

| Release | Platform | Feature | Description | Link |
| --- | --- | --- | --- | --- |
| 1903 | Win32 | UI Automation supports IAccessible2 | UI Automation clients can now seamlessly access information from IAccessible2 providers such as the Chrome browser. | n/a |
| 1903 | UWP | Scrollbar visibility  | Scroll bars automatically hidden when not being interacted with. | [UISettings.AutoHideScrollBars Property](/uwp/api/windows.ui.viewmanagement.uisettings.autohidescrollbars) |
| 1903 | Win32 | UI Automation supports structured markup | Intended, but not limited to, MathML parsing. | n/a |

## What's new for Windows 10 October 2018 Update (Version 1809)

The following features, tools, developer guidance, samples, and videos have been made available for the [Windows 10 October 2018 Update](https://blogs.windows.com/windowsexperience/2018/10/02/how-to-get-the-windows-10-october-2018-update/#R6DJStjqlIkK34BT.97).

| Release | Platform | Feature | Description | Link |
| --- | --- | --- | --- | --- |
| 1809 | Win32 | UI Automation supports Active Text Position Change events | UI Automation providers can explicitly set a starting position within a text range. Assistive technology (AT) clients can then convey this position to a user. For example, if a user clicks a link to an anchor on the same page (a bookmark link), the new location is provided to the AT. | [IUIAutomation6 interface](/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomation6) |
| 1809 | Win32 | UI Automation supports event coalescing | Improves performance by attempting to detect, filter, and ignore duplicate sequential MSAA and UIA TextChanged events raised by some providers. | [IUIAutomation6 interface](/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomation6) |
| 1809 | Win32 | UI Automation supports connection recovery behavior | Messages from a UI Automation client to a provider are suspended (for two seconds, by default) if the provider is non-responsive. This reduces the frequency of extended timeouts, and minimizes flooding a non-responsive provider with events and requests. | [IUIAutomation6 interface](/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomation6) |
| 1809 | UWP | Enhanced screen reader services | AT clients know the audible screen reading location (control or content) and the reading mode. | [ScreenReaderService Class](/uwp/api/windows.ui.accessibility.screenreaderservice) |
| 1809 | Win32, UWP | UI Automation supports dialog windows | UI Automation providers can mark UIA elements specifically as dialog windows. ATs often present dialogs differently to users. | [IUIAutomationElement9](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement9)<br/><br/>[ContentDialog Class](/uwp/api/windows.ui.xaml.controls.contentdialog) |
| 1809 |  UWP | Text scaling  | Scales text size in applications and web pages. | [UISettings.TextScaleFactorChanged Event](/uwp/api/windows.ui.viewmanagement.uisettings.textscalefactorchanged)<br/><br/>[Text scaling](/windows/uwp/design/input/text-scaling) |
