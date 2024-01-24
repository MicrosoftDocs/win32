---
title: INapComponentConfig SetConfig method (NapCommon.h)
description: Sets the system health validator (SHV) component configuration.
ms.assetid: ec27e30b-4205-40bc-a24b-61072a746e53
keywords:
- SetConfig method NAP
- SetConfig method NAP , INapComponentConfig interface
- INapComponentConfig interface NAP , SetConfig method
topic_type:
- apiref
api_name:
- INapComponentConfig.SetConfig
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig::SetConfig method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **SetConfig** method sets the system health validator (SHV) component configuration.

## Syntax


```C++
HRESULT SetConfig(
  [in] UINT16 bCount,
  [in] BYTE   *data
);
```



## Parameters

<dl> <dt>

*bCount* \[in\]
</dt> <dd>

The size, in bytes, of the *data* configuration blob.

</dd> <dt>

*data* \[in\]
</dt> <dd>

A pointer to the SHV component configuration data.

> [!Note]  
> Configuration data exported from an x86 machine using the [**GetConfig**](inapcomponentconfig-getconfig.md) method may be imported onto an x64 machine using the **SetConfig** method, and vice versa. Therefore, configuration data must be in an architecture-agnostic format such as XML. Using XML instead of a byte stream makes it easier to use configuration data on different architectures. The XML elements used in the configuration data are determined by the implementer.

 

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

Component versioning information should be included in the *data* configuration blob. The versioning information may be used when migrating from one SHV version to another.

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

[**INapConponentConfig::GetConfig**](inapcomponentconfig-getconfig.md)
</dt> </dl>

 

 





