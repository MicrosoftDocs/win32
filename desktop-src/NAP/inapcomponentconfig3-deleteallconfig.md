---
title: INapComponentConfig3 DeleteAllConfig method (NapCommon.h)
description: Is implemented by system health validators (SHVs) to provide a way to reset the SHV store to its original state after setup.
ms.assetid: 7f079743-1c32-430d-a250-b49a96b99f14
keywords:
- DeleteAllConfig method NAP
- DeleteAllConfig method NAP , INapComponentConfig3 interface
- INapComponentConfig3 interface NAP , DeleteAllConfig method
topic_type:
- apiref
api_name:
- INapComponentConfig3.DeleteAllConfig
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig3::DeleteAllConfig method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **DeleteAllConfig** method is implemented by system health validators (SHVs) to provide a way to reset the SHV store to its original state after setup. All configuration data except for the default configuration must be deleted.

## Syntax


```C++
HRESULT DeleteAllConfig();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                           | Description                             |
|---------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl> | The operation is successful.<br/> |



 

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

 

 





