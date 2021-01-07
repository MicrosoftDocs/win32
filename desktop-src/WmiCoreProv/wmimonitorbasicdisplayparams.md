---
description: Represents the basic display features of a computer monitor.
ms.assetid: 08405e7f-7824-4e44-9f37-da9bb5619cd6
title: WmiMonitorBasicDisplayParams class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorBasicDisplayParams
- WmiMonitorBasicDisplayParams.Active
- WmiMonitorBasicDisplayParams.DisplayTransferCharacteristic
- WmiMonitorBasicDisplayParams.InstanceName
- WmiMonitorBasicDisplayParams.MaxHorizontalImageSize
- WmiMonitorBasicDisplayParams.MaxVerticalImageSize
- WmiMonitorBasicDisplayParams.SupportedDisplayFeatures
- WmiMonitorBasicDisplayParams.VideoInputType
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorBasicDisplayParams class

The **WmiMonitorBasicDisplayParams** WMI class represents the basic display features of a computer monitor. The value of the **VideoInputType** property indicates whether the monitor is analog or digital. Data in this class corresponds to data in the Basic Display Parameters/Features block of Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) standard.

## Syntax

``` syntax
class WmiMonitorBasicDisplayParams : MSMonitorClass
{
  boolean                            Active;
  uint8                              DisplayTransferCharacteristic;
  string                             InstanceName;
  uint8                              MaxHorizontalImageSize;
  uint8                              MaxVerticalImageSize;
  SupportedDisplayFeaturesDescriptor SupportedDisplayFeatures;
  uint8                              VideoInputType;
};
```

## Members

The **WmiMonitorBasicDisplayParams** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorBasicDisplayParams** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

</dd> <dt>

**DisplayTransferCharacteristic**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Display transfer characteristic (100\*Gamma-100).

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

**MaxHorizontalImageSize**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum horizontal image size in centimeters. For more information, see Remarks.

</dd> <dt>

**MaxVerticalImageSize**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum vertical image size in centimeters. For more information, see Remarks.

</dd> <dt>

**SupportedDisplayFeatures**
</dt> <dd> <dl> <dt>

Data type: **[**SupportedDisplayFeaturesDescriptor**](supporteddisplayfeaturesdescriptor.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Display features supported by the monitor.

</dd> <dt>

**VideoInputType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Video input type.



| Value                                                                              | Meaning            |
|------------------------------------------------------------------------------------|--------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Analog<br/>  |
| <dl> <dt>1 (0x1)</dt> </dl> | Digital<br/> |



 

</dd> </dl>

## Remarks

**MaxHorizontalImageSize** and **MaxVerticalImageSize** represent the maximum image dimensions that the monitor can correctly display for the entire set of supported timing and format combinations. The maximum image dimension is defined by VESA Video Image Area Definition (VIAD) Standard and is rounded to the nearest centimeter. The host computer system can use this data to select the image size and aspect ratio that will allow properly scaled text. Be aware that, if either or both of these fields are zero, then the system makes no assumptions about the display size. For example, the size of a projection display may be undetermined.

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

 

 




