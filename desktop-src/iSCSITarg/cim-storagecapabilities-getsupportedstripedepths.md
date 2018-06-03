---
title: GetSupportedStripeDepths method of the CIM\_StorageCapabilities class
description: For systems that support discrete UserDataStripeDepths for volume or pool creation, this method can be used to retrieve a list of supported values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bdebfc2b-1194-42ff-8699-f97a5ebca3ae
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedStripeDepths method iSCSI Software Target API
- GetSupportedStripeDepths method iSCSI Software Target API , CIM_StorageCapabilities class
- CIM_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeDepths method
topic_type:
- apiref
api_name:
- CIM_StorageCapabilities.GetSupportedStripeDepths
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedStripeDepths method of the CIM\_StorageCapabilities class

For systems that support discrete UserDataStripeDepths for volume or pool creation, this method can be used to retrieve a list of supported values. Note that different implementations may support either the GetSupportedStripeDepths or the GetSupportedStripeDepthRange method. If the system only supports a range of sizes, then the return value will be set to 2.

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

List of supported UserDataStripeDepths for a Volume/Pool creation or modification.

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
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageCapabilities**](cim-storagecapabilities.md)
</dt> </dl>

 

 





