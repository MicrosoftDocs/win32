---
description: ICE73 verifies that your package does not reuse package codes, upgrade codes, or product codes of the Windows Installer SDK samples. Packages should never reuse the package, upgrade, or product codes of another product.
ms.assetid: a04429c2-ff9e-4ec8-8d07-faf1479f4920
title: ICE73
ms.topic: article
ms.date: 05/31/2018
---

# ICE73

ICE73 verifies that your package does not reuse package codes, upgrade codes, or product codes of the Windows Installer SDK samples. Packages should never reuse the package, upgrade, or product codes of another product.

## Result

ICE73 outputs a warning if your product's package reuses a package or product code of a Windows Installer SDK sample.

## Example

ICE73 reports the following errors for the example shown:

``` syntax
This package reuses the '{80F7E030-A751-11D2-A7D4-006097C99860}' ProductCode of the orca.msi 1.0 Windows Installer SDK package.
This package reuses the '{000C1101-0000-0000-C000-000000000047}' Package Code of the msispy.msi 1.0 Windows Installer SDK package.
This package reuses the '{8FC7****-88A0-4b41-82B8-8905D4AA904C}' Upgrade Code of a 1.1 Windows Installer SDK package.
```

> [!Note]  
> The asterisks (\*\*\*\*) in the GUID represent the range of GUIDs reserved for subsequent Windows Installer SDK packages.

 

To fix the errors, generate a new unique GUID for your package's product and package codes. You will also need a new unique GUID for your package's upgrade code.

[Summary Information Stream](summary-information-stream.md) (partial)



| Property       | Value                                  |
|----------------|----------------------------------------|
| PID\_REVNUMBER | {000C1101-0000-0000-C000-000000000047} |



 

[Property Table](property-table.md) (partial)



| Property                           | Value                                  |
|------------------------------------|----------------------------------------|
| [**ProductCode**](productcode.md) | {80F7E030-A751-11D2-A7D4-006097C99860} |
| [**UpgradeCode**](upgradecode.md) | {8FC70000-88A0-4b41-82B8-8905D4AA904C} |



 

## Related topics

<dl> <dt>

[Package Codes](package-codes.md)
</dt> <dt>

[Product Codes](product-codes.md)
</dt> <dt>

[**Revision Number Summary Property**](revision-number-summary.md)
</dt> <dt>

[**UpgradeCode Property**](upgradecode.md)
</dt> <dt>

[**ProductCode Property**](productcode.md)
</dt> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



