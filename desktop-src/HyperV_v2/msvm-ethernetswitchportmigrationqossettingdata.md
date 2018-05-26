---
Description: Represents the VFP QOS settings.
ms.assetid: e58a7a8d-0301-43ea-9338-18bc8c458e2d
title: Msvm\_EthernetSwitchPortMigrationQosSettingData class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_EthernetSwitchPortMigrationQosSettingData class

Represents the VFP QOS settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, UUID("FD2A5DE3-DC6C-4320-82A5-234D3AF55297"), Provider("VmmsWmiInstanceAndMethodProvider"), ExtensionId("E9B59CFA-2BE1-4B21-828F-B6FBDBDDC017"), InterfaceVersion("1"), InterfaceRevision("0"), DisplayName("Ethernet Switch Port VFP QOS Settings"), AMENDMENT]
class Msvm_EthernetSwitchPortMigrationQosSettingData : Msvm_EthernetSwitchPortFeatureSettingData
{
  string  QueueId = "";
  uint8   Switch_ReservationMode = 0;
  uint8   Switch_LinkSpeedPercentage = 0;
  uint64  Switch_DefaultReservation = 0;
  boolean Switch_EnableHardwareLimits = FALSE;
  boolean Switch_EnableHardwareReservations = FALSE;
  boolean Switch_EnableSoftwareReservations = TRUE;
  uint64  OutboundReservedValue = 0;
  uint64  OutboundMaximumMbps = 0;
  uint64  InboundMaximumMbps = 0;
};
```

## Members

The **Msvm\_EthernetSwitchPortMigrationQosSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetSwitchPortMigrationQosSettingData** class has these properties.

<dl> <dt>

**InboundMaximumMbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (10), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The bandwidth cap value for inbound traffic.

</dd> <dt>

**OutboundMaximumMbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (9), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The bandwidth cap value for outbound traffic.

</dd> <dt>

**OutboundReservedValue**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (8), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The bandwidth reservation value.

</dd> <dt>

**QueueId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), **WmiDataId** (1), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The ID of the QOS queue.

</dd> <dt>

**Switch\_DefaultReservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (4), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The default reservation value.

</dd> <dt>

**Switch\_EnableHardwareLimits**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (5), [**Version**](https://msdn.microsoft.com/library/aa393650) (1), [**Revision**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

Indicates whether hardware offloads for limits are attempted if available.

</dd> <dt>

**Switch\_EnableHardwareReservations**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (6), [**Version**](https://msdn.microsoft.com/library/aa393650) (1), [**Revision**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

Indicates whether hardware offloads for reservations are attempted if available.

</dd> <dt>

**Switch\_EnableSoftwareReservations**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (7), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

Indicates whether software based reservation is available.

</dd> <dt>

**Switch\_LinkSpeedPercentage**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (3), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The link speed percentage to be used for reservation.

</dd> <dt>

**Switch\_ReservationMode**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (2), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The QOS reservation mode on the switch.

<dt>

<span id="Absolute"></span><span id="absolute"></span><span id="ABSOLUTE"></span>

**Absolute** (0)


</dt> <dd></dd> <dt>

<span id="Weight"></span><span id="weight"></span><span id="WEIGHT"></span>

**Weight** (1)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_EthernetSwitchPortFeatureSettingData**](msvm-ethernetswitchportfeaturesettingdata.md)
</dt> </dl>

 

 




