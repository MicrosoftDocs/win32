---
description: Represents the switch offload settings.
ms.assetid: 4e00544e-a8db-4337-af3f-f651bfcf6b05
title: Msvm_EthernetSwitchHardwareOffloadSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_EthernetSwitchHardwareOffloadSettingData
- Msvm_EthernetSwitchHardwareOffloadSettingData.DefaultQueueVrssEnabled
- Msvm_EthernetSwitchHardwareOffloadSettingData.DefaultQueueVmmqEnabled
- Msvm_EthernetSwitchHardwareOffloadSettingData.DefaultQueueVmmqQueuePairs
- Msvm_EthernetSwitchHardwareOffloadSettingData.DefaultQueueVrssIndependentHostSpreading
- Msvm_EthernetSwitchHardwareOffloadSettingData.DefaultQueueVrssExcludePrimaryProcessor
- Msvm_EthernetSwitchHardwareOffloadSettingData.DefaultQueueVrssQueueSchedulingMode
- Msvm_EthernetSwitchHardwareOffloadSettingData.DefaultQueueVrssMinQueuePairs
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_EthernetSwitchHardwareOffloadSettingData class

Represents the switch offload settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), UUID("1550e863-4337-4917-a040-5a27dbc58b59"), ExtensionId("11EC6134-128A-4A23-B12F-164184B48348"), InterfaceVersion("2"), InterfaceRevision("0"), DisplayName("Ethernet Switch Hardware Offload Settings"), AMENDMENT]
class Msvm_EthernetSwitchHardwareOffloadSettingData : Msvm_EthernetSwitchFeatureSettingData
{
  boolean DefaultQueueVrssEnabled = TRUE;
  boolean DefaultQueueVmmqEnabled = FALSE;
  uint32  DefaultQueueVmmqQueuePairs = 16;
  boolean DefaultQueueVrssIndependentHostSpreading = TRUE;
  boolean DefaultQueueVrssExcludePrimaryProcessor = FALSE;
  uint32  DefaultQueueVrssQueueSchedulingMode = 2;
  uint32  DefaultQueueVrssMinQueuePairs = 1;
};
```

## Members

The **Msvm\_EthernetSwitchHardwareOffloadSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetSwitchHardwareOffloadSettingData** class has these properties.

<dl> <dt>

**DefaultQueueVmmqEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (2), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

Specifies the VMMQ settings for the default queue of the vswitch.

</dd> <dt>

**DefaultQueueVmmqQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (3), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

Specifies the number of queues for the default queue.

</dd> <dt>

**DefaultQueueVrssEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (1), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

Specifies the VRss settings for the default queue of the vswitch.

</dd> <dt>

**DefaultQueueVrssExcludePrimaryProcessor**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6), **InterfaceVersion** (2), **InterfaceRevision** (0)
</dt> </dl>

Indicates whether the primary VMQ CPU is excluded from the VRSS/VMMQ indirection table.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**DefaultQueueVrssIndependentHostSpreading**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7), **InterfaceVersion** (2), **InterfaceRevision** (0)
</dt> </dl>

Indicates whether to always do VRSS spreading for default queue, regardless of the RSS state of the external vPort.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**DefaultQueueVrssMinQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4), **InterfaceVersion** (2), **InterfaceRevision** (0)
</dt> </dl>

Indicates minimum number of queues used for VRSS/VMMQ.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**DefaultQueueVrssQueueSchedulingMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5), **InterfaceVersion** (2), **InterfaceRevision** (0)
</dt> </dl>

Indicates how VRSS/VMMQ queues are steered to different host processors.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_EthernetSwitchFeatureSettingData**](msvm-ethernetswitchfeaturesettingdata.md)
</dt> </dl>

 

 




