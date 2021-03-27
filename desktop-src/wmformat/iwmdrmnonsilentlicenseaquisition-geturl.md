---
title: IWMDRMNonSilentLicenseAquisition GetURL method (Wmdrmsdk.h)
description: The GetURL method retrieves the URL to which the license challenge should be posted.
ms.assetid: f65f1984-74bc-4cd0-957e-930aa6a6f6a5
keywords:
- GetURL method windows Media Format
- GetURL method windows Media Format , IWMDRMNonSilentLicenseAquisition interface
- IWMDRMNonSilentLicenseAquisition interface windows Media Format , GetURL method
topic_type:
- apiref
api_name:
- IWMDRMNonSilentLicenseAquisition.GetURL
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMNonSilentLicenseAquisition::GetURL method

The **GetURL** method retrieves the URL to which the license challenge should be posted.

## Syntax


```C++
HRESULT GetURL(
  [out] BSTR *pbstrURL
);
```



## Parameters

<dl> <dt>

*pbstrURL* \[out\]
</dt> <dd>

Address of a variable that receives the URL.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNonSilentLicenseAquisition Interface**](iwmdrmnonsilentlicenseaquisition.md)
</dt> </dl>

 

 





