---
Description: 'Updates the set of value pairs for two custom fields.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e675ed5f-f61a-48d4-b9d2-3604587f8190'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Modify method of the MSFT\_IPAM\_CustomFieldAssociation class'
---

# Modify method of the MSFT\_IPAM\_CustomFieldAssociation class

Updates the set of value pairs for two custom fields.

## Syntax


```mof
uint32 Modify(
  [in]  string                           CustomFieldOne,
  [in]  string                           CustomFieldTwo,
  [in]  string                           AddAssociationValue[],
  [in]  string                           RemoveAssociationValue[],
  [out] MSFT_IPAM_CustomFieldAssociation Output
);
```



## Parameters

<dl> <dt>

*CustomFieldOne* \[in\]
</dt> <dd>

The first custom field.

</dd> <dt>

*CustomFieldTwo* \[in\]
</dt> <dd>

The second custom field.

</dd> <dt>

*AddAssociationValue* \[in\]
</dt> <dd>

An array that contains the value pairs to add.

</dd> <dt>

*RemoveAssociationValue* \[in\]
</dt> <dd>

An array that contains the value pairs to delete.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the updated set of value pairs for the custom fields.

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

[**MSFT\_IPAM\_CustomFieldAssociation**](msft-ipam-customfieldassociation.md)
</dt> </dl>

 

 




