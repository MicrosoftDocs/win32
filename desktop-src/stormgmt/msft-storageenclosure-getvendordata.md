---
title: GetVendorData method of the MSFT\_StorageEnclosure class
description: Returns the vendor-specific data from an enclosure.
ms.assetid: 1CBBC9A4-73D1-4B4C-A164-7D9D40285709
keywords:
- GetVendorData method Windows Storage Management API
- GetVendorData method Windows Storage Management API , MSFT_StorageEnclosure class
- MSFT_StorageEnclosure class Windows Storage Management API , GetVendorData method
topic_type:
- apiref
api_name:
- MSFT_StorageEnclosure.GetVendorData
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetVendorData method of the MSFT\_StorageEnclosure class

Returns the vendor-specific data from an enclosure.

## Syntax


```mof
HRESULT GetVendorData(
  [in]  UInt16 PageNumber,
  [out] String VendorData,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*PageNumber* \[in\]
</dt> <dd>

The page number for which vendor data is requested.

</dd> <dt>

*VendorData* \[out\]
</dt> <dd>

The vendor-specific data ("page 04h", for example) from an enclosure.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                     | Description                                                              |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>     | Success.<br/>                                                      |
| <dl> <dt>1</dt> </dl>     | Not supported.<br/>                                                |
| <dl> <dt>2</dt> </dl>     | Unspecified error.<br/>                                            |
| <dl> <dt>3</dt> </dl>     | Timeout.<br/>                                                      |
| <dl> <dt>4</dt> </dl>     | Failed.<br/>                                                       |
| <dl> <dt>5</dt> </dl>     | Invalid parameter.<br/>                                            |
| <dl> <dt>40001</dt> </dl> | Access denied.<br/>                                                |
| <dl> <dt>40002</dt> </dl> | There are not enough resources to complete the operation.<br/>     |
| <dl> <dt>46000</dt> </dl> | Cannot connect to the storage provider.<br/>                       |
| <dl> <dt>46001</dt> </dl> | The storage provider cannot connect to the storage subsystem.<br/> |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
</dt> </dl>

 

 





