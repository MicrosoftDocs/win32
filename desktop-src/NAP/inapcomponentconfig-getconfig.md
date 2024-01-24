---
title: INapComponentConfig GetConfig method (NapCommon.h)
description: Retrieves the system health validator (SHV) component configuration.
ms.assetid: 57a1d3a7-05c0-4e0f-91b8-b3cf8982d04f
keywords:
- GetConfig method NAP
- GetConfig method NAP , INapComponentConfig interface
- INapComponentConfig interface NAP , GetConfig method
topic_type:
- apiref
api_name:
- INapComponentConfig.GetConfig
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig::GetConfig method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetConfig** method retrieves the system health validator (SHV) component configuration.

## Syntax


```C++
HRESULT GetConfig(
  [out] UINT16 *bCount,
  [out] BYTE   **data
) const;
```



## Parameters

<dl> <dt>

*bCount* \[out\]
</dt> <dd>

The size, in bytes, of the *data* configuration blob.

</dd> <dt>

*data* \[out\]
</dt> <dd>

A pointer to the address of the SHV component configuration data.

> [!Note]  
> Configuration data exported from an x86 machine using the **GetConfig** method may be imported onto an x64 machine using the [**SetConfig**](inapcomponentconfig-setconfig.md) method, and vice versa. Therefore, configuration data must be in an architecture-agnostic format such as XML. Using XML instead of a byte stream makes it easier to use configuration data on different architectures. The XML elements used in the configuration data are determined by the implementer.

 

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

The data parameter must be allocated by the callee (component implementor) using **CoTaskMemAlloc** and freed by the caller using **CoTaskMemFree**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig**](inapcomponentconfig.md)
</dt> <dt>

[**INapComponentConfig::SetConfig**](inapcomponentconfig-setconfig.md)
</dt> </dl>

 

 





