---
description: Generates a set of World Wide Port Names (WWPNs).
ms.assetid: 36f393eb-6f34-4ae3-a976-c5da60211f3e
title: GenerateWwpn method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.GenerateWwpn
api_type: 
- COM
api_location: 
- vmms.exe
---

# GenerateWwpn method of the Msvm\_VirtualSystemManagementService class

Generates a set of World Wide Port Names (WWPNs). The WWPNs are generated from within the pre-configured range defined by the **MinimumWWPNAddress** and **MaximumWWPNAddress** properties of the [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md) class. If the valid number of WWPNs that can be generated is less than the requested number, then the remaining entries in the *GeneratedWwpn* array will have the invalid entry of "0000000000000000" and the return value will indicate success (0).

## Syntax


```mof
uint32 GenerateWwpn(
  [in]  uint32 NumberOfWwpns,
  [out] string GeneratedWwpn[]
);
```



## Parameters

<dl> <dt>

*NumberOfWwpns* \[in\]
</dt> <dd>

The number of WWPNs to be generated.

</dd> <dt>

*GeneratedWwpn* \[out\]
</dt> <dd>

An array of strings, each of which will contain a generated WWPN. It will be formatted in string form as "01:23:45:67:89:ab:cd:ef".

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
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
</dt> </dl>

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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 




