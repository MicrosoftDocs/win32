---
description: The Cloud Filter API provides functionality at the boundary between the user mode and the file system.
ms.assetid: 72bc3e80-babd-4a39-842c-38afe4773a5e
title: Cloud Sync Engines
ms.topic: article
ms.date: 02/06/2019
ms.custom: project-verbatim
---

# Cloud Sync Engines

Also see [Cloud Mirror sample](/windows/win32/cfapi/build-a-cloud-file-sync-engine#cloud-mirror-sample).

Starting in Windows 10, version 1709, Windows provides the *cloud files API*. This API consists of several native Win32 and WinRT APIs that formalize support for cloud sync engines, and handles tasks such as creating and managing placeholder files and directories. Users of this API are typically sync providers and to some extent, Windows applications.

## In this section

| Topic                                                                | Description                                                                                        |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Build a Cloud Sync Engine that Supports Placeholder Files](build-a-cloud-file-sync-engine.md)<br/> | Learn how to use the cloud files API to build a cloud file sync engine that includes placeholder files and File Explorer integration. <br/> |
| [Cloud Filter Reference](cloud-filter-reference.md)<br/> | The cloud filter API is a native Win32 API that is part of the broader cloud files API. The cloud filter API provides functionality at the boundary between the user mode and the file system. This API handles the creation and management of placeholder files and directories. <br/> |

