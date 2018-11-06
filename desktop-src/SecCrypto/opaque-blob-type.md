---
Description: Opaque BLOBs, also known as OPAQUEKEYBLOBs, are used to store session keys in a vendor-specific format, such as Schannel.
ms.assetid: a0756c03-0c27-41ff-9b74-8af462e09675
title: Opaque BLOB Type
ms.topic: article
ms.date: 05/31/2018
---

# Opaque BLOB Type

[*Opaque BLOBs*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx), also known as OPAQUEKEYBLOBs, are used to store [*session keys*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) in a vendor-specific format, such as [*Schannel*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). They contain the base key material and all current [*state*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) information. This includes information such as the [*salt value*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx), the [*initialization vector*](https://msdn.microsoft.com/en-us/library/ms721588(v=VS.85).aspx), and the key table. The format of opaque BLOBs is unpublished. Each CSP vendor determines its own BLOB format.

Because a key is exported into an opaque BLOB in CSP-specific format, it can only be imported into the CSP from which it was originally exported.

When two processes are involved, each [*process*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) calls [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) independently. Each process gets a handle to a key container. It is possible for both processes to have handles to the same key container. One process creates the keys and exports them into opaque BLOBs, then passes the BLOBs to the second process. The second process imports the keys from the BLOB into its [*key container*](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx).

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

 

 



