---
Description: Exposes static class methods used to complete specific management tasks.
ms.assetid: 300a80a9-cac1-48c3-8948-ea593d93d8e0
title: MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetBranchCacheOrchestrator class

Exposes static class methods used to complete specific management tasks.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetBranchCacheOrchestrator : CIM_ManagedElement
{
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetBranchCacheOrchestrator** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetBranchCacheOrchestrator** class has these methods.



| Method                                                                                                                                      | Description                                                                                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add\_BCDataCacheExtensionByPercentage**](add-bcdatacacheextensionbypercentage-msft-netbranchcacheorchestrator.md)                       | Adds a new republication cache file to increase the amount of storage available on a hosted cache server.<br/>                       |
| [**Add\_BCDataCacheExtensionBySizeBytes**](add-bcdatacacheextensionbysizebytes-msft-netbranchcacheorchestrator.md)                         | Adds a new republication cache file to increase the amount of storage available on a hosted cache server.<br/>                       |
| [**Clear\_BCCache**](clear-bccache-msft-netbranchcacheorchestrator.md)                                                                     | Deletes all data in all cache files.<br/>                                                                                            |
| [**Disable\_BC**](disable-bc-msft-netbranchcacheorchestrator.md)                                                                           | Disables the BranchCache service.<br/>                                                                                               |
| [**Disable\_BCDowngrading**](disable-bcdowngrading-msft-netbranchcacheorchestrator.md)                                                     | Disables downgrading, so that the client will no longer request the specified version of content information from servers.<br/>      |
| [**Disable\_BCServeOnBattery**](disable-bcserveonbattery-msft-netbranchcacheorchestrator.md)                                               | A client may be configured to not listen for content discovery requests in distributed cache mode when operating on battery.<br/>    |
| [**Enable\_BCDistributed**](enable-bcdistributed-msft-netbranchcacheorchestrator.md)                                                       | Enables BranchCache and configures a machine to operate in distributed cache mode.<br/>                                              |
| [**Enable\_BCDowngrading**](enable-bcdowngrading-msft-netbranchcacheorchestrator.md)                                                       | Client may be instructed to operate in a downgraded mode, in which it will issue specified version requests to content servers.<br/> |
| [**Enable\_BCHostedClientByServerNames**](enable-bchostedclientbyservernames-msft-netbranchcacheorchestrator.md)                           | Configures BranchCache to operate in hosted cache client mode.<br/>                                                                  |
| [**Enable\_BCHostedClientByUseSCP**](enable-bchostedclientbyusescp-msft-netbranchcacheorchestrator.md)                                     | Configures BranchCache to operate in hosted cache client mode.<br/>                                                                  |
| [**Enable\_BCHostedServer**](enable-bchostedserver-msft-netbranchcacheorchestrator.md)                                                     | Configures BranchCache to operate in hosted cache server mode.<br/>                                                                  |
| [**Enable\_BCLocal**](enable-bclocal-msft-netbranchcacheorchestrator.md)                                                                   | Enables the BranchCache service in local caching mode.<br/>                                                                          |
| [**Enable\_BCServeOnBattery**](enable-bcserveonbattery-msft-netbranchcacheorchestrator.md)                                                 | Configures a client to listen for content discovery requests in distributed cache mode when operating on battery.<br/>               |
| [**Export\_BCCachePackageByExportDataCache**](export-bccachepackagebyexportdatacache-msft-netbranchcacheorchestrator.md)                   | Exports a cache package.<br/>                                                                                                        |
| [**Export\_BCCachePackageByStagingPath**](export-bccachepackagebystagingpath-msft-netbranchcacheorchestrator.md)                           | Exports a cache package.<br/>                                                                                                        |
| [**Export\_BCSecretKey**](export-bcsecretkey-msft-netbranchcacheorchestrator.md)                                                           | Exports a secret key to a file.<br/>                                                                                                 |
| [**Import\_BCCachePackage**](import-bccachepackage-msft-netbranchcacheorchestrator.md)                                                     | Imports a cache package.<br/>                                                                                                        |
| [**Import\_BCSecretKey**](import-bcsecretkey-msft-netbranchcacheorchestrator.md)                                                           | Imports the cryptographic key used in the generation of segment secrets.<br/>                                                        |
| [**Publish\_BCFileHashes**](publish-bcfilehashes-msft-netbranchcacheorchestrator.md)                                                       | Creates hashes for file content.<br/>                                                                                                |
| [**Publish\_BCWebHashes**](publish-bcwebhashes-msft-netbranchcacheorchestrator.md)                                                         | Creates hashes for web content.<br/>                                                                                                 |
| [**Remove\_BCDataCacheExtensionByDataCacheExtension**](remove-bcdatacacheextensionbydatacacheextension-msft-netbranchcacheorchestrator.md) | Deletes a cache file.<br/>                                                                                                           |
| [**Remove\_BCDataCacheExtensionByPath**](remove-bcdatacacheextensionbypath-msft-netbranchcacheorchestrator.md)                             | Deletes a cache file.<br/>                                                                                                           |
| [**Reset\_BC**](reset-bc-msft-netbranchcacheorchestrator.md)                                                                               | Resets BranchCache to a default configuration.<br/>                                                                                  |
| [**Set\_BCAuthentication**](set-bcauthentication-msft-netbranchcacheorchestrator.md)                                                       | Specifies the authentication scheme for clients.<br/>                                                                                |
| [**Set\_BCCacheByCache**](set-bccachebycache-msft-netbranchcacheorchestrator.md)                                                           | Modifies the cache file configuration.<br/>                                                                                          |
| [**Set\_BCCacheByPath**](set-bccachebypath-msft-netbranchcacheorchestrator.md)                                                             | Modifies the cache file configuration.<br/>                                                                                          |
| [**Set\_BCDataCacheEntryMaxAge**](set-bcdatacacheentrymaxage-msft-netbranchcacheorchestrator.md)                                           | Sets the maximum age of an entry in the data cache.<br/>                                                                             |
| [**Set\_BCMinSMBLatency**](set-bcminsmblatency-msft-netbranchcacheorchestrator.md)                                                         | Sets the minimum latency that must exist between client and server before transparent caching functions are used.<br/>               |
| [**Set\_BCSecretKey**](set-bcsecretkey-msft-netbranchcacheorchestrator.md)                                                                 | Sets the cryptographic key used in the generation of segment secrets.<br/>                                                           |



 

### Properties

The **MSFT\_NetBranchCacheOrchestrator** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




