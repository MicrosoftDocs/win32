---
title: Package resource indexing (PRI) reference
description: Package resource indexing (PRI) reference
ms.assetid: 15f41d83-d729-45e4-a6bb-5f8c6b78293c
ms.topic: concept-article
ms.date: 05/31/2018
---

# Package resource indexing (PRI) reference

A set of APIs for creating PRI files via a resource indexer. PRI files are used by both packaged and unpackaged
apps to locate resources (such as strings or image files) at runtime.

These APIs are used to create build tools that perform similar functions to the Windows SDK **MakePri** tool
and to Visual Studio MSIX projects. They are not intended to be used by applications themselves; at runtime
apps should use either [**Windows.ApplicationModel.Resources**](/uwp/api/windows.applicationmodel.resources) (for
UWP apps) or 
[**Microsoft.Windows.ApplicationModel.Resources**](/windows/windows-app-sdk/api/winrt/microsoft.windows.applicationmodel.resources) (for WinApp SDK apps) to resolve resources.

For more info, and scenario-based walkthroughs of how to use these APIs, see [Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems).

## In this section

**Conceptual**

-   [Qualifiers in MRM](mrmqualifiers.md)
-   [Resource names in MRM](mrmresourcenames.md)
-   [File resources in MRM](mrmfiles.md)

**Functions**

-   [**MrmCreateConfig**](mrmcreateconfig.md) function
-   [**MrmCreateConfigInMemory**](mrmcreateconfiginmemory.md) function
-   [**MrmCreateResourceFile**](mrmcreateresourcefile.md) function
-   [**MrmCreateResourceFileInMemory**](mrmcreateresourcefileinmemory.md) function
-   [**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md) function
-   [**MrmCreateResourceIndexerFromPreviousPriData**](mrmcreateresourceindexerfrompreviouspridata-.md) function
-   [**MrmCreateResourceIndexerFromPreviousPriFile**](mrmcreateresourceindexerfrompreviousprifile.md) function
-   [**MrmCreateResourceIndexerFromPreviousSchemaData**](mrmcreateresourceindexerfrompreviousschemadata.md) function
-   [**MrmCreateResourceIndexerFromPreviousSchemaFile**](mrmcreateresourceindexerfrompreviousschemafile.md) function
-   [**MrmDestroyIndexerAndMessages**](mrmdestroyindexerandmessages.md) function
-   [**MrmDumpPriFile**](mrmdumpprifile.md) function
-   [**MrmDumpPriFileInMemory**](mrmdumpprifileinmemory.md) function
-   [**MrmDumpPriDataInMemory**](mrmdumppridatainmemory.md) function
-   [**MrmFreeMemory**](mrmfreememory.md) function
-   [**MrmIndexEmbeddedData**](mrmindexembeddeddata.md) function
-   [**MrmIndexFile**](mrmindexfile.md) function
-   [**MrmIndexFileAutoQualifiers**](mrmindexfileautoqualifiers.md) function
-   [**MrmIndexResourceContainerAutoQualifiers**](mrmindexresourcecontainerautoqualifiers.md) function
-   [**MrmIndexString**](mrmindexstring.md) function
-   [**MrmPeekResourceIndexerMessages**](mrmpeekresourceindexermessages.md) function

**Structures**

-   [**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md) structure
-   [**MrmResourceIndexerMessage**](mrmresourceindexermessage.md) structure

**Enumerations**

-   [**MrmDumpType**](mrmdumptype.md) enumeration
-   [**MrmPackagingMode**](mrmpackagingmode.md) enumeration
-   [**MrmPackagingOptions**](mrmpackagingoptions.md) enumeration
-   [**MrmPlatformVersion**](mrmplatformversion.md) enumeration
-   [**MrmResourceIndexerMessageSeverity**](mrmresourceindexermessageseverity.md) enumeration

 

 
