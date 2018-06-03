---
title: IPC\_CREDENTIAL structure
description: Credential structure used to authenticate to a server running AD RMS.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: ce77fbc9-f1da-4556-b3d2-192dc24e0747
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_CREDENTIAL structure Active Directory Rights Management Services SDK 2.0
- PIPC_CREDENTIAL structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_CREDENTIAL
api_location:
- Ipcbase.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_CREDENTIAL structure

Credential structure used to authenticate to a server running AD RMS.

## Syntax


```C++
typedef struct _IPC_CREDENTIAL {
  DWORD dwType;
  union {
    PCCERT_CONTEXT                 pcCertContext;
    PCIPC_CREDENTIAL_SYMMETRIC_KEY pcSymmetricKey;
    PIPC_OATH2_CALLBACK_INFO       pcOAuth2;
  };
} IPC_CREDENTIAL, *PIPC_CREDENTIAL;
```



## Members

<dl> <dt>

**dwType**
</dt> <dd>

Contains the type code for the credential, which governs how the credential is interpreted. For more information, see Remarks.

<dt>

<span id="IPC_CREDENTIAL_TYPE_X509"></span><span id="ipc_credential_type_x509"></span>

<span id="IPC_CREDENTIAL_TYPE_X509"></span><span id="ipc_credential_type_x509"></span>**IPC\_CREDENTIAL\_TYPE\_X509** (1)


</dt> <dd>

X509 Credential - only allowed when the API Mode is set to **IPC\_API\_MODE\_SERVER**. For more information, see [**API mode values**](api-mode-values.md).

</dd> <dt>

<span id="IPC_CREDENTIAL_TYPE_SYMMETRIC_KEY"></span><span id="ipc_credential_type_symmetric_key"></span>

<span id="IPC_CREDENTIAL_TYPE_SYMMETRIC_KEY"></span><span id="ipc_credential_type_symmetric_key"></span>**IPC\_CREDENTIAL\_TYPE\_SYMMETRIC\_KEY** (2)


</dt> <dd>

Symmetric Key - only allowed when the API Mode is set to **IPC\_API\_MODE\_SERVER**. For more information, see [**API mode values**](api-mode-values.md).

</dd> <dt>

<span id="IPC_CREDENTIAL_TYPE_OAUTH2"></span><span id="ipc_credential_type_oauth2"></span>

<span id="IPC_CREDENTIAL_TYPE_OAUTH2"></span><span id="ipc_credential_type_oauth2"></span>**IPC\_CREDENTIAL\_TYPE\_OAUTH2** (3)


</dt> <dd>

**pcOauth2** is valid and points to an [**IPC\_OAUTH2\_CALLBACK\_INFO**](ipc-oath2-callback-info.md) structure that will be exercised to retrieve an OAuth token when authentication is required.

</dd> </dl> </dd> <dt>

**pcCertContext**
</dt> <dd>

Credential governed by **dwType**.

</dd> <dt>

**pcSymmetricKey**
</dt> <dd>

Symmetric key credential represented by an [**IPC\_CREDENTIAL\_SYMMETRIC\_KEY**](ipc-credential-symmetric-key.md) structure.

</dd> <dt>

**pcOAuth2**
</dt> <dd>

Callback for an OAuth credential represented by an [**IPC\_OAUTH2\_CALLBACK\_INFO**](ipc-oath2-callback-info.md) structure.

</dd> </dl>

## Remarks

> \[!Important\]  
> The union in this structure has been updated to work with compilers that do not support nameless unions. If your compiler does not support nameless unions, define the **NONAMELESSUNION** token before including the Msipc.h header file.

 

The value of the **dwType** member governs the interpretation of the union. The following list shows the possible values for **dwType**.

<dl> <dt>

<span id="IPC_CREDENTIAL_TYPE_X509_PCCERT_CONTEXT"></span><span id="ipc_credential_type_x509_pccert_context"></span>**IPC\_CREDENTIAL\_TYPE\_X509**/**PCCERT\_CONTEXT**
</dt> <dd>

Use one of the Cryptographic APIs defined in WinCrypt.h to create **PCCERT\_CONTEXT** (for example, [**CertFindCertificateInStore**](https://msdn.microsoft.com/library/windows/desktop/aa376064) or [**CertCreateCertificateContext**](https://msdn.microsoft.com/library/windows/desktop/aa376033)).

The **PCCERT\_CONTEXT** value should be valid until the call is returned.

This credential will be used while connecting to an AD RMS server to authenticate. If the specified credential fails to authenticate **HRESULT\_FROM\_WIN32**(**ERROR\_NOT\_AUTHENTICATED**) will be returned. This credential will be used silently (that is, no credentials UI will be displayed).

</dd> <dt>

<span id="IPC_CREDENTIAL_TYPE_SYMMETRIC_KEY_PCIPC_CREDENTIAL_SYMMETRIC_KEY"></span><span id="ipc_credential_type_symmetric_key_pcipc_credential_symmetric_key"></span>**IPC\_CREDENTIAL\_TYPE\_SYMMETRIC\_KEY**/**PCIPC\_CREDENTIAL\_SYMMETRIC\_KEY**
</dt> <dd>

The Symmetric key, Service Principal Name and BPOS Id can be acquired by registering the Service Principal in ACS. For more information, see [Enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md).

</dd> <dt>

<span id="IPC_CREDENTIAL_TYPE_OATH2_PIPC_OATH2_CALLBACK_INFO"></span><span id="ipc_credential_type_oath2_pipc_oath2_callback_info"></span>**IPC\_CREDENTIAL\_TYPE\_OATH2**/**PIPC\_OATH2\_CALLBACK\_INFO**
</dt> <dd>

The RMS SDK will exercise this callback when OAuth authentication is needed.

For more information on how to retrieve a token, see [Azure Active Directory Authentication Libraries](https://azure.microsoft.com/documentation/articles/active-directory-authentication-libraries/).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**API mode values**](api-mode-values.md)
</dt> <dt>

[**IPC\_CREDENTIAL\_SYMMETRIC\_KEY**](ipc-credential-symmetric-key.md)
</dt> <dt>

[**IPC\_OAUTH2\_CALLBACK\_INFO**](ipc-oath2-callback-info.md)
</dt> <dt>

[**CertCreateCertificateContext**](https://msdn.microsoft.com/library/windows/desktop/aa376033)
</dt> <dt>

[**CertFindCertificateInStore**](https://msdn.microsoft.com/library/windows/desktop/aa376064)
</dt> <dt>

[ADAL authentication for your RMS enabled application](authentication-with-adal.md)
</dt> <dt>

[Azure Active Directory Authentication Libraries](https://azure.microsoft.com/documentation/articles/active-directory-authentication-libraries/)
</dt> <dt>

[Enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md)
</dt> </dl>

 

 





