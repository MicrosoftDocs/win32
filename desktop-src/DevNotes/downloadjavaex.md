---
Description: Downloads the .cab file signature, verifies the permissions associated with the packages, and executes them based on authentication.
ms.assetid: b86a8f39-73a1-4e17-ac83-9ed095de4922
title: DownloadJavaEX function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DownloadJavaEX
api_type: 
- DllExport
api_location: 
- Javacypt.dll
---

# DownloadJavaEX function

Downloads the .cab file signature, verifies the permissions associated with the packages, and executes them based on authentication.

## Syntax


```C++
HRESULT WINAPI DownloadJavaEX(
  _In_ PALLOCATOR               Reserved,
  _In_ PCRYPT_PROVIDER_DATA     pProviderData,
  _In_ PJAVA_POLICY_PROVIDER    pJava,
  _In_ CRYPT_PROVIDER_FUNCTIONS *pFunctions,
  _In_ BOOL                     fCertificate,
  _In_ PJAVA_TRUST              pTrust
);
```



## Parameters

<dl> <dt>

*Reserved* \[in\]
</dt> <dd>

This parameter is reserved.

</dd> <dt>

*pProviderData* \[in\]
</dt> <dd>

A [**CRYPT\_PROVIDER\_DATA**](https://msdn.microsoft.com/en-us/library/Aa381453(v=VS.85).aspx) structure that contains certificate data such as file and zone permissions.

</dd> <dt>

*pJava* \[in\]
</dt> <dd>

A [**JAVA\_POLICY\_PROVIDER**](https://msdn.microsoft.com/library/Bb432350(v=VS.85).aspx) structure that contains data related to the policy provider.

</dd> <dt>

*pFunctions* \[in\]
</dt> <dd>

A [**CRYPT\_PROVIDER\_FUNCTIONS**](https://msdn.microsoft.com/en-us/library/Aa381455(v=VS.85).aspx) structure that contains a list of methods to verify certificate objects, signatures, and final policies.

</dd> <dt>

*fCertificate* \[in\]
</dt> <dd>

If a certificate is present, this parameter is **TRUE**. Otherwise, it is **FALSE**.

</dd> <dt>

*pTrust* \[in\]
</dt> <dd>

A [**JAVA\_TRUST**](/windows/desktop/api/Capi/ns-capi-_java_trust) structure that contains trust information such as encoded permission, encoder signature, and authentic return policy code.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Javacypt.dll</dt> </dl> |



 

 




