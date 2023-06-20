---
title: IWMDRMSecurity GetMachineCertificate method (Wmdrmsdk.h)
description: The GetMachineCertificate method retrieves the machine certificate of the DRM subsystem on the client computer.
ms.assetid: 38b8e812-e997-4a63-b906-ebd26a5556be
keywords:
- GetMachineCertificate method windows Media Format
- GetMachineCertificate method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , GetMachineCertificate method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.GetMachineCertificate
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMSecurity::GetMachineCertificate method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetMachineCertificate** method retrieves the machine certificate of the DRM subsystem on the client computer.

## Syntax


```C++
HRESULT GetMachineCertificate(
  [in]      DWORD dwCertificateType,
  [out]     BYTE  rgbVersion[4],
  [out]     BYTE  **ppbCertificate,
  [in, out] DWORD *pcbCertificate
);
```



## Parameters

<dl> <dt>

*dwCertificateType* \[in\]
</dt> <dd>

Type of certificate to retrieve. Set to one of the values in the following table.



| Value                        | Description                                                                           |
|------------------------------|---------------------------------------------------------------------------------------|
| WMDRM\_CERTIFICATE\_TYPE\_V1 | The certificate will be retrieved in the format used by legacy components.            |
| WMDRM\_CERTIFICATE\_TYPE\_V2 | The certificate will be retrieved in the format used by the Windows Vista components. |



 

</dd> <dt>

*rgbVersion\[4\]* \[out\]
</dt> <dd>

Array of four bytes specifying the version of the DRM subsystem on the client computer.

</dd> <dt>

*ppbCertificate* \[out\]
</dt> <dd>

Address of a variable that receives a pointer to the certificate data. Set to **NULL** to have the method provide the buffer size required to hold the certificate in *pcbCertificate*.

</dd> <dt>

*pcbCertificate* \[in, out\]
</dt> <dd>

Size of the certificate in bytes. If *ppbCertificate* is **NULL**, this value will be set to the size of the certificate. If *ppbCertificate* is not **NULL**, this value must be set to the size of the buffer.

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

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> </dl>

 

 





