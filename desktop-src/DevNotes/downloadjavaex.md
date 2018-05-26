---
Description: Downloads the .cab file signature, verifies the permissions associated with the packages, and executes them based on authentication.
ms.assetid: b86a8f39-73a1-4e17-ac83-9ed095de4922
title: DownloadJavaEX function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

A [**CRYPT\_PROVIDER\_DATA**](security.crypt_provider_data) structure that contains certificate data such as file and zone permissions.

</dd> <dt>

*pJava* \[in\]
</dt> <dd>

A [**JAVA\_POLICY\_PROVIDER**](winprog.java_policy_provider) structure that contains data related to the policy provider.

</dd> <dt>

*pFunctions* \[in\]
</dt> <dd>

A [**CRYPT\_PROVIDER\_FUNCTIONS**](security.crypt_provider_functions) structure that contains a list of methods to verify certificate objects, signatures, and final policies.

</dd> <dt>

*fCertificate* \[in\]
</dt> <dd>

If a certificate is present, this parameter is **TRUE**. Otherwise, it is **FALSE**.

</dd> <dt>

*pTrust* \[in\]
</dt> <dd>

A [**JAVA\_TRUST**](/windows/win32/Capi/ns-capi-_java_trust?branch=master) structure that contains trust information such as encoded permission, encoder signature, and authentic return policy code.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Javacypt.dll</dt> </dl> |



 

 




