---
description: ICE09 validates that the permanent bit is set for every component marked for installation into the SystemFolder.
ms.assetid: b4e11d75-4214-49de-ac12-6f360771ad73
title: ICE09
ms.topic: article
ms.date: 05/31/2018
---

# ICE09

ICE09 validates that the permanent bit is set for every component marked for installation into the SystemFolder. ICE09 posts a warning because you should avoid installing non-permanent system components to the SystemFolder. To prevent this warning, set the Permanent bit in the Attributes column of the [Component table](component-table.md) for every component that is marked for installation into the SystemFolder. No validation is done if the database does not have a Component table.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



