---
description: Supported groups enabled in Windows 11 versions 24H2 and later.
title: TLS Supported Groups in Windows 11 version 24H2, Windows Server 2025, and later
ms.topic: reference
ms.keywords: 'hybrid key exchange, tls supported groups, supported groups, ecc curves, elliptic curves, tls elliptic curves, ECC curves, schannel, ECC, EC, Elliptic Curve Cryptography'
ms.date: 05/20/2026
---

# TLS Supported Groups in Windows 11 versions 24H2 and later
> [!NOTE]
> With the addition of post-quantum key exchange algorithms, the TLS parameter previously referred to as "Elliptic Curves" has been renamed "Supported Groups" to be inclusive of non-EC algorithms. Reference: [IANA TLS parameters](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-8). 

> [!NOTE]
> NEW post-quantum ML-KEM groups are now available in the latest Windows Insider Preview builds for Windows 11 client and Windows Server 2025. These groups are disabled by default, and must be enabled using one of the configuration methods linked at the end of this article. The minimum supported builds are [26100.8514](https://learn.microsoft.com/en-us/windows-insider/release-notes/release-preview-24h2-25h2/build-26100-8514-26200-8514) for Windows 11 24H2 and 25H2, [28000.2173](https://learn.microsoft.com/en-us/windows-insider/release-notes/release-preview-26h1/build-28000-2173) for Windows 11 26H2, and [29550](https://techcommunity.microsoft.com/discussions/windowsserverinsiders/announcing-windows-server-vnext-preview-build-29550/4501665) for Windows Server 2025.

For Windows 11, versions 24H2 and later, the following groups are enabled and in this priority order by default using the Microsoft Schannel Provider:

| Elliptic curve string | Supported Protocol Versions | Available in FIPS mode | 
|-------------|--------------|
| curve25519 | TLS 1.0, 1.1, 1.2, 1.3 | No |
| nistP256 | TLS 1.0, 1.1, 1.2, 1.3 | Yes |
| nistP384 | TLS 1.0, 1.1, 1.2, 1.3 | Yes |


The following groups are supported by the Microsoft Schannel Provider, but are not enabled by default:

| Elliptic curve string |  Supported Protocol Versions | Available in FIPS mode |
|-------------|--------------|
| x25519_mlkem768 | TLS 1.3 | Yes |
| secp256r1_mlkem768 | TLS 1.3 | Yes |
| secp384r1_mlkem1024 | TLS 1.3 | Yes |
| brainpoolP256r1 | TLS 1.0, 1.1, 1.2 | No |
| brainpoolP384r1 | TLS 1.0, 1.1, 1.2 | No |
| brainpoolP512r1 | TLS 1.0, 1.1, 1.2 | No |
| curve25519 | TLS 1.0, 1.1, 1.2, 1.3 | No |
| nistP192 | TLS 1.0, 1.1, 1.2, 1.3 | No |
| nistP224 | TLS 1.0, 1.1, 1.2, 1.3 | No |
| nistP521 | TLS 1.0, 1.1, 1.2, 1.3 | Yes |
| secP160k1 | TLS 1.0, 1.1, 1.2 | No |
| secP160r1 | TLS 1.0, 1.1, 1.2 | No |
| secP160r2 | TLS 1.0, 1.1, 1.2 | No |
| secP192k1 | TLS 1.0, 1.1, 1.2 | No |
| secP192r1 | TLS 1.0, 1.1, 1.2 | No |
| secP224k1 | TLS 1.0, 1.1, 1.2 | No |
| secP224r1 | TLS 1.0, 1.1, 1.2 | No |
| secP256k1 | TLS 1.0, 1.1, 1.2 | No |
| secP256r1 | TLS 1.0, 1.1, 1.2, 1.3 | No |
| secP384r1 | TLS 1.0, 1.1, 1.2, 1.3 | No |
| secP521r1 | TLS 1.0, 1.1, 1.2, 1.3 | No |



## Enabling Supported Groups

To add supported groups or change the default priority order, either deploy a group policy or use the TLS cmdlets:
- To use group policy, [configure ECC Curve Order](/windows-server/security/tls/manage-tls#configuring-tls-ecc-curve-order) under Computer Configuration > Administrative Templates > Network > SSL Configuration Settings with the priority list for all elliptic curves you want enabled.

- To use PowerShell, see [TLS cmdlets](/powershell/module/tls) for a complete list of TLS cmdlet syntax and descriptions.



## See Also

[Configuring TLS ECC Curve Order](/windows-server/security/tls/manage-tls#configuring-tls-ecc-curve-order)

[Managing TLS ECC order](/windows-server/security/tls/manage-tls#managing-tls-ecc-order)

[Managing Windows ECC curves using Group Policy](/windows-server/security/tls/manage-tls#managing-windows-ecc-curves-using-group-policy)

[TLS cmdlets](/powershell/module/tls)
