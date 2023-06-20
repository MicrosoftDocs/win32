---
title: IWMDRMLicenseManagement CreateLicenseEnumeration method (Wmdrmsdk.h)
description: The CreateLicenseEnumeration method creates a license enumerator object with which you can get information about licenses in the local license store.
ms.assetid: 48da1ef4-89bc-4cba-b5c9-0e202eb2986f
keywords:
- CreateLicenseEnumeration method windows Media Format
- CreateLicenseEnumeration method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , CreateLicenseEnumeration method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.CreateLicenseEnumeration
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseManagement::CreateLicenseEnumeration method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CreateLicenseEnumeration** method creates a license enumerator object with which you can get information about licenses in the local license store.

## Syntax


```C++
HRESULT CreateLicenseEnumeration(
  [in]  WMDRM_LICENSE_FILTER *pLicenseFilter,
  [out] IWMDRMLicense        **pEnumerator
);
```



## Parameters

<dl> <dt>

*pLicenseFilter* \[in\]
</dt> <dd>

Pointer to a [**WMDRM\_LICENSE\_FILTER**](wmdrm-license-filter.md) structure containing the filtering parameters for the list of licenses in the enumerator.

</dd> <dt>

*pEnumerator* \[out\]
</dt> <dd>

Pointer that receives the address of the [**IWMDRMLicense**](iwmdrmlicense.md) interface of the newly created license enumerator object.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                | Description                                              |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**NS\_E\_DRM\_RIV\_TOO\_SMALL**</dt> </dl> | An updated content revocation list is needed.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                       | The method succeeded.<br/>                         |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**Enumerating Licenses in the Local License Store**](enumerating-licenses-in-the-local-license-store.md)
</dt> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 





