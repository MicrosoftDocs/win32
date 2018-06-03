---
title: MSFT\_SmbClientConfiguration class
description: Represents the configuration settings for an SMB client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c47905a6-d52a-495a-b73f-39b615395c76
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbClientConfiguration class SMB
- MSFT_SmbClientConfiguration class SMB , described
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SmbClientConfiguration class

Represents the configuration settings for an SMB client.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("30")]
class MSFT_SmbClientConfiguration
{
  uint32  ConnectionCountPerRssNetworkInterface;
  uint32  DirectoryCacheEntriesMax;
  uint32  DirectoryCacheEntrySizeMax;
  uint32  DirectoryCacheLifetime;
  boolean EnableBandwidthThrottling;
  boolean EnableByteRangeLockingOnReadOnlyFiles;
  boolean EnableLargeMtu;
  boolean EnableMultiChannel;
  uint32  DormantFileLimit;
  boolean EnableSecuritySignature;
  uint32  ExtendedSessionTimeout;
  uint32  FileInfoCacheEntriesMax;
  uint32  FileInfoCacheLifetime;
  uint32  FileNotFoundCacheEntriesMax;
  uint32  FileNotFoundCacheLifetime;
  uint32  KeepConn;
  uint32  MaxCmds;
  uint32  MaximumConnectionCountPerServer;
  boolean OplocksDisabled;
  boolean RequireSecuritySignature;
  uint32  SessionTimeout;
  boolean UseOpportunisticLocking;
  uint32  WindowSizeThreshold;
  boolean EnableLoadBalanceScaleOut;
  boolean EnableInsecureGuestLogons;
};
```

## Members

The **MSFT\_SmbClientConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbClientConfiguration** class has these methods.



| Method                                                                   | Description                                                    |
|:-------------------------------------------------------------------------|:---------------------------------------------------------------|
| [**GetConfiguration**](getconfiguration-msft-smbclientconfiguration.md) | Retrieves SMB client configuration settings.<br/>        |
| [**SetConfiguration**](setconfiguration-msft-smbclientconfiguration.md) | Sets one or more SMB client configuration settings.<br/> |



 

### Properties

The **MSFT\_SmbClientConfiguration** class has these properties.

<dl> <dt>

**ConnectionCountPerRssNetworkInterface**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of TCP connections per RSS network interface.

</dd> <dt>

**DirectoryCacheEntriesMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of entries that can be stored in the directory cache.

</dd> <dt>

**DirectoryCacheEntrySizeMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum size, in bytes, of an entry in the directory cache.

</dd> <dt>

**DirectoryCacheLifetime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum lifetime, in seconds, of the directory cache.

</dd> <dt>

**DormantFileLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of file handles the SMB network redirector can continue to keep open after the application has closed the corresponding handle.

</dd> <dt>

**EnableBandwidthThrottling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether bandwidth throttling is enabled.

</dd> <dt>

**EnableByteRangeLockingOnReadOnlyFiles**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether byte-range locking is enabled on read-only files.

</dd> <dt>

**EnableInsecureGuestLogons**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2016.

</dd> <dt>

**EnableLargeMtu**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the Large MTU (maximum transmission unit) feature is enabled.

</dd> <dt>

**EnableLoadBalanceScaleOut**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether load balancing is enabled with scale out clusters. **True** to enable load balancing with scale out clusters; **False** to disable it.

**Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2012 R2 and Windows 8.1.

</dd> <dt>

**EnableMultiChannel**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enable the use of multiple physical network interfaces.

</dd> <dt>

**EnableSecuritySignature**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether security signatures are enabled.

</dd> <dt>

**ExtendedSessionTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An additional timeout, in seconds, for the SMB client to wait for servers that take more than 45 seconds to respond. (See the **SessionTimeout** property.) The default value is zero.

</dd> <dt>

**FileInfoCacheEntriesMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of entries that can be stored in the file information cache.

</dd> <dt>

**FileInfoCacheLifetime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum lifetime, in seconds, of the file information cache.

</dd> <dt>

**FileNotFoundCacheEntriesMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of entries that can be stored in the file not found cache.

</dd> <dt>

**FileNotFoundCacheLifetime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum lifetime, in seconds, of the file not found cache.

</dd> <dt>

**KeepConn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the maximum amount of time, in seconds, that an idle connection can remain open. If the idle time for a connection reaches the value of this entry, the connection is closed. The default value is 600.

> [!Note]  
> This is an SMB1-only setting.

 

</dd> <dt>

**MaxCmds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the maximum number of network control blocks that the redirector can reserve. The value of this entry coincides with the number of execution threads that can be outstanding simultaneously.

> [!Note]  
> This is an SMB1-only setting.

 

</dd> <dt>

**MaximumConnectionCountPerServer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of Multichannel client connections (across multiple interfaces) for a given server. The default value is 8.

</dd> <dt>

**OplocksDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if opportunistic locking is disabled. See **UseOpportunisticLocking**.

</dd> <dt>

**RequireSecuritySignature**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether security signatures are required.

</dd> <dt>

**SessionTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of seconds that the client waits before disconnecting an inactive session. The default value is 45.

</dd> <dt>

**UseOpportunisticLocking**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls whether the opportunistic-locking (oplock) performance enhancement is enabled. If enabled, the redirector requests an opportunistic lock on any file opened in "Deny None" mode. As a result, the server performs automatic read-ahead and write-behind caching on behalf of the redirector.

</dd> <dt>

**WindowSizeThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum window size before Multichannel will trigger the use of multiple connections. The default value is 1 for Windows Server operating systems and 8 for Windows client operating systems.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





