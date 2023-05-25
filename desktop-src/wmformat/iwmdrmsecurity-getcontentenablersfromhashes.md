---
title: IWMDRMSecurity GetContentEnablersFromHashes method (Wmdrmsdk.h)
description: The GetContentEnablersFromHashes method retrieves content enabler interfaces that enable renewal of components based on hashed certificates.
ms.assetid: d7429859-b609-49a2-a369-d02260bc15bf
keywords:
- GetContentEnablersFromHashes method windows Media Format
- GetContentEnablersFromHashes method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , GetContentEnablersFromHashes method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.GetContentEnablersFromHashes
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMSecurity::GetContentEnablersFromHashes method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetContentEnablersFromHashes** method retrieves content enabler interfaces that enable renewal of components based on hashed certificates.

## Syntax


```C++
HRESULT GetContentEnablersFromHashes(
  [in]      BSTR              *rgpbCertHashes,
  [in]      DWORD             cCerts,
  [in]      HRESULT           hResultHint,
  [out]     IMFContentEnabler **prgContentEnablers,
  [in, out] DWORD             *pcContentEnablers
);
```



## Parameters

<dl> <dt>

*rgpbCertHashes* \[in\]
</dt> <dd>

Array of certificate hashes to obtain content enablers for.

</dd> <dt>

*cCerts* \[in\]
</dt> <dd>

Number of certificates to retrieve content enablers for. This is the number of elements in the *rgpbCertHashes* array.

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

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> </dl>

 

 





