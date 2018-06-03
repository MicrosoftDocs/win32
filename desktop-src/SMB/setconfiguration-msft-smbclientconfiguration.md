---
title: SetConfiguration method of the MSFT\_SmbClientConfiguration class
description: Sets one or more SMB client configuration settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 55bb0493-9481-48ed-92df-97accc33202d
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetConfiguration method SMB
- SetConfiguration method SMB , MSFT_SmbClientConfiguration class
- MSFT_SmbClientConfiguration class SMB , SetConfiguration method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetConfiguration method of the MSFT\_SmbClientConfiguration class

Sets one or more SMB client configuration settings.

## Syntax


```mof
uint32 SetConfiguration(
  [in] uint32  ConnectionCountPerRssNetworkInterface,
  [in] uint32  DirectoryCacheEntriesMax,
  [in] uint32  DirectoryCacheEntrySizeMax,
  [in] uint32  DirectoryCacheLifetime,
  [in] boolean EnableBandwidthThrottling,
  [in] boolean EnableByteRangeLockingOnReadOnlyFiles,
  [in] boolean EnableLargeMtu,
  [in] boolean EnableMultiChannel,
  [in] uint32  DormantFileLimit,
  [in] boolean EnableSecuritySignature,
  [in] uint32  ExtendedSessionTimeout,
  [in] uint32  FileInfoCacheEntriesMax,
  [in] uint32  FileInfoCacheLifetime,
  [in] uint32  FileNotFoundCacheEntriesMax,
  [in] uint32  FileNotFoundCacheLifetime,
  [in] uint32  KeepConn,
  [in] uint32  MaxCmds,
  [in] uint32  MaximumConnectionCountPerServer,
  [in] boolean OplocksDisabled,
  [in] boolean RequireSecuritySignature,
  [in] uint32  SessionTimeout,
  [in] boolean UseOpportunisticLocking,
  [in] uint32  WindowSizeThreshold,
  [in] boolean EnableLoadBalanceScaleOut,
  [in] boolean EnableInsecureGuestLogons
);
```



## Parameters

<dl> <dt>

*ConnectionCountPerRssNetworkInterface* \[in\]
</dt> <dd>

The number of TCP connections per RSS network interface.

</dd> <dt>

*DirectoryCacheEntriesMax* \[in\]
</dt> <dd>

The maximum number of entries that can be stored in the directory cache.

</dd> <dt>

*DirectoryCacheEntrySizeMax* \[in\]
</dt> <dd>

The maximum size, in bytes, of an entry in the directory cache.

</dd> <dt>

*DirectoryCacheLifetime* \[in\]
</dt> <dd>

The maximum lifetime, in seconds, of the directory cache.

</dd> <dt>

*EnableBandwidthThrottling* \[in\]
</dt> <dd>

Controls whether bandwidth throttling is enabled.

</dd> <dt>

*EnableByteRangeLockingOnReadOnlyFiles* \[in\]
</dt> <dd>

Controls whether byte-range locking is enabled on read-only files.

</dd> <dt>

*EnableLargeMtu* \[in\]
</dt> <dd>

Controls whether large maximum transmission units (MTU) are enabled.

</dd> <dt>

*EnableMultiChannel* \[in\]
</dt> <dd>

Enable the use of multiple physical network interfaces.

</dd> <dt>

*DormantFileLimit* \[in\]
</dt> <dd>

The maximum number of file handles the SMB network redirector can continue to keep open after the application has closed the corresponding handle.

</dd> <dt>

*EnableSecuritySignature* \[in\]
</dt> <dd>

Controls whether security signatures are enabled.

</dd> <dt>

*ExtendedSessionTimeout* \[in\]
</dt> <dd>

An additional timeout, in seconds, for the SMB client to wait for servers that take more than 45 seconds to respond. (See the *SessionTimeout* parameter.) The default value is zero.

</dd> <dt>

*FileInfoCacheEntriesMax* \[in\]
</dt> <dd>

The maximum number of entries that can be stored in the file information cache.

</dd> <dt>

*FileInfoCacheLifetime* \[in\]
</dt> <dd>

The maximum lifetime, in seconds, of the file information cache.

</dd> <dt>

*FileNotFoundCacheEntriesMax* \[in\]
</dt> <dd>

The maximum number of entries that can be stored in the file not found cache.

</dd> <dt>

*FileNotFoundCacheLifetime* \[in\]
</dt> <dd>

The maximum lifetime, in seconds, of the file not found cache.

</dd> <dt>

*KeepConn* \[in\]
</dt> <dd>

Specifies the maximum amount of time, in seconds, that an idle connection can remain open. If the idle time for a connection reaches the value of this entry, the connection is closed.

</dd> <dt>

*MaxCmds* \[in\]
</dt> <dd>

Specifies the maximum number of network control blocks that the redirector can reserve. The value of this entry coincides with the number of execution threads that can be outstanding simultaneously.

</dd> <dt>

*MaximumConnectionCountPerServer* \[in\]
</dt> <dd>

The maximum number of Multichannel client connections (across multiple interfaces) for a given server. The default value is 8.

</dd> <dt>

*OplocksDisabled* \[in\]
</dt> <dd>

**True** if opportunistic locking is disabled. See *UseOpportunisticLocking.*

</dd> <dt>

*RequireSecuritySignature* \[in\]
</dt> <dd>

Controls whether security signatures are required.

</dd> <dt>

*SessionTimeout* \[in\]
</dt> <dd>

The number of seconds that the client waits before disconnecting an inactive session.

</dd> <dt>

*UseOpportunisticLocking* \[in\]
</dt> <dd>

Controls whether the opportunistic-locking (oplock) performance enhancement is enabled. If **True**, the redirector requests an opportunistic lock on any file opened in "Deny None" mode. As a result, the server performs automatic read-ahead and write-behind caching on behalf of the redirector.

</dd> <dt>

*WindowSizeThreshold* \[in\]
</dt> <dd>

The minimum window size before Multichannel will trigger the use of multiple connections. The default value is 1 for Windows Server operating systems and 8 for Windows client operating systems.

</dd> <dt>

*EnableLoadBalanceScaleOut* \[in\]
</dt> <dd>

Specifies whether load balancing is enabled with scale out clusters. **True** to enable load balancing with scale out clusters; **False** to disable it.

**Windows Server 2012 and Windows 8:** This parameter is not supported before Windows Server 2012 R2 and Windows 8.1.

</dd> <dt>

*EnableInsecureGuestLogons* \[in\]
</dt> <dd>

TBD

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

[**MSFT\_SmbClientConfiguration**](msft-smbclientconfiguration.md)
</dt> </dl>

 

 





