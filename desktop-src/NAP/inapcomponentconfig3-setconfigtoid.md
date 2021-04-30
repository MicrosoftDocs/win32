---
title: INapComponentConfig3 SetConfigToID method (NapCommon.h)
description: Is implemented by system health validators (SHVs) to provide a way to set the configuration data for a specific configuration ID.
ms.assetid: 1fa0b8e7-b597-4ab1-bb61-2cab47b92ce3
keywords:
- SetConfigToID method NAP
- SetConfigToID method NAP , INapComponentConfig3 interface
- INapComponentConfig3 interface NAP , SetConfigToID method
topic_type:
- apiref
api_name:
- INapComponentConfig3.SetConfigToID
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig3::SetConfigToID method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **SetConfigToID** method is implemented by system health validators (SHVs) to provide a way to set the configuration data for a specific configuration ID.

## Syntax


```C++
HRESULT SetConfigToID(
  [in] UINT32 configID,
  [in] UINT16 count,
  [in] BYTE   *data
);
```



## Parameters

<dl> <dt>

*configID* \[in\]
</dt> <dd>

A value that represents the configuration. *ConfigID* is assigned by the Network Policy Server (NPS) service and is unique within the SHV. If *ConfigID* is 0, the default configuration of the SHV is set.

</dd> <dt>

*count* \[in\]
</dt> <dd>

The size, in bytes, of the configuration data in *data*.

</dd> <dt>

*data* \[in\]
</dt> <dd>

On input, a BYTE array that contains the configuration data set to *ConfigID*.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                                    | Description                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                          | The operation is successful.<br/> |
| <dl> <dt>**NAP\_E\_SHV\_CONFIG\_NOT\_FOUND**</dt> </dl> | *ConfigID* cannot be found.<br/>  |



 

## Remarks

The [**NewConfig**](inapcomponentconfig3-newconfig.md) method must be used to allocate configuration data for *ConfigID* before this method can be called.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig3**](inapcomponentconfig3.md)
</dt> </dl>

 

 





