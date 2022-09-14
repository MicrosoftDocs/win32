---
title: IWMDRMLicenseQuery SetActionAllowedQueryParams method (Wmdrmsdk.h)
description: The SetActionAllowedQueryParams method sets environment-specific information for more accurate query results when using the QueryActionAllowed method.
ms.assetid: 1c8f9d4e-999d-4d7c-87fd-9d30e432350c
keywords:
- SetActionAllowedQueryParams method windows Media Format
- SetActionAllowedQueryParams method windows Media Format , IWMDRMLicenseQuery interface
- IWMDRMLicenseQuery interface windows Media Format , SetActionAllowedQueryParams method
topic_type:
- apiref
api_name:
- IWMDRMLicenseQuery.SetActionAllowedQueryParams
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicenseQuery::SetActionAllowedQueryParams method

The **SetActionAllowedQueryParams** method sets environment-specific information for more accurate query results when using the [**QueryActionAllowed**](iwmdrmlicensequery-queryactionallowed.md) method.

## Syntax


```C++
HRESULT SetActionAllowedQueryParams(
  [in] BOOL  fIsMF,
  [in] DWORD dwAppSecLevel,
  [in] BOOL  fHasSerialNumber,
  [in] BSTR  bstrDeviceCert
);
```



## Parameters

<dl> <dt>

*fIsMF* \[in\]
</dt> <dd>

Specifies whether the content will be rendered by using the objects of the Microsoft Media Foundation SDK. **FALSE** indicates rendering by the objects of the Windows Media Format SDK. This parameter is optional.

</dd> <dt>

*dwAppSecLevel* \[in\]
</dt> <dd>

Security level of the querying application. This value is only important if the objects of the Windows Media Format SDK will be used, in which case *fIsMF* should be set to **FALSE**. This parameter is optional.

</dd> <dt>

*fHasSerialNumber* \[in\]
</dt> <dd>

Specifies whether the target device for a copy operation has a serial number. This parameter is optional and only applies to queries for copy operations.

</dd> <dt>

*bstrDeviceCert* \[in\]
</dt> <dd>

Device certificate of the target device when using Windows Media DRM for Portable Devices. This parameter is optional and only applies to queries for copy operations.

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

[**IWMDRMLicenseQuery Interface**](iwmdrmlicensequery.md)
</dt> <dt>

[**Querying for Detailed Rights Information**](querying-for-detailed-rights-information.md)
</dt> </dl>

 

 





