---
title: Deleting a Directory Object
description: The following code example deletes the object Jeff Smith from the fabrikam.com LDAP directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 080e6eae-99f5-4ff7-b887-c32877a8e34d
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Deleting a Directory Object DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Deleting a Directory Object

The following code example deletes the object `Jeff Smith` from the fabrikam.com LDAP directory.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest>
         <delRequest dn="cn=Jeff Smith,ou=DSMLTesting,dc=fabrikam,dc=com"/>
      </batchRequest>
   </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **delRequest** element deletes the object `Jeff Smith` from the `DSMLTesting` organizational unit in the directory.

For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




