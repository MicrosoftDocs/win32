---
title: Merge-ProfilingResults cmdlet
description: Merges multiple Get-ProfilingResults output files into a single file.
ms.topic: reference
ms.date: 08/27/2024
---

# Merge-ProfilingResults

The **Merge-ProfilingResults** cmdlet is used to merge multiple **Get-ProfilingResults** output files into a single output file.

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Module Name: [Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler](Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)

## Syntax

Use the following syntax to merge results from an XML Set:

```powershell
Merge-ProfilingResults [-XmlInput] <string[]> [-OutputPath <string>] [-PackageNames <string[]>] [-Quiet]
[-ShowNoNameObjectFailures] [-WhatIf] [-Confirm] [<CommonParameters>]
```

Use the following syntax to merge results from a CSV Set:

```powershell
Merge-ProfilingResults [-CsvInput] <string[]> [-OutputPath <string>] [-PackageNames <string[]>] [-Quiet]
[-ShowNoNameObjectFailures] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## Parameters

### -XmlInput

Specifies an array of paths to XML application package manifests to be merged.

```yaml
Type: System.String[]
Parameter Sets: XML
Aliases: c, Capabilities

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CsvInput

Specifies an array of paths to CSV access attempt records to be merged.

```yaml
Type: System.String[]
Parameter Sets: CSV
Aliases: r, Records

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```t wildcard characters: False
```

### -OutputPath

Specifies the path to the output file where the merged output will be saved.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: o, Output

Required: False
Position: Named
Default value: <working directory>\merged\AppXManifest-Capabilities.xml (XML) or <working directory>\merged\AccessAttemptRecords.csv (CSV)
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageNames

Specifies an array of package names to filter the merging. Only information related to the specified packages will be merged into the output file.

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

### Merge multiple XML results

The following example merges two results listed in the AppXManifest file into a single file:

```powershell
Merge-ProfilingResults -XmlInput "C:\Path\To\AppXManifest1.xml", "C:\Path\To\AppXManifest2.xml" -OutputPath "C:\Path\To\MergedAppXManifest.xml"
```

### Merge multiple CSV results

The following example merges two results listed in the AccessAttemptRecords.csv file into a single file:

```powershell
Merge-ProfilingResults -CsvInput "C:\Path\To\AccessAttemptRecords1.csv", "C:\Path\To\AccessAttemptRecords2.csv" -OutputPath "C:\Path\To\MergedAccessAttemptRecords.csv"
```

## Related topics

[Application capability profiler](../app-isolation-capability-profiler.md)

[Get-ProfilingResults](Get-ProfilingResults.md)

[Start-Profiling](Start-Profiling.md)

[Stop-Profiling](Stop-Profiling.md)
