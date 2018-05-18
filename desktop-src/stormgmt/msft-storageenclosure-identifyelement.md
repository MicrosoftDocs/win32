---
title: IdentifyElement method of the MSFT\_StorageEnclosure class
description: Permits a user to perform identification tasks on the enclosure and its elements.
ms.assetid: '9993C05C-28A4-4AB8-8860-ADE5D3032AF3'
keywords: ["IdentifyElement method Windows Storage Management API", "IdentifyElement method Windows Storage Management API , MSFT_StorageEnclosure class", "MSFT_StorageEnclosure class Windows Storage Management API , IdentifyElement method"]
topic_type:
- apiref
api_name:
- MSFT_StorageEnclosure.IdentifyElement
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# IdentifyElement method of the MSFT\_StorageEnclosure class

Permits a user to perform identification tasks on the enclosure and its elements.

## Syntax


```mof
HRESULT IdentifyElement(
  [in]  Boolean Enable,
  [in]  UInt32  SlotNumber[],
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Enable* \[in\]
</dt> <dd>

If **TRUE**, this instructs the enclosure to enable its identification LED on the specified element(s). The identification LED should remain enabled until a second call to **IdentifyElement** on the same element is made with this parameter set to FALSE.

This parameter is required and cannot be NULL.

</dd> <dt>

*SlotNumber* \[in\]
</dt> <dd>

An array of slot numbers on which to enable or disable the identification LED.

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
| <dl> <dt>55000</dt> </dl> | One or more slot numbers provided are not valid.<br/>              |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
</dt> </dl>

 

 





