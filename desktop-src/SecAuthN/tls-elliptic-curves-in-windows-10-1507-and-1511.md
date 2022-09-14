---
description: Elliptic curves enabled in Windows 10 versions 1507 and 1511.
title: TLS Elliptic Curves in Windows 10 version 1507 and 1511
ms.topic: article
ms.keywords: 'ecc curves, elliptic curves, tls elliptic curves, ECC curves, schannel, ECC, EC, Elliptic Curve Cryptography'
ms.date: 06/10/2020
---

# TLS Elliptic Curves in Windows 10 version 1507 and 1511

For Windows 10, versions 1507 and 1511, the following elliptic curves are enabled and in this priority order by default using the Microsoft Schannel Provider:

| Elliptic curve string | Available in FIPS mode |
|-------------|--------------|
| NistP256 | Yes |
| NistP384 | Yes |


The following elliptic curves are supported by the Microsoft Schannel Provider, but not enabled by default:

| Elliptic curve string | Available in FIPS mode |
|-------------|--------------|
| brainpoolP256r1 | No |
| brainpoolP384r1 | No |
| brainpoolP512r1 | No |
| nistP192 | No |
| nistP224 | No |
| nistP521 | Yes |
| secP160k1 | No |
| secP160r1 | No |
| secP160r2 | No |
| secP192k1 | No |
| secP192r1 | No |
| secP224k1 | No |
| secP224r1 | No |
| secP256k1 | No |
| secP256r1 | No |
| secP384r1 | No |
| secP521r1 | No |

## Enabling Elliptic Curves

To add elliptic curves, either deploy a group policy or use the TLS cmdlets:
- To use group policy, [configure ECC Curve Order](/windows-server/security/tls/manage-tls#configuring-tls-ecc-curve-order) under Computer Configuration > Administrative Templates > Network > SSL Configuration Settings with the priority list for all elliptic curves you want enabled.

- To use PowerShell, see [TLS cmdlets](/powershell/module/tls) for a complete list of TLS cmdlet syntax and descriptions.


> [!NOTE]
> Prior to Windows 10, cipher suite strings were appended with the elliptic curve to determine the curve priority. Windows 10 supports an elliptic curve priority order setting so the elliptic curve suffix is not required and is overridden by the new elliptic curve priority order, when provided, to allow organizations to use group policy to configure different versions of Windows with the same cipher suites.


## See Also

[Configuring TLS ECC Curve Order](/windows-server/security/tls/manage-tls#configuring-tls-ecc-curve-order)

[Managing TLS ECC order](/windows-server/security/tls/manage-tls#managing-tls-ecc-order)

[Managing Windows ECC curves using Group Policy](/windows-server/security/tls/manage-tls#managing-windows-ecc-curves-using-group-policy)

[TLS cmdlets](/powershell/module/tls)
