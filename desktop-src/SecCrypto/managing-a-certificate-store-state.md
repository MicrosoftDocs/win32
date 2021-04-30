---
description: Several functions provide services for managing a certificate store state.
ms.assetid: bae3d693-31b3-4c1d-9a8f-0dafa8bb6897
title: Managing a Certificate Store State
ms.topic: article
ms.date: 05/31/2018
---

# Managing a Certificate Store State

Several functions provide services for managing a [*certificate store*](../secgloss/c-gly.md) [*state*](../secgloss/s-gly.md).

To gain access to certificates, the certificate store in which they are stored must be opened through a call to [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore) or [**CertOpenSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopensystemstorea).

Usually a certificate store is opened in cached memory. It can be a new store or its contents can be loaded from the local registry, the registry on a remote computer, a disk file, a PKCS \#7 message, or some other source.

CryptoAPI certificate store functions also allow a store to maintain certificates outside cached memory in, for example, an external database of certificates such as the one provided by the Microsoft Certificate Server Database.

One of the parameters of the [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore) function, *lpszStoreProvider,* determines the type of store opened and the provider used to open that store. For examples of opening certificate stores using various providers, see [Example C Code for Opening Certificate Stores](example-c-code-for-opening-certificate-stores.md).

[**CertCloseStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certclosestore) closes a certificate store. When a certificate store is closed, each of the certificate contexts in that store has its [*reference count*](../secgloss/r-gly.md) reduced by one. Memory is freed for certificates whose reference count goes to zero.

Setting CERT\_CLOSE\_STORE\_FORCE\_FLAG with [**CertCloseStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certclosestore) closes the certificate store and frees memory for all of its certificate contexts regardless of their reference count. In some cases, such as in multithreaded programs, this cannot be desirable. If CERT\_CLOSE\_STORE\_CHECK\_FLAG is set, the store is closed, but a warning value is returned by the function if memory is still allocated for certificates whose reference counts have not been reduced to zero. If a certificate's reference count is greater than zero, a duplicate of that certificate context has not been freed. Use [**CertFreeCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatecontext), [**CertFreeCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecrlcontext), and [**CertFreeCTLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreectlcontext) to free any certificates left open.

> [!Note]
> A [*certificate context*](../secgloss/c-gly.md) is a structure of type [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) that has, among other members, a pointer to the encoded [*certificate BLOB*](../secgloss/c-gly.md) and a pointer to a [**CERT\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_info) structure. The **CERT\_INFO** structure contains the most significant certificate data. For more information about [*certificate*](../secgloss/c-gly.md), [*certificate revocation list*](../secgloss/c-gly.md) (CRL), and [*certificate trust list*](../secgloss/c-gly.md) (CTL) context structures, see [Encoding and Decoding a Certificate Context](encoding-and-decoding-a-certificate-context.md).
> 
> Each certificate context also contains a [*reference count*](../secgloss/r-gly.md) indicating the number of copies of the context's address that have been assigned. Each time a certificate context is duplicated in any way, its reference count is incremented by one. Each time a pointer to a certificate context is freed, the reference count in the certificate context is decremented by one. When the reference count on a certificate context reaches zero, the memory holding the context is de-allocated. Memory allocated for a certificate context is also de-allocated when that context is in a store and the store is closed using CERT\_CLOSE\_STORE\_FORCE\_FLAG. If the memory for a context is de-allocated and pointers to that context are still in use, those pointers are no longer valid.

 

[**CertDuplicateStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatestore) increases the [*reference count*](../secgloss/r-gly.md) on the store.

[**CertSaveStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsavestore) saves the contents of a store to a disk file or a memory location, and

[**CertControlStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcontrolstore) manages a store while it is open. An application with an open store can be notified when the persisted state of that store has changed by some other process. This could happen if new certificates were copied to the local computer store from a domain control computer.

When changes are discovered, the cached store can re-synchronize its cached store to match the persisted state of the store. [**CertControlStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcontrolstore) also supports a process that copies cached store changes to permanent storage when these changes in the cached store are not automatically saved.

Certificate store-like certificate contexts can have extended properties. [**CertSetStoreProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetstoreproperty) adds extended properties to a certificate store. [**CertGetStoreProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetstoreproperty) retrieves any properties set on a certificate store. Currently, the only predefined certificate store property is a store's localized name.

 

 
