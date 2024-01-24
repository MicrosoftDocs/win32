---
title: INapComponentConfig2 IsRemoteConfigSupported method (NapCommon.h)
description: Is implemented by system health validators (SHVs) to indicate whether remote configuration is supported.
ms.assetid: c4b8e60b-ed60-49ec-b4d6-4e1575e4d1a5
keywords:
- IsRemoteConfigSupported method NAP
- IsRemoteConfigSupported method NAP , INapComponentConfig2 interface
- INapComponentConfig2 interface NAP , IsRemoteConfigSupported method
topic_type:
- apiref
api_name:
- INapComponentConfig2.IsRemoteConfigSupported
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig2::IsRemoteConfigSupported method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **IsRemoteConfigSupported** method is implemented by system health validators (SHVs) to indicate whether remote configuration is supported.

## Syntax


```C++
HRESULT IsRemoteConfigSupported(
  [out] BOOL  *isSupported,
  [out] UINT8 *remoteConfigType
);
```



## Parameters

<dl> <dt>

*isSupported* \[out\]
</dt> <dd>

A pointer to a BOOL that is set to **TRUE** if the component supports remote configuration, and **FALSE** if it does not.

</dd> <dt>

*remoteConfigType* \[out\]
</dt> <dd>

Indicates the type of remote configuration supported using value from the [**RemoteConfigurationType**](/windows/win32/api/naptypes/ne-naptypes-remoteconfigurationtype) enumeration:



| Value                                                                                                 | Meaning                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>remoteConfigTypeMachine</dt> </dl>    | [**InvokeUIForMachine**](inapcomponentconfig2-invokeuiformachine.md) is implemented.<br/>                                                                                                                                                                                                |
| <dl> <dt>remoteConfigTypeConfigBlob</dt> </dl> | [**InvokeUIFromConfigBlob**](inapcomponentconfig2-invokeuifromconfigblob.md) is implemented. [**INapComponentConfig::GetConfig**](inapcomponentconfig-getconfig.md) and [**INapComponentConfig::SetConfig**](inapcomponentconfig-setconfig.md) can be called remotely using DCOM.<br/> |



 

</dd> </dl>

## Return value

Returns S\_OK if successful, or one of the standard Windows error codes.

## Remarks

If neither [**InvokeUIForMachine**](inapcomponentconfig2-invokeuiformachine.md) nor [**InvokeUIFromConfigBlob**](inapcomponentconfig2-invokeuifromconfigblob.md) are implemented, remote configuration of the SHV is not possible.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig2**](inapcomponentconfig2.md)
</dt> </dl>

 

 





