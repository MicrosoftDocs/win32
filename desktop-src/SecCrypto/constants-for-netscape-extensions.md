---
description: Used with encode and decode operations.
ms.assetid: 713c95ae-e5d0-416c-ba0c-4b5399aa8a33
title: Constants for Netscape Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Constants for Netscape Extensions

The following Netscape extensions are used with encode and decode operations. The Netscape predefined constants and object identifier strings are not be used directly with the encoding or decoding functions, [**CryptEncodeObject**](/windows/win32/api/Wincrypt/nf-wincrypt-cryptencodeobject), [**CryptEncodeObjectEx**](/windows/win32/api/Wincrypt/nf-wincrypt-cryptencodeobjectex), [**CryptSignAndEncodeCertificate**](/windows/win32/api/Wincrypt/nf-wincrypt-cryptsignandencodecertificate), [**CryptDecodeObject**](/windows/win32/api/Wincrypt/nf-wincrypt-cryptdecodeobject), or [**CryptDecodeObjectEx**](/windows/win32/api/Wincrypt/nf-wincrypt-cryptdecodeobjectex). Instead, these extensions require the use of the *lpszStructType* shown.

For additional details that apply to some Netscape extensions, see the remarks following the table.



| Netscape certificate extension object identifiers                      | *lpszStructType*                                           | Corresponding *pvStructInfo*                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| szOID\_NETSCAPE\_BASE\_URL"2.16.840.1.113730.1.2"<br/>           | X509\_ANY\_STRING or X509\_UNICODE\_ANY\_STRING<br/> | [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value). The **dwValueType** member is set to CERT\_RDN\_IA5\_STRING. The **Value** member's **pbData** member points to an IA5\_STRING added to the beginning of all relative URL addresses in a certificate. This extension can be considered an optimization to reduce the size of the URL extensions.                                                                                                       |
| szOID\_NETSCAPE\_CA\_POLICY\_URL"2.16.840.1.113730.1.8"<br/>     | X509\_ANY\_STRING or X509\_UNICODE\_ANY\_STRING<br/> | [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value). The **dwValueType** member is set to CERT\_RDN\_IA5\_STRING. The **Value** member's **pbData** member points to an IA5\_STRING, the relative or absolute URL of the webpage describing the policies under which the certificate was issued.                                                                                                                                                            |
| szOID\_NETSCAPE\_CA\_REVOCATION\_URL"2.16.840.1.113730.1.4"<br/> | X509\_ANY\_STRING or X509\_UNICODE\_ANY\_STRING<br/> | [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value). The **dwValueType** member is set to CERT\_RDN\_IA5\_STRING. The **Value** member's **pbData** member points to an IA5\_STRING that is the relative or absolute URL used to check the revocation status of certificates signed by the [*certification authority*](../secgloss/c-gly.md) that the current certificate belongs to. |
| szOID\_NETSCAPE\_CERT\_RENEWAL\_URL"2.16.840.1.113730.1.7"<br/>  | X509\_ANY\_STRING or X509\_UNICODE\_ANY\_STRING<br/> | [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value). The **dwValueType** member is set to CERT\_RDN\_IA5\_STRING. The **Value** member's **pbData** member points to an IA5\_STRING that is the relative or absolute URL of a certificate renewal form.                                                                                                                                                                                                     |
| szOID\_NETSCAPE\_CERT\_SEQUENCE"2.16.840.1.113730.2.5"<br/>      | PKCS\_CONTENT\_INFO\_SEQUENCE\_OF\_ANY                     | [**CRYPT\_CONTENT\_INFO\_SEQUENCE\_OF\_ANY**](/windows/win32/api/Wincrypt/ns-wincrypt-crypt_content_info_sequence_of_any)                                                                                                                                                                                                                                                                                                                                                                |
| szOID\_NETSCAPE\_CERT\_TYPE"2.16.840.1.113730.1.1"<br/>          | X509\_BITS                                                 | [**CRYPT\_BIT\_BLOB**](/windows/win32/api/Wincrypt/ns-wincrypt-crypt_bit_blob)                                                                                                                                                                                                                                                                                                                                                                                                           |
| szOID\_NETSCAPE\_COMMENT"2.16.840.1.113730.1.13"<br/>            | X509\_ANY\_STRING or X509\_UNICODE\_ANY\_STRING<br/> | [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value). The **dwValueType** member is set to CERT\_RDN\_IA5\_STRING. The **Value** member's **pbData** member points to an IA5\_STRING that is a comment to be display when the certificate is viewed.                                                                                                                                                                                                         |
| szOID\_NETSCAPE\_REVOCATION\_URL"2.16.840.1.113730.1.3"<br/>     | X509\_ANY\_STRING or X509\_UNICODE\_ANY\_STRING<br/> | [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value). The **dwValueType** member is set to CERT\_RDN\_IA5\_STRING. The **Value** member's **pbData** member points to an IA5\_STRING that is a relative or absolute URL used to check the revocation status of the certificate.                                                                                                                                                                              |
| szOID\_NETSCAPE\_SSL\_SERVER\_NAME"2.16.840.1.113730.1.12"<br/>  | X509\_ANY\_STRING or X509\_UNICODE\_ANY\_STRING<br/> | [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value). The **dwValueType** member is set to CERT\_RDN\_IA5\_STRING. The **Value** member's **pbData** member points to an IA5\_STRING that is a shell expression used to match the host name off the SSL server using this certificate.                                                                                                                                                                       |



 

