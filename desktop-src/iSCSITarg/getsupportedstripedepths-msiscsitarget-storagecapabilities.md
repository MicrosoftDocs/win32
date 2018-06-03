---
title: GetSupportedStripeDepths method of the MSISCSITARGET\_StorageCapabilities class
description: Retrieves a list of supported values for systems that support discrete user data stripe depths.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4e5abf7f-221d-4252-9218-ff9406820d31
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedStripeDepths method iSCSI Software Target API
- GetSupportedStripeDepths method iSCSI Software Target API , MSISCSITARGET_StorageCapabilities class
- MSISCSITARGET_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeDepths method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageCapabilities.GetSupportedStripeDepths
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedStripeDepths method of the MSISCSITARGET\_StorageCapabilities class

Retrieves a list of supported values for systems that support discrete user data stripe depths.

Different implementations can support either the **GetSupportedStripeDepths** or the [**GetSupportedStripeDepthRange**](getsupportedstripedepthrange-msiscsitarget-storagecapabilities.md) method. If the system only supports a range of sizes, then this method returns **Use GetSupportedStripeDepthRange instead** (2).

This method is inherited from the **CIM\_StorageCapabilities** class.

## Syntax


```mof
uint32 GetSupportedStripeDepths(
  [out] uint64 StripeDepths[]
);
```



## Parameters

<dl> <dt>

*StripeDepths* \[out\]
</dt> <dd>

On return, contains a list of supported user data stripe depths in bytes for a volume or pool.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Use GetSupportedStripeDepthRange instead** (2)
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

[**GetSupportedStripeDepthRange**](getsupportedstripedepthrange-msiscsitarget-storagecapabilities.md)
</dt> </dl>

 

 





