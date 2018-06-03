---
title: Chkdsk method of the Win32\_Volume class
description: The Chkdsk method invokes the Chkdsk operation on the volume.
ms.assetid: 9ddbf5e5-4a1c-4e1c-8a86-72d5ec7210f6
keywords:
- Chkdsk method
- Chkdsk method, Win32_Volume class
- Win32_Volume class, Chkdsk method
topic_type:
- apiref
api_name:
- Win32_Volume.Chkdsk
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

# Chkdsk method of the Win32\_Volume class

The **Chkdsk** method invokes the Chkdsk operation on the volume. The method is only applicable to volume instances that represent a physical disk on the computer. It is not applicable to mapped logical drives.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Chkdsk(
  [in] boolean FixErrors = FALSE,
  [in] boolean VigorousIndexCheck = TRUE,
  [in] boolean SkipFolderCycle = TRUE,
  [in] boolean ForceDismount = FALSE,
  [in] boolean RecoverBadSectors = FALSE,
  [in] boolean OkToRunAtBootUp = FALSE
);
```



## Parameters

<dl> <dt>

*FixErrors* \[in\]
</dt> <dd>

If **true**, errors found on the disk are fixed. The default is **false**.

</dd> <dt>

*VigorousIndexCheck* \[in\]
</dt> <dd>

If **true**, a vigorous check of index entries is performed. The default is **true**.

</dd> <dt>

*SkipFolderCycle* \[in\]
</dt> <dd>

If **true**, the folder cycle checking should be skipped. The default is **true**.

</dd> <dt>

*ForceDismount* \[in\]
</dt> <dd>

If **true**, the volume is dismounted before checking. The default is **false**.

</dd> <dt>

*RecoverBadSectors* \[in\]
</dt> <dd>

If **true**, the bad sectors are located and the readable information is recovered. The default is **false**.

</dd> <dt>

*OkToRunAtBootUp* \[in\]
</dt> <dd>

If **true**, the Chkdsk operation is performed at the next boot up, in case the Chkdsk operation could not be performed because the volume was locked at the time the method was called. The default is **false**.

</dd> </dl>

## Return value



| Return code                                                                      | Description                                                       |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl> | Success - Chkdsk Completed<br/>                             |
| <dl> <dt>**1**</dt> </dl> | Success - Volume Locked and Chkdsk Scheduled on Reboot<br/> |
| <dl> <dt>**2**</dt> </dl> | Unsupported File System<br/>                                |
| <dl> <dt>**3**</dt> </dl> | Unknown File System<br/>                                    |
| <dl> <dt>**4**</dt> </dl> | No Media In Drive<br/>                                      |
| <dl> <dt>**5**</dt> </dl> | Unknown Error<br/>                                          |



 

## Examples

The following code sample runs a Chkdsk on the specified drive.


```PowerShell
# Helper function to Decode Return Code

function Get-DfragReturn {
param ([uint16] $char)

# parse and return values

If ($char -ge 0 -and $char -le 5) {

  switch ($char) {
  0  {"00-Success"}
  1     {"01-sUCCESS (volume locked and chkdsk scheduled for reboot"}
  2  {"02-unsupported file system"}
  3  {"03-Unknown file system"}
  4  {"04-No Media in drive"}
  5  {"05-Unknown Error"}
  }
}

Else {
 "{0} - *Invalid Result Code*" -f $char}
 Return
}

# Get all local disks
# then get first drive (C:)
$disks=gwmi win32_Volume
$c=$disks | where {$_.name -eq "C:\"}

# print start
"Checking {0} on system: {1}" -f $c.name,$c.SystemName

# Now specify chkdsk paramaters and call chkdsk

$FixErrors          = $false    # does not fix errors 
$VigorousIndexCheck = $true     # performs a vigorous check of the indexes
$SkipFolderCycle    = $false    # does not skip folder cycle checking.
$ForceDismount      = $false    # will not force a dismount (to enable errors to be fixed)
$RecoverBadSecors   = $false    # does not recover bad sectors
$OKToRunAtBootup    = $false    # runs now, vs at next bootup

$start=get-date
"Commencing Defrag"
$res=$c.chkdsk($FixErrors, 
              $VigorousIndexCheck, 
              $SkipFolderCycle, 
              $ForceDismount,
              $RecoverBadSecors, 
              $OKToRunAtBootup)
$finish=get-date

# Now Display returndvalue 
"Chkdsk call returned: {0}" -f (Get-DfragReturn($res.ReturnValue))

# Finally print time elapsed
"Starting Check Disk at: {0}" -f $start
"Finished at             {0}" -f $finish

$duration = $finish-$start
"Elapsed time            {0} minutes" -f ($duration.totalminutes.tostring("0.00"))
```



When run, the previous code sample returns the following information:

``` syntax
Checking C:\ on system: LHS1
Commencing Defrag
Chkdsk call returned: 00-Success
Starting Check Disk at: 16/06/2007 16:45:55
Finished at             16/06/2007 16:50:31
Elapsed time            4.59 minutes
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

 

 





