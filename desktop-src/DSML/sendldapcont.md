---
title: Sending LDAP Controls
description: The following code example retrieves the first 750 objects in the fabrikam.com LDAP directory, sorted by the name attribute value of the object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ffa3b9cf-cd1b-48f5-befd-db9bff228bc0
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Sending LDAP Controls DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Sending LDAP Controls

The following code example retrieves the first 750 objects in the fabrikam.com LDAP directory, sorted by the name attribute value of the object.


```soap
<!-- SORT by Name  -->
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
         <searchRequest dn="dc=fabrikam,dc=com" scope="wholeSubtree" derefAliases="neverDerefAliases" sizeLimit="750">
            <control type="1.2.840.113556.1.4.473" criticality="true">
               <controlValue xsi:type="xsd:base64Binary">MIQAAAAPMIQAAAAJBARuYW1lAQEA</controlValue>
            </control>
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



The **se:Envelope** and **se:Body** SOAP elements wrap the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **searchRequest** element retrieves the directory objects. The **control** element sends the extended LDAP control to sort the results by object name. The **attribute** elements specify which directory attribute values to return with each associated directory object.

The LDAP control OID ("1.2.840.113556.1.4.473") is the server sort control. For more information about the sort control, see [LDAP\_SERVER\_SORT\_OID](https://msdn.microsoft.com/library/aa366990).

The **controlValue** type is encoded by taking the base-64 encoding of the LDAP BER-encoded value of the control.

For more information about how to send and receive SOAP messages, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




