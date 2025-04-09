---
description: MSFT\_NetAdapterPowerManagement\_Offload is the base class for various network adapter offloads.
ms.assetid: cc95129a-c2f7-45c9-b689-38a3513dda7c
title: MSFT\_NetAdapterPowerManagement\_Offload class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagement_Offload
- MSFT_NetAdapterPowerManagement_Offload.OffloadType
- MSFT_NetAdapterPowerManagement_Offload.ID
- MSFT_NetAdapterPowerManagement_Offload.Priority
- MSFT_NetAdapterPowerManagement_Offload.FriendlyName
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagement\_Offload class

MSFT\_NetAdapterPowerManagement\_Offload is the base class for various network adapter offloads.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagement_Offload
{
  uint32 OffloadType;
  uint32 ID;
  uint32 Priority;
  string FriendlyName;
};
```

## Members

The **MSFT\_NetAdapterPowerManagement\_Offload** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterPowerManagement\_Offload** class has these properties.

<dl> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the friendly name of the offload.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the identifier ID of this offload, assigned by the system.

</dd> <dt>

**OffloadType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the type of offload.

<dl> <dt>

<span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span>**Unspecified** (0)
</dt> <dt>

<span id="IPv4Arp"></span><span id="ipv4arp"></span><span id="IPV4ARP"></span>**IPv4Arp** (1)
</dt> <dt>

<span id="IPv6NS"></span><span id="ipv6ns"></span><span id="IPV6NS"></span>**IPv6NS** (2)
</dt> <dt>

<span id="RsnRekey_"></span><span id="rsnrekey_"></span><span id="RSNREKEY_"></span>**RsnRekey** (3 )
</dt> </dl>

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the priority of this offload. A lower value implies a higher priority offload.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




