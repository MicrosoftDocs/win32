---
description: Although providers are encouraged to use unique instance names, not all providers do.
ms.assetid: 3c8fcb8d-2ea4-4b24-b649-7bd375c1133d
title: Handling Duplicate Instance Names
ms.topic: article
ms.date: 08/17/2020
---

# Handling Duplicate Instance Names

Although providers are strongly encouraged to use unique instance names, not all providers do. The convention for displaying duplicate instance names is to append a `#` character and a serial number to the instance name, except for the first occurrence of the name. For example, if there are three instances of `svchost` in a sample, the three names are displayed as `svchost`, `svchost#1`, and `svchost#2`.

Unfortunately, this convention does not completely resolve the issue. Serial numbers are assigned based on the order in which a particular instance name appears in a sample, and this order may be inconsistent from sample to sample. For example, sample A might see `svchost` (PID 100), `svchost#1` (PID 200), and `svchost#2` (PID 300). Then if the svchost with PID 100 shuts down, the next sample would see `svchost` (PID 200) and `svchost#1` (PID 300). Basic matching logic would try to match sample A's `svchost#1` statistics (from PID 200) against sample B's `svchost#1` statistics (from PID 300), resulting in invalid results for sample B. Errors occur when a new non-unique instance shows up in a sample or when a non-unique instance stops showing up in a sample (unless the added/removed instance was the last one).

## Process counterset

This issue is especially problematic for the `Process` counterset because it uses only the process's EXE name as the instance name even though the EXE name is not unique. The default behavior of the `Process` counterset on Windows cannot be changed due to compatibility issues.

> [!TIP]
> Windows 10 20H2 and later include the new `Process V2` counterset. The `Process V2` counterset includes the process ID (PID) in the instance name which avoids the name duplication issue of the `Process` counterset.

You can alter the behavior of the `Process` and `Thread` countersets to use unique instance names by setting the `ProcessNameFormat` or `ThreadNameFormat` registry values under the `HKLM\System\CurrentControlSet\Services\Perfproc\Performance` registry key.

> [!CAUTION]
> Enabling unique instance names for the `Process` counterset may cause some programs to behave incorrectly, since many programs expect the non-unique naming pattern. For example, a program that is looking for an instance with a specific well-known EXE name will no longer be able to find that instance after enabling unique instance names.

The registry type for these values is `REG_DWORD`. Setting the value to `2` appends the process identifier (PID) to the process instance name and the thread identifier (TID) to the thread instance name. To disable this feature, set the value to 1 or delete the value.
