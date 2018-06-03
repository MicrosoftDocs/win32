---
title: SetConfiguration method of the MSFT\_SmbServerConfiguration class
description: Sets SMB server configuration values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b9435ba2-647f-4fbc-942f-0283ab213d67
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetConfiguration method SMB
- SetConfiguration method SMB , MSFT_SmbServerConfiguration class
- MSFT_SmbServerConfiguration class SMB , SetConfiguration method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetConfiguration method of the MSFT\_SmbServerConfiguration class

Sets SMB server configuration values.

## Syntax


```mof
uint32 SetConfiguration(
  [in] boolean AnnounceServer,
  [in] uint32  AsynchronousCredits,
  [in] boolean AutoShareServer,
  [in] boolean AutoShareWorkstation,
  [in] uint32  CachedOpenLimit,
  [in] string  AnnounceComment,
  [in] boolean EnableDownlevelTimewarp,
  [in] boolean EnableLeasing,
  [in] boolean EnableMultiChannel,
  [in] boolean EnableStrictNameChecking,
  [in] uint32  AutoDisconnectTimeout,
  [in] uint32  DurableHandleV2TimeoutInSeconds,
  [in] boolean EnableAuthenticateUserSharing,
  [in] boolean EnableForcedLogoff,
  [in] boolean EnableOplocks,
  [in] boolean EnableSecuritySignature,
  [in] boolean ServerHidden,
  [in] uint32  IrpStackSize,
  [in] uint32  KeepAliveTime,
  [in] uint32  MaxChannelPerSession,
  [in] uint32  MaxMpxCount,
  [in] uint32  MaxSessionPerConnection,
  [in] uint32  MaxThreadsPerQueue,
  [in] uint32  MaxWorkItems,
  [in] string  NullSessionPipes,
  [in] string  NullSessionShares,
  [in] uint32  OplockBreakWait,
  [in] uint32  PendingClientTimeoutInSeconds,
  [in] boolean RequireSecuritySignature,
  [in] boolean EnableSMB1Protocol,
  [in] boolean EnableSMB2Protocol,
  [in] uint32  Smb2CreditsMax,
  [in] uint32  Smb2CreditsMin,
  [in] uint32  SmbServerNameHardeningLevel,
  [in] boolean TreatHostAsStableStorage,
  [in] boolean ValidateAliasNotCircular,
  [in] boolean ValidateShareScope,
  [in] boolean ValidateShareScopeNotAliased,
  [in] boolean ValidateTargetName,
  [in] boolean EncryptData,
  [in] boolean RejectUnencryptedAccess,
  [in] boolean AuditSmb1Access
);
```



## Parameters

<dl> <dt>

*AnnounceServer* \[in\]
</dt> <dd>

Controls whether the server announces itself via browser announcements.

</dd> <dt>

*AsynchronousCredits* \[in\]
</dt> <dd>

The maximum number of concurrent asynchronous SMB commands that are allowed on a single connection.

</dd> <dt>

*AutoShareServer* \[in\]
</dt> <dd>

Controls whether default server shares will be shared out.

</dd> <dt>

*AutoShareWorkstation* \[in\]
</dt> <dd>

Controls whether default workstation shares will be shared out.

</dd> <dt>

*CachedOpenLimit* \[in\]
</dt> <dd>

Controls the maximum number of cached open files.

</dd> <dt>

*AnnounceComment* \[in\]
</dt> <dd>

A string to be used in browser announcements. See the *AnnounceServer* parameter.

</dd> <dt>

*EnableDownlevelTimewarp* \[in\]
</dt> <dd>

Controls whether down-level timewarp is enabled.

</dd> <dt>

*EnableLeasing* \[in\]
</dt> <dd>

Controls whether leasing will be enabled.

</dd> <dt>

*EnableMultiChannel* \[in\]
</dt> <dd>

Controls whether SMB Multichannel is enabled for this server.

</dd> <dt>

*EnableStrictNameChecking* \[in\]
</dt> <dd>

Controls whether the server should do strict name checking on incoming connection requests.

</dd> <dt>

*AutoDisconnectTimeout* \[in\]
</dt> <dd>

The number of minutes after which an idle connection will be disconnected.

</dd> <dt>

*DurableHandleV2TimeoutInSeconds* \[in\]
</dt> <dd>

Number of minutes after which a handle that has been preserved for durability will be closed by the system if a client has not reclaimed it.

</dd> <dt>

