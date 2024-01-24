---
description: Removes DH-CHAP (Diffie Hellman - Challenge Handshake Authentication Protocol) parameters from a synthetic Fibre Channel port in a virtual machine.
ms.assetid: f15673e2-287d-4e87-bee4-6c0f5f9178c8
title: RemoveFibreChannelChap method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.RemoveFibreChannelChap
api_type: 
- COM
api_location: 
- vmms.exe
---

# RemoveFibreChannelChap method of the Msvm\_VirtualSystemManagementService class

Removes DH-CHAP (Diffie Hellman - Challenge Handshake Authentication Protocol) parameters from a synthetic Fibre Channel port in a virtual machine. This method will fail if the virtual machine is running.

## Syntax


```mof
uint32 RemoveFibreChannelChap(
  [in] string FcPortSettings[]
);
```



## Parameters

<dl> <dt>

*FcPortSettings* \[in\]
</dt> <dd>

An array of strings that contain an embedded instance of the [**Msvm\_SyntheticFcPortSettingData**](msvm-syntheticfcportsettingdata.md) class that define the synthetic Fibre Channel ports to remove the DH-CHAP parameters from. The **InstanceID** property of each of these instances identifies the elements to be modified.

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

 

 




