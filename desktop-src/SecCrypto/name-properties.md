---
description: Name properties are properties of certificates and certificate requests that represent data about the subject, that is, the owner of the certificate or the individual for whom a certificate is requested.
ms.assetid: c32756f7-4431-410e-ab3a-c7b748a43829
title: Name Properties
ms.topic: article
ms.date: 05/31/2018
---

# Name Properties

Name properties are properties of certificates and certificate requests that represent data about the subject, that is, the owner of the certificate or the individual for whom a certificate is requested. Each name property is identified by a property name. These names are not localizable; however, name properties typically correspond to a Certificate Services database column, and you can use the Certification Authority MMC snap-in, the command line tool 'certutil -schema', or the [**IEnumCERTVIEWCOLUMN::GetDisplayName**](/windows/desktop/api/Certview/nf-certview-ienumcertviewcolumn-getdisplayname) method to display localized versions of the database column names.

The property name (but not the aliases) may have "Subject." as an optional prefix. For example, to refer to the subject's common name, you can use either "CommonName" or "Subject.CommonName".

In addition to its name, each property has some number of aliases that Certificate Services recognizes as alternate names for the property. Note that [*object identifiers*](../secgloss/o-gly.md) (OIDs) are acceptable aliases, as are the **szOID\_\*** constants. These constants are definitions (in Wincrypt.h) that represent the OIDs. For example, **szOID\_COMMON\_NAME** is defined as "2.5.4.3". Consequently, you can use the **szOID\_\*** constants as aliases in place of the OIDs they represent.



| Property name                 | Aliases                                                                                                                                                        | Data type                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "Subject.CommonName"          | "CommonName" "CN"<br/> "2.5.4.3"<br/> **szOID\_COMMON\_NAME**<br/>                                                                           | **String** (max. 64 chars)  | For user certificates, the person's full name. For computer certificates, the fully qualified *HostName***/***Path* used in Domain Name System (DNS) lookups (for example, *HostName***.***Example***.com**).<br/>                                                                                                                                                                                                                                                                        |
| "Subject.Country"             | "Country" "C"<br/> "2.5.4.6"<br/> **szOID\_COUNTRY\_NAME**<br/>                                                                              | **String** (max 2 chars)    | The subject's country or region. This is an [*X.500*](../secgloss/x-gly.md) two-character country/region code (for example US for United States or CA for Canada).<br/> Many of these two-character codes are defined in the ISO 3166 standard. Additionally, the current locale's code is available through a call to the Windows function [**GetLocaleInfo**](/windows/win32/api/winnls/nf-winnls-getlocaleinfoa) (by specifying an *LCType* of LOCALE\_SISO3166CTRYNAME).<br/> |
| "Subject.DeviceSerialNumber"  | "DeviceSerialNumber" "2.5.4.5"<br/> **szOID\_DEVICE\_SERIAL\_NUMBER**<br/>                                                                         | **String** (max 1024 chars) | Device serial number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| "Subject.DomainComponent"     | "DomainComponent" "DC"<br/> "0.9.2342.19200300.100.1.25"<br/> **szOID\_DOMAIN\_COMPONENT**<br/>                                              | **String** (max 128 chars)  | Component of a Domain Name System (DNS) name.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| "Subject.EMail"               | "EMail" "E"<br/> "1.2.840.113549.1.9.1"<br/> **szOID\_RSA\_emailAddr**<br/>                                                                  | **String** (max 128 chars)  | Email address (for example, "someone@example.com").                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "Subject.GivenName"           | "GivenName" "G"<br/> "2.5.4.42"<br/> **szOID\_GIVEN\_NAME**<br/>                                                                             | **String** (max 16 chars)   | First name of the subject.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| "Subject.Initials"            | "Initials" "I"<br/> "2.5.4.43"<br/> **szOID\_INITIALS**<br/>                                                                                 | **String** (max 5 chars)    | Initials of the subject (optional).                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "Subject.Locality"            | "Locality" "L"<br/> "2.5.4.7"<br/> **szOID\_LOCALITY\_NAME**<br/>                                                                            | **String** (max 128 chars)  | Name of the subject's city.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| "Subject.Organization"        | "Organization" "Org"<br/> "O"<br/> "2.5.4.10"<br/> **szOID\_ORGANIZATION\_NAME**<br/>                                                  | **String** (max 64 chars)   | Legal name of the subject's organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| "Subject.OrgUnit"             | "OrgUnit" "OrganizationUnit"<br/> "OrganizationalUnit"<br/> "OU"<br/> "2.5.4.11"<br/> **szOID\_ORGANIZATIONAL\_UNIT\_NAME**<br/> | **String** (max 64 chars)   | Name of the subject's sub-organization or department.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| "Subject.State"               | "State" "ST"<br/> "S"<br/> "2.5.4.8"<br/> **szOID\_STATE\_OR\_PROVINCE\_NAME**<br/>                                                    | **String** (max 128 chars)  | Full name of the subject's state or province (for example, California).                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "Subject.StreetAddress"       | "StreetAddress" "Street"<br/> "2.5.4.9"<br/> **szOID\_STREET\_ADDRESS**<br/>                                                                 | **String** (max 30 chars)   | Subject's street address or PO Box.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "Subject.SurName"             | "SurName" "SN"<br/> "2.5.4.4"<br/> **szOID\_SUR\_NAME**<br/>                                                                                 | **String** (max 40 chars)   | Last name of the subject.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| "Subject.Title"               | "Title" "T"<br/> "2.5.4.12"<br/> **szOID\_TITLE**<br/>                                                                                       | **String** (max 64 chars)   | Title of individual who requested the certificate (optional).                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| "Subject.UnstructuredAddress" | "UnstructuredAddress" "1.2.840.113549.1.9.8"<br/> **szOID\_RSA\_unstructAddr**<br/>                                                                | **String** (max 1024 chars) | Unstructured address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| "Subject.UnstructuredName"    | "UnstructuredName" "1.2.840.113549.1.9.2"<br/> **szOID\_RSA\_unstructName**<br/>                                                                   | **String** (max 1024 chars) | Unstructured name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

