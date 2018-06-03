---
title: Add method of the PS\_IPFilter class
description: Adds an IP filter to a BGP router interface.
audience: developer
ms.assetid: 254f2a89-b576-498f-9869-ae6d65879112
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_IPFilter class
- PS_IPFilter class, Add method
topic_type:
- apiref
api_name:
- PS_IPFilter.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_IPFilter class

Adds an IP filter to a BGP router interface.

## Syntax


```mof
uint32 Add(
  [in]  string            InterfaceAlias,
  [in]  uint32            Action,
  [in]  string            List[],
  [in]  uint32            Direction,
  [in]  boolean           PassThru,
  [in]  uint32            AddressFamily,
  [out] InterfaceIpFilter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The alias of interface to add filters to.

</dd> <dt>

*Action* \[in\]
</dt> <dd>

The action for the filter to perform. You can set this parameter to one of the following values.

<dt>

0
</dt> <dd>

Allow traffic.

</dd> <dt>

1
</dt> <dd>

Deny traffic.

</dd> </dl> </dd> <dt>

*List* \[in\]
</dt> <dd>

An array that contains the IP filters of the interface.

</dd> <dt>

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

*PassThru* \[in\]
</dt> <dd>

Indicates wether the *cmdletOutput* parameter returns an object. **True** to return and object; otherwise **false**.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

Indicates whether the filter is an IPv4 filter or IPv6.

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

The [**InterfaceIpFilter**](interfaceipfilter.md) object that receives the added IP filter.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_IPFilter**](ps-ipfilter.md)
</dt> </dl>

 

 





