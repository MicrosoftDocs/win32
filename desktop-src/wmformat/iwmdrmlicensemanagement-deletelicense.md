---
title: IWMDRMLicenseManagement DeleteLicense method (Wmdrmsdk.h)
description: The DeleteLicense method removes a license from the temporary local license store.
ms.assetid: 0aa7143a-845a-41a4-8b3c-a04c68ee280a
keywords:
- DeleteLicense method windows Media Format
- DeleteLicense method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , DeleteLicense method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.DeleteLicense
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicenseManagement::DeleteLicense method

The **DeleteLicense** method removes a license from the temporary local license store.

## Syntax


```C++
HRESULT DeleteLicense(
  [in] BSTR  bstrKID,
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*bstrKID* \[in\]
</dt> <dd>

Key ID (KID) of the license to be deleted.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

License deletion option flags. Set to one of the values in the following table.



| Value                                    | Description                                                                                                                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDRM\_DELETE\_LICENSE\_IMMEDIATELY      | Specifies that the license should be removed from the store immediately.                                                                                                                              |
| WMDRM\_DELETE\_LICENSE\_MARK\_FOR\_PURGE | Specifies that the license should be marked for deletion, but should not be removed from the store until the [**CleanLicenseStore**](iwmdrmlicensemanagement-cleanlicensestore.md) method is called. |



 

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                            | Description                                                                                                         |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | The method succeeded.<br/>                                                                                    |
| <dl> <dt>**DRM\_E\_LICENSENOTFOUND**</dt> </dl> | The specified license does not exist in the store.<br/> - OR -<br/> The store was not found.<br/> |



 

## Remarks

To delete licenses from the permanent local license store, you must use license revocation.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 





