---
title: Deleting an Entire Directory Subtree
description: The following code example deletes the DSMLTesting container object and all related subobjects from the fabrikam.com LDAP directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'e37a302a-8bc7-403a-85d5-81d6968b7ebb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Deleting an Entire Directory Subtree DSML"]
---

# Deleting an Entire Directory Subtree

The following code example deletes the `DSMLTesting` container object and all related subobjects from the fabrikam.com LDAP directory.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest>
         <delRequest dn="ou=DSMLTesting,dc=fabrikam,dc=com">
            <control type="1.2.840.113556.1.4.805" criticality="false"/>
         </delRequest>
      </batchRequest>
   </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements wrap the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **delRequest** element uses the LDAP tree delete control OID ("1.2.840.113556.1.4.805") to delete the `DSMLTesting` container object and its related subobjects from the directory.

For more information about how to send and receive the SOAP messages, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




