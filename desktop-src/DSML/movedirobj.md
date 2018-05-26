---
title: Moving a Directory Object
description: The following code example moves the Consulting organizational unit down one level to the Sales organizational unit in the fabrikam.com LDAP directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 892d6c63-caec-41d3-9cd9-22afed18131d
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Moving a Directory Object DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Moving a Directory Object

The following code example moves the `Consulting` organizational unit down one level to the `Sales` organizational unit in the fabrikam.com LDAP directory.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest xmlns="urn:oasis:names:tc:DSML:2:0:core" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
         <modDNRequest dn="ou=Consulting,ou=DSMLTesting,dc=fabrikam,dc=com" 
                       newrdn="ou=Consulting" newSuperior="ou=Sales,ou=DSMLTesting,dc=fabrikam,dc=com"/>
      </batchRequest>
   </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **modDNRequest** element moves the existing Consulting organizational unit below the `Sales` organizational unit in the directory.

For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




