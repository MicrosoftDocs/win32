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

[*Opaque BLOBs*](https://msdn.microsoft.com/e6be8932-015e-4058-b249-1671b3fea521), also known as OPAQUEKEYBLOBs, are used to store [*session keys*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) in a vendor-specific format, such as [*Schannel*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50). They contain the base key material and all current [*state*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) information. This includes information such as the [*salt value*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50), the [*initialization vector*](https://msdn.microsoft.com/af511aed-88f5-4b12-ad44-317925297f70), and the key table. The format of opaque BLOBs is unpublished. Each CSP vendor determines its own BLOB format.

Because a key is exported into an opaque BLOB in CSP-specific format, it can only be imported into the CSP from which it was originally exported.

When two processes are involved, each [*process*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) calls [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) independently. Each process gets a handle to a key container. It is possible for both processes to have handles to the same key container. One process creates the keys and exports them into opaque BLOBs, then passes the BLOBs to the second process. The second process imports the keys from the BLOB into its [*key container*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33).

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

 

 



