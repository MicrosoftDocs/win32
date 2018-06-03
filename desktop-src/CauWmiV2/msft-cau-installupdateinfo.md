---
title: MSFT\_CAU\_InstallUpdateInfo class
description: A dynamic WMI class that represents the result from the InstallUpdates method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4a20f772-ed75-4f3b-90b0-f4185e8884f2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAU_InstallUpdateInfo class
- MSFT_CAU_InstallUpdateInfo class, described
topic_type:
- apiref
api_name:
- MSFT_CAU_InstallUpdateInfo
- MSFT_CAU_InstallUpdateInfo.UpdateResultCode
- MSFT_CAU_InstallUpdateInfo.UpdateErrorCode
- MSFT_CAU_InstallUpdateInfo.UpdateTimestamp
- MSFT_CAU_InstallUpdateInfo.UpdateDesc
- MSFT_CAU_InstallUpdateInfo.UpdateId
- MSFT_CAU_InstallUpdateInfo.UpdateTitle
- MSFT_CAU_InstallUpdateInfo.RebootRequired
- MSFT_CAU_InstallUpdateInfo.LongRebootHint
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_CAU\_InstallUpdateInfo class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the result from the [**InstallUpdates**](https://msdn.microsoft.com/library/hh706776) method.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAU_InstallUpdateInfo : MSFT_CAU_DownloadUpdateInfo
{
  uint32   UpdateResultCode;
  sint32   UpdateErrorCode;
  datetime UpdateTimestamp;
  string   UpdateDesc;
  string   UpdateId;
  string   UpdateTitle;
  boolean  RebootRequired;
  boolean  LongRebootHint;
};
```

## Members

The **MSFT\_CAU\_InstallUpdateInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_CAU\_InstallUpdateInfo** class has these properties.

<dl> <dt>

**LongRebootHint**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the update can result in a longer reboot. Updates that are marked in the service pack category or that are greater than 100 megabytes in size may cause long reboots (restart) after the installation, should a restart be required.

</dd> <dt>

**RebootRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the node requires a reboot after installing the update.

</dd> <dt>

**UpdateDesc**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the description of the update.

This property is inherited from [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md).

</dd> <dt>

**UpdateErrorCode**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the error code for a download or installation operation.

This property is inherited from [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md).

</dd> <dt>

**UpdateId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique identifier for the update.

This property is inherited from [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md).

</dd> <dt>

**UpdateResultCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the result code for a download or installation operation.

This property is inherited from [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md).

<dt>

<span id="Succeeded"></span><span id="succeeded"></span><span id="SUCCEEDED"></span>

**Succeeded** (0)


</dt> <dd></dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

**Failed** (1)


</dt> <dd></dd> <dt>

<span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>

**Canceled** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**UpdateTimestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the UTC timestamp when the update was downloaded or installed.

This property is inherited from [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md).

</dd> <dt>

**UpdateTitle**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the title of the update.

This property is inherited from [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



 

 





