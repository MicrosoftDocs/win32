---
description: Learn about TLS cipher suites in Windows Server 2022. Cipher suites can only be negotiated for TLS versions which support them.
title: TLS Cipher Suites in Windows Server 2022.
ms.topic: article
ms.date: 02/16/2021
---

# TLS Cipher Suites in Windows Server 2022

Cipher suites can only be negotiated for TLS versions which support them. The highest supported TLS version is always preferred in the TLS handshake.

Availability of cipher suites should be controlled in one of two ways:

-   Default priority order is overridden when a priority list is configured. Cipher suites not in the priority list will not be used.
-   Allowed when the application passes SCH\_USE\_STRONG\_CRYPTO: The Microsoft Schannel provider will filter out known weak cipher suites when the application uses the SCH\_USE\_STRONG\_CRYPTO flag. RC4, DES, export and null cipher suites are filtered out.

> [!IMPORTANT]
> HTTP/2 web services fail with non-HTTP/2-compatible cipher suites. To ensure your web services function with HTTP/2 clients and browsers, see [How to deploy custom cipher suite ordering](https://support.microsoft.com/help/4032720/how-to-deploy-custom-cipher-suite-ordering-in-windows-server-2016).

 

FIPS-compliance has become more complex with the addition of elliptic curves making the FIPS mode enabled column in previous versions of this table misleading. For example, a cipher suite such as TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 is only FIPS-compliant when using NIST elliptic curves. To find out which combinations of elliptic curves and cipher suites will be enabled in FIPS mode, see section 3.3.1 of [Guidelines for the Selection, Configuration, and Use of TLS Implementations]( https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf).

For Windows Server 2022, the following cipher suites are enabled and in this priority order by default using the Microsoft Schannel Provider:



| Cipher suite string                                                                           | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS\_AES\_256\_GCM\_SHA384<br/>                                                               | Yes<br/>                      | TLS 1.3<br/>                            |
| TLS\_AES\_128\_GCM\_SHA256<br/>                                                               | Yes<br/>                      | TLS 1.3<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384<br/>                                           | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256<br/>                                           | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br/>                                             | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256<br/>                                             | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_DHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br/>                                               | Yes<br/>                       | TLS 1.2<br/>                            |
| TLS\_DHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256<br/>                                               | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384<br/>                                           | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256<br/>                                           | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384<br/>                                             | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br/>                                             | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA<br/>                                              | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA<br/>                                              | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA<br/>                                                | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA<br/>                                                | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br/>                                                    | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256<br/>                                                    | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256<br/>                                                    | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br/>                                                    | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA<br/>                                                       | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA<br/>                                                       | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA<br/>                                                      | No<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_NULL\_SHA256 <br/> Only used when application explicitly requests.<br/>       | No<br/>                       | TLS 1.2<br/>                            |
| TLS\_RSA\_WITH\_NULL\_SHA <br/> Only used when application explicitly requests.<br/>          | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |



 

The following cipher suites are supported by the Microsoft Schannel Provider, but not enabled by default:



| Cipher suite string                                                                               | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions                     |
|---------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS\_CHACHA20\_POLY1305\_SHA256<br/>                                                        | Yes<br/>                      | TLS 1.3<br/>                            |
| TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA<br/>                                                | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_RSA\_WITH\_AES\_128\_CBC\_SHA<br/>                                                | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA256<br/>                                             | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA256<br/>                                             | Yes<br/>                      | TLS 1.2<br/>                            |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA<br/>                                                | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA<br/>                                                | Yes<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA<br/>                                               | No<br/>                      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_RC4\_128\_SHA<br/>                                                          | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_RC4\_128\_MD5<br/>                                                          | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_DES\_CBC\_SHA<br/>                                                          | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_DHE\_DSS\_WITH\_DES\_CBC\_SHA<br/>                                                     | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_DHE\_DSS\_EXPORT1024\_WITH\_DES\_CBC\_SHA<br/>                                         | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_NULL\_MD5 <br/> Only used when application explicitly requests. <br/> | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_EXPORT1024\_WITH\_RC4\_56\_SHA<br/>                                               | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_EXPORT\_WITH\_RC4\_40\_MD5<br/>                                                   | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_EXPORT1024\_WITH\_DES\_CBC\_SHA<br/>                                              | No<br/>                       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |



 

The following PSK cipher suites are enabled and in this priority order by default using the Microsoft Schannel Provider:



| Cipher suite string                              | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions |
|--------------------------------------------------|-------------------------------------|---------------------------|
| TLS\_PSK\_WITH\_AES\_256\_GCM\_SHA384<br/> | Yes<br/>                      | TLS 1.2<br/>        |
| TLS\_PSK\_WITH\_AES\_128\_GCM\_SHA256<br/> | Yes<br/>                      | TLS 1.2<br/>        |
| TLS\_PSK\_WITH\_AES\_256\_CBC\_SHA384<br/> | Yes<br/>                      | TLS 1.2<br/>        |
| TLS\_PSK\_WITH\_AES\_128\_CBC\_SHA256<br/> | Yes<br/>                      | TLS 1.2<br/>        |
| TLS\_PSK\_WITH\_NULL\_SHA384<br/>          | No<br/>                       | TLS 1.2<br/>        |
| TLS\_PSK\_WITH\_NULL\_SHA256<br/>          | No<br/>                       | TLS 1.2<br/>        |



 

> [!Note]  
> No PSK cipher suites are enabled by default. Applications need to request PSK using SCH\_USE\_PRESHAREDKEY\_ONLY. For more information on Schannel flags, see [**SCHANNEL\_CRED**](/windows/desktop/api/Schannel/ns-schannel-schannel_cred).

 

To add cipher suites, either deploy a group policy or use the TLS cmdlets:

-   To use group policy, configure SSL Cipher Suite Order under Computer Configuration > Administrative Templates > Network > SSL Configuration Settings with the priority list for all cipher suites you want enabled.
-   To use PowerShell, see [TLS cmdlets](/powershell/module/tls/).

> [!Note]  
> Prior to Windows 10, cipher suite strings were appended with the elliptic curve to determine the curve priority. Windows 10 supports an elliptic curve priority order setting so the elliptic curve suffix is not required and is overridden by the new elliptic curve priority order, when provided, to allow organizations to use group policy to configure different versions of Windows with the same cipher suites.
