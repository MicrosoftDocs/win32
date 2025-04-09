---
description: Bindlink library.
ms.assetid: d38b3a2b-0526-4ce7-8f18-7b5d845e4d01
title: Bindlink API (bindlink.h)
ms.topic: reference
ms.date: 02/27/2024
---

# Bindlink API

## Purpose

This Bindlink API allows admin users to bind a filesystem namespace to a local "virtual path" via the Bind Filter (mini filter bindflt.sys). Bind links provide file system redirection from a local "virtual path" to a local or remote "backing path". They can primarily enable two kinds of scenarios: first, they can make remote files over a network share appear local which improves app compatibility, and second, they enable scenarios where an application wants files from different locations to  appear in a new location, potentially with different names and directory structures, without copying the files. Bind Links are transparent to applications and all existing APIs work without the knowledge of this redirection. No physical file or directory is created for the virtual path and bind links extend the security descriptors and permissions of the files and directories in the backing path to the virtual path.

## Developer audience

The Bindlink API is designed for use by professional C/C++ developers of Windows applications. Developers can use the API to get information about a hardware device and determine if the machine is eligible to run a specific version of Windows.

## Run-time requirements

The Bindlink API is available beginning with Windows 11, version 10.0.25314.0.

## In this section

- [Bindlink overview](bindlink-overview.md)
- [Bindlink functions](bindlink-api-functions.md)
- [Bindlink enums](bindlink-api-enums.md)
- [Bindlink examples](bindlink-example.md)
