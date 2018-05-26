---
Description: Describes settings related to the BranchCache hosted cache server role.
ms.assetid: b408beb1-96ac-4bbd-b4dc-7c269e624636
title: MSFT\_NetBranchCacheHostedCacheServerSettingData class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_NetBranchCacheHostedCacheServerSettingData class

Describes settings related to the BranchCache hosted cache server role

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetPeerDist")]
class MSFT_NetBranchCacheHostedCacheServerSettingData : MSFT_NetBranchCacheSettingData
{
  boolean HostedCacheServerIsEnabled;
  string  ClientAuthenticationMode;
  boolean HostedCacheScpRegistrationEnabled;
};
```

## Members

The **MSFT\_NetBranchCacheHostedCacheServerSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCacheHostedCacheServerSettingData** class has these properties.

<dl> <dt>

**ClientAuthenticationMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The authentication mode for hosted cache clients

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>**Domain** (1)
</dt> </dl>

</dd> <dt>

**HostedCacheScpRegistrationEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if BranchCache hosted cache server Scp registration is enabled

</dd> <dt>

**HostedCacheServerIsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if BranchCache hosted cache server is enabled

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




