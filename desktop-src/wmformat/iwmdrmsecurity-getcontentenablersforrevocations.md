---
title: IWMDRMSecurity GetContentEnablersForRevocations method (Wmdrmsdk.h)
description: The GetContentEnablersForRevocations method retrieves content enabler interfaces that enable renewal of components based on revoked certificates.
ms.assetid: 9e5b58b8-07d6-4607-a40f-cd7df4984ac5
keywords:
- GetContentEnablersForRevocations method windows Media Format
- GetContentEnablersForRevocations method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , GetContentEnablersForRevocations method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.GetContentEnablersForRevocations
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMSecurity::GetContentEnablersForRevocations method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetContentEnablersForRevocations** method retrieves content enabler interfaces that enable renewal of components based on revoked certificates.

## Syntax


```C++
HRESULT GetContentEnablersForRevocations(
  [in]      BYTE              **rgpbCerts,
  [in]      DWORD             *rgpdwCertSizes,
  [in]      GUID              **rgpguidCerts,
  [in]      DWORD             cCerts,
  [in]      HRESULT           hResultHint,
  [out]     IMFContentEnabler **prgContentEnablers,
  [in, out] DWORD             *pcContentEnablers
);
```



## Parameters

<dl> <dt>

*rgpbCerts* \[in\]
</dt> <dd>

Array of certificates to retrieve content enablers for. The number of elements in the array must be specified by *cCerts*.

</dd> <dt>

*rgpdwCertSizes* \[in\]
</dt> <dd>

Array containing the sizes of the certificates in the *rgpbCerts* array. The number of elements in the array must be specified by *cCerts*.

</dd> <dt>

*rgpguidCerts* \[in\]
</dt> <dd>

Array containing the types of the certificates in the *rgpbCerts* array. The number of elements in the array must be specified by *cCerts*. For each element of the array, use one of the following values.



| GUID constant                 | Description                                                    |
|-------------------------------|----------------------------------------------------------------|
| WMDRM\_REVOCATIONTYPE\_APP    | Specifies an application certificate.                          |
| WMDRM\_REVOCATIONTYPE\_DEVICE | Specifies a device certificate.                                |
| WMDRM\_REVOCATIONTYPE\_CARDEA | Specifies a Windows Media DRM for Network Devices certificate. |



 

</dd> <dt>

*cCerts* \[in\]
</dt> <dd>

Number of certificates to retrieve content enablers for. This is the number of elements in the *rgpbCerts* array, the *rgpdwCertSizes* array, and the *rgpguidCerts* array.

</dd> <dt>

*hResultHint* \[in\]
</dt> <dd>

Return value received from the operation that failed due to a revoked certificate. If you are not calling in response to a failed method call, set to S\_OK.

</dd> <dt>

*prgContentEnablers* \[out\]
</dt> <dd>

Array that receives the addresses of the newly created **IMFContentEnabler** interfaces. Set to **NULL** to get the number of content enablers in the *pcContentEnablers* parameter.

</dd> <dt>

*pcContentEnablers* \[in, out\]
</dt> <dd>

Number of elements in the *prgContentEnablers* array. If *prgContentEnablers* is **NULL**, this value is set to the number of needed content enablers on output.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

If you use the **IMFContentEnabler** interface to renew revoked components, you must clarify the process to the user. This clarification must be made because the update process sends information from the client computer to a Microsoft Web site.

When you call **IMFContentEnabler::AutomaticEnable**, the content enabler launches the default browser with the address of the update service on the Microsoft Web site. A unique identifier that identifies the revoked component is sent to the update service. The service then redirects the browser to a Web page from which the user may be able to download and install the new version of the revoked component.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**Automated Component Revocation and Renewal**](automated-component-revocation-and-renewal.md)
</dt> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> </dl>

 

 





