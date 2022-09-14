---
description: Detaches the mounted storage image that is associated with this class.
ms.assetid: C3AB0EEE-71FE-4049-90AB-01F5D77E3B97
title: DetachVirtualHardDisk method of the Msvm_MountedStorageImage class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MountedStorageImage.DetachVirtualHardDisk
api_type: 
- COM
api_location: 
- vmms.exe
---

# DetachVirtualHardDisk method of the Msvm\_MountedStorageImage class

Detaches the mounted storage image that is associated with this class.

## Syntax


```mof
uint32 DetachVirtualHardDisk();
```



## Parameters

This method has no parameters.

## Return value

Type: **uint32**

This method can return one of the following values.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Failed** (1)
</dt> </dl>

## Remarks

Access to the [**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

The following C# example shows how to detach a virtual hard disk file. The referenced utilities can be found in [Common utilities for the virtualization samples (V2)](common-utilities-for-the-virtualization-samples-v2.md).


```CSharp
public static void DetachVirtualHardDisk(string path)
{
    ManagementScope scope = new ManagementScope(@"root\virtualization\V2", null);

    ManagementClass mountedStorageImageServiceClass = new ManagementClass("Msvm_MountedStorageImage");

    mountedStorageImageServiceClass.Scope = scope;

    using (ManagementObjectCollection collection = mountedStorageImageServiceClass.GetInstances())
    {
        foreach (ManagementObject image in collection)
        {
            using (image)
            {
                string name = image.GetPropertyValue("Name").ToString();
                if (string.Equals(name, path, StringComparison.OrdinalIgnoreCase))
                {
                    ManagementBaseObject outParams = image.InvokeMethod("DetachVirtualHardDisk", null, null);

                    if ((UInt32)outParams["ReturnValue"] == 0)
                    {
                        Console.WriteLine("{0} was detached successfully.", path);
                    }
                    else
                    {
                        Console.WriteLine("Unable to dettach {0}", path);
                    }

                    outParams.Dispose();

                    break;
                }

                image.Dispose();
            }
        }
    }
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

[**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md)
</dt> </dl>

 

