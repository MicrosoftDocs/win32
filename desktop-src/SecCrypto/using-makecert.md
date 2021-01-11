---
description: Use MakeCert commands to create test certificates using options available with Internet Explorer version 4.0 or later.
ms.assetid: 5dbcc8d0-ffd1-4418-adf6-a9805280ee6d
title: Using MakeCert
ms.topic: article
ms.date: 05/31/2018
---

# Using MakeCert

The following examples use [MakeCert](makecert.md) commands to create test certificates using options available with Internet Explorer version 4.0 or later.

-   Make a certificate issued by the default test root. Save the certificate to a file.

    **MakeCert** *MyNew.cer*

-   Make a certificate issued by the default test root. Save it to a certificate store.

    **MakeCert -ss** *MyNewStore*

-   Make a certificate issued by the default test root. Create a key container and save the certificate to both a store and a file.

    **MakeCert -sk** *MyNewKey* **-ss** *MyNewStore* *MyNew.cer*

-   Make a certificate issued by the default test root. Create a private key file and save the certificate to both a store and a file.

    **MakeCert -sv** *MyKeyFile* **-ss** *MyNewStore* *MyNew.cer*

-   Make a certificate issued by the default test root. Create a key container, save the certificate to both a store and a file, and make the private key exportable.

    **MakeCert -sk** *MyNewKey* **-ss** *MyNewStore* *MyNew.cer* **-pe**

-   Make a certificate by using the default test root. Save the certificate to a store. Then make another certificate issued by the newly created certificate. Save the second certificate to another store.

    **MakeCert -sk** *MyNewKey* **-ss** *MyNewStore* **MakeCert -is** *MyNewStore* **-ss** *AnotherStore*

-   Make a certificate by using the default test root. Save the certificate to the MY store. Then make another certificate by using the newly created certificate. If there is more than one certificate in the MY store, the certificate must be identified by using its common name.

    **MakeCert -sk** *MyNewKey* **-n "CN=XXZZYY" -ss my MakeCert -is my -in "XXZZYY" -ss** *AnotherStore*

-   Make a certificate by using the default test root. Save the certificate to the MY store and to a file. Then make another certificate by using the newly created *MyNew* certificate. If there is more than one certificate in the MY store, uniquely identify the first certificate by using the certificate file name.

    **MakeCert -sk** *MyNewKey* **-n "CN=XXZZYY" -ss my** *MyNew.cer* **MakeCert -is my -ic** *MyNew.cer* **-ss** *AnotherStore*

 

 



