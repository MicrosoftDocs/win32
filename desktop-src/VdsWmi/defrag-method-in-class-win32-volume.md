---
title: Defrag method of the Win32\_Volume class
description: The Defrag method defragments the volume.This topic uses Managed Object Format (MOF) syntax.
ms.assetid: 'f4782327-0cc6-447e-bc27-7b2042075fb0'
keywords: ["Defrag method", "Defrag method, Win32_Volume class", "Win32_Volume class, Defrag method"]
topic_type:
- apiref
api_name:
- Win32_Volume.Defrag
api_location:
- Vdswmi.dll
api_type:
- COM
---

# Defrag method of the Win32\_Volume class

The **Defrag** method defragments the volume.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832). The **Defrag** method, like the [**Format**](format-method-in-class-win32-volume.md) method, can run for a very long time. These methods are normally called asynchronously. If your code cancels the call by calling [**IWbemServices::CancelAsyncCall**](https://msdn.microsoft.com/library/aa392094) (or [**SWbemSink.Cancel**](https://msdn.microsoft.com/library/aa393878) in script or Visual Basic), then the provider is not notified and the operation continues to completion. During this time, no other disk defragmentation operations can be performed, because only one instance of a defragmentation engine can run at a time.

## Syntax


```mof
 uint32 Defrag(
  [in]   boolean Force,
  [out]  object DefragAnalysis
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

If **true**, forces defragmenting of the volume even if free space is low. The default is **false**.

</dd> <dt>

*DefragAnalysis* \[out\]
</dt> <dd>

A [**Win32\_DefragAnalysis**](win32-defraganalysis.md) object that contains the properties that describe the extent to which the volume is fragmented.

</dd> </dl>

## Return value



| Return code                                                                       | Description                                                                                                             |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | Success<br/>                                                                                                      |
| <dl> <dt>**1**</dt> </dl>  | Access Denied<br/>                                                                                                |
| <dl> <dt>**2**</dt> </dl>  | Not Supported<br/>                                                                                                |
| <dl> <dt>**3**</dt> </dl>  | Volume Dirty Bit Is Set<br/>                                                                                      |
| <dl> <dt>**4**</dt> </dl>  | Not Enough Free Space<br/>                                                                                        |
| <dl> <dt>**5**</dt> </dl>  | Corrupt Master File Table Detected<br/>                                                                           |
| <dl> <dt>**6**</dt> </dl>  | Call Canceled<br/>                                                                                                |
| <dl> <dt>**7**</dt> </dl>  | Call Cancellation Request Too Late<br/>                                                                           |
| <dl> <dt>**8**</dt> </dl>  | Defrag Engine Is Already Running<br/>                                                                             |
| <dl> <dt>**9**</dt> </dl>  | Unable To Connect To Defrag Engine<br/>                                                                           |
| <dl> <dt>**10**</dt> </dl> | Defrag Engine Error. You may receive this code if there is less than 20% space left on the specified volume.<br/> |
| <dl> <dt>**11**</dt> </dl> | Unknown Error<br/>                                                                                                |



 

## Examples

The following PowerShell code sample defrags the C volume on the local machine.


```PowerShell
Win32_Volume Class Defrag Method - Sample in PowerShell 


# First - get the volumes via WMI
$v=gwmi win32_volume



  # Display Number of volumes
"Number of volumes {0}: "  -f $v.length

# Now get the C:\ volume
$v1=$v | where {$_.name -eq "C:\"}

# Perform a defrag analysis
$v1.defraganalysis().defraganalysis

# Defrag the volume
$v1.defrag($true)

# Redo the Defrag analysis
$v1.defraganalysis().defraganalysis   
```



The previous code sample returns the following information:

``` syntax
__GENUS                       : 1
__CLASS                       : Win32_DefragAnalysis
__SUPERCLASS                  :
__DYNASTY                     : Win32_DefragAnalysis
__RELPATH                     : Win32_DefragAnalysis
__PROPERTY_COUNT              : 27
__DERIVATION                  : {}
__SERVER                      : LHS1
__NAMESPACE                   : ROOT\CIMV2
__PATH                        : \\LHS1\ROOT\CIMV2:Win32_DefragAnalysis
AverageFileSize               : 198959
AverageFragmentsPerFile       : 1.05
AverageFreeSpacePerExtent     : 54900541
ClusterSize                   : 4096
ExcessFolderFragments         : 0
FilePercentFragmentation      : 1
FragmentedFolders             : 1
FreeSpace                     : 60061192192
FreeSpacePercent              : 87
FreeSpacePercentFragmentation : 0
LargestFreeSpaceExtent        : 34030051328
MFTPercentInUse               : 91
MFTRecordCount                : 45348
PageFileSize                  : 0
TotalExcessFragments          : 1931
TotalFiles                    : 37038
TotalFolders                  : 8223
TotalFragmentedFiles          : 10
TotalFreeSpaceExtents         : 1094
TotalMFTFragments             : 2
TotalMFTSize                  : 50790400
TotalPageFileFragments        : 0
TotalPercentFragmentation     : 0
TotalUnmovableFiles           : 24
UsedSpace                     : 8655134720
VolumeName                    :
VolumeSize                    : 68716326912
            __GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
DefragAnalysis   : System.Management.ManagementBaseObject
ReturnValue      : 0


__GENUS                       : 1
__CLASS                       : Win32_DefragAnalysis
__SUPERCLASS                  :
__DYNASTY                     : Win32_DefragAnalysis
__RELPATH                     : Win32_DefragAnalysis
__PROPERTY_COUNT              : 27
__DERIVATION                  : {}
__SERVER                      : LHS1
__NAMESPACE                   : ROOT\CIMV2
__PATH                        : \\LHS1\ROOT\CIMV2:Win32_DefragAnalysis
AverageFileSize               : 198970
AverageFragmentsPerFile       : 1
AverageFreeSpacePerExtent     : 46885460
ClusterSize                   : 4096
ExcessFolderFragments         : 0
FilePercentFragmentation      : 0
FragmentedFolders             : 1
FreeSpace                     : 60060274688
FreeSpacePercent              : 87
FreeSpacePercentFragmentation : 1
LargestFreeSpaceExtent        : 34251751424
MFTPercentInUse               : 91
MFTRecordCount                : 45353
PageFileSize                  : 0
TotalExcessFragments          : 35
TotalFiles                    : 37038
TotalFolders                  : 8223
TotalFragmentedFiles          : 1
TotalFreeSpaceExtents         : 1281
TotalMFTFragments             : 2
TotalMFTSize                  : 50790400
TotalPageFileFragments        : 0
TotalPercentFragmentation     : 0
TotalUnmovableFiles           : 24
UsedSpace                     : 8656052224
VolumeName                    :
VolumeSize                    : 68716326912
```

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> </dl>

 

 





