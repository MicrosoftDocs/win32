---
description: The image integrity functions manage the set of certificates in an image file.
ms.assetid: db77b8af-3c36-4e01-88e0-4c44ef8504ff
title: Image Integrity Functions
ms.topic: article
ms.date: 05/31/2018
---

# Image Integrity Functions

The image integrity functions manage the set of certificates in an image file. Routines are provided to add, remove, and query certificates. There is also a function available for obtaining the byte stream of an image file required to calculate a message digest of the image file. This is needed to create signature certificates.

Every certificate in a file has an index which can change as certificates are removed. New certificates will always be added "at the end" of the list of existing certificates. That is, they will be assigned indices that are greater than any index currently in use. In general, an application should not assume that a given certificate has the same index it had the last time it was referenced.

-   [**DigestFunction**](/windows/desktop/api/Imagehlp/nc-imagehlp-digest_function)
-   [**ImageAddCertificate**](/windows/desktop/api/Imagehlp/nf-imagehlp-imageaddcertificate)
-   [**ImageEnumerateCertificates**](/windows/desktop/api/Imagehlp/nf-imagehlp-imageenumeratecertificates)
-   [**ImageGetCertificateData**](/windows/desktop/api/Imagehlp/nf-imagehlp-imagegetcertificatedata)
-   [**ImageGetCertificateHeader**](/windows/desktop/api/Imagehlp/nf-imagehlp-imagegetcertificateheader)
-   [**ImageGetDigestStream**](/windows/desktop/api/Imagehlp/nf-imagehlp-imagegetdigeststream)
-   [**ImageRemoveCertificate**](/windows/desktop/api/Imagehlp/nf-imagehlp-imageremovecertificate)

 

 



