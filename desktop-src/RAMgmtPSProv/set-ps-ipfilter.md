---
title: Set method of the PS\_IPFilter class
description: Updates the filtering action of an IP filter for a BGP router.
audience: developer
ms.assetid: '1f44a89a-1e9c-4fd2-b2fa-6996d2425d18'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_IPFilter class", "PS_IPFilter class, Set method"]
topic_type:
- apiref
api_name:
- PS_IPFilter.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_IPFilter class

Updates the filtering action of an IP filter for a BGP router.

## Syntax


```mof
uint32 Set(
  [in]  uint32            Action,
  [in]  uint32            Direction,
  [in]  string            InterfaceAlias,
  [in]  uint32            AddressFamily,
  [in]  boolean           PassThru,
  [out] InterfaceIpFilter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Action* \[in\]
</dt> <dd>

The action for the filter to perform. You can set this parameter to one of the following values.

**Windows Server 2012:** This parameter was changed from a sting data type in Windows Server 2012 R2.

<dt>

0
</dt> <dd>

Allow traffic.

</dd> <dt>

1
</dt> <dd>

Deny traffic.

</dd> </dl> </dd> <dt>

*Direction* \[in\]
</dt> <dd>

The direction of network traffic that the filter applies to. You can set this parameter to one of the following values.

<dt>

0
</dt> <dd>

Inbound traffic.

</dd> <dt>

1
</dt> <dd>

Outbound traffic.

</dd> </dl> </dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The alias of interface that contains the filters to update.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

Indicates whether the filter is an IPv4 filter or IPv6.

**Windows Server 2012:** This parameter replaced the *IpVersion* parameter in Windows Server 2012 R2.

<dt>

0
</dt> <dd>

Specifies IPv4.

</dd> <dt>

1
</dt> <dd>

Specifies IPv6.

</dd> </dl> </dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates wether the *cmdletOutput* parameter returns an object. **True** to return and object; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**InterfaceIpFilter**](interfaceipfilter.md) object that receives the updated IP filter.

**Windows Server 2012:** This parameter was changed to an array in Windows Server 2012 R2.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_IPFilter**](ps-ipfilter.md)
</dt> </dl>

 

 





