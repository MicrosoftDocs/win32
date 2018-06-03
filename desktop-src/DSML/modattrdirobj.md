---
title: Modifying Attributes on Directory Objects
description: The following code example replaces the existing description attribute of the DSMLSamples object in the fabrikam.com LDAP directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 53e2136f-8284-429f-a301-240644b592a7
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Modifying Attributes on Directory Objects DSML
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Modifying Attributes on Directory Objects

The following code example replaces the existing description attribute of the `DSMLSamples` object in the fabrikam.com LDAP directory.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
  <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
    <batchRequest>
      <modifyRequest dn="ou=DSMLSamples,dc=fabrikam,dc=com">
        <modification name="description" operation="replace">
          <value>Directory Services Markup Language Sample Organizational Unit</value>
        </modification>
      </modifyRequest>
    </batchRequest>
  </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **modifyRequest** element modifies the description property of the `DSMLSamples` object to have the value "Directory Services Markup Language Sample Organizational Unit".

The following code example replaces the existing binary-valued **someProperties** attribute of the `DSMLSamples` object in the fabrikam.com LDAP directory. It also appends two new string values to the multi-valued **someMultivaluedProperty** attribute.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/" 
             se:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
    <batchRequest xmlns="urn:oasis:names:tc:DSML:2:0:core" 
                  xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <modifyRequest dn="ou=DSMLSamples,dc=fabrikam,dc=com">
        <modification name="someProperty" operation="replace">
          <value xsi:type="xsd:base64Binary">VGVzdA==</value>
        </modification>
        <modification name="someMultivaluedProperty" operation="add">
          <value>45</value>
          <value>78</value>
        </modification>
      </modifyRequest>
    </batchRequest>
  </se:Body>
</se:Envelope>
```



For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




