---
description: Identifies the possible signer certificates used to digitally sign patches.
ms.assetid: 8f76c27d-92f1-4de7-a69c-fba877e0325d
title: MsiPatchCertificate Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiPatchCertificate Table

The MsiPatchCertificate Table identifies the possible signer certificates used to digitally sign patches. The MsiPatchCertificate Table contains the information that is needed to enable [User Account Control (UAC) Patching](user-account-control--uac--patching.md) for an application.

The MsiPatchCertificate Table has the following columns:



| Column               | Type                         | Key | Nullable |
|----------------------|------------------------------|-----|----------|
| PatchCertificate     | [Identifier](identifier.md) | Y   | N        |
| DigitalCertificate\_ | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="PatchCertificate"></span><span id="patchcertificate"></span><span id="PATCHCERTIFICATE"></span>PatchCertificate
</dt> <dd>

The unique identifier for this row in the MsiPatchCertificate Table.

</dd> <dt>

<span id="DigitalCertificate"></span><span id="digitalcertificate"></span><span id="DIGITALCERTIFICATE"></span>DigitalCertificate
</dt> <dd>

An external key into the first column of the [MsiDigitalCertificate Table](msidigitalcertificate-table.md). The row indicated in the MsiDigitalCertificate Table contains the binary representation of the signer certificate.

</dd> </dl>

## Remarks

Patches are always evaluated against the MsiPatchCertificate Table that is current at the time the patch is applied. A patch can modify the MsiPatchCertificate Table by adding or removing entries. This enables a patch to modify the evaluation of future patches that are applied later in the patching sequence. Multiple certificates can exist in the table, and the patch must match at least one certificate to be applied.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE81](ice81.md)  
</dl>

## Related topics

<dl> <dt>

[DisableLUAPatching](disableluapatching.md)
</dt> <dt>

[User Account Control (UAC) Patching](user-account-control--uac--patching.md)
</dt> <dt>

[**MSIDISABLELUAPATCHING**](msidisableluapatching.md)
</dt> <dt>

[Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 



