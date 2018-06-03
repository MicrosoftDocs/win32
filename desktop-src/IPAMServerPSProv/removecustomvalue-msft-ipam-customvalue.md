---
Description: Deletes a value from a custom metadata field.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e87497a9-d9f7-47bc-953d-6ce293e8ac49
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RemoveCustomValue method of the MSFT\_IPAM\_CustomValue class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveCustomValue method of the MSFT\_IPAM\_CustomValue class

Deletes a value from a custom metadata field.Removes a value from set of possible values for a given multi-valued custom field. This returns an error if the value is currently in use. IPAM doesn't allow deletion of inbuilt custom fields.

## Syntax


```mof
uint32 RemoveCustomValue(
  [in]  string                Name,
  [in]  string                Value,
  [out] MSFT_IPAM_CustomValue Output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the value.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The value to remove.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the updated metadata field.

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

[**MSFT\_IPAM\_CustomValue**](msft-ipam-customvalue.md)
</dt> </dl>

 

 




