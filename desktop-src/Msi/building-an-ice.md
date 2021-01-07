---
description: If you are unable to find the Internal Consistency Evaluators you need among the existing ICE custom actions listed in the ICE Reference, you will need to prepare your own ICE to validate your package.
ms.assetid: d9ff43ee-8e7a-4132-ac2f-232dc24606d8
title: Building An ICE
ms.topic: article
ms.date: 05/31/2018
---

# Building An ICE

If you are unable to find the [Internal Consistency Evaluators](internal-consistency-evaluators-ices.md) you need among the existing ICE custom actions listed in the [ICE Reference](ice-reference.md), you will need to prepare your own ICE to validate your package.

When authoring ICE custom actions you should do the following:

-   Base the ICEs only on custom actions of types listed in the table shown.
-   Call [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) and post an INSTALLMESSAGE\_USER type of message. When authoring your ICE messages follow the message format in the [ICE Message Guidelines](ice-message-guidelines.md).
-   Write your ICE such that it captures any API errors and always returns ERROR\_SUCCESS. This is necessary to allow subsequent custom actions to run following the failure of an ICE.

ICE custom actions are limited to the following custom action types.



| Custom action type                                 | Description               |
|----------------------------------------------------|---------------------------|
| [Custom Action Type 1](custom-action-type-1.md)   | DLL in binary stream      |
| [Custom Action Type 2](custom-action-type-2.md)   | EXE in binary stream      |
| [Custom Action Type 5](custom-action-type-5.md)   | JScript in binary stream  |
| [Custom Action Type 6](custom-action-type-6.md)   | VBScript in binary stream |
| [Custom Action Type 37](custom-action-type-37.md) | JScript code as string    |
| [Custom Action Type 38](custom-action-type-38.md) | VBScript code as string   |



 

When authoring an ICE custom action, do not do the following:

-   Do not assume that the handle to the engine that the ICE receives is an installation instance of the installer database. If it is not a installation instance, certain properties are not defined, the source and target directories are not resolved, and current feature states are not defined.
-   Do not rely on the prior execution, or non-execution, of any installer action, custom action, or another ICE. Because a prior ICE may have created temporary columns in any table, authors should reference columns by name whenever possible. ICEs should cleanup any temporary columns or tables before they exit.
-   Do not assume that authors have access to an image of the source directory of the database.
-   Do not assume that changes made to the database do not persist.

## Related topics

<dl> <dt>

[Sample ICE in C++](sample-ice-in-c-.md)
</dt> <dt>

[Sample ICE in VBScript](sample-ice-in-vbscript.md)
</dt> </dl>

 

 



