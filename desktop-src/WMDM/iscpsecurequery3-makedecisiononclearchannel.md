---
title: ISCPSecureQuery3 MakeDecisionOnClearChannel method
description: The MakeDecisionOnClearChannel method determines whether access to the content is allowed on a clear channel. If access is allowed, this method returns the interface used to access the content.
ms.assetid: '63ffa9ec-b8bb-4d5d-b380-e4dbe0fc865a'
keywords: ["MakeDecisionOnClearChannel method windows Media Device Manager", "MakeDecisionOnClearChannel method windows Media Device Manager , ISCPSecureQuery3 interface", "ISCPSecureQuery3 interface windows Media Device Manager , MakeDecisionOnClearChannel method"]
topic_type:
- apiref
api_name:
- ISCPSecureQuery3.MakeDecisionOnClearChannel
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureQuery3::MakeDecisionOnClearChannel method

The **MakeDecisionOnClearChannel** method determines whether access to the content is allowed on a clear channel. If access is allowed, this method returns the interface used to access the content.

## Syntax


```C++
HRESULT MakeDecisionOnClearChannel(
  [in]      UINT                fuFlags,
  [in]      BYTE                *pData,
  [in]      DWORD               dwSize,
  [in]      DWORD               dwAppSec,
  [in]      BYTE                *pbSPSessionKey,
  [in]      DWORD               dwSessionKeyLen,
  [in]      IMDSPStorageGlobals *pStorageGlobals,
  [in]      IWMDMProgress3      *pProgressCallback,
  [in]      BYTE                *pAppCertApp,
  [in]      DWORD               dwAppCertAppLen,
  [in]      BYTE                *pAppCertSP,
  [in]      DWORD               dwAppCertSPLen,
  [in, out] LPWSTR              *pszRevocationURL,
  [in, out] DWORD               *pdwRevocationURLLen,
  [out]     DWORD               *pdwRevocationBitFlag,
  [in, out] ULONGLONG           *pqwFileSize,
  [in]      IUnknown            *pUnknown,
  [out]     ISCPSecureExchange  **ppExchange
);
```



## Parameters

<dl> <dt>

*fuFlags* \[in\]
</dt> <dd>

Flags describing the data offered to the content provider for making decisions. The following flags can be present.



| Flag                              | Description                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDM\_SCP\_DECIDE\_DATA           | The *pData* parameter points to data to be examined.                                                                                                                                                                                                                                                                              |
| WMDM\_MODE\_TRANSFER\_PROTECTED   | The output object data from the [**ISCPSecureExchange**](iscpsecureexchange.md) interface must be protected. If Windows Media Device Manager sets neither or both mode flags, digital rights management (DRM) decides whether the output object data from the **ISCPSecureExchange** interface must be protected or unprotected. |
| WMDM\_MODE\_TRANSFER\_UNPROTECTED | The output object data from the **ISCPSecureExchange** interface must be unprotected. If Windows Media Device Manager sets neither or both mode flags, digital rights management (DRM) decides whether the output object data from the **ISCPSecureExchange** interface must be protected or unprotected.                         |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to a data object containing the data to be examined.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

**DWORD** that contains the length, in bytes, of the data to be examined.

</dd> <dt>

*dwAppSec* \[in\]
</dt> <dd>

**DWORD** that indicates the current level of security of Windows Media Device Manager. This is the smaller of the current security levels of the application and the target service provider.

</dd> <dt>

*pbSPSessionKey* \[in\]
</dt> <dd>

Pointer to an array of bytes containing the session key for securing communication with the service provider to which *pStgGlobals* points.

</dd> <dt>

*dwSessionKeyLen* \[in\]
</dt> <dd>

Length of the byte array to which *pbSPSessionKey* points.

</dd> <dt>

*pStorageGlobals* \[in\]
</dt> <dd>

Pointer to the [**IWMDMStorageGlobals**](iwmdmstorageglobals.md) interface on the root storage of the media or device to or from which the file is being transferred.

</dd> <dt>

*pProgressCallback* \[in\]
</dt> <dd>

Pointer to a progress callback object.

</dd> <dt>

*pAppCertApp* \[in\]
</dt> <dd>

Pointer to an application certificate of the application object.

</dd> <dt>

*dwAppCertAppLen* \[in\]
</dt> <dd>

**DWORD** containing the length, in bytes, of the application certificate.

</dd> <dt>

*pAppCertSP* \[in\]
</dt> <dd>

Pointer to the application certificate of the service provider object.

</dd> <dt>

*dwAppCertSPLen* \[in\]
</dt> <dd>

**DWORD** containing the length, in bytes, of the application certificate.

</dd> <dt>

*pszRevocationURL* \[in, out\]
</dt> <dd>

Pointer to a buffer to hold the revocation URL.

</dd> <dt>

*pdwRevocationURLLen* \[in, out\]
</dt> <dd>

Pointer to a **DWORD** containing the size of the *rpszRevocationURL* buffer in bytes.

</dd> <dt>

*pdwRevocationBitFlag* \[out\]
</dt> <dd>

Pointer to a **DWORD** containing the revocation bit flag. The flag value will be either zero or one or more of the following flag names combined by using a bitwise **OR**.



| Value               | Description                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------|
| WMDM\_WMDM\_REVOKED | Windows Media Device Manager itself has been revoked.                                                                    |
| WMDM\_APP\_REVOKED  | The application has been revoked and needs to be updated before any DRM-protected content can be transferred.            |
| WMDM\_SP\_REVOKED   | The service provider has been revoked and needs to be updated before any DRM-protected content can be transferred to it. |
| WMDM\_SCP\_REVOKED  | The content provider has been revoked and needs to be updated before any DRM-protected content can be transferred.       |



 

</dd> <dt>

*pqwFileSize* \[in, out\]
</dt> <dd>

Pointer to a **QWORD** containing the file size. The content provider is responsible for updating this value or setting it to zero if the size of the destination file cannot be determined at this point.

</dd> <dt>

*pUnknown* \[in\]
</dt> <dd>

Pointer to an unknown interface from the application.

</dd> <dt>

*ppExchange* \[out\]
</dt> <dd>

Pointer to an exchange object that receives the exchange interface.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If the method fails, it returns an **HRESULT** error code.



| Return code                                                                                                     | Description                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_CALL\_OUT\_OF\_SEQUENCE**</dt> </dl> | This method was called out of sequence.<br/>                                                                                                                                                                                                                   |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl>      | The message authentication code is not valid.<br/>                                                                                                                                                                                                             |
| <dl> <dt>**WMDM\_E\_MOREDATA**</dt> </dl>                | Windows Media Device Manager must call this method again with another packet of data. The size of the packet is determined by the *pdwMinDecisionData* parameter in the [**ISCPSecureQuery::GetDataDemands**](iscpsecurequery-getdatademands.md) method.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>                         | The caller does not have the rights required to perform the requested transfer.<br/>                                                                                                                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                    | A parameter is invalid or is a **NULL** pointer.<br/>                                                                                                                                                                                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>                          | An unspecified error occurred.<br/>                                                                                                                                                                                                                            |



 

## Remarks

This method is identical to [**ISCPSecureQuery2::MakeDecision2**](iscpsecurequery2-makedecision2.md) except that the parameters passed to this method are not encrypted. Consequently this method is more efficient.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureQuery2::MakeDecision2**](iscpsecurequery2-makedecision2.md)
</dt> <dt>

[**ISCPSecureQuery3 Interface**](iscpsecurequery3.md)
</dt> </dl>

 

 





