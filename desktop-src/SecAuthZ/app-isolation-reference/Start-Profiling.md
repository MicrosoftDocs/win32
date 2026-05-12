---
title: Start-Profiling cmdlet
description: The Start-Profiling cmdlet is used to start access attempt profiling for an application package.
ms.topic: reference
ms.date: 08/27/2024
---

# Start-Profiling

The **Start-Profiling** cmdlet is used to start access attempt profiling for an application package. The cmdlet both starts an access attempt trace logging session and instruments the application package so it's able to log to the session.

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

> [!NOTE]
> **Start-Profiling** requires administrator privileges and that Developer Mode be enabled in Windows settings. See [Enable your device for development](/windows/apps/get-started/enable-your-device-for-development) for more information.

Module Name: [Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler](Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)

## Syntax

```powershell
Start-Profiling [[-ManifestPath] <string>] [-PackageFullName <string>] [-SignedFilePath <string>] [-Quiet]
[-Force] [-WhatIf] [-Confirm] [<CommonParameters>]

```

## Parameters

### -ManifestPath

Specifies the path to the manifest file of the application package to be profiled. The package full name will be inferred from the manifest. This parameters supersedes `-PackageFullName`.

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

This parameter is superseded by `-ManifestPath`. Specifies the full name of the application package to be profiled. This value can be obtained by calling [Get-AppxPackage](/powershell/module/appx/get-appxpackage). See [ApplicationCapabilityProfiler](../app-isolation-capability-profiler.md) for more information.

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

### -Force

Forces the cmdlet to proceed with profiling without displaying any confirmation prompts. **Use this parameter with caution.**

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

### Profile an application package specified by manifest

The following example starts profiling for an application package specified by a manifest file.

```powershell
Start-Profiling -ManifestPath C:\Path\To\MyAppXManifest.xml
```

### Profile an application package specified by package full name

The following example starts profiling for an application package specified by its package full name.

```powershell
Start-Profiling -PackageFullName "Contoso.Application_1.0.0.0_neutral__8wekyb3d8bbwe"
```

## Related topics

[Application capability profiler](../app-isolation-capability-profiler.md)

[Stop-Profiling](Stop-Profiling.md)

[Get-ProfilingResults](Get-ProfilingResults.md)

[Merge-ProfilingResults](Merge-ProfilingResults.md)

[Get-AppxPackage](/powershell/module/appx/get-appxpackage)
