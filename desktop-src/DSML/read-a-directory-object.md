---
title: Reading a Directory Object
description: Reading a Directory Object
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5bc0f102-f827-405b-a931-e30f8337e4ab
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Reading a Directory Object DSML
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reading a Directory Object

The following code example retrieves the `Jeff Smith` user object from the fabrikam.com LDAP directory.

``` syntax
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest>
         <searchRequest dn="cn=Jeff Smith,ou=Sales,dc=fabrikam,dc=com" scope="baseObject" derefAliases="neverDerefAliases">
            <filter>
               <present name="objectclass"/>
            </filter>
         </searchRequest>
      </batchRequest>
   </se:Body>
</se:Envelope>
```

The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **searchRequest** element requests the `Jeff Smith` user object from the fabrikam.com directory.

For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




