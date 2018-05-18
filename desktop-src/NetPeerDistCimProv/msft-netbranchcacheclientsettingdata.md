---
Description: Describes settings related to the BranchCache client role
ms.assetid: '32c58262-0387-4211-bb54-8ef043f9b7e7'
title: 'MSFT\_NetBranchCacheClientSettingData class'
---

# MSFT\_NetBranchCacheClientSettingData class

Describes settings related to the BranchCache client role

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetPeerDist")]
class MSFT_NetBranchCacheClientSettingData : MSFT_NetBranchCacheSettingData
{
  string  CurrentClientMode;
  uint16  PreferredContentInformationVersion;
  boolean DistributedCachingIsEnabled;
  boolean ServeDistributedCachingPeersOnBatteryPower;
  string  HostedCacheServerName;
  uint16  HostedCacheVersion;
  uint32  MinimumSMBLatencyInMilliseconds;
};
```

## Members

The **MSFT\_NetBranchCacheClientSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCacheClientSettingData** class has these properties.

<dl> <dt>

**CurrentClientMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current operating mode of this BranchCache client

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="LocalCache"></span><span id="localcache"></span><span id="LOCALCACHE"></span>**LocalCache** (1)
</dt> <dt>

<span id="DistributedCache"></span><span id="distributedcache"></span><span id="DISTRIBUTEDCACHE"></span>**DistributedCache** (2)
</dt> <dt>

<span id="HostedCache"></span><span id="hostedcache"></span><span id="HOSTEDCACHE"></span>**HostedCache** (3)
</dt> </dl>

</dd> <dt>

**DistributedCachingIsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if Distributed Caching is enabled

</dd> <dt>

**HostedCacheServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Hosted cache servers to which this client will connect

</dd> <dt>

**HostedCacheVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the hosted cache server

</dd> <dt>

**MinimumSMBLatencyInMilliseconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum network latency, in milliseconds, before the SMB client will use BranchCache

</dd> <dt>

**PreferredContentInformationVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The content information version this client will request from content servers

</dd> <dt>

**ServeDistributedCachingPeersOnBatteryPower**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if this client will serve other distributed caching peers when operating on battery power

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




