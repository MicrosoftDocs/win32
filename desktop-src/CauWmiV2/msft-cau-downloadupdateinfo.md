---
title: MSFT\_CAU\_DownloadUpdateInfo class
description: A dynamic WMI class that represents the result from the DownloadUpdates method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1dedf776-c1c2-43f5-9962-cf0021c32b83
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAU_DownloadUpdateInfo class
- MSFT_CAU_DownloadUpdateInfo class, described
topic_type:
- apiref
api_name:
- MSFT_CAU_DownloadUpdateInfo
- MSFT_CAU_DownloadUpdateInfo.UpdateResultCode
- MSFT_CAU_DownloadUpdateInfo.UpdateErrorCode
- MSFT_CAU_DownloadUpdateInfo.UpdateTimestamp
- MSFT_CAU_DownloadUpdateInfo.UpdateDesc
- MSFT_CAU_DownloadUpdateInfo.UpdateId
- MSFT_CAU_DownloadUpdateInfo.UpdateTitle
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_CAU\_DownloadUpdateInfo class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the result from the [**DownloadUpdates**](https://msdn.microsoft.com/library/hh706773) method.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAU_DownloadUpdateInfo : MSFT_CAU_ScanUpdateInfo
{
  uint32   UpdateResultCode;
  sint32   UpdateErrorCode;
  datetime UpdateTimestamp;
  string   UpdateDesc;
  string   UpdateId;
  string   UpdateTitle;
};
```

## Members

The **MSFT\_CAU\_DownloadUpdateInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_CAU\_DownloadUpdateInfo** class has these properties.

<dl> <dt>

**UpdateDesc**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the description of the update.

</dd> <dt>

**UpdateErrorCode**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the error code for a download or installation operation.

</dd> <dt>

**UpdateId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique identifier for the update.

</dd> <dt>

**UpdateResultCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the result code for a download or installation operation.

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

</dd> <dt>

**UpdateTitle**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the title of the update.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



 

 





