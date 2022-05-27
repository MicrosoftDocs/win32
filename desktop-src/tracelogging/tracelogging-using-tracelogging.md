---
title: Using TraceLogging
description:
  The following topics provide a TraceLogging quick start for native and managed
  code, with examples.
ms.assetid: CEC57517-7A0E-45AA-85F7-F358AE51EF4A
ms.topic: article
ms.date: 05/31/2018
---

# Using TraceLogging

The following topics provide a TraceLogging quick start for native and managed
code, with examples.

## Prerequisites

- Windows 10 Software Development Kit (SDK) is required to write a user-mode
  provider
- Windows Driver Kit (WDK) is required to write a kernel-mode provider

## In this section

- [**TraceLogging C/C++ Quick Start**](tracelogging-native-quick-start.md)

  This topic describes the basic steps required to add TraceLogging to native
  user-mode code.

- [**TraceLogging Managed Quick Start**](tracelogging-managed-quick-start.md)

  This topic describes the basic steps required to add TraceLogging to native
  user-mode code.

- [**Record and Display TraceLogging Events**](tracelogging-record-and-display-tracelogging-events.md)

  Record TraceLogging events with the Windows Performance Recorder (WPR) and
  view them with the Windows Performance Analyzer (WPA).

- [**C/C++ Tracelogging Examples**](tracelogging-c-cpp-tracelogging-examples.md)

  This topic contains C/C++ Tracelogging examples.

- [**.NET Tracelogging Examples**](tracelogging-net-examples.md)

  This topic contains a managed code Tracelogging example that illustrates how
  to log an event only when the session verbosity level is verbose, and how to
  log structured event data.

- [**Universal Windows Platform Logging Example**](universal-windows-platform-logging-examples.md)

  This sample shows how to use the Logging APIs in the
  Windows.Foundation.Diagnostics namespace, including LoggingChannel,
  LoggingActivity, LoggingSession, and FileLoggingSession. These classes are
  designed for diagnostic logging within a Windows app. These APIs were added in
  Windows 8.1.

  The LoggingChannel and LoggingActivity APIs have been extended in Windows 10
  to support writing complex events using TraceLogging event encoding.

  The Universal Windows Platform logging example can downloaded from
  [GitHub](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/Logging).

## Related topics

[TraceLogging for kernel-mode drivers and components](/windows-hardware/drivers/devtest/tracelogging-for-kernel-mode-drivers-and-components)
