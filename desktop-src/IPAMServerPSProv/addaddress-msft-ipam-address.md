---
Description: Adds a new IP Address to IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7bc81f20-a2ad-45ac-8400-2c8b0c951655
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AddAddress method of the MSFT\_IPAM\_Address class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddAddress method of the MSFT\_IPAM\_Address class

Adds a new IP Address to IPAM.

## Syntax


```mof
uint32 AddAddress(
  [in]  string            Address,
  [in]  uint16            NetworkType,
  [in]  string            AddressSpace,
  [in]  string            ManagedByService,
  [in]  string            ServiceInstance,
  [in]  string            DeviceType = Host,
  [in]  string            IPAddressState,
  [in]  uint16            AssignmentType = Static,
  [in]  string            MacAddress,
  [in]  datetime          AssignmentDate,
  [in]  datetime          ExpiryDate,
  [in]  string            Description,
  [in]  string            Owner,
  [in]  string            AssetTag,
  [in]  string            SerialNumber,
  [in]  string            ClientID,
  [in]  string            Duid,
  [in]  uint32            Iaid,
  [in]  string            ReservationServer,
  [in]  string            ReservationName,
  [in]  uint16            ReservationType,
  [in]  string            ReservationDescription,
  [in]  string            DeviceName,
  [in]  string            ForwardLookupZone,
  [in]  string            ForwardLookupPrimaryServer,
  [in]  string            ReverseLookupZone,
  [in]  string            ReverseLookupPrimaryServer,
  [in]  string            CustomConfiguration,
  [out] MSFT_IPAM_Address OutputAddress
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

The new IP address to add.

</dd> <dt>

*NetworkType* \[in\]
</dt> <dd>

The network type of the address.

The possible values are:

<dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>

**Provider** (1)


</dt> <dd></dd> <dt>

<span id="Customer"></span><span id="customer"></span><span id="CUSTOMER"></span>

**Customer** (2)


</dt> <dd></dd> <dt>

<span id="NonVirtualized"></span><span id="nonvirtualized"></span><span id="NONVIRTUALIZED"></span>

**NonVirtualized** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*AddressSpace* \[in\]
</dt> <dd>

The address space that is associated with the IP address.

</dd> <dt>

*ManagedByService* \[in\]
</dt> <dd>

The name of the service that manages the IP address.

</dd> <dt>

*ServiceInstance* \[in\]
</dt> <dd>

The instance of the service that manages the IP address.

</dd> <dt>

*DeviceType* \[in\]
</dt> <dd>

The type of device to which you assigned the address. The default value is "Host".

The possible values are:

<dt>

VM
</dt> <dd>

A virtual machine.

</dd> <dt>

Host
</dt> <dd>

A host device.

</dd> </dl> </dd> <dt>

*IPAddressState* \[in\]
</dt> <dd>

The usage state of the IP address. By default, the address is set to "In-Use". You can specify a valid custom value for this parameter.

</dd> <dt>

*AssignmentType* \[in\]
</dt> <dd>

The type of address assignment used by IPAM to assign the IP address.

The possible values are:

<dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>

**Static** (0)


</dt> <dd></dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (1)


</dt> <dd></dd> <dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>

**Auto** (2)


</dt> <dd></dd> <dt>

<span id="VIP"></span><span id="vip"></span>

**VIP** (3)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*MacAddress* \[in\]
</dt> <dd>

The media access control (MAC) address of the device to which the address is assigned.

</dd> <dt>

*AssignmentDate* \[in\]
</dt> <dd>

The date on which the IP address was assigned to a device.

</dd> <dt>

*ExpiryDate* \[in\]
</dt> <dd>

Specifies an expiration date for the address.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A description of the IP address assignment for a device.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

The name of the owner of the IP address.

</dd> <dt>

*AssetTag* \[in\]
</dt> <dd>

The asset tag associated with the IP address.

</dd> <dt>

*SerialNumber* \[in\]
</dt> <dd>

The serial number of the device that is associated with the IP address.

</dd> <dt>

*ClientID* \[in\]
</dt> <dd>

The ID of the client.

</dd> <dt>

*Duid* \[in\]
</dt> <dd>

The DHCP device unique identifier (DUID) for the client. Clients use the DUID to get an IP address from a DHCPv6 server.

</dd> <dt>

*Iaid* \[in\]
</dt> <dd>

The identity association ID (IAID) of an IPv6 address.

</dd> <dt>

*ReservationServer* \[in\]
</dt> <dd>

The name of the DHCP server on which the DHCP reservation is assigned.

</dd> <dt>

*ReservationName* \[in\]
</dt> <dd>

The name of the DHCP reservation on the DHCP server for the device.

</dd> <dt>

*ReservationType* \[in\]
</dt> <dd>

This specifies the protocols supported by the DHCP reservation.

The possible values are:

<dt>

<span id="DHCP"></span><span id="dhcp"></span>

**DHCP** (0)


</dt> <dd></dd> <dt>

<span id="BootP"></span><span id="bootp"></span><span id="BOOTP"></span>

**BootP** (1)


</dt> <dd></dd> <dt>

<span id="DHCP_and_BootPr"></span><span id="dhcp_and_bootpr"></span><span id="DHCP_AND_BOOTPR"></span>

**DHCP and BootPr** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*ReservationDescription* \[in\]
</dt> <dd>

A description for the DHCP reservation.

</dd> <dt>

*DeviceName* \[in\]
</dt> <dd>

The name of the device to which the IP address is assigned.

</dd> <dt>

*ForwardLookupZone* \[in\]
</dt> <dd>

The name of the forward lookup zone that contains a mapping of host names to IP addresses.

</dd> <dt>

*ForwardLookupPrimaryServer* \[in\]
</dt> <dd>

The name of the DNS server that IPAM uses to resolve host names to IP addresses.

</dd> <dt>

*ReverseLookupZone* \[in\]
</dt> <dd>

The reverse lookup zone that contains the mapping from IP addresses to fully qualified domain names (FQDNs).

</dd> <dt>

*ReverseLookupPrimaryServer* \[in\]
</dt> <dd>

The DNS server that IPAM uses to resolve IP addresses to host names.

</dd> <dt>

*CustomConfiguration* \[in\]
</dt> <dd>

A set of custom metadata for the IP address. The metadata is formatted with semicolon-separated name/value pairs.

</dd> <dt>

*OutputAddress* \[out\]
</dt> <dd>

When this method returns, this parameter receives the IP address object.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_Address**](msft-ipam-address.md)
</dt> </dl>

 

 