*EnableAuthenticateUserSharing* \[in\]
</dt> <dd>

Controls whether the connection can be shared among authenticated users.

</dd> <dt>

*EnableForcedLogoff* \[in\]
</dt> <dd>

Controls whether forced logoff will be enabled.

</dd> <dt>

*EnableOplocks* \[in\]
</dt> <dd>

Controls whether opportunistic locking will be enabled.

</dd> <dt>

*EnableSecuritySignature* \[in\]
</dt> <dd>

Controls whether security signature will be enabled.

</dd> <dt>

*ServerHidden* \[in\]
</dt> <dd>

Controls whether the server will announce itself. If **True**, the server will not announce itself.

</dd> <dt>

*IrpStackSize* \[in\]
</dt> <dd>

Controls the default IRP stack size.

</dd> <dt>

*KeepAliveTime* \[in\]
</dt> <dd>

Controls how often TCP attempts to verify that an idle connection is still available by sending a Keep Alive packet. This property overrides the server Keep Alive time setting.

</dd> <dt>

*MaxChannelPerSession* \[in\]
</dt> <dd>

Maximum number of channels per session.

</dd> <dt>

*MaxMpxCount* \[in\]
</dt> <dd>

Controls the maximum MPX count for SMB1.

</dd> <dt>

*MaxSessionPerConnection* \[in\]
</dt> <dd>

Maximum number of sessions that can be served per connection.

</dd> <dt>

*MaxThreadsPerQueue* \[in\]
</dt> <dd>

Maximum threads per worker queue.

</dd> <dt>

*MaxWorkItems* \[in\]
</dt> <dd>

Controls the maximum SMB1 work items.

</dd> <dt>

*NullSessionPipes* \[in\]
</dt> <dd>

The pipes allowable by null sessions for this server.

</dd> <dt>

*NullSessionShares* \[in\]
</dt> <dd>

The shares allowable by null sessions for this server.

</dd> <dt>

*OplockBreakWait* \[in\]
</dt> <dd>

Controls how long the create caller will wait on an oplock break.

</dd> <dt>

*PendingClientTimeoutInSeconds* \[in\]
</dt> <dd>

Number of seconds after which a pending client request will be timed out.

</dd> <dt>

*RequireSecuritySignature* \[in\]
</dt> <dd>

Controls whether security signature will be required.

</dd> <dt>

*EnableSMB1Protocol* \[in\]
</dt> <dd>

Controls whether SMB1 protocol will be enabled.

</dd> <dt>

*EnableSMB2Protocol* \[in\]
</dt> <dd>

Controls whether SMB2 protocol will be enabled.

</dd> <dt>

*Smb2CreditsMax* \[in\]
</dt> <dd>

Maximum number of SMB2 credits.

</dd> <dt>

*Smb2CreditsMin* \[in\]
</dt> <dd>

Minimum number of SMB2 credits.

</dd> <dt>

*SmbServerNameHardeningLevel* \[in\]
</dt> <dd>

The SMB server name hardening level.

</dd> <dt>

*TreatHostAsStableStorage* \[in\]
</dt> <dd>

Controls whether the host will be treated as stable storage.

</dd> <dt>

*ValidateAliasNotCircular* \[in\]
</dt> <dd>

Controls whether aliases not being circular will be validated.

</dd> <dt>

*ValidateShareScope* \[in\]
</dt> <dd>

Controls whether existence of share scopes will be checked during share creation.

</dd> <dt>

*ValidateShareScopeNotAliased* \[in\]
</dt> <dd>

Controls whether to validate share scopes that are not aliased on creation.

</dd> <dt>

*ValidateTargetName* \[in\]
</dt> <dd>

Controls whether to validate target name on alias creation.

</dd> <dt>

*EncryptData* \[in\]
</dt> <dd>

Controls whether this server allows for SMB Encryption. To ensure security, data will be encrypted in flight if this parameter is **True** or if the **EncryptData** property of the corresponding [**MSFT\_SmbShare**](msft-smbshare.md) object is **True**.

</dd> <dt>

*RejectUnencryptedAccess* \[in\]
</dt> <dd>

**True** if unencrypted access requests should be rejected.

</dd> <dt>

*AuditSmb1Access* \[in\]
</dt> <dd>

TBD.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012 and Windows 8:** This parameter is not supported before Windows Server 2016 and Windows 10.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbServerConfiguration**](msft-smbserverconfiguration.md)
</dt> </dl>

 

 





