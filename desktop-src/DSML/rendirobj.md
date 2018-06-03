---
title: Renaming a Directory Object
description: The following code example renames the DSMLSamples object to DSMLTesting in the fabrikam.com LDAP directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 906d23bf-9bc8-4397-9169-21ff4aa55ee6
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Renaming a Directory Object DSML
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Renaming a Directory Object

The following code example renames the `DSMLSamples` object to `DSMLTesting` in the fabrikam.com LDAP directory.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest xmlns="urn:oasis:names:tc:DSML:2:0:core" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
         <modDNRequest dn="ou=DSMLSamples,dc=fabrikam,dc=com" newrdn="ou=DSMLTesting"/>
      </batchRequest>
   </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **modDNRequest** element renames the `DSMLSamples` object to `DSMLTesting`.

For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




