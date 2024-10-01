---
title: Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler module
description: This module contains the cmdlets that are installed with the Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler PowerShell module.
ms.topic: article
ms.date: 08/27/2024
---

# Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler Module

This section contains information about the cmdlets that are installed with **Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler** PowerShell module. These cmdlets enable access attempt profiling for an application package in order to identify what access capabilities should be declared the in application package manifest.

## Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler Cmdlets

The following App Isolation profiling cmdlets are included with this module:

| Cmdlet | Description |
|--------|-------------|
| [Get-ProfilingResults](Get-ProfilingResults.md) | Retrieves capability access information from input ETL files. |
| [Merge-ProfilingResults](Merge-ProfilingResults.md) | Merges multiple **Get-ProfilingResults** output files into a single output file. |
| [Start-Profiling](Start-Profiling.md) | Initiates access attempt profiling for a specified application package. |
| [Stop-Profiling](Stop-Profiling.md) | Stops access attempt profiling for a specified application package. |

## Related topics

[Application capability profiler](../app-isolation-capability-profiler.md)
