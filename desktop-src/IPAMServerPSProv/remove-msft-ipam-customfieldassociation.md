---
Description: 'Deletes items from the set of values pairs for two custom fields.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'b3649820-fc03-4175-9962-3ed5d14ac486'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Remove method of the MSFT\_IPAM\_CustomFieldAssociation class'
---

# Remove method of the MSFT\_IPAM\_CustomFieldAssociation class

Deletes items from the set of values pairs for two custom fields.

## Syntax


```mof
uint32 Remove(
  [in]  string                           CustomFieldOne,
  [in]  string                           CustomFieldTwo,
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

 

 




