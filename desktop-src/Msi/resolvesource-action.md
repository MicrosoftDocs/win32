---
description: The ResolveSource action determines the location of the source and sets the SourceDir property if the source has not been resolved yet.
ms.assetid: 6d6205a0-a870-4df2-922b-befea7e28a1a
title: ResolveSource Action
ms.topic: article
ms.date: 05/31/2018
---

# ResolveSource Action

The ResolveSource action determines the location of the source and sets the [**SourceDir**](sourcedir.md) property if the source has not been resolved yet.

## Sequence Restrictions

The ResolveSource action must come after the [CostInitialize action](costinitialize-action.md).

## ActionData Messages

There are no ActionData messages.

## Remarks

The ResolveSource action must be called before using the [**SourceDir**](sourcedir.md) property in any expression. It must also be called before attempting to retrieve the value of the **SourceDir** property using [**MsiGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msigetpropertya). The ResolveSource action should not be executed when the source is unavailable, as it may be when uninstalling the application.

## Related topics

<dl> <dt>

[Source Resiliency](source-resiliency.md)
</dt> </dl>

 

 



