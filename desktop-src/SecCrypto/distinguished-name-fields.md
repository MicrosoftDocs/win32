---
description: Contains information that should uniquely identify the individual making the request.
ms.assetid: f0cc0e1b-370e-4548-97fe-8f6a4005540b
title: Distinguished Name Fields
ms.topic: article
ms.date: 05/31/2018
---

# Distinguished Name Fields

A [*certificate request*](../secgloss/c-gly.md) contains information that should uniquely identify the individual making the request.

PKCS \#10 format certificate requests that are accepted by Certificate Services contain identification fields that are referred to as Distinguished Name (DN) fields. These fields will contain the information that is input by the user when a certificate request is being created by Key Manager, [Certificate Enrollment Control](certificate-enrollment-control.md), or some other means.

The following are some guidelines for completion of DN fields in a certificate request.



| Field               | Description                                                                                                                                                                                                                                                                                                                                                      |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common Name         | User Certificates: You should enter the person's full name. Machine Certificates: You should enter the fully qualified *HostName***/***Path* used in DNS lookups that the server will be running on (for example, *HostName***.***Example***.com**).<br/>                                                                                                  |
| Organization        | The name you specify for the Organization field should be the legal name for your organization that is registered with the appropriate city, state, or country/region authority. The legal name of the organization must be used in the Organization field.                                                                                                      |
| Organizational Unit | The Organizational Unit field can be used to differentiate between different divisions within an organization, for example "Internet Security Unit" or "Human Resources." This field is also recommended to be used for specifying a DBA (Doing Business As...) value.                                                                                           |
| Locality            | The Locality field denotes the city that the organization resides in. If the organization has local standing only, by virtue of having a business license registered with the City Clerk for the City of Cambridge in the State of Massachusetts, then the Locality field must contain Cambridge.                                                                |
| State or Province   | The State or Province field specifies where the organization is physically located. If your organization is incorporated in Delaware but has a DBA (Doing Business As...) within California, use California. The State or Province field should not be an abbreviated field. For example, "CA" is not a valid state name. "California" is the proper state name. |
| Country/region      | The [*X.500*](../secgloss/x-gly.md) Naming Scheme standard requires a 2-character country/region code. The country/region code for the United States is US; the country/region code for Canada is CA.                                                                                                                          |



 

## Related topics

<dl> <dt>

[Name Properties](name-properties.md)
</dt> </dl>

 

 
