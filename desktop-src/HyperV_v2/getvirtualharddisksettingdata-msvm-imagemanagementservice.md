---
description: Retrieves the setting data associated with a virtual hard disk file.
ms.assetid: b82c018e-8d23-4615-99c1-3b622a8f41da
title: GetVirtualHardDiskSettingData method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.GetVirtualHardDiskSettingData
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetVirtualHardDiskSettingData method of the Msvm\_ImageManagementService class

Retrieves the setting data associated with a virtual hard disk file.

## Syntax


```mof
uint32 GetVirtualHardDiskSettingData(
  [in]  string              Path,
  [out] string              SettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The fully qualified path of the disk image file.

</dd> <dt>

*SettingData* \[out\]
</dt> <dd>

If successful, receives an embedded instance of the [**Msvm\_VirtualHardDiskSettingData**](msvm-virtualharddisksettingdata.md) class that contains the setting data for the virtual hard disk.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> <dt>

**File not found** (32779)
</dt> </dl>

## Remarks

Access to the [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

The following C# example shows how to call the [**GetVirtualHardDiskState**](getvirtualharddiskstate-msvm-imagemanagementservice.md) method. The referenced utilities can be found in [Common utilities for the virtualization samples (V2)](common-utilities-for-the-virtualization-samples-v2.md).


```CSharp
public static void GetVirtualHardDiskSettingData(string vhdPath)
{
    ManagementScope scope = new ManagementScope(@"root\virtualization\V2", null);
    ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");
    ManagementBaseObject inParams = imageService.GetMethodParameters("GetVirtualHardDiskSettingData");

    inParams["Path"] = vhdPath;

    ManagementBaseObject outParams = imageService.InvokeMethod("GetVirtualHardDiskSettingData", inParams, null);
    if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
    {
        if (Utility.JobCompleted(outParams, scope))
        {
            Console.WriteLine("GetVirtualHardDiskSettingData was successful.");
        }
        else
        {
            Console.WriteLine("GetVirtualHardDiskSettingData was not successful.");
        }
    }
    else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
    {
        string diskStateString = outParams["SettingData"].ToString();
        Utility.PrintEmbeddedInstance(diskStateString);
    }

    outParams.Dispose();
    inParams.Dispose();
    imageService.Dispose();
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

