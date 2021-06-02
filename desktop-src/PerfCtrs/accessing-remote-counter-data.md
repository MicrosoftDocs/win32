---
description: To access counter data on a remote computer:The remote computer must have the Remote Registry service enabled.The File and Print Sharing exception must be selected in Windows Firewall Settings.Prior to Windows Vista:  The Remote Registry service is enabled by default.
ms.assetid: 0a6b40b2-6cc7-4bfd-8315-8b5c12954df8
title: Accessing Remote Counter Data
ms.topic: article
ms.date: 08/17/2020
---

# Accessing Remote Counter Data

To access counter data on a remote computer:

- The remote computer must have the Remote Registry service enabled.
- The **File and Print Sharing** exception must be selected in **Windows Firewall Settings**.

**Prior to Windows Vista:** The Remote Registry service is enabled by default.

> [!NOTE]
> Windows Performance Counter APIs and tools include limited support for accessing performance counters from other machines via RPC (for V2 providers) and Remote Registry (for V1 providers). This support is often hard to use in terms of authentication controls (the tools and APIs can only authenticate as the current user) as well as in terms of system configuration (the necessary endpoints and services are disabled by default on most systems). In many cases, it is better to access the performance counters of remote systems via [WMI](/windows/desktop/WmiSdk/monitoring-performance-data) rather than via the built-in remote access support.
