---
description: Learn about TLS cipher suites in Windows 10 v1903, v1909, and v2004. Cipher suites can only be negotiated for TLS versions which support them.
title: TLS Cipher Suites in Windows 10 v1903, v1909, and v2004
ms.topic: reference
ms.date: 10/23/2024
---

# TLS Cipher Suites in Windows 10 v1903, v1909, and v2004

Cipher suites can only be negotiated for TLS versions which support them. The highest supported TLS version is always preferred in the TLS handshake.

Availability of cipher suites are controlled by combining the two configurations below:

- LSA Configuration: Default priority order is overridden when a priority list is configured. Cipher suites not in the priority list will not be used.
- App Configuration: Applications can pass [SCHANNEL\_CRED](/windows/win32/api/schannel/ns-schannel-schannel_cred) or [SCH\_CREDENTIALS](/windows/win32/api/schannel/ns-schannel-sch_credentials) to specify the flags and enable (or disabled) specific protocols/algorithms during [AcquireCredentialsHandle (Schannel) function](/windows/win32/secauthn/acquirecredentialshandle--schannel). More details can be referred at: [Creating a Secure Connection Using Schannel](/windows/win32/secauthn/creating-a-secure-connection-using-schannel)

> [!IMPORTANT]
> HTTP/2 web services fail with non-HTTP/2-compatible cipher suites. To ensure your web services function with HTTP/2 clients and browsers, see [How to deploy custom cipher suite ordering](/troubleshoot/windows-server/windows-security/deploy-custom-cipher-suite-ordering).

FIPS-compliance has become more complex with the addition of elliptic curves making the FIPS mode enabled column in previous versions of this table misleading. For example, a cipher suite such as TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 is only FIPS-compliant when using NIST elliptic curves. To find out which combinations of elliptic curves and cipher suites will be enabled in FIPS mode, see section 3.3.1 of [Guidelines for the Selection, Configuration, and Use of TLS Implementations]( https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf).

For Windows 10, version 1903, 1909, and 2004, the following cipher suites are enabled and in this priority order by default using the Microsoft Schannel Provider:

| Cipher suite string                                                                                 | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions                     |
|-----------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384                                                | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256                                                | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384                                                  | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256                                                  | Yes                           | TLS 1.2                                 |
| TLS\_DHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384                                                    | No                           | TLS 1.2                                 |
| TLS\_DHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256                                                    | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384                                                | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256                                                | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384                                                  | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256                                                  | Yes                           | TLS 1.2                                 |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA                                                   | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA                                                   | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA                                                     | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA                                                     | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384                                                         | Yes                           | TLS 1.2                                 |
| TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256                                                         | Yes                           | TLS 1.2                                 |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256                                                         | Yes                           | TLS 1.2                                 |
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256                                                         | Yes                           | TLS 1.2                                 |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA                                                            | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA                                                            | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA                                                           | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_RSA\_WITH\_NULL\_SHA256       Only used when application explicitly requests.      | No                            | TLS 1.2                                 |
| TLS\_RSA\_WITH\_NULL\_SHA       Only used when application explicitly requests.         | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |

The following cipher suites are supported by the Microsoft Schannel Provider, but not enabled by default:

| Cipher suite string                                                                               | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions                     |
|---------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA                                                     | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_DHE\_RSA\_WITH\_AES\_128\_CBC\_SHA                                                     | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA256                                                  | Yes                           | TLS 1.2                                 |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA256                                                  | Yes                           | TLS 1.2                                 |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA                                                     | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA                                                     | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA                                                    | Yes                           | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_WITH\_RC4\_128\_SHA                                                               | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_WITH\_RC4\_128\_MD5                                                               | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_WITH\_DES\_CBC\_SHA                                                               | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_DHE\_DSS\_WITH\_DES\_CBC\_SHA                                                          | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_DHE\_DSS\_EXPORT1024\_WITH\_DES\_CBC\_SHA                                              | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_WITH\_NULL\_MD5       Only used when application explicitly requests.       | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_EXPORT1024\_WITH\_RC4\_56\_SHA                                                    | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_EXPORT\_WITH\_RC4\_40\_MD5                                                        | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_EXPORT1024\_WITH\_DES\_CBC\_SHA                                                   | No                            | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |

The following PSK cipher suites are enabled and in this priority order by default using the Microsoft Schannel Provider:

| Cipher suite string                              | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions |
|--------------------------------------------------|-------------------------------------|---------------------------|
| TLS\_PSK\_WITH\_AES\_256\_GCM\_SHA384      | Yes                           | TLS 1.2             |
| TLS\_PSK\_WITH\_AES\_128\_GCM\_SHA256      | Yes                           | TLS 1.2             |
| TLS\_PSK\_WITH\_AES\_256\_CBC\_SHA384      | Yes                           | TLS 1.2             |
| TLS\_PSK\_WITH\_AES\_128\_CBC\_SHA256      | Yes                           | TLS 1.2             |
| TLS\_PSK\_WITH\_NULL\_SHA384               | No                            | TLS 1.2             |
| TLS\_PSK\_WITH\_NULL\_SHA256               | No                            | TLS 1.2             |

> [!NOTE]
> No PSK cipher suites are enabled by default. Applications need to request PSK using SCH\_USE\_PRESHAREDKEY\_ONLY. For more information on Schannel flags, see [**SCHANNEL\_CRED**](/windows/desktop/api/Schannel/ns-schannel-schannel_cred).

To add cipher suites, either deploy a group policy or use the TLS cmdlets:

- To use group policy, configure SSL Cipher Suite Order under Computer Configuration > Administrative Templates > Network > SSL Configuration Settings with the priority list for all cipher suites you want enabled.
- To use PowerShell, see [TLS cmdlets](/powershell/module/tls/).

> [!NOTE]
> Prior to Windows 10, cipher suite strings were appended with the elliptic curve to determine the curve priority. Windows 10 supports an elliptic curve priority order setting so the elliptic curve suffix is not required and is overridden by the new elliptic curve priority order, when provided, to allow organizations to use group policy to configure different versions of Windows with the same cipher suites.
