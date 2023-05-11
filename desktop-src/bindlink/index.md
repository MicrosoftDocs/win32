---
description: Bindlink library.
ms.assetid: d38b3a2b-0526-4ce7-8f18-7b5d845e4d01
title: Bindlink API (bindlink.h)
ms.topic: article
ms.date: 05/11/2023
---

# Bindlink API

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these features appear is Windows Insider Preview, version 10.0.25314.0.

## Purpose

This Bindlink library allows admin users to bind a filesystem namespace to a local "virtual path" via the Bind Filter (mini filter bindflt.sys). Bind Links provide file system redirection from a local "virtual path" to a local or remote "backing path". They can primarily enable two kinds of scenarios: first, they can make remote files over a network share appear local which improves app compatibility, and second, they enable scenarios where an application wants files from different locations to  appear in a new location, potentially with different names and directory structures, without copying the files. Bind Links are transparent to applications and all existing APIs work without the knowledge of this redirection. No physical file or directory is created for the virtual path and bind links extend the security descriptors and permissions of the files and directories in the backing path to the virtual path.

## Developer audience

The Bindlink API is designed for use by professional C/C++ developers of Windows applications. Developers can use the API to get information about a hardware device and determine if the machine is eligible to run a specific version of Windows.

## Run-time requirements

The Bindlink API is available beginning with Windows 11, version 10.0.25314.0.

## In this section

- [Bindlink overview](bindlink-overview.md)
- [Bindlink functions](bindlink-api-functions.md)
- [Bindlink enums](bindlink-api-enums.md)
- [Bindlink examples](bindlink-example.md)
