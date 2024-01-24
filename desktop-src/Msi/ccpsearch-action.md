---
description: The CCPSearch action uses file signatures to validate that qualifying products are installed on a system before an upgrade installation is performed.
ms.assetid: 0aa7bf8b-de76-464d-8e7b-3aa4f609fe19
title: CCPSearch Action
ms.topic: article
ms.date: 05/31/2018
---

# CCPSearch Action

The CCPSearch action uses file signatures to validate that qualifying products are installed on a system before an upgrade installation is performed.

## Sequence Restrictions

CCPSearch action should be authored into the [InstallUISequence table](installuisequence-table.md) and [InstallExecuteSequence table](installexecutesequence-table.md). The installer prevents the CCPSearch action from running in the InstallExecuteSequence sequence if the action has already run in InstallUISequence sequence. The CCPSearch action must come before the [RMCCPSearch](rmccpsearch-action.md) action.

## ActionData Messages

There are no ActionData messages.

## Remarks

The CCPSearch action searches for file signatures listed in the CCPSearch table on the system using the following tables in order: Signature, CompLocator, RegLocator, IniLocator, and DrLocator.

If any signature is determined to exist, the **CCP\_Success** property is set to 1 and the CCPSearch action terminates.

The absence of the signature from the Signature table denotes a directory.

## Related topics

<dl> <dt>

[CCPSearch](ccpsearch-table.md)
</dt> <dt>

[Signature](signature-table.md)
</dt> <dt>

[CompLocator](complocator-table.md)
</dt> <dt>

[RegLocator](reglocator-table.md)
</dt> <dt>

[IniLocator](inilocator-table.md)
</dt> <dt>

[DrLocator](drlocator-table.md)
</dt> </dl>

 

 



