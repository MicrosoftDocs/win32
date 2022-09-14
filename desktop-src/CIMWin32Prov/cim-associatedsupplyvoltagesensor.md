---
description: Associates a power supply with a voltage sensor that monitors its input voltage.
ms.assetid: 4164320e-8362-4ce2-9949-f14669278bd8
ms.tgt_platform: multiple
title: CIM_AssociatedSupplyVoltageSensor class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_AssociatedSupplyVoltageSensor
- CIM_AssociatedSupplyVoltageSensor.Dependent
- CIM_AssociatedSupplyVoltageSensor.Antecedent
- CIM_AssociatedSupplyVoltageSensor.MonitoringRange
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_AssociatedSupplyVoltageSensor class

The **CIM\_AssociatedSupplyVoltageSensor** class associates a power supply with a voltage sensor that monitors its input voltage.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{327ABD78-E3D3-11d2-8601-0000F8102E5F}"), AMENDMENT]
class CIM_AssociatedSupplyVoltageSensor : CIM_AssociatedSensor
{
  CIM_PowerSupply   REF Dependent;
  CIM_VoltageSensor REF Antecedent;
  uint16                MonitoringRange;
};
```

## Members

The **CIM\_AssociatedSupplyVoltageSensor** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AssociatedSupplyVoltageSensor** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VoltageSensor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_VoltageSensor**](cim-voltagesensor.md) that describes the voltage sensor.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PowerSupply**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_PowerSupply**](cim-powersupply.md) that describes the power supply associated with the voltage sensor.

</dd> <dt>

**MonitoringRange**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the power supply's input voltage range measured by the associated sensor.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Range_1"></span><span id="range_1"></span><span id="RANGE_1"></span>

<span id="Range_1"></span><span id="range_1"></span><span id="RANGE_1"></span>**Range 1** (2)


</dt> <dd></dd> <dt>

<span id="Range_2"></span><span id="range_2"></span><span id="RANGE_2"></span>

<span id="Range_2"></span><span id="range_2"></span><span id="RANGE_2"></span>**Range 2** (3)


</dt> <dd></dd> <dt>

<span id="Both_Range_1_and_2"></span><span id="both_range_1_and_2"></span><span id="BOTH_RANGE_1_AND_2"></span>

<span id="Both_Range_1_and_2"></span><span id="both_range_1_and_2"></span><span id="BOTH_RANGE_1_AND_2"></span>**Both Range 1 and 2** (4)


</dt> <dd>

Range 1 and 2

</dd> </dl>

</dd> </dl>

## Remarks

The **CIM\_AssociatedSupplyVoltageSensor** class is derived from [**CIM\_AssociatedSensor**](cim-associatedsensor.md).

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

[**CIM\_AssociatedSensor**](cim-associatedsensor.md)
</dt> </dl>

 

