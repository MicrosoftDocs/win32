---
Description: Adds a set of custom metadata values to IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c1f1e21-b73b-47f1-a19f-3c9c8517f0d0
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: BulkAddCustomValue method of the MSFT\_IPAM\_CustomValue class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BulkAddCustomValue method of the MSFT\_IPAM\_CustomValue class

Adds a set of custom metadata values to IPAM.

## Syntax


```mof
uint32 BulkAddCustomValue(
  [in]  string                    Name,
  [in]  string                    Value[],
  [out] MSFT_IPAM_OperationStatus Output[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the set of values.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

An array that contains the values to add.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the updated metadata fields.

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

 

 




