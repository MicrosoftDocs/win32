---
description: Learn about TLS cipher suites in Windows Server 2022 and later. Cipher suites can only be negotiated for TLS versions which support them.
title: TLS Cipher Suites in Windows Server 2022 and later.
ms.topic: reference
ms.date: 11/13/2024
---

# TLS Cipher Suites in Windows Server 2022 and later

Cipher suites can only be negotiated for TLS versions which support them. The highest supported TLS version is always preferred in the TLS handshake.

Availability of cipher suites should be controlled in one of two ways:

- Default priority order is overridden when a priority list is configured. Cipher suites not in the priority list will not be used.
- Allowed when the application passes **SCH_USE_STRONG_CRYPTO**: The Microsoft Schannel provider will filter out known weak cipher suites when the application uses the **SCH_USE_STRONG_CRYPTO** flag. RC4, DES, export and null cipher suites are filtered out.

> [!IMPORTANT]
> HTTP/2 web services fail with non-HTTP/2-compatible cipher suites. To ensure your web services function with HTTP/2 clients and browsers, see [How to deploy custom cipher suite ordering](/troubleshoot/windows-server/windows-security/deploy-custom-cipher-suite-ordering).

FIPS-compliance has become more complex with the addition of elliptic curves making the FIPS mode enabled column in previous versions of this table misleading. For example, a cipher suite such as **TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256** is only FIPS-compliant when using NIST elliptic curves. To find out which combinations of elliptic curves and cipher suites will be enabled in FIPS mode, see section 3.3.1 of [Guidelines for the Selection, Configuration, and Use of TLS Implementations]( https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf).

For Windows Server 2022 and later, the following cipher suites are enabled and in this priority order by default using the Microsoft Schannel Provider:

| Cipher suite string | Allowed by SCH_USE_STRONG_CRYPTO | TLS/SSL Protocol versions |
|-----------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS_AES_256_GCM_SHA384 | Yes | TLS 1.3 |
| TLS_AES_128_GCM_SHA256 | Yes | TLS 1.3 |
| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | Yes | TLS 1.2 |
| TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | Yes | TLS 1.2 |
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | Yes | TLS 1.2 |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | Yes | TLS 1.2 |
| TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 | Yes | TLS 1.2 |
| TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 | Yes | TLS 1.2 |
| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | Yes | TLS 1.2 |
| TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | Yes | TLS 1.2       |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 | Yes | TLS 1.2       |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 | Yes | TLS 1.2       |
| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA                         | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA                         | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA                           | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA                           | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_RSA_WITH_AES_256_GCM_SHA384                               | Yes | TLS 1.2       |
| TLS_RSA_WITH_AES_128_GCM_SHA256                               | Yes | TLS 1.2       |
| TLS_RSA_WITH_AES_256_CBC_SHA256                               | Yes | TLS 1.2       |
| TLS_RSA_WITH_AES_128_CBC_SHA256                               | Yes | TLS 1.2       |
| TLS_RSA_WITH_AES_256_CBC_SHA                                  | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_RSA_WITH_AES_128_CBC_SHA                                  | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_RSA_WITH_3DES_EDE_CBC_SHA                                 | No | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_RSA_WITH_NULL_SHA256<br/>Only used when application explicitly requests. | No  | TLS 1.2       |
| TLS_RSA_WITH_NULL_SHA<br/>Only used when application explicitly requests. | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |

The following cipher suites are supported by the Microsoft Schannel Provider, but not enabled by default:

| Cipher suite string | Allowed by SCH_USE_STRONG_CRYPTO | TLS/SSL Protocol versions |
|---------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|
| TLS_CHACHA20_POLY1305_SHA256                                   | Yes | TLS 1.3       |
| TLS_DHE_RSA_WITH_AES_256_CBC_SHA                           | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_DHE_RSA_WITH_AES_128_CBC_SHA                           | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_DHE_DSS_WITH_AES_256_CBC_SHA256                        | Yes | TLS 1.2       |
| TLS_DHE_DSS_WITH_AES_128_CBC_SHA256                        | Yes | TLS 1.2       |
| TLS_DHE_DSS_WITH_AES_256_CBC_SHA                           | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_DHE_DSS_WITH_AES_128_CBC_SHA                           | Yes | TLS 1.2, TLS 1.1, TLS 1.0 |
| TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA                          | No | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_RSA_WITH_RC4_128_SHA                                     | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_RSA_WITH_RC4_128_MD5                                     | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_RSA_WITH_DES_CBC_SHA                                     | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_DHE_DSS_WITH_DES_CBC_SHA                                | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_DHE_DSS_EXPORT1024_WITH_DES_CBC_SHA                    | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_RSA_WITH_NULL_MD5<br/>Only used when application explicitly requests. | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_RSA_EXPORT1024_WITH_RC4_56_SHA                          | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_RSA_EXPORT_WITH_RC4_40_MD5                              | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |
| TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA                         | No  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0 |

The following PSK cipher suites are enabled and in this priority order by default using the Microsoft Schannel Provider:

| Cipher suite string                              | Allowed by SCH\_USE\_STRONG\_CRYPTO | TLS/SSL Protocol versions |
|--------------------------------------------------|-------------------------------------|---------------------------|
| TLS_PSK_WITH_AES_256_GCM_SHA384 | Yes | TLS 1.2 |
| TLS_PSK_WITH_AES_128_GCM_SHA256 | Yes | TLS 1.2 |
| TLS_PSK_WITH_AES_256_CBC_SHA384 | Yes | TLS 1.2 |
| TLS_PSK_WITH_AES_128_CBC_SHA256 | Yes | TLS 1.2 |
| TLS_PSK_WITH_NULL_SHA384 | No  | TLS 1.2 |
| TLS_PSK_WITH_NULL_SHA256 | No  | TLS 1.2 |

> [!NOTE]
> No PSK cipher suites are enabled by default. Applications need to request PSK using SCH\_USE\_PRESHAREDKEY\_ONLY. For more information on Schannel flags, see [**SCHANNEL\_CRED**](/windows/win32/api/Schannel/ns-schannel-schannel_cred).

To add cipher suites, either deploy a group policy or use the TLS cmdlets:

- To use group policy, configure SSL Cipher Suite Order under Computer Configuration > Administrative Templates > Network > SSL Configuration Settings with the priority list for all cipher suites you want enabled.
- To use PowerShell, see [TLS cmdlets](/powershell/module/tls/).

> [!NOTE]
> Prior to Windows 10, cipher suite strings were appended with the elliptic curve to determine the curve priority. Windows 10 supports an elliptic curve priority order setting so the elliptic curve suffix is not required and is overridden by the new elliptic curve priority order, when provided, to allow organizations to use group policy to configure different versions of Windows with the same cipher suites.
