---
title: IWMDRMLicense GetLicenseProperty method (Wmdrmsdk.h)
description: The GetLicenseProperty method retrieves a property from the current license.
ms.assetid: 5431f849-b37e-40b7-8bdb-ee30948aeff1
keywords:
- GetLicenseProperty method windows Media Format
- GetLicenseProperty method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , GetLicenseProperty method
topic_type:
- apiref
api_name:
- IWMDRMLicense.GetLicenseProperty
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicense::GetLicenseProperty method

The **GetLicenseProperty** method retrieves a property from the current license.

## Syntax


```C++
HRESULT GetLicenseProperty(
  [in]  BSTR        bstrName,
  [out] PROPVARIANT *ppropVariant
);
```



## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

Name of the property to retrieve. Set to one of the constants in the following table:



| Constant                   | Description                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------------------|
| g\_wszWMDRMNet\_Revocation | Use to get the Windows Media DRM for Network Devices revocation list for the current license.                        |
| g\_wszWMDRM\_SAPLEVEL      | Use to get the Secure Audio Path (SAP) level required to play content covered by the current license.                |
| g\_wszWMDRM\_SAPRequired   | Use to ascertain whether the current license requires SAP be used to play the content.                               |
| g\_wszWMDRM\_SOURCEID      | Use to get the source identifier for the current license.                                                            |
| g\_wszWMDRM\_PRIORITY      | Use to get the priority of the current license. Higher priority licenses are applied before lower priority licenses. |
| g\_wszWMDRM\_UplinkID      | Use to get the key ID of the root license in the license chain that the current license belongs to.                  |



 

</dd> <dt>

*ppropVariant* \[out\]
</dt> <dd>

Receives the property value.

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

[**GetLicense**](iwmdrmlicense-getlicense.md)
</dt> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





