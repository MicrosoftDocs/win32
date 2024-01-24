---
description: An association between an object and another object which has been applied to it.
ms.assetid: ee6b17b7-4f01-4731-8d6b-a3421621a75a
ms.tgt_platform: multiple
title: CIM_LastAppliedSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_LastAppliedSettingData
- Root\CIMV2.CIM_LastAppliedSettingData.Target
- Root\CIMV2.CIM_LastAppliedSettingData.AppliedObject
api_type: 
- Schema
api_location: 
- Root\CIMV2
---

# CIM\_LastAppliedSettingData class

An association between an object and another object which has been applied to it.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class CIM_LastAppliedSettingData
{
  CIM_ManagedElement REF Target;
  CIM_ManagedElement REF AppliedObject;
};
```

## Members

The **CIM\_LastAppliedSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_LastAppliedSettingData** class has these properties.

<dl> <dt>

**AppliedObject**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The object that was applied to the target object.

</dd> <dt>

**Target**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The object that was the target of the object's application.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------------|------------------------|
| Namespace<br/> | Root\\CIMV2<br/> |



 

 




