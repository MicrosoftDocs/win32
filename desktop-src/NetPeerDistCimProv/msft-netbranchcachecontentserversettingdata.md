---
Description: Describes settings related to the BranchCache content server role.
ms.assetid: 12fc7705-3edc-4e7b-a3b5-d6b2fafcce05
title: MSFT\_NetBranchCacheContentServerSettingData class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetBranchCacheContentServerSettingData class

Describes settings related to the BranchCache content server role.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetPeerDist")]
class MSFT_NetBranchCacheContentServerSettingData : MSFT_NetBranchCacheSettingData
{
  boolean ContentServerIsEnabled;
};
```

## Members

The **MSFT\_NetBranchCacheContentServerSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCacheContentServerSettingData** class has these properties.

<dl> <dt>

**ContentServerIsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if BranchCache content server functionality is enabled.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




