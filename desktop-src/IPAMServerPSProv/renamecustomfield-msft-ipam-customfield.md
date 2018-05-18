---
Description: 'Renames a custom metadata field in IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '6efe397c-b584-4633-a8ea-7922b616371c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'RenameCustomField method of the MSFT\_IPAM\_CustomField class'
---

# RenameCustomField method of the MSFT\_IPAM\_CustomField class

Renames a custom metadata field in IPAM.

## Syntax


```mof
uint32 RenameCustomField(
  [in]  string                Name,
  [in]  string                newName,
  [out] MSFT_IPAM_CustomField output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the metadata field.

</dd> <dt>

*newName* \[in\]
</dt> <dd>

The new name of the metadata field.

</dd> <dt>

*output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the updated metadata field.

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

[**MSFT\_IPAM\_CustomField**](msft-ipam-customfield.md)
</dt> </dl>

 

 




