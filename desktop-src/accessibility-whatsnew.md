---
Description: Describes recent innovations and updates to Windows accessibility features, tools, documentation, and samples.
title: What's new in Windows accessibility for developers
ms.topic: article
ms.date: 04/18/2019
---

# New Windows accessibility features, tools, documentation, and samples for developers

The Windows platform is constantly being updated with new accessibility and automation features for developers.

[Install the tools and SDK](https://go.microsoft.com/fwlink/?LinkId=821431) on Windows 10 and you’re ready to either create a new Universal Windows app or explore how you can use your existing app code on Windows.

## What's new for Build 2019

The following features, tools, developer guidance, samples, and videos have been made available for the [Microsoft Build 2019 Developer Conference](https://www.microsoft.com/en-us/build).

## What's new for Windows 10 May 2019 Update (Version 1903)

The following features, tools, developer guidance, samples, and videos have been made available for the [Windows 10 May 2019 Update](https://blogs.windows.com/windowsexperience/2019/04/08/releasing-the-may-2019-update-to-the-release-preview-ring/#oTrOrMWFFgWJuCqO.97).

## What's new for Windows 10 October 2018 Update (Version 1809)

The following features, tools, developer guidance, samples, and videos have been made available for the [Windows 10 October 2018 Update](https://blogs.windows.com/windowsexperience/2018/10/02/how-to-get-the-windows-10-october-2018-update/#R6DJStjqlIkK34BT.97).

| Release | Platform | Feature | Description | Link |
| --- | --- | --- | --- | --- |
| 1809 | Win32 | UI Automation supports Active Text Position Change events | UI Automation providers can explicitly set a starting position within a text range. Assistive technology (AT) clients can then convey this position to a user. For example, if a user clicks a link to an anchor on the same page (a bookmark link), the new location is provided to the AT. | [IUIAutomation6 interface](https://docs.microsoft.com/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomation6) |
| 1809 | Win32 | UI Automation supports event coalescing | Duplicate events are detected and filtered for AT clients. | [IUIAutomation6 interface](https://docs.microsoft.com/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomation6) |
| 1809 | Win32 | UI Automation supports connection recovery behavior | AT clients can adjust provider request timeouts if the provider is non-responsive. | [IUIAutomation6 interface](https://docs.microsoft.com/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomation6) |
| 1809 | UWP | Enhanced screen reader services | AT clients know the audible screen reading location (control or content) and the reading mode. | [ScreenReaderService Class](https://docs.microsoft.com/en-us/uwp/api/windows.ui.accessibility.screenreaderservice) |
| 1809 | Win32, UWP | UI Automation supports dialog windows | UI Automation providers can mark UIA elements specifically as dialog windows. ATs often present dialogs differently to users.  | [ScreenReaderService Class](https://docs.microsoft.com/en-us/uwp/api/windows.ui.accessibility.screenreaderservice) |
