---
title: UI Automation Verify (UIA Verify)
description: UI Automation Verify (UIA Verify) is a testing framework for manual and automated testing of a control's or application's implementation of Microsoft UI Automation.
ms.assetid: C66AF411-2746-4695-A893-1552B3ED1066
keywords:
- UI Automation Verify
- UIA Verify
- UI Automation implementation,testing
- testing UI Automation
- UIA testing tools
- UI Automation testing tools
ms.topic: article
ms.date: 05/31/2018
---

# Accessibility tools - UI Automation Verify (UIA Verify)

**UI Automation Verify (UIA Verify)** is a testing framework for manual and automated testing of a control's or application's implementation of Microsoft UI Automation. Most of the testing framework's functionality comes from a DLL called WUIATestLibrary.dll. This DLL contains the code for testing specific UI Automation functionality, and it also supports logging of the test results. You can integrate your application into the test code and conduct regular, automated testing or spot checks of your UI Automation scenarios.

**UIA Verify** is installed with the Windows Software Development Kit (SDK). It is located in the \\bin\\<*version*>\\<*platform*>\\UIAVerify folder of the SDK installation path (VisualUIAVerifyNative.exe).

**UIA Verify** consists of an API called the UI Automation Test Library, and a GUI interface called Visual **UI Automation Verify**. These are described in the following topics.

> [!NOTE]
> **UI Automation Verify** is a legacy tool. We recommend using [Accessibility Insights](https://accessibilityinsights.io/) instead.

## Requirements

UI Automation must be present on the system. For more information, see the "Requirements" section of [UI Automation](entry-uiauto-win32.md).

**UIA Verify** is installed as part of the overall set of tools in the Windows SDK, it is not distributed as a separate download. The Windows SDK includes all of the accessibility-related tools documented in this section. [Get the Windows SDK.](https://developer.microsoft.com/) (There's also an SDK download archive linked from that page, if you need a previous version.)

To run **UIA Verify** as a visual tool, find VisualUIAVerifyNative.exe in the \\bin\\<*platform*>\\UIAVerify folder and run it (you don't typically have to run as administrator). For more information, see [Visual UI Automation Verify](visual-ui-automation-verify.md). To use the libraries, see [UI Automation Test Library](ui-automation-test-library.md).

## Related topics

<dl> <dt>

[Accessible Event Watcher](accessible-event-watcher.md)
</dt> <dt>

[Inspect](inspect-objects.md)
</dt> <dt>

[Testing Tools](testing-tools.md)
</dt> <dt>

[UI Accessibility Checker](ui-accessibility-checker.md)
</dt> </dl>

 

 




