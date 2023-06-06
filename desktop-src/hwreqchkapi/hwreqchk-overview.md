---
description: The HWREQCHK API coordinates execution of deferrable tasks, called activities, on a Windows system.
ms.assetid: f2bb0996-a864-41db-ba40-820aaf4e09d6
title: Overview of the HWREQCHK API
ms.topic: article
ms.date: 01/04/2023
---

# Overview of the HWREQCHK API

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these features appear is Windows Insider Preview, version 10.0.25289.

The **Hardware Requirement Evaluator (HWREQCHK)** library is a set of APIs that allows developers to get information about a hardware device and determine if the machine is eligible to run a specific version of Windows 11 or later. These APIs are a family of APIs used to evaluate a machine/device against the new Windows 11 hardware requirements. It can also be used to determine which of the requirements are not met and what the machine’s hardware is currently.

## Usage

The set of APIs is comprised of 4 related APIs:

- **GetHardwareRequirementSystemInfo** – This function returns the actual hardware device system information (**HWREQCHK_DEVICE_HARDWARE_SYSINFO**) that is used to evaluate and compare against a given hardware requirement.
- **EvaluateHardwareRequirement** – This function evaluates a specific **HWREQCHK_DEVICE_HARDWARE_REQUIREMENT** and returns a **BOOL** pass or fail result informing the caller whether the device meets the hardware requirement or not.
- **GetLatestHardwareRequirement** – This function returns the latest defined requirement for a given **HWREQCHK_PRODUCT_TYPE**.
- **GetHardwareRequirements** – This function returns a collection of defined hardware requirements (**HWREQCHK_DEVICE_HARDWARE_REQUIREMENT**) for all product types.

For sample usage of these functions, see [HWREQCHK API examples](hwreqchk-examples.md).

## Related topics

[HWREQCHK API functions](hwreqchk-api-functions.md)

[HWREQCHK API structures](hwreqchk-api-structures.md)

[HWREQCHK API enums](hwreqchk-api-enums.md)

[HWREQCHK API examples](hwreqchk-examples.md)
