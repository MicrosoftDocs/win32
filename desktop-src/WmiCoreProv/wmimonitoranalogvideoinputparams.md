---
description: Represents the analog video input parameters of a computer monitor.
ms.assetid: 87d4260d-06c7-4a76-a3a1-8f6e51e23d92
title: WmiMonitorAnalogVideoInputParams class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorAnalogVideoInputParams
- WmiMonitorAnalogVideoInputParams.Active
- WmiMonitorAnalogVideoInputParams.CompositeSyncSupported
- WmiMonitorAnalogVideoInputParams.InstanceName
- WmiMonitorAnalogVideoInputParams.SeparateSyncsSupported
- WmiMonitorAnalogVideoInputParams.SerrationOfVsyncRequired
- WmiMonitorAnalogVideoInputParams.SetupExpected
- WmiMonitorAnalogVideoInputParams.SignalLevelStandard
- WmiMonitorAnalogVideoInputParams.SyncOnGreenVideoSupported
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorAnalogVideoInputParams class

The **WmiMonitorAnalogVideoInputParams** WMI class represents the analog video input parameters of a computer monitor. The data in this class corresponds to data in the Video Input Definition of Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) standard. An instance of this class is available only when the value of the **VideoInputType** property of the [**WmiMonitorBasicDisplayParams**](wmimonitorbasicdisplayparams.md) class is "Analog".

## Syntax

``` syntax
class WmiMonitorAnalogVideoInputParams : MSMonitorClass
{
  boolean Active;
  uint8   CompositeSyncSupported;
  string  InstanceName;
  uint8   SeparateSyncsSupported;
  uint8   SerrationOfVsyncRequired;
  uint8   SetupExpected;
  uint8   SignalLevelStandard;
  uint8   SyncOnGreenVideoSupported;
};
```

## Members

The **WmiMonitorAnalogVideoInputParams** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorAnalogVideoInputParams** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

</dd> <dt>

**CompositeSyncSupported**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether composite sync is supported.



| Value                                                                              | Meaning                                                             |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Composite sync on horizontal sync line is supported.<br/>     |
| <dl> <dt>1 (0x1)</dt> </dl> | Composite sync on horizontal sync line is not supported.<br/> |



 

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

**SeparateSyncsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether separate syncs are supported.



| Value                                                                              | Meaning                                      |
|------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Separate syncs are supported.<br/>     |
| <dl> <dt>1 (0x1)</dt> </dl> | Separate syncs are not supported.<br/> |



 

</dd> <dt>

**SerrationOfVsyncRequired**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether vertical sync pulse serration is required.



| Value                                                                              | Meaning                                                                                                             |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Serration of the vertical sync pulse is required when composite sync or sync-on-green video is used.<br/>     |
| <dl> <dt>1 (0x1)</dt> </dl> | Serration of the vertical sync pulse is not required when composite sync or sync-on-green video is used.<br/> |



 

</dd> <dt>

**SetupExpected**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether setup is expected.



| Value                                                                              | Meaning                                                                                                                   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Monitor expects a blank-to-blank setup or pedestal per appropriate Signal Level Standard.<br/>                      |
| <dl> <dt>1 (0x1)</dt> </dl> | Monitor does not expect a blank-to-blank setup or pedestal according to the appropriate signal level standard.<br/> |



 

</dd> <dt>

**SignalLevelStandard**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Signal level standard for Enhanced video connector (EVC) connections.



| Value                                                                              | Meaning                     |
|------------------------------------------------------------------------------------|-----------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | 0.7,0.3\[V\]<br/>     |
| <dl> <dt>1 (0x1)</dt> </dl> | 0.714,0.286\[V\]<br/> |
| <dl> <dt>2 (0x2)</dt> </dl> | 1.0,0.4\[V\]<br/>     |
| <dl> <dt>3 (0x3)</dt> </dl> | 0.7,0.0\[V\]<br/>     |



 

</dd> <dt>

**SyncOnGreenVideoSupported**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether sync on green is supported.



| Value                                                                              | Meaning                                          |
|------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Sync on green video is supported.<br/>     |
| <dl> <dt>1 (0x1)</dt> </dl> | Sync on green video is not supported.<br/> |



 

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

 

 




