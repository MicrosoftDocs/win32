---
description: Provides a method to enable specific power management capabilities on the adapter.
ms.assetid: 26e17d94-9708-4eb1-8639-b3aa22b6768b
title: Enable method of the MSFT\_NetAdapterPowerManagementSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagementSettingData.Enable
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Enable method of the MSFT\_NetAdapterPowerManagementSettingData class

Provides a method to enable specific power management capabilities on the adapter.

## Syntax


```mof
uint32 Enable(
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

**true** to enable the setting for ARP offloads on the adapter.

</dd> <dt>

*D0PacketCoalescing* \[in\]
</dt> <dd>

**true** to enable the D0 Packet Coalescing on the adapter.

</dd> <dt>

*DeviceSleepOnDisconnect* \[in\]
</dt> <dd>

**true** to enable sleeping on media disconnect on the adapter.

</dd> <dt>

*NSOffload* \[in\]
</dt> <dd>

**true** to enable NS offloads on the adapter.

</dd> <dt>

*RsnRekeyOffload* \[in\]
</dt> <dd>

**true** to enable 802.11i RSN offloading on the adapter.

</dd> <dt>

*SelectiveSuspend* \[in\]
</dt> <dd>

**true** to enable selective suspend on the adapter.

</dd> <dt>

*WakeOnMagicPacket* \[in\]
</dt> <dd>

**true** to enable waking on Magic Packets on the adapter.

</dd> <dt>

*WakeOnPattern* \[in\]
</dt> <dd>

**true** to enable waking on a packet pattern for the adapter.

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

 

 




