---
Description: Renames a value of a custom metadata field.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f183a1d9-8f93-4f3e-814b-926b7fcf9fcb
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RenameCustomValue method of the MSFT\_IPAM\_CustomValue class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RenameCustomValue method of the MSFT\_IPAM\_CustomValue class

Renames a value of a custom metadata field.

## Syntax


```mof
uint32 RenameCustomValue(
  [in]  string                Name,
  [in]  string                Value,
  [in]  string                NewValue,
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

The value to rename.

</dd> <dt>

*NewValue* \[in\]
</dt> <dd>

The new value name.

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

 

 




