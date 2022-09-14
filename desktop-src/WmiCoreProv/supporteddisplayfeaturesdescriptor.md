---
description: Represents the supported display features of the monitor.
ms.assetid: 28eeead3-8fb9-4720-8d93-1c6757dfb31b
title: SupportedDisplayFeaturesDescriptor class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SupportedDisplayFeaturesDescriptor
- SupportedDisplayFeaturesDescriptor.ActiveOffSupported
- SupportedDisplayFeaturesDescriptor.DisplayType
- SupportedDisplayFeaturesDescriptor.GTFSupported
- SupportedDisplayFeaturesDescriptor.HasPreferredTimingMode
- SupportedDisplayFeaturesDescriptor.sRGBSupported
- SupportedDisplayFeaturesDescriptor.StandbySupported
- SupportedDisplayFeaturesDescriptor.SuspendSupported
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# SupportedDisplayFeaturesDescriptor class

The **SupportedDisplayFeaturesDescriptor**represents the supported display features of the monitor. The information in this class corresponds to data in the Video Input Definition of the Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) standard.

## Syntax

``` syntax
class SupportedDisplayFeaturesDescriptor
{
  boolean ActiveOffSupported;
  uint8   DisplayType;
  boolean GTFSupported;
  boolean HasPreferredTimingMode;
  boolean sRGBSupported;
  boolean StandbySupported;
  boolean SuspendSupported;
};
```

## Members

The **SupportedDisplayFeaturesDescriptor** class has these types of members:

-   [Properties](#properties)

### Properties

The **SupportedDisplayFeaturesDescriptor** class has these properties.

<dl> <dt>

**ActiveOffSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Support for active off and very low power. The display consumes less power when it receives a timing signal that is outside the declared active operating range. The display will revert to normal operation if the timing signal returns to the normal operating range. Examples of timing signals outside the normal operating range are no sync signals or no DE signal.

</dd> <dt>

**DisplayType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of display for the monitor. The following table lists possible values.



| Value                                                                              | Meaning                                 |
|------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Monochrome/grayscale display<br/> |
| <dl> <dt>1 (0x1)</dt> </dl> | RGB color display<br/>            |
| <dl> <dt>2 (0x2)</dt> </dl> | Non-RGB multicolor display<br/>   |



 

</dd> <dt>

**GTFSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the display has GTF support. If **True**, the display supports timings based on the GTF standard using default GTF parameter values.

</dd> <dt>

**HasPreferredTimingMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the display has has a preferred timing mode. If **True**, the first detailed timing block contains the preferred timing mode of the monitor. Use of preferred timing mode is required by EDID v.1.3 and higher.

</dd> <dt>

**sRGBSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the display supports sRGB.

</dd> <dt>

**StandbySupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the display supports VESA Display Power Management Signaling (DPMS) standby. If **True**, DPMS standby is supported.

</dd> <dt>

**SuspendSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the display supports VESA Display Power Management Signaling (DPMS) suspend. If **True**, DPMS suspend is supported.

</dd> </dl>

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

 

 




