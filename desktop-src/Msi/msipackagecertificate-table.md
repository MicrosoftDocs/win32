---
description: The MsiPackageCertificate Table lists digital signature certificates used to verify the identity of the installation packages that make this Multiple-Package Installation.
ms.assetid: d3a97325-2136-4745-8a7d-57e4d6b9d27e
title: MsiPackageCertificate Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiPackageCertificate Table

The MsiPackageCertificate Table lists digital signature certificates used to verify the identity of the installation packages that make this [Multiple-Package Installation](multiple-package-installations.md).

Use this table to author a [multiple-package installation](multiple-package-installations.md) for a product containing multiple Windows Installer packages. If the first package is digitally signed, and contains a MsiPackageCertificate Table specifying digital certificates for all the remaining packages in the product, the administrator needs only accept the [*User Account Control*](u-gly.md) (UAC) prompt displayed for the first package. After accepting the UAC's prompt for the first package, the user-defined functions in the [MsiEmbeddedChainer table](msiembeddedchainer-table.md) can then join the remaining packages to the multiple-package installation without displaying a UAC prompt and requiring an administrator response for each package.

If one or more of the functions in the [MsiEmbeddedChainer table](msiembeddedchainer-table.md) request an unsigned package, another UAC prompt requiring administrator interaction is displayed for each unsigned package. If the administrator accepts this UAC prompt, the multi-package installation continues. Once an administrator has provided credentials for a package, no UAC prompt will again be displayed for that package during this multi-package installation. If the administrator rejects a UAC prompt for a package, the Windows installer rolls back the multi-package installation before it commits to install any packages belonging to the product.

**[Windows Installer 4.0 or earlier](not-supported-in-windows-installer-4-0.md):** Not supported. This table is available beginning with Windows Installer 4.5.

The MsiPackageCertificate Table has the following columns:



| Column               | Type                         | Key | Nullable |
|----------------------|------------------------------|-----|----------|
| PackageCertificate   | [Identifier](identifier.md) | Y   | N        |
| DigitalCertificate\_ | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="PackageCertificate"></span><span id="packagecertificate"></span><span id="PACKAGECERTIFICATE"></span>PackageCertificate
</dt> <dd>

The unique identifier for this row in the MsiPackageCertificate Table.

</dd> <dt>

<span id="DigitalCertificate"></span><span id="digitalcertificate"></span><span id="DIGITALCERTIFICATE"></span>DigitalCertificate
</dt> <dd>

An external key into the first column of the [MsiDigitalCertificate Table](msidigitalcertificate-table.md). The row indicated in the MsiDigitalCertificate Table contains the binary representation of the signer certificate.

</dd> </dl>

## Validation

<dl>

[ICE39](ice39.md)  
[ICE81](ice81.md)  
</dl>

## Related topics

<dl> <dt>

[MsiEmbeddedChainer](msiembeddedchainer-table.md)
</dt> <dt>

[MsiDigitalCertificate Table](msidigitalcertificate-table.md)
</dt> </dl>

 

 



