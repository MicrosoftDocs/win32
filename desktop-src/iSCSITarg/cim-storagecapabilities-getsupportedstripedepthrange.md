---
title: GetSupportedStripeDepthRange method of the CIM\_StorageCapabilities class
description: For systems that support a range of UserDataStripeDepths for volume or pool creation, this method can be used to retrieve the supported range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b51092c5-f7c5-43ca-b0bb-0dfe45b28ac8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedStripeDepthRange method iSCSI Software Target API", "GetSupportedStripeDepthRange method iSCSI Software Target API , CIM_StorageCapabilities class", "CIM_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeDepthRange method"]
topic_type:
- apiref
api_name:
- CIM_StorageCapabilities.GetSupportedStripeDepthRange
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetSupportedStripeDepthRange method of the CIM\_StorageCapabilities class

For systems that support a range of UserDataStripeDepths for volume or pool creation, this method can be used to retrieve the supported range. Note that different implementations may support either the GetSupportedStripeDepths or the GetSupportedStripeDepthRange method. If the system only supports discrete values, then the return value will be set to 2.

## Syntax


```mof
uint32 GetSupportedStripeDepthRange(
  [out] uint64 MinimumStripeDepth,
  [out] uint64 MaximumStripeDepth,
  [out] uint64 StripeDepthDivisor
);
```



## Parameters

<dl> <dt>

*MinimumStripeDepth* \[out\]
</dt> <dd>

The minimum UserDataStripeDepth for a volume/pool in bytes.

</dd> <dt>

*MaximumStripeDepth* \[out\]
</dt> <dd>

The maximum UserDataStripeDepth for a volume/pool in bytes.

</dd> <dt>

*StripeDepthDivisor* \[out\]
</dt> <dd>

A volume/pool UserDataStripeDepth must be a multiple of this value which is specified in bytes.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Use GetSupportedStripeDepths instead** (2)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageCapabilities**](cim-storagecapabilities.md)
</dt> </dl>

 

 





