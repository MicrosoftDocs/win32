---
title: GetSupportedStripeLengths method of the MSISCSITARGET\_StorageCapabilities class
description: Retrieves a list of supported extent stripe lengths for systems that support discrete lengths.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12a3f248-8a51-4bdb-9310-c3ad69c2b034
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedStripeLengths method iSCSI Software Target API
- GetSupportedStripeLengths method iSCSI Software Target API , MSISCSITARGET_StorageCapabilities class
- MSISCSITARGET_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeLengths method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageCapabilities.GetSupportedStripeLengths
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedStripeLengths method of the MSISCSITARGET\_StorageCapabilities class

Retrieves a list of supported extent stripe lengths for systems that support discrete lengths. Retrieved values can change after the call due to requests from other clients.

Different implementations can support either the **GetSupportedStripeLengths** or the [**GetSupportedStripeLengthRange**](getsupportedstripelengthrange-msiscsitarget-storagecapabilities.md) method. If the system only supports a range of sizes, then this method returns **Use GetSupportedStripeLengthRange instead** (3).

This method is inherited from the **CIM\_StorageCapabilities** class.

## Syntax


```mof
uint32 GetSupportedStripeLengths(
  [out] uint16 StripeLengths[]
);
```



## Parameters

<dl> <dt>

*StripeLengths* \[out\]
</dt> <dd>

On return, contains a list of extent stripe lengths that are supported for volume or pool creation or modification.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Choices not available for this capability** (2)
</dt> <dt>

**Use GetSupportedStripeLengthRange instead** (3)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>Smiscsitarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
</dt> <dt>

[**GetSupportedStripeLengthRange**](getsupportedstripelengthrange-msiscsitarget-storagecapabilities.md)
</dt> </dl>

 

 





