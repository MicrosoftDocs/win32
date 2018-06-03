---
title: DefragAnalysis method of the Win32\_Volume class
description: The DefragAnalysis method generates a fragmentation analysis for a volume.This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see Calling a Method.
ms.assetid: 22619e64-845c-4369-9d27-2ccbffed8ad4
keywords:
- DefragAnalysis method
- DefragAnalysis method, Win32_Volume class
- Win32_Volume class, DefragAnalysis method
topic_type:
- apiref
api_name:
- Win32_Volume.DefragAnalysis
api_location:
- Vdswmi.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DefragAnalysis method of the Win32\_Volume class

The **DefragAnalysis** method generates a fragmentation analysis for a volume.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 DefragAnalysis(
  [out] boolean DefragRecommended,
  [out] object DefragAnalysis
);
```



## Parameters

<dl> <dt>

*DefragRecommended* \[out\]
</dt> <dd>

If **true**, defragmentation of the volume is recommended.

On Windows Vista, this value will be **true** if the file fragmentation on the volume exceeds 10%. On earlier versions of Windows, this value will be **true** if the average of the percent file fragmentation and percent free space fragmentation of the volume exceeds 10%.

</dd> <dt>

*DefragAnalysis* \[out\]
</dt> <dd>

Embedded instance of a [**Win32\_DefragAnalysis**](win32-defraganalysis.md) containing the properties that describe the extent to which the volume is fragmented.

</dd> </dl>

## Return value



| Return code                                                                       | Description                                   |
|-----------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | Success<br/>                            |
| <dl> <dt>**1**</dt> </dl>  | Access Denied<br/>                      |
| <dl> <dt>**2**</dt> </dl>  | Not Supported<br/>                      |
| <dl> <dt>**3**</dt> </dl>  | Volume Dirty Bit Is Set<br/>            |
| <dl> <dt>**4**</dt> </dl>  | Not Enough Free Space<br/>              |
| <dl> <dt>**5**</dt> </dl>  | Corrupt Master File Table Detected<br/> |
| <dl> <dt>**6**</dt> </dl>  | Call Canceled<br/>                      |
| <dl> <dt>**7**</dt> </dl>  | Call Cancellation Request Too Late<br/> |
| <dl> <dt>**8**</dt> </dl>  | Defrag Engine Is Already Running<br/>   |
| <dl> <dt>**9**</dt> </dl>  | Unable To Connect To Defrag Engine<br/> |
| <dl> <dt>**10**</dt> </dl> | Defrag Engine Error<br/>                |
| <dl> <dt>**11**</dt> </dl> | Unknown Error<br/>                      |



 

## Examples

The following PowerShell code sample uses **DefragAnalysis** to analyze the C drive.


```PowerShell
Win32_Volume Class DefragAnalysis sample using PowerShell 

# get volumes on local system
$v = get-wmiobject win32_volume

# Display Number of volumes
"Number of volumes {0}: " -f $v.length

# Now get the C:\ volume
$v1=$v | where {$_.name -eq "C:\"}

# Perform a defrag analysis on the C: drive
"Performing Defrag Analysis"
$dfa = $v1.DefragAnalysis().DefragAnalysis

# Display results
"";"Defrag Results - defrag of C:"
"-----------------------------"

"Average File Size (KB) : {0} KB" -f ($dfa.AverageFileSize/1kb)
"Average Fragments per File : {0} " -f $dfa.averageFragmentsPerfile
"Average Free Space per Extent : {0} " -f $dfa.AverageFreeSpacePerExtent
"Cluster Size (KB) : {0} " -f ($dfa.clustersize/1KB)
"Excess Folder Fragments : {0} " -f $dfa.ExcessFolderFragments
"File Percent Fragementation : {0} " -f $dfa.FilePercentFragementation
"Fragmented folders : {0} " -f $dfa.FragmentedFolders
"Free Space (GB) : {0} GB" -f ($dfa.FreeSpace/1gb)
"Free Space Percent : {0} " -f $dfa.FreeSpacePercent
"Free Space Percent Fragementation : {0} " -f $dfa.FreeSpacePercentFragementaion
"Largest free Space Extent : {0} " -f $dfa.LargestFreeSpaceExtent
"MFT Percent In Use : {0} " -f $dfa.MFTPercentInUse
"MFT Record count : {0} " -f $dfa.MFTRecordCount
"Page File Size : {0} " -f $dfa.PageFileSize
"Total Excess Fragements : {0} " -f $dfa.TotalExcessFragements
"Total Files : {0} " -f $dfa.TotalFiles
"Total Folders : {0} " -f $dfa.TotalFolders
"Total Fragmented Files : {0} " -f $dfa.TotalFragmentedFiles
"Total Free Space Extents : {0} " -f $dfa.TotalFreeSpaceExtents
"Total MFT Fragments : {0} " -f $dfa.TotalMftFragments
"Total MFT Size : {0} " -f $dfa.TotalMftSize
"Total Page File Fragements : {0} " -f $dfa.TotalPageFileFragements
"Total Percent Fragementation : {0} " -f $dfa.TotalPercentFragementation
"Total Unmovable Files : {0} " -f $dfa.TotalUnmovableFiles
"Used Space (GB) : {0} GB" -f ($dfa.UsedSpace/1gb)
"Volume Name : {0} " -f $dfa.VolumeName
"Volume Size (GB) : {0} GB" -f ($dfa.VolumeSize/1gb)
```



The previous sample displays the following information:

``` syntax
Number of volumes 2:
Performing Defrag Analysis

## Defrag Results - defrag of C:

Average File Size (KB) : 194.904296875 KB
Average Fragments per File : 1.04
Average Free Space per Extent : 66928900
Cluster Size (KB) : 4
Excess Folder Fragments : 0
File Percent Fragementation :
Fragmented folders : 1
Free Space (GB) : 55.9121589660645 GB
Free Space Percent : 87
Free Space Percent Fragementation :
Largest free Space Extent : 34251751424
MFT Percent In Use : 91
MFT Record count : 45363
Page File Size : 0
Total Excess Fragements :
Total Files : 37044
Total Folders : 8223
Total Fragmented Files : 14
Total Free Space Extents : 897
Total MFT Fragments : 2
Total MFT Size : 50790400
Total Page File Fragements :
Total Percent Fragementation :
Total Unmovable Files : 24
Used Space (GB) : 8.08490753173828 GB
Volume Name :
Volume Size (GB) : 63.9970664978027 GB
```

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> </dl>

 

 





