---
description: An association between a virtual system and the setting data of the snapshot which is the parent to the virtual system.
ms.assetid: d11e00e0-a163-49ea-b8ef-e3909a7dc83f
ms.tgt_platform: multiple
title: CIM_PreviousSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_PreviousSettingData
- Root\CIMV2.CIM_PreviousSettingData.Target
- Root\CIMV2.CIM_PreviousSettingData.PreviousObject
api_type: 
- Schema
api_location: 
- Root\CIMV2
---

# CIM\_PreviousSettingData class

An association between a virtual system and the setting data of the snapshot which is the parent to the virtual system.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class CIM_PreviousSettingData
{
  CIM_ManagedElement REF Target;
  CIM_ManagedElement REF PreviousObject;
};
```

## Members

The **CIM\_PreviousSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PreviousSettingData** class has these properties.

<dl> <dt>

**PreviousObject**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The snapshot setting data that is the parent of this computer system.

</dd> <dt>

**Target**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The computer system that was the target of the application.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------------|------------------------|
| Namespace<br/> | Root\\CIMV2<br/> |



 

 




