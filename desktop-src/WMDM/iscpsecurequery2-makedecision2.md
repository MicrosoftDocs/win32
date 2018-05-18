---
title: ISCPSecureQuery2 MakeDecision2 method
description: The MakeDecision2 method determines whether the secure content provider is responsible for the content by examining data that Windows Media Device Manager passes to this method.
ms.assetid: 'a3031585-7a56-49d9-ad4b-d2f9e687dd6b'
keywords: ["MakeDecision2 method windows Media Device Manager", "MakeDecision2 method windows Media Device Manager , ISCPSecureQuery2 interface", "ISCPSecureQuery2 interface windows Media Device Manager , MakeDecision2 method"]
topic_type:
- apiref
api_name:
- ISCPSecureQuery2.MakeDecision2
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureQuery2::MakeDecision2 method

The **MakeDecision2** method determines whether the secure content provider is responsible for the content by examining data that Windows Media Device Manager passes to this method. This method provides two output parameters for error handling, a default location for updating revoked components, and a bit flag indicating which components have been revoked.

## Syntax


```C++
HRESULT MakeDecision2(
  [in]      UINT                fuFlags,
  [in]      BYTE                *pData,
  [in]      DWORD               dwSize,
  [in]      DWORD               dwAppSec,
  [in]      BYTE                *pbSPSessionKey,
  [in]      DWORD               dwSessionKeyLen,
  [in]      IMDSPStorageGlobals *pStorageGlobals,
  [in]      BYTE                *pAppCertApp,
  [in]      DWORD               dwAppCertAppLen,
  [in]      BYTE                *pAppCertSP,
  [in]      DWORD               dwAppCertSPLen,
  [in, out] LPWSTR              *pszRevocationURL,
  [in, out] DWORD               *pdwRevocationURLLen,
  [out]     DWORD               *pdwRevocationBitFlag,
  [in, out] ULONGLONG           *pqwFileSize,
  [in]      IUnknown            *pUnknown,
  [out]     ISCPSecureExchange  **ppExchange,
  [in, out] BYTE                abMac[WMDM_MAC_LENGTH]
);
```



## Parameters

<dl> <dt>

*fuFlags* \[in\]
</dt> <dd>

Flags describing the data offered to the secure content provider for making decisions. This parameter must be included in the input message authentication code. One or more of the following flags can be combined using a bitwise **OR**.



| Flag                              | Description                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDM\_SCP\_DECIDE\_DATA           | The *pData* parameter points to the data to be examined.                                                                                                                                                                                                                                                                               |
| WMDM\_MODE\_TRANSFER\_PROTECTED   | The output object data from the [**ISCPSecureExchange**](iscpsecureexchange.md) interface must be protected. If Windows Media Device Manager sets neither or both mode flags, Windows Media Digital Rights Manager decides whether the output object data from the **ISCPSecureExchange** interface must be protected or unprotected. |
| WMDM\_MODE\_TRANSFER\_UNPROTECTED | The output object data from the **ISCPSecureExchange** interface must be unprotected. If Windows Media Device Manager sets neither or both mode flags, Windows Media Digital Rights Manager decides whether the output object data from the **ISCPSecureExchange** interface must be protected or unprotected.                         |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to a data object containing the data to be examined. This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

**DWORD** containing the size of the file data.

</dd> <dt>

*dwAppSec* \[in\]
</dt> <dd>

**DWORD** that contains the length, in bytes, of the **dwAppSec** member of the [**WMDMRIGHTS**](wmdmrights.md) structure of the service provider and secure content provider to be examined. This parameter must be included in the input message authentication code.

</dd> <dt>

*pbSPSessionKey* \[in\]
</dt> <dd>

Pointer to an array of bytes containing the session key for securing communication with the service provider to which *pStgGlobals* points. This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSessionKeyLen* \[in\]
</dt> <dd>

**DWORD** containing the session key length.

</dd> <dt>

*pStorageGlobals* \[in\]
</dt> <dd>

Pointer to the [**IWMDMStorageGlobals**](iwmdmstorageglobals.md) interface on the root storage of the media or device to or from which the file is being transferred. This parameter must be included in the input message authentication code.

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

Pointer to a **DWORD** containing the revocation bit flag. The flag value will be either zero, or one or more of the following flag names combined by using a bitwise **OR**.



| Value               | Description                                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------------------------------|
| WMDM\_WMDM\_REVOKED | Windows Media Device Manager itself has been revoked.                                                                     |
| WMDM\_APP\_REVOKED  | The application has been revoked and needs to be updated before any DRM-protected content can be transferred.             |
| WMDM\_SP\_REVOKED   | The service provider has been revoked and needs to be updated before any DRM-protected content can be transferred to it.  |
| WMDM\_SCP\_REVOKED  | The secure content provider has been revoked and needs to be updated before any DRM-protected content can be transferred. |



 

</dd> <dt>

*pqwFileSize* \[in, out\]
</dt> <dd>

Pointer to a **QWORD** containing the file size. The secure content provider is responsible for updating this value or setting it to zero if the size of the destination file cannot be determined at this point.

</dd> <dt>

*pUnknown* \[in\]
</dt> <dd>

Pointer to an unknown interface from the application.

</dd> <dt>

*ppExchange* \[out\]
</dt> <dd>

Pointer to an exchange object that receives the exchange interface.

</dd> <dt>

*abMac\[WMDM\_MAC\_LENGTH\]* \[in, out\]
</dt> <dd>

Array of eight bytes containing the message authentication code for the parameter data of this method. (WMDM\_MAC\_LENGTH is defined as 8.)

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.



| Return code                                                                                     | Description                                                                                                              |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_REVOKED**</dt> </dl> | The application certificate that the secure content provider uses to talk to the DRM client has been revoked.<br/> |



 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureQuery Interface**](iscpsecurequery.md)
</dt> <dt>

[**ISCPSecureQuery::MakeDecision**](iscpsecurequery-makedecision.md)
</dt> <dt>

[**ISCPSecureQuery2 Interface**](iscpsecurequery2.md)
</dt> </dl>

 

 





