---
title: GetSupportedStripeLengthRange method of the CIM\_StorageCapabilities class
description: For systems that support a range of ExtentStripeLengths for volume or pool creation, this method can be used to retrieve the supported range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a07694d6-b28c-43fc-9f5c-b7d5b7692c5c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedStripeLengthRange method iSCSI Software Target API
- GetSupportedStripeLengthRange method iSCSI Software Target API , CIM_StorageCapabilities class
- CIM_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeLengthRange method
topic_type:
- apiref
api_name:
- CIM_StorageCapabilities.GetSupportedStripeLengthRange
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedStripeLengthRange method of the CIM\_StorageCapabilities class

For systems that support a range of ExtentStripeLengths for volume or pool creation, this method can be used to retrieve the supported range. Note that different implementations may support either the GetSupportedExtentLengths or the GetSupportedExtentLengthRange method. Also note that the advertised sizes may change after the call due to requests from other clients. If the system only supports discrete values, then the return value will be set to 3.

## Syntax


```mof
uint32 GetSupportedStripeLengthRange(
  [out] uint16 MinimumStripeLength,
  [out] uint16 MaximumStripeLength,
  [out] uint32 StripeLengthDivisor
);
```



## Parameters

<dl> <dt>

*MinimumStripeLength* \[out\]
</dt> <dd>

The minimum ExtentStripeDepth for a volume/pool in bytes.

</dd> <dt>

*MaximumStripeLength* \[out\]
</dt> <dd>

The maximum ExtentStripeLength for a volume/pool in bytes.

</dd> <dt>

*StripeLengthDivisor* \[out\]
</dt> <dd>

A volume/pool ExtentStripeLength must be a multiple of this value which is specified in bytes.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Choices not available for this Capability** (2)
</dt> <dt>

**Use GetSupportedStripeLengths instead** (3)
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

 

 





