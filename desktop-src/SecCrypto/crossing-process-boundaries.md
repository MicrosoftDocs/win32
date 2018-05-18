---
Description: 'The Schannel protocol engine performs the handshaking and authentication in a secure process and the bulk encryption/message passing in the application process.'
ms.assetid: 'bcd49aaf-b0e3-4c31-be95-986b8ad843a8'
title: Crossing Process Boundaries
---

# Crossing Process Boundaries

The [*Schannel*](security.s_gly#-security-schannel-gly) protocol engine performs the handshaking and authentication in a secure [*process*](security.p_gly#-security-process-gly) and the bulk encryption/message passing in the application process. This means that the [*bulk encryption keys*](security.b_gly#-security-bulk-encryption-key-gly) and [*MAC*](security.m_gly#-security-mac-gly) keys must be copied from one process to another. To copy the keys from one process to another, use the [**CryptExportKey**](cryptexportkey.md) and [**CryptImportKey**](cryptimportkey.md) functions as follows:

1.  The secure process exports each key into an [*OPAQUEKEYBLOB*](security.o_gly#-security-opaque-blob-gly) using [**CryptExportKey**](cryptexportkey.md), then destroys the key using [**CryptDestroyKey**](cryptdestroykey.md). Note that if the key is stored in hardware, the CSP must recognize this and must not attempt to destroy the key.
2.  The secure process passes the OPAQUEKEYBLOBs to the application process in a manner beyond the scope of this document.
3.  The application process imports each OPAQUEKEYBLOB back into the CSP using [**CryptImportKey**](cryptimportkey.md). At this point, the key must be in exactly the same [*state*](security.s_gly#-security-state-gly) as when it was exported.

 

 



