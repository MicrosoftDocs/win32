---
title: IWMDRMSecurity SetRevocationData method (Wmdrmsdk.h)
description: The SetRevocationData method sets a certificate revocation list in the local store.
ms.assetid: 7e1c6d50-7a22-41b7-b29f-b1e5809a2097
keywords:
- SetRevocationData method windows Media Format
- SetRevocationData method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , SetRevocationData method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.SetRevocationData
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMSecurity::SetRevocationData method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **SetRevocationData** method sets a certificate revocation list in the local store.

## Syntax


```C++
HRESULT SetRevocationData(
  [in] REFGUID f_guidRevocationType,
  [in] BYTE    *f_pbCRL,
  [in] DWORD   f_cbCRL
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

*f\_pbCRL* \[in\]
</dt> <dd>

Buffer containing the certificate revocation list.

</dd> <dt>

*f\_cbCRL* \[in\]
</dt> <dd>

Size of the buffer, in bytes.

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

[**GetRevocationData**](iwmdrmsecurity-getrevocationdata.md)
</dt> <dt>

[**GetRevocationDataVersion**](iwmdrmsecurity-getrevocationdataversion.md)
</dt> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> </dl>

 

 





