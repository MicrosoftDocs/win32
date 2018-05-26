---
Description: Adds new custom metadata field to IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ddeae195-a486-4ac0-a8e3-f8e7dd882318
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AddCustomField method of the MSFT\_IPAM\_CustomField class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddCustomField method of the MSFT\_IPAM\_CustomField class

Adds new custom metadata field to IPAM.

## Syntax


```mof
uint32 AddCustomField(
  [in]  string                Name,
  [in]  boolean               MultiValue,
  [in]  string                CustomValue[],
  [out] MSFT_IPAM_CustomField output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the metadata field.

</dd> <dt>

*MultiValue* \[in\]
</dt> <dd>

**True** if the field contains multiple values; otherwise, **false**.

</dd> <dt>

*CustomValue* \[in\]
</dt> <dd>

An array that contains the values to add to the field.

</dd> <dt>

*output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the new metadata field.

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

 

 




