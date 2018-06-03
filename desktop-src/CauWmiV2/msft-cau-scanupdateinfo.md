---
title: MSFT\_CAU\_ScanUpdateInfo class
description: A dynamic WMI class that represents the result from the ScanUpdates method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d55ca4f6-4d7f-4f50-9561-f162abff2a4e
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAU_ScanUpdateInfo class
- MSFT_CAU_ScanUpdateInfo class, described
topic_type:
- apiref
api_name:
- MSFT_CAU_ScanUpdateInfo
- MSFT_CAU_ScanUpdateInfo.UpdateId
- MSFT_CAU_ScanUpdateInfo.UpdateTitle
- MSFT_CAU_ScanUpdateInfo.UpdateDesc
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_CAU\_ScanUpdateInfo class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the result from the [**ScanUpdates**](scanupdates-msft-caunode.md) method.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAU_ScanUpdateInfo
{
  string UpdateId;
  string UpdateTitle;
  string UpdateDesc;
};
```

## Members

The **MSFT\_CAU\_ScanUpdateInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_CAU\_ScanUpdateInfo** class has these properties.

<dl> <dt>

**UpdateDesc**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the description of the update.

</dd> <dt>

**UpdateId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique identifier for the update.

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



 

 





