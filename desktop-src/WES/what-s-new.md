---
title: What's New (Windows Event Log)
description: This page summarizes the new features that were added to the Windows Event Log API for each release.
ms.assetid: 90adf08c-177f-46ae-82e1-f7cca5a46db8
ms.topic: article
ms.date: 05/31/2018
---

# What's New (Windows Event Log)

This page summarizes the new features that were added to the Windows Event Log API for each release.

## Windows 7 and Windows Server 2008 R2

The following are the changes that were made to the [EventManifest](eventmanifestschema-schema.md) schema:

-   Removed the [**TaskEventDefinitionType**](eventmanifestschema-taskeventdefinitiontype-complextype.md) complex type. To provide the same functionality, use task-specific opcodes (see the **opcodes** element of the [**TaskType**](eventmanifestschema-tasktype-complextype.md) complex type.
-   Added the [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md), [**filePath**](eventmanifestschema-filepath-simpletype.md), and [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) simple types to restrict values assigned to attributes of these types.
-   Added the **filters** attribute to the [**ProviderType**](eventmanifestschema-providertype-complextype.md) complex type. Providers can use filters in the same way that providers use level and keywords to determine whether they should write an event.
-   Added the following output types that you can specify for data items defined in an event data template:
    -   win:DateTimeCultureInsensitive
    -   win:HResult
    -   win:NTSTATUS
-   The output types are now honored whereas before they were ignored.

The following changes were made to the version of the [**Message Compiler**](message-compiler--mc-exe-.md) that ships with the Windows 7 version of the Windows SDK:

-   Added arguments to have the compiler generate logging code based on your manifest. You can also request that the compiler generate code to log events on operating systems prior to Windows Vista. For a list of the arguments, see the "Arguments specific to generating code used to log events" section of the [**Message Compiler**](message-compiler--mc-exe-.md) topic.
-   The compiler now enforces stricter syntactic and semantic validation on the manifest. This may cause some manifests that successfully compiled on previous versions of the message compiler to require changes in order to successfully compile using the latest version.
