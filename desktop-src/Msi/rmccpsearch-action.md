---
description: The RMCCPSearch action uses file signatures to validate that qualifying products are installed on a system before an upgrade installation is performed.
ms.assetid: d37b2434-86eb-4c6e-b817-77c75dcebbf5
title: RMCCPSearch Action
ms.topic: article
ms.date: 05/31/2018
---

# RMCCPSearch Action

The RMCCPSearch action uses file signatures to validate that qualifying products are installed on a system before an upgrade installation is performed.

## Sequence Restrictions

RMCCPSearch action should be authored into the [InstallUISequence table](installuisequence-table.md) and [InstallExecuteSequence table](installexecutesequence-table.md). The installer prevents RMCCPSearch from running in the InstallExecuteSequence sequence if the action has already run in InstallUISequence sequence.

## ActionData Messages

There are no ActionData messages.

## Remarks

The RMCCPSearch action requires the [**CCP\_DRIVE**](ccp-drive.md) property to be set to the root path on the removable [*volume*](v-gly.md) that has the installation for any of the qualifying products.

Each file signature in the CCPSearch table is searched for under the path referred to by the [**CCP\_DRIVE**](ccp-drive.md) property using the [DrLocator](drlocator-table.md) table. The absence of the signature from the [Signature](signature-table.md) table denotes a directory. If any signature is determined to exist, the RMCCPSearch action terminates.

## Related topics

<dl> <dt>

[CCPSearch table](ccpsearch-table.md)
</dt> </dl>

 

 



