---
description: MSFT\_NetAdapterPowerManagement\_Offload\_Arp contains settings related to ARP offloading.
ms.assetid: 40a2c3fa-eeca-4e05-bf7b-1b759f5a5529
title: MSFT\_NetAdapterPowerManagement\_Offload\_Arp class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagement_Offload_Arp
- MSFT_NetAdapterPowerManagement_Offload_Arp.RemoteIPv4Address
- MSFT_NetAdapterPowerManagement_Offload_Arp.HostIPv4Address
- MSFT_NetAdapterPowerManagement_Offload_Arp.MACAddress
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagement\_Offload\_Arp class

MSFT\_NetAdapterPowerManagement\_Offload\_Arp contains settings related to ARP offloading.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagement_Offload_Arp : MSFT_NetAdapterPowerManagement_Offload
{
  string RemoteIPv4Address;
  string HostIPv4Address;
  string MACAddress;
};
```

## Members

The **MSFT\_NetAdapterPowerManagement\_Offload\_Arp** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterPowerManagement\_Offload\_Arp** class has these properties.

<dl> <dt>

**HostIPv4Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the IPv4 address used as the Source Protocol Address (SPA) in ARP responses.

</dd> <dt>

**MACAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the MAC address used as the Source Hardware Address (SHA) field of the ARP response.

</dd> <dt>

**RemoteIPv4Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies an optional IPv4 address representing the Source Protocol Address (SPA) of the ARP request.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




