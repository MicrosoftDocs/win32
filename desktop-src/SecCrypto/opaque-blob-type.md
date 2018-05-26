---
Description: Opaque BLOBs, also known as OPAQUEKEYBLOBs, are used to store session keys in a vendor-specific format, such as Schannel.
ms.assetid: a0756c03-0c27-41ff-9b74-8af462e09675
title: Opaque BLOB Type
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Opaque BLOB Type

[*Opaque BLOBs*](security.o_gly#-security-opaque-blob-gly), also known as OPAQUEKEYBLOBs, are used to store [*session keys*](security.s_gly#-security-session-key-gly) in a vendor-specific format, such as [*Schannel*](security.s_gly#-security-schannel-gly). They contain the base key material and all current [*state*](security.s_gly#-security-state-gly) information. This includes information such as the [*salt value*](security.s_gly#-security-salt-value-gly), the [*initialization vector*](security.i_gly#-security-initialization-vector-gly), and the key table. The format of opaque BLOBs is unpublished. Each CSP vendor determines its own BLOB format.

Because a key is exported into an opaque BLOB in CSP-specific format, it can only be imported into the CSP from which it was originally exported.

When two processes are involved, each [*process*](security.p_gly#-security-process-gly) calls [**CryptAcquireContext**](/windows/win32/Wincrypt/nf-wincrypt-cryptacquirecontexta?branch=master) independently. Each process gets a handle to a key container. It is possible for both processes to have handles to the same key container. One process creates the keys and exports them into opaque BLOBs, then passes the BLOBs to the second process. The second process imports the keys from the BLOB into its [*key container*](security.k_gly#-security-key-container-gly).

If a hardware CSP does not support exporting keys, the BLOB might only contain the index of a key register, or something similar. In this case, the rest of the procedure is ignored.

``` syntax
<secure process>
cbBlob = sizeof(rgbBlob);
CryptExportKey(
          hKey, 
          0, 
          OPAQUEKEYBLOB, 
          0, 
          rgbBlob, 
          &cbBlob);
hKey = 0;

<BLOB is transferred to other process>

<user process>
CryptImportKey(
            hProv, 
            pbBlob, 
            cbBlob, 
            0, 
            0, 
            &hKey);
```

 

 



