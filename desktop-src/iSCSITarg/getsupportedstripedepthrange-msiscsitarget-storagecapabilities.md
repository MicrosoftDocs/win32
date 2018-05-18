---
title: GetSupportedStripeDepthRange method of the MSISCSITARGET\_StorageCapabilities class
description: Retrieves the supported stripe depth range for systems that support a range of user data stripe depths.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '67f4feb0-c413-4e09-b348-a16ad56bc383'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedStripeDepthRange method iSCSI Software Target API", "GetSupportedStripeDepthRange method iSCSI Software Target API , MSISCSITARGET_StorageCapabilities class", "MSISCSITARGET_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeDepthRange method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageCapabilities.GetSupportedStripeDepthRange
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetSupportedStripeDepthRange method of the MSISCSITARGET\_StorageCapabilities class

Retrieves the supported stripe depth range for systems that support a range of user data stripe depths.

Different implementations can support either the [**GetSupportedStripeDepths**](getsupportedstripedepths-msiscsitarget-storagecapabilities.md) or the **GetSupportedStripeDepthRange** method. If the system only supports discrete values, then this method returns **Use GetSupportedStripeDepths instead** (2) .

This method is inherited from the **CIM\_StorageCapabilities** class.

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

On return, indicates the minimum user data stripe depth for a volume or pool in bytes.

</dd> <dt>

*MaximumStripeDepth* \[out\]
</dt> <dd>

On return, indicates the maximum user data stripe depth for a volume or pool in bytes.

</dd> <dt>

*StripeDepthDivisor* \[out\]
</dt> <dd>

On return, indicates the size in bytes of an incremental unit of stripe depth. The user data stripe depth for a volume or pool must be an even multiple of this value.

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
| MOF<br/>                      | <dl> <dt>Smiscsitarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
</dt> <dt>

[**GetSupportedStripeDepths**](getsupportedstripedepths-msiscsitarget-storagecapabilities.md)
</dt> </dl>

 

 





