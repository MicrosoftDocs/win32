---
title: Performing Batch Operations
description: The following code example performs multiple directory operations in a single message.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3df9c680-4f61-418a-96c8-ad1ed578a7ff
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Performing Batch Operations DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Performing Batch Operations

The following code example performs multiple directory operations in a single message.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
   <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
      <batchRequest xmlns="urn:oasis:names:tc:DSML:2:0:core" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
         <addRequest dn="cn=Jeff Smith, ou=DSMLTesting,dc=fabrikam,dc=com">
            <attr name="objectClass"><value>contact</value></attr>
            <attr name="sn"><value>Smith</value></attr>
            <attr name="givenName"><value>Jeff</value></attr>
            <attr name="title"><value>Vice President</value></attr>
            <attr name="telephoneNumber"><value>(206) 999 8888</value></attr>
         </addRequest>
         <addRequest dn="ou=Sales, ou=DSMLTesting,dc=fabrikam,dc=com">
            <attr name="objectClass"><value>organizationalUnit</value></attr>
            <attr name="description"><value>Sales Organization</value></attr>
         </addRequest>
         <addRequest dn="ou=Consulting, ou=DSMLTesting,dc=fabrikam,dc=com">
            <attr name="objectClass"><value>organizationalUnit</value></attr>
            <attr name="description"><value>Consulting and Service Organization</value></attr>
         </addRequest>
         <modifyRequest dn="ou=DSMLTesting,dc=fabrikam,dc=com">
            <modification name="street" operation="replace">
               <value>23315 Main Street</value>
            </modification>
            <modification name="l" operation="replace">
               <value>Seattle</value>
            </modification>
            <modification name="st" operation="replace">
               <value>WA</value>
            </modification>
            <modification name="postalCode" operation="replace">
               <value>98021</value>
            </modification>
            <modification name="c" operation="replace">
               <value>US</value>
            </modification>
         </modifyRequest>
      </batchRequest>
   </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The remaining elements show how multiple directory operations can be requested in a single DSML message. The three **addRequest** elements and the single **modifyRequest** element show how the individual operations are performed.

If the DSML payload contains more than 1,000 request operations (for example, **addRequest**, **modifyRequest**, and **searchRequest**), DSML Services for Windows will return a SOAP response that contains a client-fault error message without processing any of the request operations.

For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




