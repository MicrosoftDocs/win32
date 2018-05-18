---
title: DnsServerSetting class
description: Represents the settings for a DNS server.
audience: developer
ms.assetid: 'f0a89c2a-797c-4e29-8e75-e3aacc7a8bc1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerSetting class", "DnsServerSetting class, described"]
topic_type:
- apiref
api_name:
- DnsServerSetting
- DnsServerSetting.ComputerName
- DnsServerSetting.NameCheckFlag
- DnsServerSetting.AddressAnswerLimit
- DnsServerSetting.XfrConnectTimeout
- DnsServerSetting.BootMethod
- DnsServerSetting.UpdateOptions
- DnsServerSetting.AllowUpdate
- DnsServerSetting.DsAvailable
- DnsServerSetting.DisableAutoReverseZone
- DnsServerSetting.AutoCacheUpdate
- DnsServerSetting.RoundRobin
- DnsServerSetting.LocalNetPriority
- DnsServerSetting.LocalNetPriorityMask
- DnsServerSetting.StrictFileParsing
- DnsServerSetting.LooseWildcarding
- DnsServerSetting.BindSecondaries
- DnsServerSetting.WriteAuthorityNs
- DnsServerSetting.ForwardDelegations
- DnsServerSetting.AutoConfigFileZones
- DnsServerSetting.EnableDirectoryPartitions
- DnsServerSetting.RpcProtocol
- DnsServerSetting.EnableVersionQuery
- DnsServerSetting.EnableDuplicateQuerySuppression
- DnsServerSetting.LameDelegationTtl
- DnsServerSetting.AutoCreateDelegation
- DnsServerSetting.AllowCNameAtNs
- DnsServerSetting.RemoteIPv4RankBoost
- DnsServerSetting.RemoteIPv6RankBoost
- DnsServerSetting.EnableRsoForRodc
- DnsServerSetting.MaximumRodcRsoQueueLength
- DnsServerSetting.MaximumRodcRsoAttemptsPerCycle
- DnsServerSetting.OpenAclOnProxyUpdates
- DnsServerSetting.NoUpdateDelegations
- DnsServerSetting.EnableUpdateForwarding
- DnsServerSetting.MaxResourceRecordsInNonSecureUpdate
- DnsServerSetting.EnableWinsR
- DnsServerSetting.DeleteOutsideGlue
- DnsServerSetting.AppendMsZoneTransferTag
- DnsServerSetting.AllowReadOnlyZoneTransfer
- DnsServerSetting.MaximumUdpPacketSize
- DnsServerSetting.TcpReceivePacketSize
- DnsServerSetting.EnableSendErrorSuppression
- DnsServerSetting.SelfTest
- DnsServerSetting.XfrThrottleMultiplier
- DnsServerSetting.SilentlyIgnoreCNameUpdateConflicts
- DnsServerSetting.EnableIQueryResponseGeneration
- DnsServerSetting.SocketPoolSize
- DnsServerSetting.AdminConfigured
- DnsServerSetting.ForestDirectoryPartitionBaseName
- DnsServerSetting.DomainDirectoryPartitionBaseName
- DnsServerSetting.ServerLevelPluginDll
- DnsServerSetting.SocketPoolExcludedPortRanges
- DnsServerSetting.EnableRegistryBoot
- DnsServerSetting.PublishAutoNet
- DnsServerSetting.QuietRecvFaultInterval
- DnsServerSetting.QuietRecvLogInterval
- DnsServerSetting.ReloadException
- DnsServerSetting.SyncDsZoneSerial
- DnsServerSetting.SendPort
- DnsServerSetting.AllIPAddress
- DnsServerSetting.ListeningIPAddress
- DnsServerSetting.MajorVersion
- DnsServerSetting.MinorVersion
- DnsServerSetting.BuildNumber
- DnsServerSetting.IsReadOnlyDC
- DnsServerSetting.EnableDnsSec
- DnsServerSetting.EnableOnlineSigning
- DnsServerSetting.MaximumSignatureScanPeriod
- DnsServerSetting.MaximumTrustAnchorActiveRefreshInterval
- DnsServerSetting.EnableIPv6
- DnsServerSetting.RootTrustAnchorsURL
- DnsServerSetting.ZoneWritebackInterval
- DnsServerSetting.ScopeOptionValue
- DnsServerSetting.IgnoreServerLevelPolicies
- DnsServerSetting.IgnoreAllPolicies
- DnsServerSetting.VirtualizationInstanceOptionValue
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerSetting class

