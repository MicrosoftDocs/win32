---
description: The following example shows how Windows Installer 3.0 and later can be used to apply patches in the order in which they are authored.
ms.assetid: 98771652-cec2-4371-8132-a741cf8431fb
title: Multiple Patching Example
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Patching Example

The following example shows how Windows Installer 3.0 and later can be used to apply patches in the order in which they are authored.

## Example

In this example there are three patches, QFE1, QFE2, and ServicePack1, and they each have a [MsiPatchSequence](msipatchsequence-table.md) table. These patches have been authored to be applied to version 1.0 of the application.



| Patch Name   | Patch Type    | Sequence Number |
|--------------|---------------|-----------------|
| QFE1         | Small Update  | 1.1.0           |
| QFE2         | Small Update  | 1.2.0           |
| ServicePack1 | Minor Upgrade | 1.3.0           |



 

The [MsiPatchSequence](msipatchsequence-table.md) table of each patch has only one record that contains the patch family, product code, and sequence number. The three patches are all applied to the same product and belong to the same patch family, named AppPatch. None of the patches have the **msidbPatchSequenceSupersedeEarlier** attribute.

[MsiPatchSequence Table](msipatchsequence-table.md) for the QFE1 [small update](small-updates.md). 

| PatchFamily | ProductCode                            | Sequence | Attributes |
|-------------|----------------------------------------|----------|------------|
| AppPatch    | {18A9233C-0B34-4127-A966-C257386270BC} | 1.1.0    |            |



 

[MsiPatchSequence Table](msipatchsequence-table.md) for the QFE2 [small update](small-updates.md). 

| PatchFamily | ProductCode                            | Sequence | Attributes |
|-------------|----------------------------------------|----------|------------|
| AppPatch    | {18A9233C-0B34-4127-A966-C257386270BC} | 1.2.0    |            |



 

[MsiPatchSequence Table](msipatchsequence-table.md) for ServicePack1 [minor upgrade](minor-upgrades.md). 

| PatchFamily | ProductCode                            | Sequence | Attributes |
|-------------|----------------------------------------|----------|------------|
| AppPatch    | {18A9233C-0B34-4127-A966-C257386270BC} | 1.3.0    |            |



 

If a user installs version 1.0 of the product, and then applies QFE2, and then at a later date decides to apply QFE1, Windows Installer ensures that the effective sequence of patch application to the product is QFE1 applied ahead of QFE2. If the user applies ServicePack1, then applies QFE2 and QFE1 together at a later date, Windows Installer ensures that the effective sequence of patch application to the product is QFE1 ahead of QFE2 and ahead of ServicePack1.

If ServicePack1 has **msidbPatchSequenceSupersedeEarlier** set in the Attributes column of its [MsiPatchSequence](msipatchsequence-table.md) table, this means that the service pack contains all the changes in QFE1 and QFE2. In this case, QFE1 and QFE2 are not applied when ServicePack1 is applied.

**Windows Installer 2.0:** Not supported. Versions earlier than Windows Installer 3.0 can install only one patch per transaction and patches are applied in the sequence that they are provided. For the preceding example, if QFE2 is applied first and then QFE1 is applied, that is two transactions and the patches are applied to version 1.0 of the application in the sequence QFE2 followed by QFE1. If ServicePack1 is applied first, then QFE1 or QFE2 cannot be applied in a later transaction because ServicePack1 is a minor upgrade that changes the application version. QFE1 and QFE2 can only be applied to version 1.0 of the application.

 

 



