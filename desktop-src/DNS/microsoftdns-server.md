---
title: MicrosoftDNS_Server class
description: The MicrosoftDNS\_Server class describes a DNS Server. Every instance of this class may be associated with one instance of MicrosoftDNS\_Cache, one instance of MicrosoftDNS\_RootHints, and multiple instances of MicrosoftDNS\_Zone.
ms.assetid: 768f5f96-d7a5-472f-afe6-63aa9c0e5258
keywords:
- MicrosoftDNS_Server class DNS
- MicrosoftDNS_Server class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_Server
- MicrosoftDNS_Server.StartService
- MicrosoftDNS_Server.StopService
- MicrosoftDNS_Server.StartScavenging
- MicrosoftDNS_Server.GetDistinguishedName
- MicrosoftDNS_Server.Name
- MicrosoftDNS_Server.Version
- MicrosoftDNS_Server.LogLevel
- MicrosoftDNS_Server.LogFilePath
- MicrosoftDNS_Server.LogFileMaxSize
- MicrosoftDNS_Server.LogIPFilterList
- MicrosoftDNS_Server.EventLogLevel
- MicrosoftDNS_Server.RpcProtocol
- MicrosoftDNS_Server.NameCheckFlag
- MicrosoftDNS_Server.AddressAnswerLimit
- MicrosoftDNS_Server.RecursionRetry
- MicrosoftDNS_Server.RecursionTimeout
- MicrosoftDNS_Server.DsPollingInterval
- MicrosoftDNS_Server.DsTombstoneInterval
- MicrosoftDNS_Server.MaxCacheTTL
- MicrosoftDNS_Server.MaxNegativeCacheTTL
- MicrosoftDNS_Server.SendPort
- MicrosoftDNS_Server.XfrConnectTimeout
- MicrosoftDNS_Server.BootMethod
- MicrosoftDNS_Server.AllowUpdate
- MicrosoftDNS_Server.UpdateOptions
- MicrosoftDNS_Server.DsAvailable
- MicrosoftDNS_Server.DisableAutoReverseZones
- MicrosoftDNS_Server.AutoCacheUpdate
- MicrosoftDNS_Server.NoRecursion
- MicrosoftDNS_Server.RoundRobin
- MicrosoftDNS_Server.LocalNetPriority
- MicrosoftDNS_Server.StrictFileParsing
- MicrosoftDNS_Server.LooseWildcarding
- MicrosoftDNS_Server.BindSecondaries
- MicrosoftDNS_Server.WriteAuthorityNS
- MicrosoftDNS_Server.ForwardDelegations
- MicrosoftDNS_Server.SecureResponses
- MicrosoftDNS_Server.DisjointNets
- MicrosoftDNS_Server.AutoConfigFileZones
- MicrosoftDNS_Server.ScavengingInterval
- MicrosoftDNS_Server.DefaultRefreshInterval
- MicrosoftDNS_Server.DefaultNoRefreshInterval
- MicrosoftDNS_Server.DefaultAgingState
- MicrosoftDNS_Server.EDnsCacheTimeout
- MicrosoftDNS_Server.EnableEDnsProbes
- MicrosoftDNS_Server.EnableDnsSec
- MicrosoftDNS_Server.ServerAddresses
- MicrosoftDNS_Server.ListenAddresses
- MicrosoftDNS_Server.Forwarders
- MicrosoftDNS_Server.ForwardingTimeout
- MicrosoftDNS_Server.IsSlave
- MicrosoftDNS_Server.EnableDirectoryPartitions
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_Server class

