---
title: IWMDRMLicenseManagement StoreLicense method (Wmdrmsdk.h)
description: The StoreLicense method includes a license that was generated outside of the local DRM subsystem in the local license store.
ms.assetid: 2190ff8c-8969-4f03-9f90-331bff8f4da2
keywords:
- StoreLicense method windows Media Format
- StoreLicense method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , StoreLicense method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.StoreLicense
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicenseManagement::StoreLicense method

The **StoreLicense** method includes a license that was generated outside of the local DRM subsystem in the local license store.

## Syntax


```C++
HRESULT StoreLicense(
  [in] BSTR bstrLicenseResponse
);
```



## Parameters

<dl> <dt>

*bstrLicenseResponse* \[in\]
</dt> <dd>

License response string to be decoded and added to the local license store.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

You can use this method to add XMR licenses that you have created to the local license store.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 





