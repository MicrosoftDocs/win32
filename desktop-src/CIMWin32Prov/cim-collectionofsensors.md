---
description: The CIM\_CollectionOfSensors association represents the binary sensors that make up the multistate sensor.
ms.assetid: d9494716-bb4e-4aa2-9e3b-e865360c740f
ms.tgt_platform: multiple
title: CIM_CollectionOfSensors class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_CollectionOfSensors
- CIM_CollectionOfSensors.PartComponent
- CIM_CollectionOfSensors.GroupComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_CollectionOfSensors class

The **CIM\_CollectionOfSensors** association represents the binary sensors that make up the multistate sensor.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{A2ABF536-DB35-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_CollectionOfSensors : CIM_Component
{
  CIM_BinarySensor     REF PartComponent;
  CIM_MultiStateSensor REF GroupComponent;
};
```

## Members

The **CIM\_CollectionOfSensors** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectionOfSensors** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_MultiStateSensor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent")
</dt> </dl>

A [**CIM\_MultiStateSensor**](cim-multistatesensor.md) that describes the multi-state sensor.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BinarySensor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (2), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

A [**CIM\_BinarySensor**](cim-binarysensor.md) that describes a binary sensor that is part of the multi-state sensor.

</dd> </dl>

## Remarks

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

