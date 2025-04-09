---
description: MSFT\_NetAdapterPowerManagement\_Offload\_NS contains settings related to Neighbor Solicitation offloading.
ms.assetid: 6c57490d-1e40-4f25-9dc4-da5f346507e4
title: MSFT\_NetAdapterPowerManagement\_Offload\_NS class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagement_Offload_NS
- MSFT_NetAdapterPowerManagement_Offload_NS.RemoteIPv6Address
- MSFT_NetAdapterPowerManagement_Offload_NS.SolicitedNodeIPv6Address
- MSFT_NetAdapterPowerManagement_Offload_NS.MacAddress
- MSFT_NetAdapterPowerManagement_Offload_NS.TargetIPv6Addresses
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagement\_Offload\_NS class

MSFT\_NetAdapterPowerManagement\_Offload\_NS contains settings related to Neighbor Solicitation offloading.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagement_Offload_NS : MSFT_NetAdapterPowerManagement_Offload
{
  string RemoteIPv6Address;
  string SolicitedNodeIPv6Address;
  string MacAddress;
  string TargetIPv6Addresses[];
};
```

## Members

The **MSFT\_NetAdapterPowerManagement\_Offload\_NS** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterPowerManagement\_Offload\_NS** class has these properties.

<dl> <dt>

**MacAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the MAC address used in the TLLA field of the NA message.

</dd> <dt>

**RemoteIPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies an optional IPv6 address representing the Source Address field in the IPv6 header of the NS message.

</dd> <dt>

**SolicitedNodeIPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the solicited node IPv6 address.

</dd> <dt>

**TargetIPv6Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies an array of two IPv6 addresses. An NA message will be sent in response to any NS message with a Target Address field matching either address in this array.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




