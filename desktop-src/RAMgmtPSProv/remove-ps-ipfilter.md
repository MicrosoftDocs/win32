---
title: Remove method of the PS\_IPFilter class
description: Removes an IP filter from a BGP routing interface.
audience: developer
ms.assetid: 1e24a6e9-4191-48f9-9009-7f399aa76c30
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_IPFilter class
- PS_IPFilter class, Remove method
topic_type:
- apiref
api_name:
- PS_IPFilter.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_IPFilter class

Removes an IP filter from a BGP routing interface.

## Syntax


```mof
uint32 Remove(
  [in]  string            InterfaceAlias,
  [in]  uint32            Direction,
  [in]  string            List[],
  [in]  boolean           PassThru,
  [in]  boolean           Force,
  [in]  uint32            AddressFamily,
  [out] InterfaceIpFilter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The alias of routing interface that contains the filters to remove.

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

*List* \[in\]
</dt> <dd>

An array that contains the IP filters of the interface.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates wether the *cmdletOutput* parameter returns an object. **True** to return and object; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether a confirmation prompt should be used for this operation. **True** to use a confirmation prompt; otherwise **false**.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

Indicates whether the filter is an IPv4 filter or IPv6.

**Windows Server 2012:** This parameter replaced the *IpVersion* parameter in Windows Server 2012 R2.

<dt>

0
</dt> <dd>

Specifies IPv4.

</dd> <dt>

1
</dt> <dd>

Specifies IPv6.

</dd> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**InterfaceIpFilter**](interfaceipfilter.md) object that receives the updated IP filter info.

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

 

 





