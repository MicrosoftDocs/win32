---
description: Represents input parameters for digital video.
ms.assetid: aa459612-db79-477b-891f-28c9d0b1b497
title: WmiMonitorDigitalVideoInputParams class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorDigitalVideoInputParams
- WmiMonitorDigitalVideoInputParams.Active
- WmiMonitorDigitalVideoInputParams.InstanceName
- WmiMonitorDigitalVideoInputParams.IsDFP1xCompatible
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorDigitalVideoInputParams class

The **WmiMonitorDigitalVideoInputParams**represents input parameters for digital video. The data in this class corresponds to data in the Video Input Definition of Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) standard. An instance of this class is available only when the value of the **VideoInputType** property of the [**WmiMonitorBasicDisplayParams**](wmimonitorbasicdisplayparams.md) class is "Digital".

## Syntax

``` syntax
class WmiMonitorDigitalVideoInputParams : MSMonitorClass
{
  boolean Active;
  string  InstanceName;
  boolean IsDFP1xCompatible;
};
```

## Members

The **WmiMonitorDigitalVideoInputParams** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorDigitalVideoInputParams** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

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

**IsDFP1xCompatible**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

VESA DFP 1.x or compatible. If set, interface is signal compatible with VESA Digital Flat Panel (DFP) 1.x Transition Minimized Differential Signaling (TMDS) CRGB, 1 pixel/clock, up to 8 bits/color most significant bit (MSB) aligned, DE active high.

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

 

 




