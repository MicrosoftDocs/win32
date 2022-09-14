---
title: IWMDRMSecurity GetSecurityVersion method (Wmdrmsdk.h)
description: The GetSecurityVersion method retrieves the version of the DRM subsystem on the client computer.
ms.assetid: ec97dec8-61ba-4424-b5eb-2e6885cc1f48
keywords:
- GetSecurityVersion method windows Media Format
- GetSecurityVersion method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , GetSecurityVersion method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.GetSecurityVersion
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMSecurity::GetSecurityVersion method

The **GetSecurityVersion** method retrieves the version of the DRM subsystem on the client computer.

## Syntax


```C++
HRESULT GetSecurityVersion(
  [out] BSTR *pbstrVersion
);
```



## Parameters

<dl> <dt>

*pbstrVersion* \[out\]
</dt> <dd>

Address of a variable that receives the DRM subsystem version number.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

The version number is expressed as a string consisting of four numbers separated by periods. The first number is the major version number, which is usually set to 2. The second number is the minor version number, ranging from 2 to 10. The third number is always set to 0. The fourth number is set to 0 or 1, and is a Boolean value indicating whether the subsystem has been individualized. For example, a version number of "2.4.0.1" indicates the individualized fourth minor version of the second major version.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> </dl>

 

 





