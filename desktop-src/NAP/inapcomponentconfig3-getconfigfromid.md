---
title: INapComponentConfig3 GetConfigFromID method (NapCommon.h)
description: Is implemented by system health validators (SHVs) to provide a way to obtain configuration data for a specific configuration ID.
ms.assetid: 5c91681d-16d6-42f3-b1e0-c4b6e7561a73
keywords:
- GetConfigFromID method NAP
- GetConfigFromID method NAP , INapComponentConfig3 interface
- INapComponentConfig3 interface NAP , GetConfigFromID method
topic_type:
- apiref
api_name:
- INapComponentConfig3.GetConfigFromID
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig3::GetConfigFromID method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetConfigFromID** method is implemented by system health validators (SHVs) to provide a way to obtain configuration data for a specific configuration ID.

## Syntax


```C++
HRESULT GetConfigFromID(
  [in]  UINT32 configID,
  [out] UINT16 *count,
  [out] BYTE   **outdata
);
```



## Parameters

<dl> <dt>

*configID* \[in\]
</dt> <dd>

A value that represents the configuration. If *ConfigID* is **0**, the SHV should return the default configuration data in *outdata*.

</dd> <dt>

*count* \[out\]
</dt> <dd>

The size, in bytes, of the configuration data returned in *outdata*.

</dd> <dt>

*outdata* \[out\]
</dt> <dd>

On return, a BYTE array that contains the configuration data represented by *ConfigID*.

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

 

 





