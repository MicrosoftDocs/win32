---
title: SetByParameters method of the PS\_DnsServerPrimaryZone class
description: Overwrites settings of DNS server primary zone.
audience: developer
ms.assetid: 'ac03176c-ddd9-4461-9abc-548f17df4611'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByParameters method", "SetByParameters method, PS_DnsServerPrimaryZone class", "PS_DnsServerPrimaryZone class, SetByParameters method"]
topic_type:
- apiref
api_name:
- PS_DnsServerPrimaryZone.SetByParameters
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# SetByParameters method of the PS\_DnsServerPrimaryZone class

Overwrites settings of DNS server primary zone.

## Syntax


```mof
uint32 SetByParameters(
  [in]  string               AllowedDcForNsRecordsAutoCreation[],
  [in]  string               DynamicUpdate,
  [in]  string               Name,
  [in]  string               Notify,
  [in]  string               NotifyServers[],
  [in]  string               SecondaryServers[],
  [in]  string               SecureSecondaries,
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [in]  boolean              IsPluginEnabled,
  [in]  boolean              IgnorePolicies,
  [out] DnsServerPrimaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*AllowedDcForNsRecordsAutoCreation* \[in\]
</dt> <dd>

to allow name server (NS) resource record creation for specific domain controllers. Specifies the IP addresses of the domain controllers that add their names in NS resource records for the zone that is specified in ZoneName. Type a space-separated list of the IP addresses of the DNS servers, for example, 10.0.0.0 172.16.0.0 192.168.0.0

</dd> <dt>

*DynamicUpdate* \[in\]
</dt> <dd>

Determines whether the specified zone accepts dynamic updates.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Secure"></span><span id="secure"></span><span id="SECURE"></span>

**Secure** ("Secure")


</dt> <dd></dd> <dt>

<span id="NonsecureAndSecure"></span><span id="nonsecureandsecure"></span><span id="NONSECUREANDSECURE"></span>

**NonsecureAndSecure** ("NonsecureAndSecure")


</dt> <dd></dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*Notify* \[in\]
</dt> <dd>

Indicates whether the master Zone notifies secondaries of any changes in its RRs database. Set to 1 to notify secondaries. Specifies a change notification is sent only to certain secondary servers. nonotify: Specifies that no change notifications are sent to secondary servers. notify: Specifies that change notifications are sent to all secondary servers. notifylist: Specifies that change notifications are sent to only the list of servers. This command must be followed by an IP address or addresses that the master server uses. NotifyIPAddresses: Specifies the IP address(es) of the secondary server(s) to which change notifications are sent. This list is used only with the /notifylist parameter. {NoNotify\|Notify\|NotifyServers}

The possible values are.

<dt>

<span id="NoNotify"></span><span id="nonotify"></span><span id="NONOTIFY"></span>

**NoNotify** ("NoNotify")


</dt> <dd></dd> <dt>

<span id="Notify"></span><span id="notify"></span><span id="NOTIFY"></span>

**Notify** ("Notify")


</dt> <dd></dd> <dt>

<span id="NotifyServers"></span><span id="notifyservers"></span><span id="NOTIFYSERVERS"></span>

**NotifyServers** ("NotifyServers")


</dt> <dd></dd> </dl> </dd> <dt>

*NotifyServers* \[in\]
</dt> <dd>

Specifies Array of strings enumerating IP addresses of DNS servers to be notified of changes in this zone.

</dd> <dt>

*SecondaryServers* \[in\]
</dt> <dd>

Specifies array of IP addresses enumerating IP addresses of DNS servers allowed to receive this zone through zone replication

</dd> <dt>

*SecureSecondaries* \[in\]
</dt> <dd>

Indicates whether zone transfer is allowed to designated secondaries only. Designated secondaries are DNS Servers whose IP addresses are listed in SecondariesIPAddressesArray.

The possible values are.

<dt>

<span id="NoTransfer"></span><span id="notransfer"></span><span id="NOTRANSFER"></span>

**NoTransfer** ("NoTransfer")


</dt> <dd></dd> <dt>

<span id="TransferAnyServer"></span><span id="transferanyserver"></span><span id="TRANSFERANYSERVER"></span>

**TransferAnyServer** ("TransferAnyServer")


</dt> <dd></dd> <dt>

<span id="TransferToZoneNameServer"></span><span id="transfertozonenameserver"></span><span id="TRANSFERTOZONENAMESERVER"></span>

**TransferToZoneNameServer** ("TransferToZoneNameServer")


</dt> <dd></dd> <dt>

<span id="TransferToSecureServers"></span><span id="transfertosecureservers"></span><span id="TRANSFERTOSECURESERVERS"></span>

**TransferToSecureServers** ("TransferToSecureServers")


</dt> <dd></dd> </dl> </dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*IsPluginEnabled* \[in\]
</dt> <dd>

Marks the zone as a plugin-enabled zone.

**Windows Server 2012:** Not supported.

</dd> <dt>

*IgnorePolicies* \[in\]
</dt> <dd>

Whether to ignore the policies of this zone.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerPrimaryZone**](dnsserverprimaryzone.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerPrimaryZone**](ps-dnsserverprimaryzone.md)
</dt> </dl>

 

 





