---
Description: Downloads the .cab file signature, verifies the permissions associated with the packages, and executes them based on authentication.
ms.assetid: b86a8f39-73a1-4e17-ac83-9ed095de4922
title: DownloadJavaEX function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

A [**CRYPT\_PROVIDER\_DATA**](https://msdn.microsoft.com/93ea2ad5-65da-4daa-bfd4-e3d1307829b2) structure that contains certificate data such as file and zone permissions.

</dd> <dt>

*pJava* \[in\]
</dt> <dd>

A [**JAVA\_POLICY\_PROVIDER**](https://www.bing.com/search?q=**JAVA\_POLICY\_PROVIDER**) structure that contains data related to the policy provider.

</dd> <dt>

*pFunctions* \[in\]
</dt> <dd>

A [**CRYPT\_PROVIDER\_FUNCTIONS**](https://msdn.microsoft.com/2c00f8ec-e262-4df8-8984-a2702a4162bf) structure that contains a list of methods to verify certificate objects, signatures, and final policies.

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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Javacypt.dll</dt> </dl> |



 

 




