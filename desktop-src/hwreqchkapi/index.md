---
description: Hardware Requirement Evaluator (HWREQCHK) library
ms.assetid: b4eb3f60-a13a-4b91-b9f0-bd6b160e24d2
title: HWREQCHK API
ms.topic: article
ms.date: 01/04/2023
---

# HWREQCHK API

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these features appear is Windows Insider Preview, version 10.0.25289.

## Purpose

The **Hardware Requirement Evaluator (HWREQCHK)** library is a set of APIs that allows callers to get information about a hardware device and determine if the machine is eligible to run a specific version of Windows 11 (and new versions of the OS as they become available). The API queries various hardware properties and evaluates rules to determine eligibility.

## Developer audience

The HWREQCHK API is designed for use by professional C/C++ developers of Windows applications. Developers can use the API to get information about a hardware device and determine if the machine is eligible to run a specific version of Windows.

## Run-time requirements

The HWREQCHK API is available beginning with Windows 10, version xxxx and Windows 11, version xxxx.

## In this section

- [HWREQCHK overview](hwreqchk-overview.md)
- [HWREQCHK API functions](hwreqchk-api-functions.md)
- [HWREQCHK API structures](hwreqchk-api-structures.md)
- [HWREQCHK API enums](hwreqchk-api-enums.md)
- [HWREQCHK examples](hwreqchk-examples.md)
