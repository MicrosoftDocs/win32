---
title: Stop-Profiling cmdlet
description: Stops access attempt profiling for a specified application package.
ms.topic: reference
ms.date: 08/27/2024
---

# Stop-Profiling

The **Stop-Profiling** cmdlet is used to stop access attempt profiling for a specified application package. The cmdlet stops an active trace logging session started via [Start-Profiling](Start-Profiling.md), collects the resulting Event Trace Log (ETL) file, and takes away access attempt trace logging instrumentation from all currently instrumented packages.

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

> [!NOTE]
> **Stop-Profiling** requires administrator privileges and that Developer Mode be enabled in Windows settings. See [Enable your device for development](/windows/apps/get-started/enable-your-device-for-development) for more information.

Module Name: [Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler](Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)

## Syntax

```powershell
Stop-Profiling [[-TracePath] <string>] [-PackageFullName <string>] [-ManifestPath <string>] [-Quiet] [-WhatIf]
[-Confirm] [<CommonParameters>]
```

## Parameters

### -TracePath

Specifies the path where the collected Event Trace Log should be saved.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: t, Trace

Required: False
Position: Named
Default value: <working directory>\trace.etl
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManifestPath

Specifies the path to the manifest file of the application package from which to take away access attempt logging instrumentation. This parameter supersedes `-PackageFullName`. Avoid using this parameter unless individual packages must have instrumentation taken away.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: m, Manifest

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageFullName

This parameter is superseded by `-ManifestPath`. Specifies the full name of the application package from which to take away access attempt logging instrumentation. Avoid using this parameter unless individual packages must have instrumentation taken away. This value can be obtained via [Get-AppxPackage](/powershell/module/appx/get-appxpackage). See [ApplicationCapabilityProfiler](../app-isolation-capability-profiler.md) for details.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: p, PackageName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignedFilePath

This **optional** parameter specifies the path to the authenticode sign file for application packages that are authenticode signed.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: s

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Quiet

Indicates that the cmdlet runs in quiet mode, suppressing unnecessary output and prompts.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

Shows what would happen if the cmdlet runs. The cmdlet is not executed.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

Prompts the user for confirmation before running the cmdlet.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

## Examples

### Stop profiling and use default trace path

The following example stops profiling and saves the results to the default trace path.

```powershell
Stop-Profiling
```

### Stop profiling and use a specific trace path

The following example stops profiling and saves the results to a specific trace path.

```powershell
Stop-Profiling -TracePath "C:\Path\To\Trace.etl"
```

## Related topics

[Application capability profiler](../app-isolation-capability-profiler.md)

[Start-Profiling](Start-Profiling.md)

[Get-ProfilingResults](Get-ProfilingResults.md)

[Merge-ProfilingResults](Merge-ProfilingResults.md)

[Get-AppxPackage](/powershell/module/appx/get-appxpackage)