The **MicrosoftDNS\_Server** class describes a DNS Server. Every instance of this class may be associated with one instance of [**MicrosoftDNS\_Cache**](microsoftdns-cache.md), one instance of [**MicrosoftDNS\_RootHints**](microsoftdns-roothints.md), and multiple instances of [**MicrosoftDNS\_Zone**](microsoftdns-zone.md).

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_Server : CIM_Service
{
  string  Name;
  uint32  Version;
  uint32  LogLevel;
  string  LogFilePath;
  uint32  LogFileMaxSize;
  string  LogIPFilterList[];
  uint32  EventLogLevel;
  sint32  RpcProtocol;
  uint32  NameCheckFlag;
  uint32  AddressAnswerLimit;
  uint32  RecursionRetry;
  uint32  RecursionTimeout;
  uint32  DsPollingInterval;
  uint32  DsTombstoneInterval;
  uint32  MaxCacheTTL;
  uint32  MaxNegativeCacheTTL;
  uint32  SendPort;
  uint32  XfrConnectTimeout;
  uint32  BootMethod;
  uint32  AllowUpdate;
  uint32  UpdateOptions;
  boolean DsAvailable;
  boolean DisableAutoReverseZones;
  boolean AutoCacheUpdate;
  boolean NoRecursion;
  boolean RoundRobin;
  boolean LocalNetPriority;
  boolean StrictFileParsing;
  boolean LooseWildcarding;
  boolean BindSecondaries;
  boolean WriteAuthorityNS;
  uint32  ForwardDelegations;
  boolean SecureResponses;
  boolean DisjointNets;
  uint32  AutoConfigFileZones;
  uint32  ScavengingInterval;
  uint32  DefaultRefreshInterval;
  uint32  DefaultNoRefreshInterval;
  boolean DefaultAgingState;
  uint32  EDnsCacheTimeout;
  boolean EnableEDnsProbes;
  uint32  EnableDnsSec;
  string  ServerAddresses[];
  string  ListenAddresses[];
  string  Forwarders[];
  uint32  ForwardingTimeout;
  boolean IsSlave;
  boolean EnableDirectoryPartitions;
};
```

## Members

The **MicrosoftDNS\_Server** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_Server** class has these methods.



| Method                   | Description                                                                      |
|:-------------------------|:---------------------------------------------------------------------------------|
| **GetDistinguishedName** | Retrieves DNS distinguished name for the zone.<br/>                        |
| **StartScavenging**      | Starts scavenging stale records in the zones subjected to scavenging.<br/> |
| **StartService**         | Starts the DNS Server.<br/>                                                |
| **StopService**          | Stops the DNS Server.<br/>                                                 |



 

### Properties

The **MicrosoftDNS\_Server** class has these properties.

<dl> <dt>

**AddressAnswerLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum number of host records returned in response to an address request. Values between 5 and 28 are valid.

</dd> <dt>

**AllowUpdate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the DNS Server accepts dynamic update requests. Valid values are as shown in the following table.



| Value                                                                                                | Meaning                                                                                               |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | No Restrictions.<br/>                                                                           |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Does not allow dynamic updates of SOA records.<br/>                                             |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Does not allow dynamic updates of NS records at the zone root.<br/>                             |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Does not allow dynamic updates of NS records not at the zone root (delegation NS records).<br/> |



 

Sum these values to determine the setting value.

</dd> <dt>

**AutoCacheUpdate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server attempts to update its cache entries using data from root servers. When a DNS Server boots, it needs a list of root server 'hints' NS and A records for the servers historically called the cache file. Microsoft DNS Servers have a feature that enables them to attempt to write back a new cache file based on the responses from root servers.

</dd> <dt>

**AutoConfigFileZones**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates which standard primary zones that are authoritative for the name of the DNS Server must be updated when the name server changes. Valid values are as follows:



| Value                                                                                                | Meaning                                                    |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | None.<br/>                                           |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Only servers that allow dynamic updates.<br/>        |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Only servers that do not allow dynamic updates.<br/> |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | All servers.<br/>                                    |



 

The default value is 1.

**Windows Server 2003:  **

The number 3 represents All servers.

</dd> <dt>

**BindSecondaries**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines the AXFR message format when sending to non-Microsoft DNS Server secondaries. When set to TRUE, the DNS Server sends transfers to non-Microsoft DNS Server secondaries in the uncompressed format. When FALSE, all transfers are sent in the fast format.

</dd> <dt>

**BootMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Initialization method for the DNS Server. Valid values are shown in the following table.



| Value                                                                                                | Meaning                                      |
|------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Uninitialized.<br/>                    |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Boot from file.<br/>                   |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Boot from registry.<br/>               |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Boot from directory and registry.<br/> |



 

</dd> <dt>

**DefaultAgingState**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Default **ScavengingInterval** value set for all Active Directory-integrated zones created on this DNS Server. The default value is zero, indicating scavenging is disabled.

</dd> <dt>

**DefaultNoRefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

No-refresh interval, in hours, set for all Active Directory-integrated zones created on this DNS Server. The default value is 168 hours (seven days).

</dd> <dt>

**DefaultRefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Refresh interval, in hours, set for all Active Directory-integrated zones created on this DNS Server. The default value is 168 hours (seven days).

</dd> <dt>

**DisableAutoReverseZones**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server automatically creates standard reverse look up zones.

</dd> <dt>

**DisjointNets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the default port binding for a socket used to send queries to remote DNS Servers can be overridden.

</dd> <dt>

**DsAvailable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether there is an available DS on the DNS Server.

</dd> <dt>

**DsPollingInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Interval, in seconds, to poll the DS-integrated zones.

</dd> <dt>

**DsTombstoneInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of tombstoned records in Directory Service integrated zones, expressed in seconds.

</dd> <dt>

**EDnsCacheTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime, in seconds, of the cached information describing the EDNS version supported by other DNS Servers.

</dd> <dt>

**EnableDirectoryPartitions**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether support for application directory partitions is enabled on the DNS Server.

**Windows Server 2003:  **

This method is named EnableDirectoryPartitionSupport.

</dd> <dt>

**EnableDnsSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the DNS Server includes DNSSEC-specific RRs, KEY, SIG, and NXT in a response, per the following table:



| Value                                                                                                | Meaning                                                                                                                                        |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | No DNSSEC records are included in the response unless the query requested a resource record set of the DNSSEC record type.<br/>          |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | DNSSEC records are included in the response according to RFC 2535.<br/>                                                                  |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | DNSSEC records are included in a response only if the original client query contained the OPT resource record according to RFC 2671<br/> |



 

If a query requests a resource record set of the DNSSEC type, the DNS Server always responds with such records, if available.

</dd> <dt>

**EnableEDnsProbes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the behavior of the DNS Server. When TRUE, the DNS Server always responds with OPT resource records according to RFC 2671, unless the remote server has indicated it does not support EDNS in a prior exchange. If FALSE, the DNS Server responds to queries with OPTs only if OPTs are sent in the original query.

</dd> <dt>

**EventLogLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates which events the DNS Server records in the Event Viewer system log. The following values are used.



| Value                                                                                                | Meaning                                  |
|------------------------------------------------------------------------------------------------------|------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | None.<br/>                         |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Log only errors.<br/>              |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Log only warnings and errors.<br/> |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Log all events.<br/>               |



 

</dd> <dt>

**ForwardDelegations**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether queries to delegated sub-zones are forwarded.

</dd> <dt>

**Forwarders**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enumerates the list of IP addresses of Forwarders to which the DNS Server forwards queries.

</dd> <dt>

**ForwardingTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time, in seconds, a DNS Server forwarding a query will wait for resolution from the [*forwarder*](f-gly.md) before attempting to resolve the query itself.

This value is meaningless if the forwarding server is not set to use recursion. To determine this, check the IsSlave Boolean property.

</dd> <dt>

**IsSlave**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**TRUE** if the DNS server does not use recursion when name-resolution through forwarders fails.

</dd> <dt>

**ListenAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enumerates the list of IP addresses on which the DNS Server can receive queries.

</dd> <dt>

**LocalNetPriority**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server gives priority to the local net address when returning A records.

</dd> <dt>

**LogFileMaxSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Size of the DNS Server debug log, in bytes.

</dd> <dt>

**LogFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

File name and path for the DNS Server debug log. Default is %system32%\\dns\\dns.log. Relative paths are relative to %Systemroot%\\System32. Absolute paths may be used, but UNC paths are not supported.

</dd> <dt>

**LogIPFilterList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

List of IP addresses used to filter DNS events written to the debug log.

</dd> <dt>

**LogLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates which policies are activated in the Event Viewer system log.

Should be set to specific values based on the following algorithm: Every policy (to be activated in the Event Viewer system log) is assigned a specific value.



| Value                                                                                                                  | Meaning                                             |
|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>                   | Query.<br/>                                   |
| <span id="16"></span><dl> <dt>**16**</dt> </dl>                 | Notify.<br/>                                  |
| <span id="32"></span><dl> <dt>**32**</dt> </dl>                 | Update.<br/>                                  |
| <span id="254"></span><dl> <dt>**254**</dt> </dl>               | Nonquery transactions.<br/>                   |
| <span id="256"></span><dl> <dt>**256**</dt> </dl>               | Questions.<br/>                               |
| <span id="512"></span><dl> <dt>**512**</dt> </dl>               | Answers.<br/>                                 |
| <span id="4096"></span><dl> <dt>**4096**</dt> </dl>             | Send.<br/>                                    |
| <span id="8192"></span><dl> <dt>**8192**</dt> </dl>             | Receive.<br/>                                 |
| <span id="16384"></span><dl> <dt>**16384**</dt> </dl>           | UDP.<br/>                                     |
| <span id="32768"></span><dl> <dt>**32768**</dt> </dl>           | TCP.<br/>                                     |
| <span id="65535"></span><dl> <dt>**65535**</dt> </dl>           | All packets.<br/>                             |
| <span id="65536"></span><dl> <dt>**65536**</dt> </dl>           | NT Directory Service write transaction.<br/>  |
| <span id="131072"></span><dl> <dt>**131072**</dt> </dl>         | NT Directory Service update transaction.<br/> |
| <span id="16777216"></span><dl> <dt>**16777216**</dt> </dl>     | Full packets.<br/>                            |
| <span id="2147483648"></span><dl> <dt>**2147483648**</dt> </dl> | Write through.<br/>                           |



 

The sum of the values corresponding to all the policies to be activated is indicated in this property.

</dd> <dt>

**LooseWildcarding**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server performs loose wildcarding. If undefined or zero, the server follows the wildcarding behavior specified in the DNS RFC. In this case, an administrator is advised to include MX records for all hosts incapable of receiving mail. If nonzero, the server seeks the closest wildcard node; in this case, an administrator should put MX records at the zone root and in a wildcard node ('\*') directly below the zone root. Also, administrators should put self-referencing MX records on hosts that receive their own mail.

</dd> <dt>

**MaxCacheTTL**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum time, in seconds, the record of a recursive name query may remain in the DNS Server cache. The DNS Server deletes records from the cache when the value of this entry expires, even if the value of the TTL field in the record is greater.

The default value of this property is 86,400 seconds (1 day).

</dd> <dt>

**MaxNegativeCacheTTL**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum time, in seconds, a name error result from a recursive query may remain in the DNS Server cache. DNS deletes records from the cache when this timer expires, even if the TTL field is greater. Default value is 86,400 (one day).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Fully qualified domain name (FQDN) or IP address of the DNS Server.

</dd> <dt>

**NameCheckFlag**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the set of eligible characters to be used in DNS names. The following values are used.



| Value                                                                                                | Meaning                      |
|------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Strict RFC (ANSI)<br/> |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Non RFC (ANSI)<br/>    |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Multibyte (UTF8)<br/>  |



 

**Windows Server 2003:  **

A value of "2" indicates "Any."

</dd> <dt>

**NoRecursion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server performs recursive look ups. TRUE indicates recursive look ups are not performed.

</dd> <dt>

**RecursionRetry**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Elapsed seconds before retrying a recursive look up. If the property is undefined or zero, retries are made after three seconds. Users are discouraged from altering this property. There are certain situations when the property should be changed; one example is when the DNS Server contacts remote servers over a slow link, and the DNS Server is retrying before receiving response from the remote DNS. In this case, raising the time out to be slightly longer than the observed response time from the remote DNS would be reasonable.

</dd> <dt>

**RecursionTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Elapsed seconds before the DNS Server gives up recursive query. If the property is undefined or zero, the DNS Server gives up after 15 seconds. In general, the 15-second time out is sufficient to allow any outstanding response to get back to the DNS Server.

Users are discouraged from altering this property. One scenario where the property should be changed is when the DNS Server contacts remote servers over a slow link, and the DNS Server is observed rejecting queries (with SERVER\_FAILURE) before responses are received.

Client resolvers also retry queries, so careful investigation is required to determine whether remote responses are actually associated with the query that timed out. In this case, raising the time out value to be slightly longer than the observed response time from the remote DNS would be reasonable.

</dd> <dt>

**RoundRobin**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server round robins multiple A records.

</dd> <dt>

**RpcProtocol**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

RPC protocol or protocols over which administrative RPC runs. The following algorithm is used to assign a specific value:



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | None<br/>        |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | TCP<br/>         |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Named Pipes<br/> |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | LPC<br/>         |



 

The sum of the values indicates the protocols used.

</dd> <dt>

**ScavengingInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Interval, in hours, between two consecutive scavenging operations performed by the DNS Server. Zero indicates scavenging is disabled. The default value is 168 hours (seven days).

</dd> <dt>

**SecureResponses**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server exclusively saves records of names in the same subtree as the server that provided them.

</dd> <dt>

**SendPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Port on which the DNS Server sends UDP queries to other servers. By default, the DNS Server sends queries on a socket bound to the DNS port.

Under certain situations, this is not the best configuration. One obvious case is when an administrator blocks the DNS port with a firewall to prevent outside access to the DNS Server, but still wants the server to be able to contact Internet DNS Servers to provide name resolution for internal clients. Another case is when the DNS Server is supporting disjoint nets (the property **DisjointNets** set to TRUE identifies this scenario). In these cases, setting the **SendOnNonDnsPort** property to a nonzero value directs the DNS Server to bind to an arbitrary port for sending to remote DNS Servers.

If the **SendOnNonDnsPort** value is greater than 1024, the DNS Server binds explicitly to the port value given. This configuration option is useful when an administrator needs to fix the DNS query port for firewall purposes.

**Windows Server 2003:  **

Setting the SendPort property to a non-zero value causes the DNS server to bind to an arbitrary port for sending to remote DNS servers.

</dd> <dt>

**ServerAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Enumerates the list of IP addresses for the DNS Server.

</dd> <dt>

**StrictFileParsing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the DNS Server parses [*zone files*](z-gly.md) strictly. If undefined or zero, the server will log and ignore bad data in the zone file and continue to load. If nonzero, the server will log and fail on zone file errors.

</dd> <dt>

**UpdateOptions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Restricts the type of records that can be dynamically updated on the server, used in addition to the **AllowUpdate** settings on Server and Zone objects.

**Windows Server 2003:  **

0: No restrictions.

1: Do not allow dynamic updates of SOA records.

2: Do not allow dynamic updates of NS records at the zone root.

4: Do not allow dynamic updates of NS records not at the zone root (delegation NS records).

Sum these values to determine the setting value.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of the DNS Server.

</dd> <dt>

**WriteAuthorityNS**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the DNS Server writes NS and SOA records to the authority section on successful response.

</dd> <dt>

**XfrConnectTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time, in seconds, the DNS Server waits for a successful TCP connection to a remote server when attempting a zone transfer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**StartService Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-startservice.md)
</dt> <dt>

[**StopService Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-stopservice.md)
</dt> <dt>

[**StartScavenging Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-startscavenging.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-getdistinguishedname.md)
</dt> </dl>

 

 





