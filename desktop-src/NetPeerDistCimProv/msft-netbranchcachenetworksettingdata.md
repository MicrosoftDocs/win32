---
Description: Describes BranchCache networking settings.
ms.assetid: 1badf1cc-72ea-4eab-bae4-c7057ed21709
title: MSFT\_NetBranchCacheNetworkSettingData class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetBranchCacheNetworkSettingData class

Describes BranchCache networking settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetPeerDist")]
class MSFT_NetBranchCacheNetworkSettingData : MSFT_NetBranchCacheSettingData
{
  boolean ContentRetrievalUrlReservationEnabled;
  boolean HostedCacheHttpUrlReservationEnabled;
  boolean HostedCacheHttpsUrlReservationEnabled;
  boolean ContentRetrievalFirewallRulesEnabled;
  boolean PeerDiscoveryFirewallRulesEnabled;
  boolean HostedCacheServerFirewallRulesEnabled;
  boolean HostedCacheClientFirewallRulesEnabled;
  uint16  ContentDownloadListenPort;
  uint16  ContentDownloadConnectPort;
  uint16  HostedCacheHttpConnectPort;
  uint16  HostedCacheHttpsConnectPort;
  uint16  HostedCacheHttpListenPort;
  uint16  HostedCacheHttpsListenPort;
};
```

## Members

The **MSFT\_NetBranchCacheNetworkSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCacheNetworkSettingData** class has these properties.

<dl> <dt>

**ContentDownloadConnectPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port number to which BranchCache will send outgoing download requests.

</dd> <dt>

**ContentDownloadListenPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port number on which BranchCache is listening for incoming download requests.

</dd> <dt>

**ContentRetrievalFirewallRulesEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the BranchCache Content Retrieval Firewall Rules.

</dd> <dt>

**ContentRetrievalUrlReservationEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the BranchCache Content Retrieval HTTP URL Reservation.

</dd> <dt>

**HostedCacheClientFirewallRulesEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the BranchCache Hosted Cache Client Firewall Rules.

</dd> <dt>

**HostedCacheHttpConnectPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port to which this hosted cache client will offer content to the hosted cache server on its HTTP channel.

</dd> <dt>

**HostedCacheHttpListenPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port on which this hosted cache server will listen for incoming offer messages on its HTTP channel.

</dd> <dt>

**HostedCacheHttpsConnectPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port to which this hosted cache client will offer content to the hosted cache server on its HTTPS channel.

</dd> <dt>

**HostedCacheHttpsListenPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port on which this hosted cache server will listen for incoming offer messages on its HTTPS channel.

</dd> <dt>

**HostedCacheHttpsUrlReservationEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the BranchCache Hosted Cache HTTPS URL Reservation.

</dd> <dt>

**HostedCacheHttpUrlReservationEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the BranchCache Hosted Cache HTTP URL Reservation.

</dd> <dt>

**HostedCacheServerFirewallRulesEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the BranchCache Hosted Cache Server Firewall Rules.

</dd> <dt>

**PeerDiscoveryFirewallRulesEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the BranchCache Peer Discovery Firewall Rules.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




