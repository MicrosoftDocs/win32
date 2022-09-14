---
description: Attaches a virtual hard disk file in loopback mode.
ms.assetid: 54bd8e67-e309-4bf3-94bd-e29bc3300a3d
title: AttachVirtualHardDisk method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.AttachVirtualHardDisk
api_type: 
- COM
api_location: 
- vmms.exe
---

# AttachVirtualHardDisk method of the Msvm\_ImageManagementService class

Attaches a virtual hard disk file in loopback mode.

## Syntax


```mof
uint32 AttachVirtualHardDisk(
  [in]  string              Path,
  [in]  boolean             AssignDriveLetter,
  [in]  boolean             ReadOnly,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

A fully qualified path that specifies the location of the virtual hard disk file to attach.

</dd> <dt>

*AssignDriveLetter* \[in\]
</dt> <dd>

Indicates if drive letters are assigned to the disk's volumes.

</dd> <dt>

*ReadOnly* \[in\]
</dt> <dd>

Indicates if the attached hard disk should be read-only.

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

To detach the virtual hard disk, use the [**Msvm\_MountedStorageImage.DetachVirtualHardDisk**](detachvirtualharddisk-msvm-mountedstorageimage.md) method.

Access to the [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

The following C# example shows how to attach a virtual hard disk file. The referenced utilities can be found in [Common utilities for the virtualization samples (V2)](common-utilities-for-the-virtualization-samples-v2.md).


```CSharp
public static void AttachVirtualHardDisk(string path)
{
    ManagementScope scope = new ManagementScope(@"root\virtualization\V2", null);
    ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");

    ManagementBaseObject inParams = imageService.GetMethodParameters("AttachVirtualHardDisk");
    inParams["Path"] = path;
    inParams["AssignDriveLetter"] = true;
    inParams["ReadOnly"] = false;
    ManagementBaseObject outParams = imageService.InvokeMethod("AttachVirtualHardDisk", inParams, null);
    if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
    {
        if (Utility.JobCompleted(outParams, scope))
        {
            Console.WriteLine("{0} was attached successfully.", inParams["Path"]);
        }
        else
        {
            Console.WriteLine("Unable to attach {0}", inParams["Path"]);
        }
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

[**Msvm\_MountedStorageImage.DetachVirtualHardDisk**](detachvirtualharddisk-msvm-mountedstorageimage.md)
</dt> <dt>

[**Mount (V1)**](/previous-versions/windows/desktop/virtual/mount-msvm-imagemanagementservice)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

