---
Description: Deletes a custom metadata field from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2f027834-722a-448f-b3e4-83a7592400a7
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RemoveCustomField method of the MSFT\_IPAM\_CustomField class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveCustomField method of the MSFT\_IPAM\_CustomField class

Deletes a custom metadata field from IPAM.

## Syntax


```mof
uint32 RemoveCustomField(
  [in]  string                Name,
  [out] MSFT_IPAM_CustomField output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the metadata field to delete.

</dd> <dt>

*output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the deleted metadata field.

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

[**MSFT\_IPAM\_CustomField**](msft-ipam-customfield.md)
</dt> </dl>

 

 




