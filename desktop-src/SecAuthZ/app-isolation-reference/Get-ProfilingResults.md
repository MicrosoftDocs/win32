---
title: Get-ProfilingResults cmdlet
description: App isolation PowerShell cmdlet that retrieves capability access information from input ETL files.
ms.topic: reference
ms.date: 08/27/2024
---

# Get-ProfilingResults

The **Get-ProfilingResults** cmdlet parses one or more specified ETL (Event Tracing for Windows) files to find access denied events for application packages and identifies capabilities that would allow the package to perform those accesses. It also outputs relevant information about the access denied events found for the packages.

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Module Name: [Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler](Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)

## Syntax

```powershell
Get-ProfilingResults [[-EtlFilePaths] <string[]>] [-ExeNames <string[]>] [-ManifestPath <string>]
[-RecordsOutputPath <string>] [-SummaryOutputPath <string>] [-PackageNames <string[]>] [-Quiet]
[-ShowNoNameObjectFailures] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## Parameters

### -EtlFilePaths

Specifies an array of paths to the ETL files from which profiling results should be retrieved. **Get-ProfilingResults** requires an input ETL file. If `-EtlFilePaths` is not provided, the cmdlet will attempt to stop an active trace logging session and capture an ETL file from it.

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: Logs, l

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExeNames

Specifies an array of executable names to filter the profiling results. Only results related to the specified executables will be returned.

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: e

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManifestPath

Specifies the path to the application package manifest file to be edited by the cmdlet with the identified capabilities. If the capabilities identified cannot be attributed to this manifest's package, a copy of the manifest is generated for each package identified including the capabilities pertaining thereto.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: m

Required: False
Position: Named
Default value: <working directory>\<package name>\AppXManfiest-Capabilities.xml
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageNames

Specifies an array of package names to filter the profiling results. Only results related to the specified packages will be returned.

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: p, Packages

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecordsOutputPath

Specifies the path to a CSV file to save detailed access attempt information. If not specified, the default output path will be used.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: r, RecordsOutput, RecordsPath

Required: False
Position: Named
Default value: <working directory>\AccessAttemptRecords.csv
Accept pipeline input: False
Accept wildcard characters: False
```

### -ShowNoNameObjectFailures

Indicates whether to output summary information for access attempts to unidentified objects.

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

### -SummaryOutputPath

Specifies the path to a TXT file to save a summary of the profiling results. If not specified, the default output path will be used.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: s, SummaryPath, SummaryOutput

Required: False
Position: Named
Default value: <working directory>\summary.txt
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

### Parse captured trace and output capability access info

This example parses a trace captured with **Start-Profiling**/**Stop-Profiling** and outputs the capability access information. Any capability access information that can be matched to the application package manifest provided is automatically added to the manifest.

```powershell
Get-ProfilingResults -EtlFilePaths C:\Logs\trace.etl -ManifestPath C:\Path\To\MyAppXManifest.xml
```

### Find and parse active trace logging session

This example finds an active trace logging session from **Start-Profiling**, collects the trace, and parses it. If a trace logging session is currently active, **Stop-Profiling** will be called to attempt to collect a trace that can be parsed.

```powershell
Get-ProfilingResults -ManifestPath C:\Path\To\MyAppXManifest.xml
```

### Parse multiple traces

The following example parses multiple ETL files and outputs the capability access information.

```powershell
Get-ProfilingResults -EtlFilePaths C:\Logs\trace1.etl, C:\Logs\trace2.etl
```

## Related topics

[Application capability profiler](../app-isolation-capability-profiler.md)

[Start-Profiling](Start-Profiling.md)

[Stop-Profiling](Stop-Profiling.md)

[Merge-ProfilingResults](Merge-ProfilingResults.md)
