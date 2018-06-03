---
Description: Opaque BLOBs, also known as OPAQUEKEYBLOBs, are used to store session keys in a vendor-specific format, such as Schannel.
ms.assetid: a0756c03-0c27-41ff-9b74-8af462e09675
title: Opaque BLOB Type
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Opaque BLOB Type

[*Opaque BLOBs*](https://www.bing.com/search?q=*Opaque BLOBs*), also known as OPAQUEKEYBLOBs, are used to store [*session keys*](https://www.bing.com/search?q=*session keys*) in a vendor-specific format, such as [*Schannel*](https://www.bing.com/search?q=*Schannel*). They contain the base key material and all current [*state*](https://www.bing.com/search?q=*state*) information. This includes information such as the [*salt value*](https://www.bing.com/search?q=*salt value*), the [*initialization vector*](https://www.bing.com/search?q=*initialization vector*), and the key table. The format of opaque BLOBs is unpublished. Each CSP vendor determines its own BLOB format.

Because a key is exported into an opaque BLOB in CSP-specific format, it can only be imported into the CSP from which it was originally exported.

When two processes are involved, each [*process*](https://www.bing.com/search?q=*process*) calls [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) independently. Each process gets a handle to a key container. It is possible for both processes to have handles to the same key container. One process creates the keys and exports them into opaque BLOBs, then passes the BLOBs to the second process. The second process imports the keys from the BLOB into its [*key container*](https://www.bing.com/search?q=*key container*).

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

 

 



