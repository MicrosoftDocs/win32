---
description: Provides a method to disable specific power management capabilities on the adapter.
ms.assetid: 525c5657-ebf4-4807-bd55-9fbf3f82458a
title: Disable method of the MSFT\_NetAdapterPowerManagementSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagementSettingData.Disable
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Disable method of the MSFT\_NetAdapterPowerManagementSettingData class

Provides a method to disable specific power management capabilities on the adapter.

## Syntax


```mof
uint32 Disable(
  [out] string  cmdletOutput,
  [in]  boolean ArpOffload,
  [in]  boolean D0PacketCoalescing,
  [in]  boolean DeviceSleepOnDisconnect,
  [in]  boolean NSOffload,
  [in]  boolean RsnRekeyOffload,
  [in]  boolean SelectiveSuspend,
  [in]  boolean WakeOnMagicPacket,
  [in]  boolean WakeOnPattern
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of the [**MSFT\_NetAdapterPowerManagementSettingData**](msft-netadapterpowermanagementsettingdata.md) class.

</dd> <dt>

*ArpOffload* \[in\]
</dt> <dd>

**true** to disable the setting for ARP offloads on the adapter.

</dd> <dt>

*D0PacketCoalescing* \[in\]
</dt> <dd>

**true** to disable the D0 Packet Coalescing on the adapter.

</dd> <dt>

*DeviceSleepOnDisconnect* \[in\]
</dt> <dd>

**true** to disable sleeping on media disconnect on the adapter.

</dd> <dt>

*NSOffload* \[in\]
</dt> <dd>

**true** to disable NS offloads on the adapter.

</dd> <dt>

*RsnRekeyOffload* \[in\]
</dt> <dd>

**true** to disable 802.11i RSN offloading on the adapter.

</dd> <dt>

*SelectiveSuspend* \[in\]
</dt> <dd>

**true** to disable selective suspend on the adapter.

</dd> <dt>

*WakeOnMagicPacket* \[in\]
</dt> <dd>

**true** to disable waking on Magic Packets on the adapter.

</dd> <dt>

*WakeOnPattern* \[in\]
</dt> <dd>

**true** to disable waking on a packet pattern for the adapter.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetAdapterPowerManagementSettingData**](msft-netadapterpowermanagementsettingdata.md)
</dt> </dl>

 

 




