---
title: Msvm\_CollectionReplicationSettingData class
description: The class that represents configured settings for a Msvm\_VirtualSystemCollection object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cf578319-03ed-42e0-bcf6-5e8433cccedc
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_CollectionReplicationSettingData class
- Msvm_CollectionReplicationSettingData class, described
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationSettingData
- Msvm_CollectionReplicationSettingData.Caption
- Msvm_CollectionReplicationSettingData.Description
- Msvm_CollectionReplicationSettingData.InstanceID
- Msvm_CollectionReplicationSettingData.ElementName
- Msvm_CollectionReplicationSettingData.AuthenticationType
- Msvm_CollectionReplicationSettingData.CertificateThumbPrint
- Msvm_CollectionReplicationSettingData.RootCertificateThumbPrint
- Msvm_CollectionReplicationSettingData.CompressionEnabled
- Msvm_CollectionReplicationSettingData.BypassProxyServer
- Msvm_CollectionReplicationSettingData.RecoveryConnectionPoint
- Msvm_CollectionReplicationSettingData.PrimaryConnectionPoint
- Msvm_CollectionReplicationSettingData.RecoveryServerPortNumber
- Msvm_CollectionReplicationSettingData.ReplicateHostKvpItems
- Msvm_CollectionReplicationSettingData.ApplicationConsistentSnapshotInterval
- Msvm_CollectionReplicationSettingData.RecoveryHistory
- Msvm_CollectionReplicationSettingData.AutoResynchronizeEnabled
- Msvm_CollectionReplicationSettingData.AutoResynchronizeIntervalStart
- Msvm_CollectionReplicationSettingData.AutoResynchronizeIntervalEnd
- Msvm_CollectionReplicationSettingData.ReplicationInterval
- Msvm_CollectionReplicationSettingData.IncludedDisks
- Msvm_CollectionReplicationSettingData.RecoveryServerHosts
- Msvm_CollectionReplicationSettingData.PrimaryReplicationEntityIDs
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_CollectionReplicationSettingData class

The class that represents configured settings for a [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionReplicationSettingData : Msvm_CollectionSettingData
{
  string   Caption;
  string   Description;
  string   InstanceID;
  string   ElementName;
  uint16   AuthenticationType;
  string   CertificateThumbPrint;
  string   RootCertificateThumbPrint;
  boolean  CompressionEnabled;
  boolean  BypassProxyServer;
  string   RecoveryConnectionPoint;
  string   PrimaryConnectionPoint;
  uint16   RecoveryServerPortNumber;
  boolean  ReplicateHostKvpItems;
  uint16   ApplicationConsistentSnapshotInterval;
  uint16   RecoveryHistory;
  boolean  AutoResynchronizeEnabled = TRUE;
  datetime AutoResynchronizeIntervalStart;
  datetime AutoResynchronizeIntervalEnd;
  uint16   ReplicationInterval;
  string   IncludedDisks[];
  string   RecoveryServerHosts[];
  string   PrimaryReplicationEntityIDs[];
};
```

## Members

The **Msvm\_CollectionReplicationSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectionReplicationSettingData** class has these properties.

<dl> <dt>

**ApplicationConsistentSnapshotInterval**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval, in hours, between application consistent snapshots. This property can contain values from 1 hour to 12 hours.

</dd> <dt>

**AuthenticationType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The authentication mode used to connect to the recovery server.

<dt>

<span id="Kerberos_authentication"></span><span id="kerberos_authentication"></span><span id="KERBEROS_AUTHENTICATION"></span>

**Kerberos authentication** (1)


</dt> <dd></dd> <dt>

<span id="Certificate_based_authentication"></span><span id="certificate_based_authentication"></span><span id="CERTIFICATE_BASED_AUTHENTICATION"></span>

**Certificate based authentication** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**AutoResynchronizeEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to automatically perform a synchronization operation for replication errors due to power and hardware failures; otherwise, **false**.

</dd> <dt>

**AutoResynchronizeIntervalEnd**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The end time to use for auto synchronization when **AutoResynchronizeEnabled** is true. The default value is 0600 hours local time.

</dd> <dt>

**AutoResynchronizeIntervalStart**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The start time to use for auto synchronization when **AutoResynchronizeEnabled** is true. The default value is 1830 hours local time.

</dd> <dt>

**BypassProxyServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to bypass the proxy server when connected to the recovery server; otherwise, **false**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CertificateThumbPrint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](https://msdn.microsoft.com/library/aa393650) (128)
</dt> </dl>

The certificate thumb print to use when **AuthenticationType** is set to "2" (certificate based authorization).

</dd> <dt>

**CompressionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if compression is enabled when sending data to the recovery server; otherwise, **false**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for an instance of this class. In addition, the user-friendly name can be used as an index for a search or query. The name does not have to be unique within a namespace.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**IncludedDisks**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **HyperVEmbeddedInstance** ("CIM\_StorageAllocationSettingData"), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The list of VHDs attached to any of the **ComputerSystem** of the collection that will be included for replication. This is an array of strings each containing the **InstanceID** of the resource allocation setting data (RASD) of the VHD present in the group.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> -   *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID** property, or be a registered ID that is assigned by a recognized global authority.
> -   *OrgID* must not contain a colon. The first colon in **InstanceID** must be between the *OrgID* and*LocalID*.
> -   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
> -   If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
> -   For DMTF defined instances, the pattern must be used with the *OrgID* set to "CIM".

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**PrimaryConnectionPoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the primary connection point. For a primary cluster, this is the broker CAP name. For a standalone primary server, this is the host system name.

</dd> <dt>

**PrimaryReplicationEntityIDs**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The list of replication entities in a primary group i.e., the group ID and the virtual machine IDs. These are required when there is no broker present in the cluster.

For example: GroupId,Vm1Id,Vm2Id.

</dd> <dt>

**RecoveryConnectionPoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the connection point on the recovery server. For a recovery cluster, this is the broker CAP name. For a standalone recovery server, this is the host system name. If an external provider is used, this represents the connection point specific to the provider.

</dd> <dt>

**RecoveryHistory**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of recovery snapshots stored on the recovery server. This property can contain values from "0" to "16".

</dd> <dt>

**RecoveryServerHosts**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The list of recovery servers corresponding to the primary entity IDs, where the entity has to be placed on recovery side.

For example: RecoveryServer1forGroupId,RecoveryServer2forVm1Id,RecoveryServer1forVm2Id.

</dd> <dt>

**RecoveryServerPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The recovery server port number to use when making a secure connection for replication.

</dd> <dt>

**ReplicateHostKvpItems**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to enable a host-only [**Msvm\_KvpExchangeDataItem**](https://msdn.microsoft.com/library/windows/desktop/hh850171) object from a primary virtual machine to a recovery virtual machine; otherwise, **false**. **true** is the default value.

</dd> <dt>

**ReplicationInterval**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The replication interval to use for replication relationships, in seconds. Valid values fpr this property are "30", "300", "900".

</dd> <dt>

**RootCertificateThumbPrint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](https://msdn.microsoft.com/library/aa393650) (128)
</dt> </dl>

The root certificate thumb print of the certificate to use when **AuthenticationType** is set to "2" (certificate based authorization).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionSettingData**](msvm-collectionsettingdata.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





