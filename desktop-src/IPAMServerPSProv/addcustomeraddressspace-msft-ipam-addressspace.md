---
Description: Adds a new customer address space to IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7c0b3f93-6b2b-4b94-9ad0-60bbb874f59e
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AddCustomerAddressSpace method of the MSFT\_IPAM\_AddressSpace class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddCustomerAddressSpace method of the MSFT\_IPAM\_AddressSpace class

Adds a new customer address space to IPAM.

## Syntax


```mof
uint32 AddCustomerAddressSpace(
  [in]  string                 Name,
  [in]  string                 AssociatedProviderAddressSpace,
  [in]  string                 Tenant,
  [in]  string                 VMNetwork,
  [in]  string                 IsolationMethod,
  [in]  string                 Owner,
  [in]  string                 Description,
  [in]  string                 CustomConfiguration,
  [out] MSFT_IPAM_AddressSpace output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the address space.

</dd> <dt>

*AssociatedProviderAddressSpace* \[in\]
</dt> <dd>

Specifies a provider address space that is associated with this customer address space.

> [!Note]  
> This property can only be set if the **Type** property is set to (**CustomerAddressSpace**).

 

</dd> <dt>

*Tenant* \[in\]
</dt> <dd>

The tenant that owns the address space.

</dd> <dt>

*VMNetwork* \[in\]
</dt> <dd>

The name of the VM network that contains the address space.

</dd> <dt>

*IsolationMethod* \[in\]
</dt> <dd>

The isolation method to use for tenant traffic in the address space.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

The owner of the address space.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

The description of the address space.

</dd> <dt>

*CustomConfiguration* \[in\]
</dt> <dd>

A set of custom configuration data for the address space. The data is formatted with semi-colon separated name value pairs.

</dd> <dt>

*output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the added address space object.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_AddressSpace**](msft-ipam-addressspace.md)
</dt> </dl>

 

 




