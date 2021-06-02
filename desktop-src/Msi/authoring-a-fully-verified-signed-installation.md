---
description: Use these guidelines to cover an entire Windows Installer installation by a digital signature.
ms.assetid: e70eab94-4615-4a73-bccc-e16bd24551f6
title: Authoring a Fully Verified Signed Installation
ms.topic: article
ms.date: 05/31/2018
---

# Authoring a Fully Verified Signed Installation

You can use these guidelines to cover an entire Windows Installer installation by a digital signature.

Authors of Windows Installer installations must adhere to the following to ensure that all parts of the installation are covered by a digital signature:

-   Use internal cabinet files, or use signed external cabinet files and correctly author the [MsiDigitalSignature table](msidigitalsignature-table.md) and [MsiDigitalCertificate table](msidigitalcertificate-table.md).
-   Use only custom actions stored within the package or installed with the package.
-   Sign the installation package.
-   Include an [MsiPatchCertificate table](msipatchcertificate-table.md) in the package. To enable [User Account Control (UAC) Patching](user-account-control--uac--patching.md), this table must contain information used to identify the signer certificates used to digitally sign patches. UAC patching enables the author of the installation package to identify digitally-signed patches that can be applied in the future by non-administrator users.

For an example showing how to author a signed installation using automation, see [Authoring a Fully Verified Signed Installation Using Automation](authoring-a-fully-verified-signed-installation-using-automation.md).

 

 



