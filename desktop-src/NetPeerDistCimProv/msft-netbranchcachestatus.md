---
Description: Describes overall configuration and state for BranchCache.
ms.assetid: a1255139-3178-466f-8e26-82094e664380
title: MSFT\_NetBranchCacheStatus class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetBranchCacheStatus class

Describes overall configuration and state for BranchCache

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetPeerDist")]
class MSFT_NetBranchCacheStatus : CIM_LogicalElement
{
  string  InstanceID;
  boolean BranchCacheIsEnabled;
  uint32  BranchCacheServiceStatus;
  uint32  BranchCacheServiceStartType;
  string  ClientConfiguration;
  string  ContentServerConfiguration;
  string  HostedCacheServerConfiguration;
  string  NetworkConfiguration;
  string  HashCache;
  string  DataCache;
};
```

## Members

The **MSFT\_NetBranchCacheStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCacheStatus** class has these properties.

<dl> <dt>

**BranchCacheIsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if BranchCache is enabled

</dd> <dt>

**BranchCacheServiceStartType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The start type of the BranchCache service

</dd> <dt>

**BranchCacheServiceStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the BranchCache service

</dd> <dt>

**ClientConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Configuration related to the BranchCache client role

</dd> <dt>

**ContentServerConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Configuration related to the BranchCache content server role

</dd> <dt>

**DataCache**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

BranchCache data cache

</dd> <dt>

**HashCache**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

BranchCache hash cache

</dd> <dt>

**HostedCacheServerConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes configuration related to the BranchCache hosted cache server role

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

Identifies an instance of MSFT\_BranchCache

</dd> <dt>

**NetworkConfiguration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

BranchCache networking configuration

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




