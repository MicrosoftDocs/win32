---
title: WT\_Host class
description: Represents an iSCSI target.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e484f220-3a89-4647-b9b9-d7e0ffb06ffc'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WT_Host class iSCSI Software Target API", "WT_Host class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- WT_Host
- WT_Host.HostName
- WT_Host.Enabled
- WT_Host.Description
- WT_Host.TargetIQN
- WT_Host.Status
- WT_Host.LastLogIn
- WT_Host.IdleDuration;
- WT_Host.EnableCHAP
- WT_Host.CHAPUserName
- WT_Host.CHAPSecret
- WT_Host.EnableReverseCHAP
- WT_Host.ReverseCHAPUserName
- WT_Host.ReverseCHAPSecret
- WT_Host.TargetMaxRecvDataSegmentLength
- WT_Host.TargetFirstBurstLength
- WT_Host.TargetMaxBurstLength
- WT_Host.NumRecvBuffers
- WT_Host.EnforceIdleTimeoutDetection
- WT_Host.ResourceGroup
- WT_Host.Sessions
- WT_Host.Guid
- WT_Host.MaxConnectionsPerSession
- WT_Host.InitialR2TPreference
- WT_Host.ImmediateDataPreference
- WT_Host.MaxOutstandingR2T
- WT_Host.DataSequenceInOrderPreference
- WT_Host. DataPduInOrderPreference
- WT_Host.DefaultTime2WaitPreference
- WT_Host.DefaultTime2RetainPreference
- WT_Host.ErrorRecoveryLevelPreference
- WT_Host.PrimaryHeaderDigestMethod
- WT_Host.PrimaryDataDigestMethod
- WT_Host.SecondaryHeaderDigestMethod
- WT_Host.SecondaryDataDigestMethod
- WT_Host.RequestingMarkersOnReceive
- WT_Host.PrimaryAuthenticationMethod
- WT_Host.SecondaryAuthenticationMethod
api_location:
- WtWmiProv.dll
api_type:
- DllExport
---

# WT\_Host class

