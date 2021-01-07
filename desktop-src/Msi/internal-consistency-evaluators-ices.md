---
description: Internal consistency evaluators, also called ICEs, are custom actions written in VBScript, JScript, or as a DLL or EXE.
ms.assetid: 0789103d-ae34-46be-a9fb-093e066d6d4b
title: Internal Consistency Evaluators - ICEs
ms.topic: article
ms.date: 05/31/2018
---

# Internal Consistency Evaluators - ICEs

Internal consistency evaluators, also called ICEs, are custom actions written in VBScript, JScript, or as a DLL or EXE. When these custom actions are executed, they scan the database for entries in database records that are valid when examined individually but that may cause incorrect behavior in the context of the whole database. Note that this is different than the validation done on individual records using [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify).

For example, the [Component table](component-table.md) may list several components that are all valid when tested individually with [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify). However, **MsiViewModify** would not catch the error when two components use the same [GUID](guid.md) as their component code. The custom action [ICE08](ice08.md) is designed to validate that the Component table does not contain duplicate component code GUIDs.

ICE custom actions return four kinds of messages:

-   [**Errors**](merge-errors.md) Error messages report database authoring that cause incorrect behavior. For example, duplicate component GUIDs cause the installer to incorrectly register components.
-   **Warnings** Warning messages report database authoring that causes incorrect behavior in certain cases. Warnings can also report unexpected side-effects of database authoring. For example, entering the same property name in two conditions that differ only by the case of letters in the name. Because the installer is case-sensitive, the installer treats these as different properties.
-   **Failures** Failure messages report the failure of the ICE custom action. Failure is commonly caused by a database with such severe problems that the ICE cannot even run.
-   **Informational** Informational messages provide information from the ICE and do not indicate a problem with the database. Often they are information about the ICE itself, such as a brief description. They can also provide progress information as the ICE runs.

For more information, see [Using Internal Consistency Evaluators](using-internal-consistency-evaluators.md).

 

 



