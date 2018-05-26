---
title: Get method of the PS\_IPFilter class
description: Retrieves the IP filters for the specified BGP router interface.
audience: developer
ms.assetid: d5248b63-ba5a-4a6c-a845-8fcf3b7e8df7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_IPFilter class
- PS_IPFilter class, Get method
topic_type:
- apiref
api_name:
- PS_IPFilter.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_IPFilter class

Retrieves the IP filters for the specified BGP router interface.

## Syntax


```mof
uint32 Get(
  [in]  string            InterfaceAlias,
  [in]  uint32            Direction,
  [out] InterfaceIpFilter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The alias of routing interface that contains the filters to retrieve.

</dd> <dt>

*Direction* \[in\]
</dt> <dd>

The direction of network traffic that the filter applies to. You can set this parameter to one of the following values.

**Windows Server 2012:** This parameter was changed from a sting data type in Windows Server 2012 R2.

<dt>

0
</dt> <dd>

Inbound traffic.

</dd> <dt>

1
</dt> <dd>

Outbound traffic.

</dd> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**InterfaceIpFilter**](interfaceipfilter.md) object that receives the retrieved IP filter.

**Windows Server 2012:** This parameter was changed to an array in Windows Server 2012 R2.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_IPFilter**](ps-ipfilter.md)
</dt> </dl>

 

 





