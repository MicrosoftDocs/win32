---
description: Represents the International Commission on Illumination (CIE) color characteristics of a computer monitor.
ms.assetid: 476aefae-11c0-46be-a2bb-83fbafd70421
title: WmiMonitorColorCharacteristics class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorColorCharacteristics
- WmiMonitorColorCharacteristics.Active
- WmiMonitorColorCharacteristics.Blue
- WmiMonitorColorCharacteristics.DefaultWhite
- WmiMonitorColorCharacteristics.Green
- WmiMonitorColorCharacteristics.InstanceName
- WmiMonitorColorCharacteristics.Red
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorColorCharacteristics class

The **WmiMonitorColorCharacteristics** class represents the International Commission on Illumination (CIE) color characteristics of a computer monitor. The data corresponds to data in the Color Characteristics block of the Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) structure.

## Syntax

``` syntax
class WmiMonitorColorCharacteristics : MSMonitorClass
{
  boolean  Active;
  XYZinCIE Blue;
  XYZinCIE DefaultWhite;
  XYZinCIE Green;
  string   InstanceName;
  XYZinCIE Red;
};
```

## Members

The **WmiMonitorColorCharacteristics** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorColorCharacteristics** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

</dd> <dt>

**Blue**
</dt> <dd> <dl> <dt>

Data type: **[**XYZinCIE**](xyzincie.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CIE coordinates for blue, represented by an instance of the [**XYZinCIE**](xyzincie.md) class.

</dd> <dt>

**DefaultWhite**
</dt> <dd> <dl> <dt>

Data type: **[**XYZinCIE**](xyzincie.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default white CIE coordinates.

</dd> <dt>

**Green**
</dt> <dd> <dl> <dt>

Data type: **[**XYZinCIE**](xyzincie.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CIE coordinates for green, represented by an instance of the [**XYZinCIE**](xyzincie.md) class.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Name of the specific monitor instance.

</dd> <dt>

**Red**
</dt> <dd> <dl> <dt>

Data type: **[**XYZinCIE**](xyzincie.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CIE coordinates for red, represented by an instance of the [**XYZinCIE**](xyzincie.md) class.

</dd> </dl>

## Remarks

The chromaticity and white point values are expressed as fractional numbers using an encoding format. This format is accurate to the thousandth place, which is 10 bits in length. The most significant bit (MSB) represents 2^-1 and the least significant bit (LSB) represents 2^-10 coefficients, respectively. Precision of the stored values in the E-EDID v1.x structure should be accurate to +/- 0.005 of the actual value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> </dl>

 

 