Represents the settings for a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSetting
{
  string   ComputerName;
  uint32   NameCheckFlag;
  uint32   AddressAnswerLimit;
  uint32   XfrConnectTimeout;
  uint32   BootMethod;
  uint32   UpdateOptions;
  boolean  AllowUpdate;
  boolean  DsAvailable;
  boolean  DisableAutoReverseZone;
  boolean  AutoCacheUpdate;
  boolean  RoundRobin;
  boolean  LocalNetPriority;
  uint32   LocalNetPriorityMask;
  boolean  StrictFileParsing;
  boolean  LooseWildcarding;
  boolean  BindSecondaries;
  boolean  WriteAuthorityNs;
  boolean  ForwardDelegations;
  uint32   AutoConfigFileZones;
  boolean  EnableDirectoryPartitions;
  uint32   RpcProtocol;
  uint32   EnableVersionQuery;
  boolean  EnableDuplicateQuerySuppression;
  datetime LameDelegationTtl;
  uint32   AutoCreateDelegation;
  boolean  AllowCNameAtNs;
  uint32   RemoteIPv4RankBoost;
  uint32   RemoteIPv6RankBoost;
  boolean  EnableRsoForRodc;
  uint32   MaximumRodcRsoQueueLength;
  uint32   MaximumRodcRsoAttemptsPerCycle;
  boolean  OpenAclOnProxyUpdates;
  boolean  NoUpdateDelegations;
  boolean  EnableUpdateForwarding;
  uint32   MaxResourceRecordsInNonSecureUpdate;
  boolean  EnableWinsR;
  boolean  DeleteOutsideGlue;
  boolean  AppendMsZoneTransferTag;
  boolean  AllowReadOnlyZoneTransfer;
  uint32   MaximumUdpPacketSize;
  uint32   TcpReceivePacketSize;
  boolean  EnableSendErrorSuppression;
  uint32   SelfTest;
  uint32   XfrThrottleMultiplier;
  boolean  SilentlyIgnoreCNameUpdateConflicts;
  boolean  EnableIQueryResponseGeneration;
  uint32   SocketPoolSize;
  boolean  AdminConfigured;
  string   ForestDirectoryPartitionBaseName;
  string   DomainDirectoryPartitionBaseName;
  string   ServerLevelPluginDll;
  string   SocketPoolExcludedPortRanges[];
  uint32   EnableRegistryBoot;
  boolean  PublishAutoNet;
  uint32   QuietRecvFaultInterval;
  uint32   QuietRecvLogInterval;
  boolean  ReloadException;
  uint32   SyncDsZoneSerial;
  uint32   SendPort;
  string   AllIPAddress[];
  string   ListeningIPAddress[];
  uint32   MajorVersion;
  uint32   MinorVersion;
  uint32   BuildNumber;
  boolean  IsReadOnlyDC;
  boolean  EnableDnsSec;
  boolean  EnableOnlineSigning;
  datetime MaximumSignatureScanPeriod;
  datetime MaximumTrustAnchorActiveRefreshInterval;
  boolean  EnableIPv6;
  string   RootTrustAnchorsURL;
  datetime ZoneWritebackInterval;
  uint32   ScopeOptionValue;
  boolean  IgnoreServerLevelPolicies;
  boolean  IgnoreAllPolicies;
  uint32   VirtualizationInstanceOptionValue;
};
```

## Members

The **DnsServerSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSetting** class has these properties.

<dl> <dt>

**AddressAnswerLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the maximum number of A (host IP address) resource records that the DNS server can insert in the answer section of a response to an A record query (a query for an IP address). The value of this entry also influences the setting of the truncation bit. If the value of this entry is between 5 and 28, the truncation bit is not set on the response, even when the packet space is exceeded.

0

Range: 5–28

</dd> <dt>

**AdminConfigured**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the server has been configured by an administrator.

</dd> <dt>

**AllIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains all of the IP addresses managed by the DNS server.

</dd> <dt>

**AllowCNameAtNs**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the server will permit the target domain names of NS records to resolve to CNAME records. If true, this pattern of DNS records will be allowed; otherwise, the DNS server will return errors when encountering this pattern of DNS records while resolving queries.

</dd> <dt>

**AllowReadOnlyZoneTransfer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will allow zone transfers for zones that are stored in the directory server when the directory server does not support write operations.

</dd> <dt>

**AllowUpdate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to allow any DNS update operation; otherwise, **false**.

</dd> <dt>

**AppendMsZoneTransferTag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will indicate to the remote DNS servers that it supports multiple DNS records in each zone transfer response message by appending the characters MS at the end of zone transfer requests. The value SHOULD be limited to 0x00000000 and 0x00000001, but it MAY be any value. The default value SHOULD be 0x00000000, and the value zero MUST be allowed and treated literally.

</dd> <dt>

**AutoCacheUpdate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to cache delegation information; otherwise, **false**.

</dd> <dt>

**AutoConfigFileZones**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of zones for which SOA and NS records will be automatically configured with the DNS server's local host name as the primary DNS server for the zone when the zone is loaded from file.

</dd> <dt>

**AutoCreateDelegation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The possible settings for automatic delegation creation for new zones on the DNS server. The value SHOULD be limited to the range from 0x00000000 to 0x00000002, inclusive, but it MAY be any value. The default value SHOULD be 0x00000002, and the value zero MUST be allowed and treated literally

</dd> <dt>

**BindSecondaries**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to cache delegation information; otherwise, **false**.

A Boolean value indicating whether the server will permit send DNS zone transfer response messages with more than one record in each response if the zone transfer request did not have the characters MS appended to it. If true, the DNS server will include only one record in each response if the zone transfer request did not have the characters MS appended to it.

</dd> <dt>

**BootMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the boot method used by the DNS server.

</dd> <dt>

**BuildNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The build version of the OS of the DNS server.

</dd> <dt>

**ComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The computer name of the DNS server.

</dd> <dt>

**DeleteOutsideGlue**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will delete DNS glue records found outside a delegated subzone when reading records from persistent storage.

</dd> <dt>

**DisableAutoReverseZone**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to disables automatic reverse zones; otherwise, **false**.

</dd> <dt>

**DomainDirectoryPartitionBaseName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applicable only for active directory integrated DNS server. The application directory partition for the domain the DNS server belongs to.

</dd> <dt>

**DsAvailable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the DNS server has Active Directory–integrated DNS enabled; otherwise, **false**.

</dd> <dt>

**EnableDirectoryPartitions**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will support application directory partitions.

</dd> <dt>

**EnableDnsSec**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable DNSSEC validation on the DNS server; otherwise, **false**.

</dd> <dt>

**EnableDuplicateQuerySuppression**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will not send remote queries when there is already a remote query with the same name and query type outstanding.

</dd> <dt>

**EnableIPv6**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable IPv6 on the DNS server; otherwise, **false**.

</dd> <dt>

**EnableIQueryResponseGeneration**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will fabricate IQUERY responses. If set to true, the DNS server MUST fabricate IQUERY responses when it receives queries of type IQUERY. Otherwise, the DNS server will return an error when such queries are received.

</dd> <dt>

**EnableOnlineSigning**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable online signing; otherwise, **false**.

</dd> <dt>

**EnableRegistryBoot**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A value which, if present in local persistent configuration at boot time, indicates that the DNS server MUST rewrite the value of the BootMethod property

</dd> <dt>

**EnableRsoForRodc**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will attempt to replicate single updated DNS objects from remote directory servers ahead of normally scheduled replication when operating on a directory server that does not support write operations.

</dd> <dt>

**EnableSendErrorSuppression**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will attempt to suppress large volumes of DNS error responses sent to remote IP addresses that may be attempting to attack the DNS server.

</dd> <dt>

**EnableUpdateForwarding**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will forward updates received for secondary zones to the primary DNS server for the zone.

</dd> <dt>

**EnableVersionQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property controls what version information the DNS server will respond with when a DNS query with class set to CHAOS and type set to TXT is received. The default value MUST be 0x00000001.

</dd> <dt>

**EnableWinsR**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will perform NetBIOS name resolution in order to map IP addresses to machine names while processing queries in zones where WINS-R information has been configured.

</dd> <dt>

**ForestDirectoryPartitionBaseName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applicable only for active directory integrated DNS server. The application directory partition for the forest the DNS server belongs to.

</dd> <dt>

**ForwardDelegations**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating how the DNS server will handle forwarding and delegations. If set to true, the DNS server MUST use forwarders instead of a cached delegation when both are available. Otherwise, the DNS server MUST use a cached delegation instead of forwarders when both are available.

</dd> <dt>

**IgnoreAllPolicies**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to ignore all policies on the DNS server; otherwise, **false**.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

**IgnoreServerLevelPolicies**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to ignore the server level policies of the DNS server; otherwise, **false**.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

**IsReadOnlyDC**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to enable write operations on the directory server; otherwise, **false**.

</dd> <dt>

**LameDelegationTtl**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time span that must elapse before the DNS server will re-query DNS servers of the parent zone when a lame delegation is encountered. The value SHOULD be limited to the range from 0x00000000 to 0x00278D00 30 days, inclusive, but it MAY be any value.

</dd> <dt>

**ListeningIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the listening IP addresses of the DNS server.

</dd> <dt>

**LocalNetPriority**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to return A records in order of their similarity to the IP address of the querying client.; otherwise, **false**.

</dd> <dt>

**LocalNetPriorityMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A value which specifies the network mask the DNS server will use to sort IPv4 addresses. A value of 0xFFFFFFFF indicates that the DNS server MUST use traditional IPv4 network mask for the address. Any other value is a network mask, in host byte order that the DNS server MUST use to retrieve network masks from IP addresses for sorting purposes. The value's range MUST be unlimited. The default value MUST be 0x000000FF, and the value zero MUST be allowed and treated literally.

</dd> <dt>

**LooseWildcarding**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to cache delegation information; otherwise, **false**.

A Boolean value indicating the type of algorithm that the DNS server will use to locate a wildcard node when using a DNS wildcard record RFC1034 to answer a query. If true, the DNS server will use the first node it encounters with a record of the same type as the query type. Otherwise, the DNS server will use the first node it encounters that has records of any type.

</dd> <dt>

**MajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major version of the OS of the DNS server.

</dd> <dt>

**MaximumRodcRsoAttemptsPerCycle**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of queued single object replication operations that should be attempted during each five minute interval of DNS server operation. The value MUST be limited to the range from 0x00000001 to 0x000F4240, inclusive. The default value MUST be 0x00000064.

</dd> <dt>

**MaximumRodcRsoQueueLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of single object replication operations that may be queued at any given time by the DNS server. The value MUST be limited to the range from 0x00000000 to 0x000F4240, inclusive. If the value is 0x00000000 the DNS server MUST NOT enforce an upper bound on the number of single object replication operations queued at any given time. The default value MUST be 0x0000012C, and the value zero MUST be allowed.

</dd> <dt>

**MaximumSignatureScanPeriod**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum period between zone scans to update DnsSec signatures for resource records.

</dd> <dt>

**MaximumTrustAnchorActiveRefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum value for the active refresh interval for a trust anchor.

</dd> <dt>

**MaximumUdpPacketSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum UDP packet size, in bytes, that the DNS server can accept. The value MUST be limited to 0x00000200 to 0x00004000.&lt;138&gt; The server MUST return an error if an attempt is made to change the value of this property through this protocol. This property may only be changed by modifying the value in persistent storage.

</dd> <dt>

**MaxResourceRecordsInNonSecureUpdate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of resource records that the DNS server will accept in a single DNS update request. The value SHOULD be limited to the range from 0x0000000A to 0x00000078, inclusive, but it MAY be any value. The default value SHOULD be 0x0000001E, and the value zero SHOULD be treated as a flag value for the default, but it MAY be allowed and treated literally.

</dd> <dt>

**MinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor version of the OS of the DNS server.

</dd> <dt>

**NameCheckFlag**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the level of domain name checking and validation on the DNS server.

</dd> <dt>

**NoUpdateDelegations**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will accept DNS updates to delegation records of type NS.

</dd> <dt>

**OpenAclOnProxyUpdates**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server allows sharing of DNS records with the DnsUpdateProxy group when processing updates in secure zones that are stored in the directory service.

</dd> <dt>

**PublishAutoNet**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will publish local IPv4 addresses in the 169.254.x.x subnet as IPv4 addresses for the local machine's domain name.

</dd> <dt>

**QuietRecvFaultInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A property used to debug reception of UDP traffic for a recursive query. This property is the minimum time interval, in seconds, starting when the server begins waiting for the query to arrive on the network, after which the server MAY log a debug message indicating that the server is to stop running. If the value is zero or is less than the value of QuietRecvLogInterval, then the value of QuietRecvLogInterval MUST be used. If the value is greater than or equal to the value of QuietRecvLogInterval, then the literal value of QuietRecvFaultInterval MUST be used. The value's range MUST be unlimited. The default value MUST be 0x00000000. The server MAY ignore this property.

</dd> <dt>

**QuietRecvLogInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A property used to debug reception of UDP traffic for a recursive query. This property is the minimum time interval, in seconds, starting when the server begins waiting for the query to arrive on the network, or when the server logs an eponymous debug message for the query, after which the server MUST log a debug message indicating that the server is still waiting to receive network traffic. If the value is zero, logging associated with the two QuietRecv properties MUST be disabled, and the QuietRecvFaultInterval property MUST be ignored. If the value is non-zero, logging associated with the two QuietRecv properties MUST be enabled, and the QuietRecvFaultInterval property MUST NOT be ignored. The value's range MUST be unlimited. The default value MUST be 0x00000000. The server MAY ignore this property.

</dd> <dt>

**ReloadException**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will perform an internal restart if an unexpected fatal error is encountered.

</dd> <dt>

**RemoteIPv4RankBoost**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A value to add to all IPv4 addresses for remote DNS servers when selecting between IPv4 and IPv6 remote DNS server addresses. The value MUST be limited to the range from 0x00000000 to 0x0000000A, inclusive. The default value MUST be 0x00000000, and the value zero MUST be allowed and treated literally.

</dd> <dt>

**RemoteIPv6RankBoost**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A value to add to all IPv6 addresses for remote DNS servers when selecting between IPv4 and IPv6 remote DNS server addresses. The value MUST be limited to the range from 0x00000000 to 0x0000000A, inclusive. The default value MUST be 0x00000000, and the value zero MUST be allowed and treated literally.

</dd> <dt>

**RootTrustAnchorsURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The URL of the root trust anchor on the DNS server.

**Windows Server 2012:** Not supported.

</dd> <dt>

**RoundRobin**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable Round-robin DNS on the DNS server; otherwise, **false**.

</dd> <dt>

**RpcProtocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS\_RPC\_PROTOCOLS section 2.2.1.1.2 value corresponding to the RPC protocols to which the DNS server will respond. If this value is set to 0x00000000, the DNS server MUST NOT respond to RPC requests for any protocol. The value's range MUST be unlimited, for example, from 0x00000000 to 0xFFFFFFFF. The default value SHOULD be 0x00000005

</dd> <dt>

**ScopeOptionValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The extension mechanism for the DNS (ENDS0) scope setting on the DNS server.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

**SelfTest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A mask value indicating whether data consistency checking should be performed once, each time the service starts. If the check fails, the server posts an event log warning. If the least significant bit (regardless of other bits) of this value is one, the DNS server will verify for each active and update-allowing primary zone, that the IP address records are present in the zone for the zone's SOA record's master server. If the least significant bit (regardless of other bits) of this value is zero, no data consistency checking will be performed. The value's range MUST be from 0x00000000 to 0xFFFFFFFF, inclusive. The default value MUST be 0xFFFFFFFF.

</dd> <dt>

**SendPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The port number to use as the source port when sending UDP queries to a remote DNS server. If set to zero, the DNS server MUST allow the stack to select a random port. The value's range MUST be unlimited. The default value MUST be 0x00000000, and the value zero MUST be allowed and treated literally.

</dd> <dt>

**ServerLevelPluginDll**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the path of a custom plug-in. When DllPath specifies the fully qualified path name of a valid DNS server plug-in, the DNS server calls functions in the plug-in to resolve name queries that are outside the scope of all locally hosted zones. If a queried name is out of the scope of the plug-in, the DNS server performs name resolution using forwarding or recursion, as configured. If DllPath is not specified, the DNS server ceases to use a custom plug-in if a custom plug-in was previously configured.

</dd> <dt>

**SilentlyIgnoreCNameUpdateConflicts**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will ignore CNAME conflicts during DNS update processing.

</dd> <dt>

**SocketPoolExcludedPortRanges**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Excluded port ranges

</dd> <dt>

**SocketPoolSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of UDP sockets per address family that the DNS server will use for sending remote queries.

</dd> <dt>

**StrictFileParsing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to cache delegation information; otherwise, **false**.

A Boolean value indicating whether the DNS server will treat errors encountered while reading zones from a file as fatal.

</dd> <dt>

**SyncDsZoneSerial**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The conditions under which the DNS server should immediately commit uncommitted zone serial numbers to persistent storage. The value SHOULD be limited to the range from 0x00000000 to 0x00000004, inclusive, but it MAY be any value. The default value SHOULD be 0x00000002, and the value zero MUST be allowed and treated literally.

</dd> <dt>

**TcpReceivePacketSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum TCP packet size, in bytes, that the DNS server can accept. The value MUST be limited to the range from 0x00004000 to 0x00010000, inclusive. Values outside of this range MUST cause the server to return an error. The default value MUST be 0x00010000.

</dd> <dt>

**UpdateOptions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the DNS update options used by the DNS server.

</dd> <dt>

**VirtualizationInstanceOptionValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Virtualization instance option to be sent in ENDS0.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**WriteAuthorityNs**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value indicating whether the DNS server will include NS records for the root of a zone in DNS responses that are answered using authoritative zone data.

</dd> <dt>

**XfrConnectTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines the time span, in seconds, in which a primary DNS server waits for a transfer response from its secondary server. The default value is "30". After the time-out value expires, the connection is terminated.

</dd> <dt>

**XfrThrottleMultiplier**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The multiple used to determine how long the DNS server should refuse zone transfer requests after a successful zone transfer has been completed. The total time for which a zone will refuse another zone transfer request at the end of a successful zone transfer is computed as this value multiplied by the number of seconds required for the zone transfer that just completed. The server SHOULD refuse zone transfer requests for no more than ten minutes. The value SHOULD be limited to the range from 0x00000000 to 0x00000064, inclusive, but it MAY be any value. The default value MUST be 0x0000000A, and the value zero MUST be allowed and treated literally.

</dd> <dt>

**ZoneWritebackInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The zone write back interval for file backed zones.

**Windows Server 2012:** Not supported.

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





