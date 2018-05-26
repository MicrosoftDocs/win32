---
title: Searching a Directory
description: The following code example retrieves the first 500 objects in the fabrikam.com LDAP directory and their associated names, descriptions, and creation date attribute values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8f72b7b5-5d88-4ca4-9980-a81a69d93ffa
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Searching a Directory DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Searching a Directory

The following code example retrieves the first 500 objects in the fabrikam.com LDAP directory and their associated names, descriptions, and creation date attribute values.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest>
         <searchRequest dn="dc=fabrikam,dc=com" scope="wholeSubtree" derefAliases="neverDerefAliases" sizeLimit="500">
            <filter>
               <present name="objectclass"/>
            </filter>
            <attributes>
               <attribute name="name"/>
               <attribute name="description"/>
               <attribute name="whenCreated"/>
            </attributes>
         </searchRequest>
      </batchRequest>
   </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **searchRequest** element retrieves the directory objects and the **attribute** elements specify which directory attribute values to return with each associated directory object.

For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




