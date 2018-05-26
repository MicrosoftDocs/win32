---
title: Set method of the PS\_DnsServerDsSetting class
description: Sets Active Directory settings.
audience: developer
ms.assetid: d5d1cd59-9be9-49b7-93ba-17c91cac0473
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerDsSetting class
- PS_DnsServerDsSetting class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerDsSetting.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DnsServerDsSetting class

Sets Active Directory settings.

## Syntax


```mof
uint32 Set(
  [in]  datetime           DirectoryPartitionAutoEnlistInterval,
  [in]  uint32             LazyUpdateInterval,
  [in]  uint32             MinimumBackgroundLoadThreads,
  [in]  uint32             RemoteReplicationDelay,
  [in]  string             ComputerName,
  [in]  uint32             PollingInterval,
  [in]  datetime           TombstoneInterval,
  [in]  boolean            PassThru,
  [out] DnsServerDsSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*DirectoryPartitionAutoEnlistInterval* \[in\]
</dt> <dd>

The interval in seconds at which the DNS server will attempt to enlist itself in the DNS domain partition and DNS forest partition if it is not already enlisted. The value should be limited to the range 0x00000E10 (1 hour) to 0x00ED4E00 (180 days), inclusive, but it may be any value. The default value must be 0x00015180 (1 day), and the value zero should be treated as a flag value for the default, but it may be allowed and treated literally.

</dd> <dt>

*LazyUpdateInterval* \[in\]
</dt> <dd>

A value in seconds indicating how frequently the DNS server will submit updates to the directory server without specifying the LDAP\_SERVER\_LAZY\_COMMIT\_OID control (\[MS-ADTS\] section 3.1.1.3.4.1.7) while processing DNS dynamic update requests. This control instructs the directory server that it may sacrifice durability guarantees on updates to improve performance and is meant to improve DNS server update performance. This control must only be sent by the DNS server to the directory server attached to an LDAP update initiated by the DNS server in response to a DNS dynamic update request. If the value is nonzero, LDAP updates performed while processing DNS dynamic update requests must not specify the LDAP\_SERVER\_LAZY\_COMMIT\_OID control, if a period of fewer than DsLazyUpdateInterval seconds has passed since the last LDAP update specifying this control. If a period of time greater than DsLazyUpdateInterval seconds passes in which the DNS server does not perform an LDAP update specifying this control, the DNS server must specify this control on the next update. The value should be limited to the range 0x00000000 to 0x0000003c. The default value must be 0x00000003, and the value zero must be treated as indicating that the DNS server must not specify the LDAP\_SERVER\_LAZY\_COMMIT\_OID control while processing any DNS dynamic update requests

</dd> <dt>

*MinimumBackgroundLoadThreads* \[in\]
</dt> <dd>

The minimum number of background threads that the DNS server will use to load zone data from the directory service. The value must be limited to the range 0x00000000 to 0x00000005, inclusive. The default value must be 0x00000001, and the value zero must be treated as a flag value for the default.

</dd> <dt>

*RemoteReplicationDelay* \[in\]
</dt> <dd>

The minimum interval in seconds that the DNS server must wait between the time it determines that a single object has changed on a remote directory server and the time it attempts to replicate the single object change. The value must be limited to the range 0x00000005 to 0x00000E10, inclusive. The default value must be 0x0000001E, and the value zero must be treated as a flag value for the default.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PollingInterval* \[in\]
</dt> <dd>

Specifies how often the DNS server polls Active Directory for changes in Active Directory-integrated zones. Interval, in seconds, to poll the DS-integrated zones. The interval in seconds at which the DNS server will poll a directory server to obtain updated information for any changes that may have occurred to zones loaded in the server. The values must be between 30 and 3600 seconds inclusive. Range = 30 to 3600.

</dd> <dt>

*TombstoneInterval* \[in\]
</dt> <dd>

Amount of time in seconds to keep tombstoned records in Active Directory alive. The age at which tombstone objects in the directory service will be deleted. The value should be limited to the range 0x0003F480 (3 days) to 0x0049D400 (8 weeks), inclusive, but it may be any value. The default value should be 0x00127500 (14 days), and the value of zero should be treated as a flag value for the default, but it may be allowed and treated literally. Every day at 2:00 AM local time the DNS server must conduct a search of all zones stored in the directory server for nodes which have the dnsTombstoned attribute set to TRUE and an EntombedTime (section 2.2.2.2.3.23 of MS-DNSP) value greater than DsTombstoneInterval seconds in the past. Any such nodes must be permanently deleted from the directory server Range = 295200 to 4838400. The default value = 0x00127500.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDsSetting**](ps-dnsserverdssetting.md)
</dt> </dl>

 

 





