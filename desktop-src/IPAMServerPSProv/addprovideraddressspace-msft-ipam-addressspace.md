---
Description: 'Adds a new provider address space to IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e3f384fb-c852-4433-b52f-40ab4cde60b7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'AddProviderAddressSpace method of the MSFT\_IPAM\_AddressSpace class'
---

# AddProviderAddressSpace method of the MSFT\_IPAM\_AddressSpace class

Adds a new provider address space to IPAM.

## Syntax


```mof
uint32 AddProviderAddressSpace(
  [in]  string                 Name,
  [in]  string                 Owner,
  [in]  string                 Description,
  [in]  string                 CustomConfiguration,
  [out] MSFT_IPAM_AddressSpace output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the address space.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_AddressSpace**](msft-ipam-addressspace.md)
</dt> </dl>

 

 




