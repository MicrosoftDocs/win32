---
Description: 'Set access scope on an array of IP Blocks from IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '5d4b2ec8-9307-4f59-a05b-262c7e4c8fe3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetBlockAccessScope method of the MSFT\_IPAM\_AccessScope class'
---

# SetBlockAccessScope method of the MSFT\_IPAM\_AccessScope class

Set access scope on an array of IP Blocks from IPAM.

## Syntax


```mof
uint32 SetBlockAccessScope(
  [in]  boolean         IpamBlock,
  [in]  string          AccessScopePath,
  [in]  boolean         IsInheritedAccessScope,
  [in]  MSFT_IPAM_Block InputObject[],
  [out] MSFT_IPAM_Block Output[]
);
```



## Parameters

<dl> <dt>

*IpamBlock* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AccessScopePath* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*IsInheritedAccessScope* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

An array of [**MSFT\_IPAM\_Block**](msft-ipam-block.md) embedded instances.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the scope as an array of [**MSFT\_IPAM\_Block**](msft-ipam-block.md) embedded instances.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_AccessScope**](msft-ipam-accessscope.md)
</dt> </dl>

 

 