Represents an iSCSI target.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_Host
{
  string     HostName;
  boolean    Enabled;
  string     Description;
  string     TargetIQN;
  sint32     Status;
  datetime   LastLogIn;
  uint32     IdleDuration;;
  boolean    EnableCHAP;
  string     CHAPUserName;
  string     CHAPSecret;
  boolean    EnableReverseCHAP;
  string     ReverseCHAPUserName;
  string     ReverseCHAPSecret;
  uint32     TargetMaxRecvDataSegmentLength;
  uint32     TargetFirstBurstLength;
  uint32     TargetMaxBurstLength;
  uint32     NumRecvBuffers;
  boolean    EnforceIdleTimeoutDetection;
  string     ResourceGroup;
  WT_Session Sessions[];
  string     Guid;
  uint32     MaxConnectionsPerSession;
  boolean    InitialR2TPreference;
  boolean    ImmediateDataPreference;
  uint32     MaxOutstandingR2T;
  boolean    DataSequenceInOrderPreference;
  boolean     DataPduInOrderPreference;
  uint32     DefaultTime2WaitPreference;
  uint32     DefaultTime2RetainPreference;
  uint32     ErrorRecoveryLevelPreference;
  uint16     PrimaryHeaderDigestMethod;
  uint16     PrimaryDataDigestMethod;
  uint16     SecondaryHeaderDigestMethod;
  uint16     SecondaryDataDigestMethod;
  boolean    RequestingMarkersOnReceive;
  uint16     PrimaryAuthenticationMethod;
  uint16     SecondaryAuthenticationMethod;
};
```

## Members

The **WT\_Host** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **WT\_Host** class has these methods.



| Method                                                     | Description                                                                       |
|:-----------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**AddWTDisk**](addwtdisk-wt-host.md)                     | Assigns the specified virtual disk to the target.<br/>                      |
| [**NewHost**](newhost-wt-host.md)                         | Creates a new iSCSI target using the specified target name.<br/>            |
| [**RemoveAllWTDisks**](removeallwtdisks-wt-host.md)       | Removes all virtual disks from the iSCSI target.<br/>                       |
| [**RemoveWTDisk**](removewtdisk-wt-host.md)               | Removes the specified virtual disk from the iSCSI target.<br/>              |
| [**SetWTDiskLunMapping**](setwtdisklunmapping-wt-host.md) | Sets the SCSI Logical Unit Number (LUN) of the specified virtual disk.<br/> |



 

### Properties

The **WT\_Host** class has these properties.

<dl> <dt>

 **DataPduInOrderPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether data PDUs within sequences are preferred to be at continuously increasing addresses.

</dd> <dt>

**CHAPSecret**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string, 12-16 characters in length, that indicates whether a CHAP secret exists. For security reasons, this property value will be encrypted.

</dd> <dt>

**CHAPUserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The CHAP username, typically the initiator IQN.

</dd> <dt>

**DataSequenceInOrderPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether data sequences are preferred to be transferred with continuously non-decreasing sequence offsets.

</dd> <dt>

**DefaultTime2RetainPreference**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Preferred minimum time, in seconds, to wait before attempting an explicit or implicit logout or an active task reassignment after an unexpected connection termination or a connection reset.

</dd> <dt>

**DefaultTime2WaitPreference**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Preferred maximum time, in seconds after an initial wait (Time2Wait), before which an active task reassignment is still possible after an unexpected connection termination or a connection reset.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A user-friendly description for the target.

</dd> <dt>

**EnableCHAP**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether CHAP authentication is enabled for this target. CHAP authentication is the process of the target validating the identity of the initiator.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether or not this iSCSI target is available for access by initiators. If enabled, initiators can discover and login to the target.

> [!Note]  
> Existing initiators remain logged into the target when an iSCSI target is disabled.

 

</dd> <dt>

**EnableReverseCHAP**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether reverse CHAP authentication is enabled for this target. Reverse CHAP authentication is the process of the initiator validating the identity of the target.

</dd> <dt>

**EnforceIdleTimeoutDetection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether Microsoft iSCSI Target Server should periodically contact the initiator to see if it is still connected.

</dd> <dt>

**ErrorRecoveryLevelPreference**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Preferred error recovery level.

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier of the iSCSI target.

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A name that uniquely identifies the iSCSI target within the iSCSI target server. This is not the IQN (iSCSI Qualified Name), but a Microsoft iSCSI Target Server-specific identifier. . It is recommended that the initiatorâ€™s NetBIOS name be used as the host name for easier identification.

</dd> <dt>

**IdleDuration;**
</dt> <dd> <dl> <dt>

Data type: **uint32** 
</dt> <dt>

Access type: Read-only
</dt> </dl>

The idle duration, in seconds, since the most recent session disconnected from the current host.

</dd> <dt>

**ImmediateDataPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether immediate data is preferred.

</dd> <dt>

**InitialR2TPreference**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether an initial R2T request is preferred.

</dd> <dt>

**LastLogIn**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when the last initiator successfully logged on to the Microsoft iSCSI Target Server.

</dd> <dt>

**MaxConnectionsPerSession**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of connections allowed within an iSCSI session.

</dd> <dt>

**MaxOutstandingR2T**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of outstanding R2T requests that are supported.

</dd> <dt>

**NumRecvBuffers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of receive buffers that the Microsoft iSCSI Target Server will use when processing incoming data. It is recommended that you do not change this value. Improperly setting this value can lead to excessive memory usage and performance degradation.

</dd> <dt>

**PrimaryAuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (None, SRP, CHAP, Kerberos), **ValueMap** (2, 3, 4, 5)
</dt> </dl>

Primary authentication method.

</dd> <dt>

**PrimaryDataDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Other, None, CRC32C), **ValueMap** (1, 2, 3)
</dt> </dl>

Primary data digest method.

</dd> <dt>

**PrimaryHeaderDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Other, None, CRC32C), **ValueMap** (1, 2, 3)
</dt> </dl>

Primary header digest method.

</dd> <dt>

**RequestingMarkersOnReceive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether to request markers on receive.

</dd> <dt>

**ResourceGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the cluster group that the iSCSI target resource belongs to. If the Microsoft iSCSI Target Server Service is not running on a Microsoft Failover Cluster, this property is an empty string.

</dd> <dt>

**ReverseCHAPSecret**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string, 12-16 characters in length, that indicates whether a reverse CHAP secret exists. For security reasons, this property value will be encrypted.

</dd> <dt>

**ReverseCHAPUserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The reverse CHAP user name, typically the target IQN.

</dd> <dt>

**SecondaryAuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (None, SRP, CHAP, Kerberos), **ValueMap** (2, 3, 4, 5)
</dt> </dl>

Secondary authentication method.

</dd> <dt>

**SecondaryDataDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Other, None, CRC32C), **ValueMap** (1, 2, 3)
</dt> </dl>

Secondary data digest method.

</dd> <dt>

**SecondaryHeaderDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Other, None, CRC32C), **ValueMap** (1, 2, 3)
</dt> </dl>

Secondary header digest method.

</dd> <dt>

**Sessions**
</dt> <dd> <dl> <dt>

Data type: **WT\_Session** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of sessions that are established between initiators and the iSCSI target provided by the Microsoft iSCSI Target Server service.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Not Connected, Connected), **ValueMap** (0, 1)
</dt> </dl>

Indicates whether the target is currently connected to any initiators.

</dd> <dt>

**TargetFirstBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

iSCSI parameter that indicates the amount of data, in bytes, that the Microsoft iSCSI Target Server can receive before soliciting the initiator. Do not change this value unless you have a thorough understanding of the iSCSI standard. Improperly setting this value can lead to excessive memory usage and performance degradation.

</dd> <dt>

**TargetIQN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The target iSCSI Qualified Name (IQN) of this target.

</dd> <dt>

**TargetMaxBurstLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An iSCSI parameter that indicates the amount of data, in bytes, that Microsoft iSCSI Target Server can receive at once. Do not change this value unless you have a thorough understanding of the iSCSI standard. Improperly setting this value can lead to excessive memory usage and performance degradation.

</dd> <dt>

**TargetMaxRecvDataSegmentLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An iSCSI parameter that indicates the amount of data, in bytes, that the target can process in each Protocol Data Unit (PDU). Do not change this value unless you have a thorough understanding of the iSCSI standard. Improperly setting this value can lead to excessive memory usage and performance degradation.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





