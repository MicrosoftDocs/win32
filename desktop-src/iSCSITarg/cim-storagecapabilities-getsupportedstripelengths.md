---
title: GetSupportedStripeLengths method of the CIM\_StorageCapabilities class
description: For systems that support discrete ExtentStripeLengths for volume or pool creation, this method can be used to retrieve a list of supported values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ac09efa6-1cf2-4d12-ac53-2cf338229c9b
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedStripeLengths method iSCSI Software Target API
- GetSupportedStripeLengths method iSCSI Software Target API , CIM_StorageCapabilities class
- CIM_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeLengths method
topic_type:
- apiref
api_name:
- CIM_StorageCapabilities.GetSupportedStripeLengths
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedStripeLengths method of the CIM\_StorageCapabilities class

For systems that support discrete ExtentStripeLengths for volume or pool creation, this method can be used to retrieve a list of supported values. Note that different implementations may support either the GetSupportedStripeLengths or the GetSupportedStripeLengthRange method. Also note that the advertised sizes may change after the call due to requests from other clients. If the system only supports a range of sizes, then the return value will be set to 3.

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

List of supported ExtentStripeLengths for a Volume/Pool creation or modification.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Choices not available for this Capability** (2)
</dt> <dt>

**Use GetSupportedStripeLengthRange instead** (3)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageCapabilities**](cim-storagecapabilities.md)
</dt> </dl>

 

 





