---
title: IWMDRMSecurity GetRevocationDataVersion method (Wmdrmsdk.h)
description: The GetRevocationDataVersion method retrieves the version number of a certificate revocation list in the local store.
ms.assetid: 2fa13b38-02c2-4c81-938b-409cadca00fb
keywords:
- GetRevocationDataVersion method windows Media Format
- GetRevocationDataVersion method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , GetRevocationDataVersion method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.GetRevocationDataVersion
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMSecurity::GetRevocationDataVersion method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetRevocationDataVersion** method retrieves the version number of a certificate revocation list in the local store.

## Syntax


```C++
HRESULT GetRevocationDataVersion(
  [in]  REFGUID   f_guidRevocationType,
  [out] ULONGLONG *f_pdwCRLVersion
);
```



## Parameters

<dl> <dt>

*f\_guidRevocationType* \[in\]
</dt> <dd>

GUID specifying the type of revocation list. Set to one of the constants in the following table.



| GUID constant                 | Description                                                                      |
|-------------------------------|----------------------------------------------------------------------------------|
| WMDRM\_REVOCATIONTYPE\_APP    | Specifies the application certificate revocation list.                           |
| WMDRM\_REVOCATIONTYPE\_DEVICE | Specifies the device certificate revocation list.                                |
| WMDRM\_REVOCATIONTYPE\_CARDEA | Specifies the Windows Media DRM for Network Devices certificate revocation list. |



 

</dd> <dt>

*f\_pdwCRLVersion* \[out\]
</dt> <dd>

Variable that receives the version number.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**Automated Component Revocation and Renewal**](automated-component-revocation-and-renewal.md)
</dt> <dt>

[**GetRevocationData**](iwmdrmsecurity-getrevocationdata.md)
</dt> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> <dt>

[**SetRevocationData**](iwmdrmsecurity-setrevocationdata.md)
</dt> </dl>

 

 