The following properties are related to the subject, although they are not name properties. The policy module cannot set these properties directly.



| Property                    | Data type                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "Request.DistinguishedName" | **String** (max 8192 chars) | The [*relative distinguished name*](../secgloss/r-gly.md) for the request, a textual representation of the subject in the request. This representation consists of name properties, for example, "CN=MyName, OU=MyOrgUnit, C=US". The Certificate Services application sets this property before calling the policy module, by calling [**CertNameToStr**](/windows/desktop/api/Wincrypt/nf-wincrypt-certnametostra) using the RawRequest's Subject. |
| "Request.RawName"           | **Binary** (max 4096 bytes) | [*Abstract Syntax Notation One*](../secgloss/a-gly.md) (ASN.1) binary subject [*BLOB*](../secgloss/b-gly.md) extracted from the request. The Certificate Services application sets this property before calling the policy module; its value is determined by the RawRequest's Subject.                                                                                     |
| "DistinguishedName"         | **String** (max 8192 chars) | The relative distinguished name for the certificate, a textual representation of the subject in the certificate. This representation consists of name properties, for example, "CN=MyName, OU=MyOrgUnit, C=US". The Certificate Services application sets this property after calling the policy module, by calling [**CertNameToStr**](/windows/desktop/api/Wincrypt/nf-wincrypt-certnametostra) using the RawName.                                                                                                               |
| "RawName"                   | **Binary** (max 4096 bytes) | ASN.1 binary subject [*BLOB*](../secgloss/b-gly.md) used to construct the certificate. The Certificate Services application sets this property after calling the policy module; its value is determined by the values of specific name properties (Subject.CommonName and so on) as directed by the SubjectTemplate.                                                                                                                                        |



 

Which [*relative distinguished name*](../secgloss/r-gly.md) components appear in the DistinguishedName property and the order in which they appear are controlled by the "SubjectTemplate" registry value contained in the following registry key:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            CertSvc
               Configuration
                  CaName
```

When Certificate Services parses [*attribute*](../secgloss/a-gly.md) names, it ignores spaces, hyphens (minus signs), and case. For example, "AttributeName1", "Attribute Name1", and "Attribute-name1" are all equivalent. For attribute values, Certificate Services ignores leading and trailing white space.

All of the preceding properties except DistinguishedName, RawName, and Subject.Country, support multiple-valued syntax by using a newline character. The newline separator cannot be disabled or changed.

## Related topics

<dl> <dt>

[Certificate Properties](certificate-properties.md)
</dt> <dt>

[**ICertServerExit::GetCertificateProperty**](/windows/desktop/api/Certif/nf-certif-icertserverexit-getcertificateproperty)
</dt> <dt>

[**ICertServerExit::GetRequestProperty**](/windows/desktop/api/Certif/nf-certif-icertserverexit-getrequestproperty)
</dt> <dt>

[**ICertServerPolicy::GetCertificateProperty**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-getcertificateproperty)
</dt> <dt>

[**ICertServerPolicy::GetRequestProperty**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-getrequestproperty)
</dt> <dt>

[**ICertServerPolicy::SetCertificateProperty**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-setcertificateproperty)
</dt> </dl>

 

 
