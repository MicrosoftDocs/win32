---
title: Adding a Directory Object
description: The following code example adds an organizationalUnit object named DSMLSamples to the fabrikam.com LDAP directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '1ad20551-5653-4157-bc6f-8cec609f8434'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Adding a Directory Object DSML"]
---

# Adding a Directory Object

The following code example adds an **organizationalUnit** object named `DSMLSamples` to the fabrikam.com LDAP directory.


```soap
<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
    <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
        <batchRequest xmlns="urn:oasis:names:tc:DSML:2:0:core"
                        xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <addRequest dn="ou=DSMLSamples,dc=fabrikam,dc=com">
                <attr name="objectClass">
                    <value>organizationalUnit</value>
                </attr>
            </addRequest>
        </batchRequest>
    </se:Body>
</se:Envelope>
```



The **se:Envelope** and **se:Body** SOAP elements enclose the DSML payload. The first element of the DSML payload, **batchRequest**, is the mandatory top-level element for all DSML V2 requests. The **addRequest** element creates the new object with a distinguished name of "ou=DSMLSamples,dc=fabrikam,dc=com", with an attribute named **objectClass** that is set to a value of `organizationalUnit`.

For more information, see [Transmitting and Receiving SOAP-DSML Messages](tranrecsoapdsmlmess.md).

 

 




