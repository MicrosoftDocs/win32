---
title: MSFT\_SmbServerConfiguration class
description: Represents the configuration of an SMB server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae50d789-4cce-4c27-b50d-813d467ffc2a
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbServerConfiguration class SMB
- MSFT_SmbServerConfiguration class SMB , described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SmbServerConfiguration class

Represents the configuration of an SMB server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbServerConfiguration
{
  boolean AnnounceServer;
  uint32  AsynchronousCredits;
  boolean AutoShareServer;
  boolean AutoShareWorkstation;
  uint32  CachedOpenLimit;
  string  AnnounceComment;
  boolean EnableDownlevelTimewarp;
  boolean EnableLeasing;
  boolean EnableMultiChannel;
  boolean EnableStrictNameChecking;
  uint32  AutoDisconnectTimeout;
  uint32  DurableHandleV2TimeoutInSeconds;
  boolean EnableAuthenticateUserSharing;
  boolean EnableForcedLogoff;
  boolean EnableOplocks;
  boolean EnableSecuritySignature;
  boolean ServerHidden;
  uint32  IrpStackSize;
  uint32  KeepAliveTime;
  uint32  MaxChannelPerSession;
  uint32  MaxMpxCount;
  uint32  MaxSessionPerConnection;
  uint32  MaxThreadsPerQueue;
  uint32  MaxWorkItems;
  string  NullSessionPipes;
  string  NullSessionShares;
  uint32  OplockBreakWait;
  uint32  PendingClientTimeoutInSeconds;
  boolean RequireSecuritySignature;
  boolean EnableSMB1Protocol;
  boolean EnableSMB2Protocol;
  uint32  Smb2CreditsMax;
  uint32  Smb2CreditsMin;
  uint32  SmbServerNameHardeningLevel;
  boolean TreatHostAsStableStorage;
  boolean ValidateAliasNotCircular;
  boolean ValidateShareScope;
  boolean ValidateShareScopeNotAliased;
  boolean ValidateTargetName;
  boolean EncryptData;
  boolean RejectUnencryptedAccess;
  boolean AuditSmb1Access;
};
```

## Members

The **MSFT\_SmbServerConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbServerConfiguration** class has these methods.



| Method                                                                   | Description                                           |
|:-------------------------------------------------------------------------|:------------------------------------------------------|
| [**GetConfiguration**](getconfiguration-msft-smbserverconfiguration.md) | Retrieves SMB server configuration values.<br/> |
| [**SetConfiguration**](setconfiguration-msft-smbserverconfiguration.md) | Sets SMB server configuration values.<br/>      |



 

### Properties

The **MSFT\_SmbServerConfiguration** class has these properties.

<dl> <dt>

**AnnounceComment**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string to be used in browser announcements. See the **AnnounceServer** property.

</dd> <dt>

**AnnounceServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the server announces itself via browser announcements.

</dd> <dt>

**AsynchronousCredits**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of concurrent asynchronous SMB commands that are allowed on a single connection.

</dd> <dt>

**AuditSmb1Access**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**AutoDisconnectTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of minutes after which an idle connection will be disconnected.

</dd> <dt>

**AutoShareServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether default server shares will be shared out.

</dd> <dt>

**AutoShareWorkstation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether default workstation shares will be shared out.

</dd> <dt>

**CachedOpenLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls maximum number of cached open files.

</dd> <dt>

**DurableHandleV2TimeoutInSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of minutes after which a handle that has been preserved for durability will be closed by the system if a client has not reclaimed it.

</dd> <dt>

**EnableAuthenticateUserSharing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the connection can be shared among authenticated users.

</dd> <dt>

**EnableDownlevelTimewarp**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether down-level timewarp is enabled.

</dd> <dt>

**EnableForcedLogoff**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether forced logoff will be enabled.

</dd> <dt>

**EnableLeasing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether leasing will be enabled.

</dd> <dt>

**EnableMultiChannel**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether SMB Multichannel is enabled for this server.

</dd> <dt>

**EnableOplocks**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether opportunistic locking is enabled.

</dd> <dt>

**EnableSecuritySignature**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether security signature is enabled.

</dd> <dt>

**EnableSMB1Protocol**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether SMB1 protocol is enabled.

</dd> <dt>

**EnableSMB2Protocol**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether SMB2 protocol is enabled.

</dd> <dt>

**EnableStrictNameChecking**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the server should do strict name checking on incoming connection requests.

</dd> <dt>

**EncryptData**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether this server allows for SMB Encryption. To ensure security, data will be encrypted in flight if this property is **True** or if the **EncryptData** property of the corresponding [**MSFT\_SmbShare**](msft-smbshare.md) object is **True**.

</dd> <dt>

**IrpStackSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the default IRP stack size.

</dd> <dt>

**KeepAliveTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how often TCP attempts to verify that an idle connection is still available by sending a Keep Alive packet. This property overrides the server Keep Alive time setting.

</dd> <dt>

**MaxChannelPerSession**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum number of channels per session.

</dd> <dt>

**MaxMpxCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the maximum MPX count for SMB1.

</dd> <dt>

**MaxSessionPerConnection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum number of sessions that can be served per connection.

</dd> <dt>

**MaxThreadsPerQueue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum threads per worker queue.

</dd> <dt>

**MaxWorkItems**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the maximum SMB1 work items.

</dd> <dt>

**NullSessionPipes**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The pipes allowable by null sessions for this server.

</dd> <dt>

**NullSessionShares**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The shares allowable by null sessions for this server.

</dd> <dt>

**OplockBreakWait**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how long the create caller will wait on an oplock break.

</dd> <dt>

**PendingClientTimeoutInSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of seconds after which a pending client request will be timed out.

</dd> <dt>

**RejectUnencryptedAccess**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if unencrypted access requests should be rejected.

</dd> <dt>

**RequireSecuritySignature**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether security signature is required.

</dd> <dt>

**ServerHidden**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the server will announce itself. If **True**, the server will not announce itself.

</dd> <dt>

**Smb2CreditsMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum number of SMB2 credits.

</dd> <dt>

**Smb2CreditsMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Minimum number of SMB2 credits.

</dd> <dt>

**SmbServerNameHardeningLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The SMB server name hardening level.

</dd> <dt>

**TreatHostAsStableStorage**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the host is treated as stable storage.

</dd> <dt>

**ValidateAliasNotCircular**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether aliases not being circular will be validated.

</dd> <dt>

**ValidateShareScope**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether existence of share scopes will be checked during share creation.

</dd> <dt>

**ValidateShareScopeNotAliased**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether to validate share scopes that are not aliased on creation.

</dd> <dt>

**ValidateTargetName**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether to validate target name on alias creation.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





