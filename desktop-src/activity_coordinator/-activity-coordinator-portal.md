---
description: Activity Coordinator API
ms.assetid: 5edef7eb-d32e-4dea-8967-e8a1709d9be4
title: Activity Coordinator API
ms.topic: article
ms.date: 04/27/2022
---

# Activity Coordinator API

## Purpose

The Activity Coordinator API coordinates execution of deferrable tasks on a system. Deferrable tasks are those tasks which don’t need to be run immediately. They can defer their execution to a time when the system is in a desired state where running the task does not interfere with other ongoing work.

## Developer audience

The Activity Coordinator API is designed for use by professional C/C++ developers of Windows applications. Developers can use the API to get notifications of when the system is in the desired state to run a particular task. This feature is 64-bit on 64-bit Windows and 32-bit on 32-bit Windows.

## Run-time requirements

The Activity Coordinator API is available beginning with the Windows 11 version xxx. **TODO - Get version info.**

## In this section

- [Activity Coordinator API Overview](activity-coordinator-api-overview.md)
- [Activity Coordinator API Functions](activity-coordinator-api-functions.md)
- [Activity Coordinator API Enumerations](activity-coordinator-api-enumerations.md)
