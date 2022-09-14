---
description: You can use the IX500DistinguishedName interface to create a subject name from a distinguished name string.
ms.assetid: 78fbf15a-678f-4d87-a309-e70374e3ecee
title: Creating a Subject Name
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Subject Name

You can use the [**IX500DistinguishedName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix500distinguishedname) interface to create a subject name from a distinguished name string. The string consists of concatenated relative distinguished names (RDNs). The following RDN keys are supported by the Certificate Enrollment API.

| Key                               | OID                                             | Description                                                                                        |
|-----------------------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------|
| C<br/>                      | XCN\_OID\_COUNTRY\_NAME<br/>              | Contains a two-letter ISO 3166 country or region code.<br/>                                  |
| CN<br/>                     | XCN\_OID\_COMMON\_NAME<br/>               | Contains a common name.<br/>                                                                 |
| E<br/> EMAIL<br/>     | XCN\_OID\_RSA\_emailAddr<br/>             | Contains an email address.<br/>                                                              |
| DC<br/>                     | XCN\_OID\_DOMAIN\_COMPONENT<br/>          | Contains one part of a Domain Name System (DNS) name.<br/>                                   |
| G<br/> GivenName<br/> | XCN\_OID\_GIVEN\_NAME<br/>                | Contains the part of a person's name that is not a surname.<br/>                             |
| I<br/>                      | XCN\_OID\_INITIALS<br/>                   | Contains a person's initials.<br/>                                                           |
| L<br/>                      | XCN\_OID\_LOCALITY\_NAME<br/>             | Contains the locality name that identifies a city, country, or other geographic region.<br/> |
| O<br/>                      | XCN\_OID\_ORGANIZATION\_NAME<br/>         | Contains the name of an organization.<br/>                                                   |
| OU<br/>                     | XCN\_OID\_ORGANIZATIONAL\_UNIT\_NAME<br/> | Contains the name of a unit subdivision within an organization.<br/>                         |
| S<br/> ST<br/>        | XCN\_OID\_STATE\_OR\_PROVINCE\_NAME<br/>  | Contains the full name of a state or province.<br/>                                          |
| STREET<br/>                 | XCN\_OID\_STREET\_ADDRESS<br/>            | Contains the physical address.<br/>                                                          |
| SN<br/>                     | XCN\_OID\_SUR\_NAME<br/>                  | Contains the family name of a person.<br/>                                                   |
| T<br/> TITLE<br/>     | XCN\_OID\_TITLE<br/>                      | Contains the title of a person in the organization.<br/>                                     |



 

When you initialize an [**IX500DistinguishedName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix500distinguishedname) object, you can identify the format of the distinguished name by specifying a value from the [**X500NameFlags**](/windows/desktop/api/CertEnroll/ne-certenroll-x500nameflags) enumeration type. For example, assume that the subject distinguished name consists of the following RDNs:<dl> CN=Administrator  
CN=Users  
DC=jdomcsc  
DC=nttest  
DC=microsoft  
DC=com  
</dl>

If you concatenate these RDNs into the following comma-delimited distinguished name string, you can specify the **XCN\_CERT\_NAME\_STR\_COMMA\_FLAG** value when initializing an [**IX500DistinguishedName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix500distinguishedname) object.

``` syntax
CN=Administrator,CN=Users,DC=jdomcsc,DC=nttest,DC=microsoft,DC=com
```

## Related topics

<dl> <dt>

[Encoding a Subject Name](encoding-a-subject-name.md)
</dt> <dt>

[Subject Names](subject-names.md)
</dt> </dl>

 

 




