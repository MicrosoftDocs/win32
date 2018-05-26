---
Description: The image integrity functions manage the set of certificates in an image file.
ms.assetid: db77b8af-3c36-4e01-88e0-4c44ef8504ff
title: Image Integrity Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Image Integrity Functions

The image integrity functions manage the set of certificates in an image file. Routines are provided to add, remove, and query certificates. There is also a function available for obtaining the byte stream of an image file required to calculate a message digest of the image file. This is needed to create signature certificates.

Every certificate in a file has an index which can change as certificates are removed. New certificates will always be added "at the end" of the list of existing certificates. That is, they will be assigned indices that are greater than any index currently in use. In general, an application should not assume that a given certificate has the same index it had the last time it was referenced.

-   [**DigestFunction**](/windows/win32/Imagehlp/nc-imagehlp-digest_function?branch=master)
-   [**ImageAddCertificate**](/windows/win32/Imagehlp/nf-imagehlp-imageaddcertificate?branch=master)
-   [**ImageEnumerateCertificates**](/windows/win32/Imagehlp/nf-imagehlp-imageenumeratecertificates?branch=master)
-   [**ImageGetCertificateData**](/windows/win32/Imagehlp/nf-imagehlp-imagegetcertificatedata?branch=master)
-   [**ImageGetCertificateHeader**](/windows/win32/Imagehlp/nf-imagehlp-imagegetcertificateheader?branch=master)
-   [**ImageGetDigestStream**](/windows/win32/Imagehlp/nf-imagehlp-imagegetdigeststream?branch=master)
-   [**ImageRemoveCertificate**](/windows/win32/Imagehlp/nf-imagehlp-imageremovecertificate?branch=master)

 

 



