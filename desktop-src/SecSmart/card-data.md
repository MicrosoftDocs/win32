---
title: CARD\_DATA structure
description: Contains context information used during communication between a smart card module and either the Microsoft Base Smart Card Cryptographic Service Provider (CSP) or the smart card key storage provider (KSP).
ms.assetid: 47ac884b-c9f8-43a2-bff4-8b2bfcd94db0
keywords:
- CARD_DATA structure Security
- PCARD_DATA structure pointer Security
topic_type:
- apiref
api_name:
- CARD_DATA
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CARD\_DATA structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_DATA** structure contains context information used during communication between a smart card module and either the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) (CSP) or the smart card [*key storage provider*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-storage-provider-gly) (KSP). The structure includes pointers to all functions that the smart card module implements. It also includes pointers to the functions that the CSP and KSP export to the smart card module.

## Syntax


```C++
typedef struct _CARD_DATA {
  DWORD                           dwVersion;
  PBYTE                           pbAtr;
  DWORD                           cbAtr;
  LPWSTR                          pwszCardName;
  PFN_CSP_ALLOC                   pfnCspAlloc;
  PFN_CSP_REALLOC                 pfnCspReAlloc;
  PFN_CSP_FREE                    pfnCspFree;
  PFN_CSP_CACHE_ADD_FILE          pfnCspCacheAddFile;
  PFN_CSP_CACHE_LOOKUP_FILE       pfnCspCacheLookupFile;
  PFN_CSP_CACHE_DELETE_FILE       pfnCspCacheDeleteFile;
  PVOID                           pvCacheContext;
  PFN_CSP_PAD_DATA                pfnCspPadData;
  SCARDCONTEXT                    hSCardCtx;
  SCARDHANDLE                     hScard;
  PVOID                           pvVendorSpecific;
  PFN_CARD_DELETE_CONTEXT         pfnCardDeleteContext;
  PFN_CARD_QUERY_CAPABILITIES     pfnCardQueryCapabilities;
  PFN_CARD_DELETE_CONTAINER       pfnCardDeleteContainer;
  PFN_CARD_CREATE_CONTAINER       pfnCardCreateContainer;
  PFN_CARD_GET_CONTAINER_INFO     pfnCardGetContainerInfo;
  PFN_CARD_AUTHENTICATE_PIN       pfnCardAuthenticatePin;
  PFN_CARD_GET_CHALLENGE          pfnCardGetChallenge;
  PFN_CARD_AUTHENTICATE_CHALLENGE pfnCardAuthenticateChallenge;
  PFN_CARD_UNBLOCK_PIN            pfnCardUnblockPin;
  PFN_CARD_CHANGE_AUTHENTICATOR   pfnCardChangeAuthenticator;
  PFN_CARD_DEAUTHENTICATE         pfnCardDeauthenticate;
  PFN_CARD_CREATE_DIRECTORY       pfnCardCreateDirectory;
  PFN_CARD_DELETE_DIRECTORY       pfnCardDeleteDirectory;
  LPVOID                          pvUnused3;
  LPVOID                          pvUnused4;
  PFN_CARD_CREATE_FILE            pfnCardCreateFile;
  PFN_CARD_READ_FILE              pfnCardReadFile;
  PFN_CARD_WRITE_FILE             pfnCardWriteFile;
  PFN_CARD_DELETE_FILE            pfnCardDeleteFile;
  PFN_CARD_ENUM_FILES             pfnCardEnumFiles;
  PFN_CARD_GET_FILE_INFO          pfnCardGetFileInfo;
  PFN_CARD_QUERY_FREE_SPACE       pfnCardQueryFreeSpace;
  PFN_CARD_QUERY_KEY_SIZES        pfnCardQueryKeySizes;
  PFN_CARD_SIGN_DATA              pfnCardSignData;
  PFN_CARD_RSA_DECRYPT            pfnCardRSADecrypt;
  PFN_CARD_CONSTRUCT_DH_AGREEMENT pfnCardConstructDHAgreement;
  PFN_CARD_DERIVE_KEY             pfnCardDeriveKey;
  PFN_CARD_DESTROY_DH_AGREEMENT   pfnCardDestroyDHAgreement;
  PFN_CSP_GET_DH_AGREEMENT        pfnCspGetDHAgreement;
} CARD_DATA, *PCARD_DATA;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the smart card module.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function with the requested version.

On output, this member must be set to the version of this structure that the smart card module returns.

</dd> <dt>

**pbAtr**
</dt> <dd>

The [*ATR string*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-atr-string-gly) that identifies the [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**cbAtr**
</dt> <dd>

The size, in bytes, of the string contained in the *pbAtr* parameter.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**pwszCardName**
</dt> <dd>

A pointer to a null-terminated wide character string that contains the name of the smart card.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**pfnCspAlloc**
</dt> <dd>

A [**PFN\_CSP\_ALLOC**](pfn-csp-alloc.md) function pointer.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**pfnCspReAlloc**
</dt> <dd>

A [**PFN\_CSP\_ALLOC**](pfn-csp-alloc.md) function pointer.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**pfnCspFree**
</dt> <dd>

A [**PFN\_CSP\_FREE**](pfn-csp-free.md) function pointer.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**pfnCspCacheAddFile**
</dt> <dd>

A [**PFN\_CSP\_CACHE\_ADD\_FILE**](pfn-csp-cache-add-file.md) function pointer.

This member must be initialized by the CSP or KSP after calling the [**CardAcquireContext**](cardacquirecontext.md) function. Implementations of **CardAcquireContext** must check that this member is not set to **NULL** before using or caching the pointer.

</dd> <dt>

**pfnCspCacheLookupFile**
</dt> <dd>

A [**PFN\_CSP\_CACHE\_LOOKUP\_FILE**](pfn-csp-cache-lookup-file.md) function pointer.

This member must be initialized by the CSP or KSP after calling the [**CardAcquireContext**](cardacquirecontext.md) function. Implementations of **CardAcquireContext** must check that this member is not set to **NULL** before using or caching the pointer.

</dd> <dt>

**pfnCspCacheDeleteFile**
</dt> <dd>

A [**PFN\_CSP\_CACHE\_DELETE\_FILE**](pfn-csp-cache-delete-file.md) function pointer.

This member must be initialized by the CSP or KSP after calling the [**CardAcquireContext**](cardacquirecontext.md) function. Implementations of **CardAcquireContext** must check that this member is not set to **NULL** before using or caching the pointer.

</dd> <dt>

**pvCacheContext**
</dt> <dd>

A pointer to a context value used by the functions pointed to by the [**PFN\_CSP\_CACHE\_ADD\_FILE**](pfn-csp-cache-add-file.md), [**PFN\_CSP\_CACHE\_LOOKUP\_FILE**](pfn-csp-cache-lookup-file.md), and [**PFN\_CSP\_CACHE\_DELETE\_FILE**](pfn-csp-cache-delete-file.md) function pointers.

This member must be initialized by the CSP or KSP after calling the [**CardAcquireContext**](cardacquirecontext.md) function. Implementations of **CardAcquireContext** must check that this member is not set to **NULL** before using or caching the pointer.

</dd> <dt>

**pfnCspPadData**
</dt> <dd>

A [**PFN\_CSP\_PAD\_DATA**](pfn-csp-pad-data.md) function pointer.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**hSCardCtx**
</dt> <dd>

A handle that identifies the [*resource manager context*](https://msdn.microsoft.com/library/windows/desktop/ms721604#-security-resource-manager-context-gly). The CSP or KSP retrieves the resource manager context from a previous call to the [**SCardEstablishContext**](https://msdn.microsoft.com/library/windows/desktop/aa379479) function.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**hScard**
</dt> <dd>

A handle to a smart card. The CSP or KSP retrieves this handle from a previous call to the [**SCardConnect**](https://msdn.microsoft.com/library/windows/desktop/aa379473) function.

This member must be initialized by the CSP or KSP before calling the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

**pvVendorSpecific**
</dt> <dd>

A pointer to card-specific information that the smart card module can use.

</dd> <dt>

**pfnCardDeleteContext**
</dt> <dd>

A pointer to the [**CardDeleteContext**](carddeletecontext.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardQueryCapabilities**
</dt> <dd>

A pointer to the [**CardQueryCapabilities**](cardquerycapabilities.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardDeleteContainer**
</dt> <dd>

A pointer to the [**CardDeleteContainer**](carddeletecontainer.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardCreateContainer**
</dt> <dd>

A pointer to the [**CardCreateContainer**](cardcreatecontainer.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardGetContainerInfo**
</dt> <dd>

A pointer to the [**CardGetContainerInfo**](cardgetcontainerinfo.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardAuthenticatePin**
</dt> <dd>

A pointer to the [**CardAuthenticatePin**](cardauthenticatepin.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardGetChallenge**
</dt> <dd>

A pointer to the [**CardGetChallenge**](cardgetchallenge.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardAuthenticateChallenge**
</dt> <dd>

A pointer to the [**CardAuthenticateChallenge**](cardauthenticatechallenge.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardUnblockPin**
</dt> <dd>

A pointer to the [**CardUnblockPin**](cardunblockpin.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardChangeAuthenticator**
</dt> <dd>

A pointer to the [**CardChangeAuthenticator**](cardchangeauthenticator.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardDeauthenticate**
</dt> <dd>

A pointer to the [**CardDeauthenticate**](carddeauthenticate.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardCreateDirectory**
</dt> <dd>

A pointer to the [**CardCreateDirectory**](cardcreatedirectory.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardDeleteDirectory**
</dt> <dd>

A pointer to the [**CardDeleteDirectory**](carddeletedirectory.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pvUnused3**
</dt> <dd>

Reserved.

</dd> <dt>

**pvUnused4**
</dt> <dd>

Reserved.

</dd> <dt>

**pfnCardCreateFile**
</dt> <dd>

A pointer to the [**CardCreateFile**](cardcreatefile.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardReadFile**
</dt> <dd>

A pointer to the [**CardReadFile**](cardreadfile.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardWriteFile**
</dt> <dd>

A pointer to the [**CardWriteFile**](cardwritefile.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardDeleteFile**
</dt> <dd>

A pointer to the [**CardDeleteFile**](carddeletefile.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardEnumFiles**
</dt> <dd>

A pointer to the [**CardEnumFiles**](cardenumfiles.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardGetFileInfo**
</dt> <dd>

A pointer to the [**CardGetFileInfo**](cardgetfileinfo.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardQueryFreeSpace**
</dt> <dd>

A pointer to the [**CardQueryFreeSpace**](cardqueryfreespace.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardQueryKeySizes**
</dt> <dd>

A pointer to the [**CardQueryKeySizes**](cardquerykeysizes.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardSignData**
</dt> <dd>

A pointer to the [**CardSignData**](cardsigndata.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardRSADecrypt**
</dt> <dd>

A pointer to the [**CardRSADecrypt**](cardrsadecrypt.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardConstructDHAgreement**
</dt> <dd>

A pointer to the [**CardConstructDHAgreement**](cardconstructdhagreement.md) function implemented by the smart card module.

This member is initialized by the [**CardAcquireContext**](cardacquirecontext.md) function of the smart card module.

</dd> <dt>

**pfnCardDeriveKey**
</dt> <dd>

A pointer to the [**CardDeriveKey**](cardderivekey.md) function implemented by the smart card module.

**Windows Server 2003, Windows XP, Windows 2000 Server and Windows 2000 Professional:** This function is not supported.

</dd> <dt>

**pfnCardDestroyDHAgreement**
</dt> <dd>

A pointer to the [**CardDestroyDHAgreement**](carddestroydhagreement.md) function implemented by the smart card module.

**Windows Server 2003, Windows XP, Windows 2000 Server and Windows 2000 Professional:** This function is not supported.

</dd> <dt>

**pfnCspGetDHAgreement**
</dt> <dd>

A pointer to the [*CspGetDHAgreement*](cspgetdhagreement.md) callback function set by the CSP.

**Windows Server 2003, Windows XP, Windows 2000 Server and Windows 2000 Professional:** This function is not supported.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> </dl>

 

 





