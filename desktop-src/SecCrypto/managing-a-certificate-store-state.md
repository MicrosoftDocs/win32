---
Description: Several functions provide services for managing a certificate store state.
ms.assetid: bae3d693-31b3-4c1d-9a8f-0dafa8bb6897
title: Managing a Certificate Store State
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing a Certificate Store State

Several functions provide services for managing a [*certificate store*](security.c_gly#-security-certificate-store-gly) [*state*](security.s_gly#-security-state-gly).

To gain access to certificates, the certificate store in which they are stored must be opened through a call to [**CertOpenStore**](/windows/win32/Wincrypt/nf-wincrypt-certopenstore?branch=master) or [**CertOpenSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certopensystemstorea?branch=master).

Usually a certificate store is opened in cached memory. It can be a new store or its contents can be loaded from the local registry, the registry on a remote computer, a disk file, a PKCS \#7 message, or some other source.

CryptoAPI certificate store functions also allow a store to maintain certificates outside cached memory in, for example, an external database of certificates such as the one provided by the Microsoft Certificate Server Database.

One of the parameters of the [**CertOpenStore**](/windows/win32/Wincrypt/nf-wincrypt-certopenstore?branch=master) function, *lpszStoreProvider,* determines the type of store opened and the provider used to open that store. For examples of opening certificate stores using various providers, see [Example C Code for Opening Certificate Stores](example-c-code-for-opening-certificate-stores.md).

[**CertCloseStore**](/windows/win32/Wincrypt/nf-wincrypt-certclosestore?branch=master) closes a certificate store. When a certificate store is closed, each of the certificate contexts in that store has its [*reference count*](security.r_gly#-security-reference-count-gly) reduced by one. Memory is freed for certificates whose reference count goes to zero.

Setting CERT\_CLOSE\_STORE\_FORCE\_FLAG with [**CertCloseStore**](/windows/win32/Wincrypt/nf-wincrypt-certclosestore?branch=master) closes the certificate store and frees memory for all of its certificate contexts regardless of their reference count. In some cases, such as in multithreaded programs, this cannot be desirable. If CERT\_CLOSE\_STORE\_CHECK\_FLAG is set, the store is closed, but a warning value is returned by the function if memory is still allocated for certificates whose reference counts have not been reduced to zero. If a certificate's reference count is greater than zero, a duplicate of that certificate context has not been freed. Use [**CertFreeCertificateContext**](/windows/win32/Wincrypt/nf-wincrypt-certfreecertificatecontext?branch=master), [**CertFreeCRLContext**](/windows/win32/Wincrypt/nf-wincrypt-certfreecrlcontext?branch=master), and [**CertFreeCTLContext**](/windows/win32/Wincrypt/nf-wincrypt-certfreectlcontext?branch=master) to free any certificates left open.

> [!Note]A [*certificate context*](security.c_gly#-security-certificate-context-gly) is a structure of type [**CERT\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_cert_context?branch=master) that has, among other members, a pointer to the encoded [*certificate BLOB*](security.c_gly#-security-certificate-blob-gly) and a pointer to a [**CERT\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cert_info?branch=master) structure. The **CERT\_INFO** structure contains the most significant certificate data. For more information about [*certificate*](security.c_gly#-security-certificate-gly), [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL), and [*certificate trust list*](security.c_gly#-security-certificate-trust-list-gly) (CTL) context structures, see [Encoding and Decoding a Certificate Context](encoding-and-decoding-a-certificate-context.md).
>
> Each certificate context also contains a [*reference count*](security.r_gly#-security-reference-count-gly) indicating the number of copies of the context's address that have been assigned. Each time a certificate context is duplicated in any way, its reference count is incremented by one. Each time a pointer to a certificate context is freed, the reference count in the certificate context is decremented by one. When the reference count on a certificate context reaches zero, the memory holding the context is de-allocated. Memory allocated for a certificate context is also de-allocated when that context is in a store and the store is closed using CERT\_CLOSE\_STORE\_FORCE\_FLAG. If the memory for a context is de-allocated and pointers to that context are still in use, those pointers are no longer valid.

 

[**CertDuplicateStore**](/windows/win32/Wincrypt/nf-wincrypt-certduplicatestore?branch=master) increases the [*reference count*](security.r_gly#-security-reference-count-gly) on the store.

[**CertSaveStore**](/windows/win32/Wincrypt/nf-wincrypt-certsavestore?branch=master) saves the contents of a store to a disk file or a memory location, and

[**CertControlStore**](/windows/win32/Wincrypt/nf-wincrypt-certcontrolstore?branch=master) manages a store while it is open. An application with an open store can be notified when the persisted state of that store has changed by some other process. This could happen if new certificates were copied to the local computer store from a domain control computer.

When changes are discovered, the cached store can re-synchronize its cached store to match the persisted state of the store. [**CertControlStore**](/windows/win32/Wincrypt/nf-wincrypt-certcontrolstore?branch=master) also supports a process that copies cached store changes to permanent storage when these changes in the cached store are not automatically saved.

Certificate store-like certificate contexts can have extended properties. [**CertSetStoreProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetstoreproperty?branch=master) adds extended properties to a certificate store. [**CertGetStoreProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetstoreproperty?branch=master) retrieves any properties set on a certificate store. Currently, the only predefined certificate store property is a store's localized name.

 

 



