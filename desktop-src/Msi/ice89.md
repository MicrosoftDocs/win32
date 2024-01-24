---
description: ICE89 validates that the value in the Progid\_Parent column in ProgId table is a valid foreign key into the ProgId column in ProgId table. Every ProgId parent should have a record in the ProgId table.
ms.assetid: 3f5c1720-d90f-4af7-9162-520b846efbb6
title: ICE89
ms.topic: article
ms.date: 05/31/2018
---

# ICE89

ICE89 validates that the value in the Progid\_Parent column in [ProgId table](progid-table.md) is a valid foreign key into the ProgId column in ProgId table. Every ProgId parent should have a record in the ProgId table.

## Result

ICE89 posts the following errors.



| ICE89 error                                                           | Description                                                                |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------|
| The ProgId\_Parent '\[1\]' in the ProgId table is not a valid ProgId. | There is a ProgId parent specified that is not listed in the ProgId table. |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



