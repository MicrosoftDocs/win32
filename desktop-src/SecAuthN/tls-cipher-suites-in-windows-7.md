---
description: Learn about TLS cipher suites in Windows 7. Cipher suites can only be negotiated for TLS versions which support them.
ms.assetid: 283CB634-25EA-47F5-A2E3-0913F7D3D9DC
title: TLS Cipher Suites in Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# TLS Cipher Suites in Windows 7

Cipher suites can only be negotiated for TLS versions which support them. The highest supported TLS version is always preferred in the TLS handshake. For example, SSL\_CK\_RC4\_128\_WITH\_MD5 can only be used when both the client and server do not support TLS 1.2, 1.1 & 1.0 or SSL 3.0 since it is only supported with SSL 2.0.

Availability of cipher suites should be controlled in one of two ways:

-   Default priority order is overridden when a priority list is configured. Cipher suites not in the priority list will not be used.
-   Allowed when application passes SCH\_USE\_STRONG\_CRYPTO: The Microsoft Schannel provider will filter out known weak cipher suites when the application uses the SCH\_USE\_STRONG\_CRYPTO flag. In Windows 7, RC4 cipher suites are filtered out.

> [!IMPORTANT]
> HTTP/2 web services fail with non-HTTP/2-compatible cipher suites. To ensure your web services function with HTTP/2 clients and browsers, see [How to deploy custom cipher suite ordering](https://support.microsoft.com/help/4032720/how-to-deploy-custom-cipher-suite-ordering-in-windows-server-2016).

 

FIPS-compliance has become more complex with the addition of elliptic curves making the FIPS mode enabled column in previous versions of this table misleading. For example, a cipher suite such as TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 is only FIPS-compliant when using NIST elliptic curves. To find out which combinations of elliptic curves and cipher suites will be enabled in FIPS mode, see section 3.3.1 of [Guidelines for the Selection, Configuration, and Use of TLS Implementations]( https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r1.pdf).

Windows 7, Windows 8, and Windows Server 2012 are updated by the Windows Update by the 3042058 update which changes the priority order. See [Microsoft Security Advisory 3042058](/security-updates/SecurityAdvisories/2015/3042058) for more information. The following cipher suites are enabled and in this priority order by default by the Microsoft Schannel Provider:



| Cipher suite string                                                                                            | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384\_P256<br/>                                                  | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384\_P384<br/>                                                  | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256\_P256<br/>                                                  | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256\_P384<br/>                                                  | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P256<br/>                                                     | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P384<br/>                                                     | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P256<br/>                                                     | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P384<br/>                                                     | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br/>                                                          | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_DHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256<br/>                                                          | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA<br/>                                                             | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_RSA\_WITH\_AES\_128\_CBC\_SHA<br/>                                                             | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br/>                                                               | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256<br/>                                                               | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256<br/>                                                               | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br/>                                                               | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA<br/>                                                                  | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA<br/>                                                                  | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384\_P384<br/>                                                | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256\_P256<br/>                                                | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256\_P384<br/>                                                | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384\_P384<br/>                                                | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256\_P256<br/>                                                | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256\_P384<br/>                                                | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P256<br/>                                                   | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P384<br/>                                                   | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P256<br/>                                                   | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P384<br/>                                                   | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA256<br/>                                                          | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA256<br/>                                                          | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA<br/>                                                             | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA<br/>                                                             | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA<br/>                                                                 | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA<br/>                                                            | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_RC4\_128\_SHA<br/>                                                                       | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_RC4\_128\_MD5<br/>                                                                       | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_NULL\_SHA256 <br/> Only used when application explicitly requests.<br/>            | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_NULL\_SHA <br/> Only used when application explicitly requests.<br/>               | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| SSL\_CK\_RC4\_128\_WITH\_MD5 <br/> Only used when application explicitly requests.<br/>            | No<br/>                       | SSL 2.0<br/>                            |
| SSL\_CK\_DES\_192\_EDE3\_CBC\_WITH\_MD5 <br/> Only used when application explicitly requests.<br/> | Yes<br/>                      | SSL 2.0<br/>                            |



 

The following cipher suites are supported by the Microsoft Schannel Provider, but not enabled by default:



| Cipher suite string                                             | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions                     |
|-----------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384\_P521<br/>   | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256\_P521<br/>   | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P521<br/>      | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P521<br/>      | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384\_P521<br/> | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256\_P521<br/> | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384\_P521<br/> | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256\_P521<br/> | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P521<br/>    | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P521<br/>    | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_DES\_CBC\_SHA<br/>                        | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_EXPORT1024\_WITH\_RC4\_56\_SHA<br/>             | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_EXPORT1024\_WITH\_DES\_CBC\_SHA<br/>            | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_EXPORT\_WITH\_RC4\_40\_MD5<br/>                 | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_NULL\_MD5<br/>                            | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_DHE\_DSS\_WITH\_DES\_CBC\_SHA<br/>                   | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_DHE\_DSS\_EXPORT1024\_WITH\_DES\_CBC\_SHA<br/>       | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| SSL\_CK\_DES\_64\_CBC\_WITH\_MD5<br/>                     | Yes<br/>                      | SSL 2.0<br/>                            |
| SSL\_CK\_RC4\_128\_EXPORT40\_WITH\_MD5<br/>               | No<br/>                       | SSL 2.0<br/>                            |



 

To add cipher suites, use the group policy setting SSL Cipher Suite Order under Computer Configuration > Administrative Templates > Network > SSL Configuration Settings to configure a priority list for all cipher suites you want enabled.

 

 
