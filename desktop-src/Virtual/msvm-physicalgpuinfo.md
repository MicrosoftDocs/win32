---
title: Msvm\_PhysicalGPUInfo class
description: Contains information about a RemoteFX physical graphics processing unit (GPU).
ms.assetid: 68F6F642-77FC-4F3D-A0AB-DC13BB0A0FA2
keywords:
- Msvm_PhysicalGPUInfo class Hyper-V
- Msvm_PhysicalGPUInfo class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_PhysicalGPUInfo
- Msvm_PhysicalGPUInfo.Caption
- Msvm_PhysicalGPUInfo.Description
- Msvm_PhysicalGPUInfo.ElementName
- Msvm_PhysicalGPUInfo.Name
- Msvm_PhysicalGPUInfo.ID
- Msvm_PhysicalGPUInfo.TotalVideoMemory
- Msvm_PhysicalGPUInfo.AvailableVideoMemory
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_PhysicalGPUInfo class

Contains information about a RemoteFX physical graphics processing unit (GPU).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_PhysicalGPUInfo : CIM_ManagedElement
{
  string Caption;
  string Description;
  string ElementName;
  string Name;
  string ID;
  uint64 TotalVideoMemory;
  uint64 AvailableVideoMemory;
};
```

## Members

The **Msvm\_PhysicalGPUInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_PhysicalGPUInfo** class has these properties.

<dl> <dt>

**AvailableVideoMemory**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of unused video memory, in bytes, on the physical GPU that can be used by RemoteFX.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MAXLEN**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The unique identifier of the physical GPU.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MAXLEN**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The display name of the physical GPU.

</dd> <dt>

**TotalVideoMemory**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total amount of video memory, in bytes, on the physical GPU that can be used by RemoteFX.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 with SP1<br/>                                                           |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





