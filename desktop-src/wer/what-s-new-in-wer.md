---
title: Whats New in WER
description: This page summarizes the new features of Windows Error Reporting (WER) for each release.
ms.assetid: 6cdd6c64-ba67-40dc-9942-0371320f1881
keywords:
- Windows error reporting Windows Error Reporting , whats new
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in WER

This page summarizes the new features of Windows Error Reporting (WER) for each release.

## Windows 7 and Windows Server 2008 R2

The following list summarizes the new WER features for Windows 7 and Windows Server 2008 R2.

-   Adds the ability to raise an exception that bypasses all exception handlers thus terminating the application immediately and invoking Windows Error Reporting. For details, see the [**RaiseFailFastException**](https://msdn.microsoft.com/library/windows/desktop/dd941688) function.
-   Adds the ability to register an out-of-process exception handler that WER calls when a crash occurs to collect the event name, reporting parameters, and debug launching options. For details, see the [**WerRegisterRuntimeExceptionModule**](/windows/win32/Werapi/nf-werapi-werregisterruntimeexceptionmodule?branch=master) function.

Functions that were added:

-   [**OutOfProcessExceptionEventCallback**](/windows/win32/Werapi/nc-werapi-pfn_wer_runtime_exception_event?branch=master)
-   [**OutOfProcessExceptionEventSignatureCallback**](/windows/win32/Werapi/nc-werapi-pfn_wer_runtime_exception_event_signature?branch=master)
-   [**OutOfProcessExceptionEventDebuggerLaunchCallback**](/windows/win32/Werapi/nc-werapi-pfn_wer_runtime_exception_debugger_launch?branch=master)
-   [**RaiseFailFastException**](https://msdn.microsoft.com/library/windows/desktop/dd941688)
-   [**WerRegisterRuntimeExceptionModule**](/windows/win32/Werapi/nf-werapi-werregisterruntimeexceptionmodule?branch=master)
-   [**WerUnregisterRuntimeExceptionModule**](/windows/win32/Werapi/nf-werapi-werunregisterruntimeexceptionmodule?branch=master)

Structures that were added:

-   [**WER\_RUNTIME\_EXCEPTION\_INFORMATION**](/windows/win32/Werapi/ns-werapi-_wer_runtime_exception_information?branch=master)

## Windows Server 2008 and Windows Vista SP1

The following list summarizes the new features of WER for Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

-   WER can be configured so that full user-mode dumps are collected and stored locally after a user-mode application crashes (applications that do their own custom crash reporting, including .NET applications are not supported). For more information, see [Collecting User-Mode Dumps](collecting-user-mode-dumps.md).

## Windows Vista

The following list summarizes the new features of Windows Error Reporting (WER) for Windows Vista:

-   WER has been extended beyond monitoring crashes and unresponsive processes. WER includes support for many new types of non-critical events, such as performance issues. This enables developers to learn more about the experiences their customers have with the applications they have developed.
-   New functions give developers the flexibility in creating, customizing, and submitting problem reports. For more information, see [WER Functions](wer-functions.md).
-   The improved [Windows Quality Online Services](Http://go.microsoft.com/fwlink/p/?linkid=84169) provides developers with access to the problem information that customers are submitting for their applications, and a mechanism to deliver solutions to these customers.
-   The functions introduced by [Application Recovery and Restart](https://msdn.microsoft.com/library/windows/desktop/cc948909) and [Restart Manager](https://msdn.microsoft.com/library/windows/desktop/cc948910) enable applications to automatically recover information and restart in the event of a critical failure. Developers can use these features in their applications to significantly improve their user experience.
-   **Problem Reports and Solutions on Windows Vista or the Action Center on Windows 7** is the central location for users to interact with WER. Users can check for new solutions, manage their reporting history, view the details of a problem report, and manage reporting settings including enabling WER to check for solutions automatically without interrupting the user.

## Related topics

<dl> <dt>

[Windows Error Reporting](windows-error-reporting.md)
</dt> </dl>

 

 




