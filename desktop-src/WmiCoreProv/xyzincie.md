---
description: Contains the coordinates of the display in the International Commission on Illumination (CIE) XYZ color space.
ms.assetid: e44e8a5f-005d-4d58-84e3-135d4e396086
title: XYZinCIE class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- XYZinCIE
- XYZinCIE.X
- XYZinCIE.Y
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# XYZinCIE class

The **XYZinCIE** WMI class contains the coordinates of the display in the International Commission on Illumination (CIE) XYZ color space.

## Syntax

``` syntax
class XYZinCIE : WmiMonitorColorCharacteristics
{
  uint16 X;
  uint16 Y;
};
```

## Members

The **XYZinCIE** class has these types of members:

-   [Properties](#properties)

### Properties

The **XYZinCIE** class has these properties.

<dl> <dt>

**X**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

X-coordinate.

</dd> <dt>

**Y**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Y-coordinate.

</dd> </dl>

## Remarks

The [**WmiMonitorColorCharacteristics**](wmimonitorcolorcharacteristics.md) class contains embedded instances of the **XYZinCIE** class to describe the color characteristics of a monitor.

To calculate the z-coordinate, based on the x and y values, use the relation \|\|(x,y,z)\|\| = 1.

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

 

 




