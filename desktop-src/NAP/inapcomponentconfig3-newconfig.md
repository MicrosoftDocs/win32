---
title: INapComponentConfig3 NewConfig method (NapCommon.h)
description: Is implemented by system health validators (SHVs) to provide a way to create configuration data for a specific configuration ID.
ms.assetid: cea762d3-815d-4034-94c1-5fa9a859cce8
keywords:
- NewConfig method NAP
- NewConfig method NAP , INapComponentConfig3 interface
- INapComponentConfig3 interface NAP , NewConfig method
topic_type:
- apiref
api_name:
- INapComponentConfig3.NewConfig
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig3::NewConfig method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **NewConfig** method is implemented by system health validators (SHVs) to provide a way to create configuration data for a specific configuration ID. When this function is called, an SHV must allocate new configuration data and populate it with a copy of the default configuration data.

## Syntax


```C++
HRESULT NewConfig(
   UINT32 configID
);
```



## Parameters

<dl> <dt>

*configID* 
</dt> <dd>

A value that represents the configuration. *ConfigID* is assigned by the Network Policy Server (NPS) service and is unique within the SHV.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                                 | Description                                                                                   |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                       | The operation is successful.<br/>                                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | *ConfigID* is 0 (a value reserved for the default configuration).<br/>                  |
| <dl> <dt>**NAP\_E\_SHV\_CONFIG\_EXISTED**</dt> </dl> | *ConfigID* already exists. The list of IDs known to NPS is different from the SHV.<br/> |



 

## Remarks

After the new configuration is created by **NewConfig**, the [**GetConfigFromID**](inapcomponentconfig3-getconfigfromid.md), [**InvokeUIFromConfigBlob**](inapcomponentconfig2-invokeuifromconfigblob.md), and [**SetConfigToID**](inapcomponentconfig3-setconfigtoid.md) methods should be used to alter the configuration as needed.

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

 

 





