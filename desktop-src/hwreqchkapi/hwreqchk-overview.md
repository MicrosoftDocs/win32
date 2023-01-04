---
description: The HWREQCHK API coordinates execution of deferrable tasks, called activities, on a Windows system.
ms.assetid: f2bb0996-a864-41db-ba40-820aaf4e09d6
title: Overview of the HWREQCHK API
ms.topic: article
ms.date: 01/04/2023
---

# Overview of the HWREQCHK API

The **hardware requirement evaluator (HWREQCHK)** library is a set of APIs that allows developers to get information about a hardware device and determine if the machine is eligible to run a specific version of Windows 11 or later.

The API queries various hardware properties and evaluates rules to determine eligibility.

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

[HWREQCHK API examples](hwreqchk-examples.md)
