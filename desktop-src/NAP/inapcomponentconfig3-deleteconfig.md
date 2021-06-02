---
title: INapComponentConfig3 DeleteConfig method (NapCommon.h)
description: Is implemented by system health validators (SHVs) to provide a way to delete configuration data for a specific configuration ID.
ms.assetid: 9740c122-86c8-4b77-9268-faa90e84d8aa
keywords:
- DeleteConfig method NAP
- DeleteConfig method NAP , INapComponentConfig3 interface
- INapComponentConfig3 interface NAP , DeleteConfig method
topic_type:
- apiref
api_name:
- INapComponentConfig3.DeleteConfig
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig3::DeleteConfig method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **DeleteConfig** method is implemented by system health validators (SHVs) to provide a way to delete configuration data for a specific configuration ID. The ID may be reused after the configuration data has been deleted.

## Syntax


```C++
HRESULT DeleteConfig(
   UINT32 configID
);
```



## Parameters

<dl> <dt>

*configID* 
</dt> <dd>

A value that represents the configuration data to delete.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                                    | Description                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                          | The operation is successful.<br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | *ConfigID* is 0 (a value reserved for the default configuration).<br/> |
| <dl> <dt>**NAP\_E\_SHV\_CONFIG\_NOT\_FOUND**</dt> </dl> | *ConfigID* cannot be found.<br/>                                       |



 

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

 

 