For all encoding functions that use either the X509\_ANY\_STRING or the X5O9\_UNICODE\_ANY\_STRING **lpszStructType**, X509\_ANY\_STRING is used if the string format in the **Value** member's **pbData** member is [*ASCII*](../secgloss/a-gly.md), and X509\_UNICODE\_ANY\_STRING is used if the string format is UNICODE. In the Unicode case, the string must be converted to an IA5\_STRING before encoding by setting the **dwValueType** member of the [**CERT\_NAME\_VALUE**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_name_value) structure to CERT\_RDN\_IA5\_STRING.

For decoding functions, the user selects the format of the output string. Use X509\_ANY\_STRING if the desired string format is ASCII, and X509\_UNICODE\_ANY\_STRING if the desired string format is Unicode.

For the szOID\_NETSCAPE\_CERT\_RENEWAL\_URL extension, the data structure contains a relative or absolute URL that points to a certificate renewal form. The renewal form will be accessed with an HTTP GET method using a URL that is the concatenation of the renewal-URL and certificate-serial-number. The certificate-serial-number is encoded as a string of ASCII hexadecimal digits. For example, if the netscape-base-url is https://*certification authority URL*/, the netscape-cert-renewal-url is cgi-bin/check-renew.cgi?, and the certificate serial number is 173420, the resulting URL would be: https://*certification authority URL*/cgi-bin/check-renew.cgi?02a56c. The document returned should be an HTML form that will allow the user to request a renewal of their certificate.

For the szOID\_NETSCAPE\_CERT\_SEQUENCE extension using X509\_ASN\_ENCODING, the certificate is encoded as a PKCS\_CONTENT\_INFO structure wrapping a sequence of ANY. The value of the **contentType** member is **pszObjId**, while the content field is the following structure:

SequenceOfAny ::= SEQUENCE OF ANY

The [**CRYPT\_DER\_BLOB**](/previous-versions/windows/desktop/legacy/aa381414(v=vs.85))s in the [**CRYPT\_CONTENT\_INFO\_SEQUENCE\_OF\_ANY**](/windows/win32/api/Wincrypt/ns-wincrypt-crypt_content_info_sequence_of_any)'s **rgValue** member point to encoded X509 certificates.

For szOID\_NETSCAPE\_CERT\_TYPE extensions, the following bits are defined.



| Bit value | Corresponding type                      |
|-----------|-----------------------------------------|
| 0x80      | NETSCAPE\_SSL\_CLIENT\_AUTH\_CERT\_TYPE |
| 0x40      | NETSCAPE\_SSL\_SERVER\_AUTH\_CERT\_TYPE |
| 0x04      | NETSCAPE\_SSL\_CA\_CERT\_TYPE           |



 

For the szOID\_NETSCAPE\_REVOCATION\_URL extensions, a relative or absolute URL can be used to check the revocation status of a certificate. The revocation check will be performed as an HTTP GET method using a URL that is the concatenation of revocation-URL and certificate-serial-number. The certificate-serial-number is encoded as a string of ASCII hexadecimal digits. For example, if the netscape-base-url is https:\//www.certs-r-us.com/, the netscape-revocation-url is cgi-bin/check-rev.cgi?, and the certificate serial number is 173420, the resulting URL would be: https:\//www.certs-r-us.com/cgi-bin/check-rev.cgi?02a56c.

The server should return a document with a Content-Type of application/x-netscape-revocation. The document should contain a single ASCII digit, "1" if the certificate is not currently valid, and "0" if it is currently valid.

Note that for all of the URLs that include the certificate serial number, the serial number will be encoded as a string that consists of an even number of hexadecimal digits. If the number of significant digits is odd, the string will have a single leading zero to ensure an even number of digits is generated.

 

 
