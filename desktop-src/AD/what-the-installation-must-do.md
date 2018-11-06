---
title: What the Installation Must Do
description: New attributes referenced in Step 3 must be referred to by its OID because the new attribute name is not present in the schema cache at this point.
ms.assetid: 57da8740-7646-4ca9-ba8d-832e4f520b13
ms.tgt_platform: multiple
keywords:
- What the Installation Must Do AD
ms.topic: article
ms.date: 05/31/2018
---

# What the Installation Must Do

Applications that extend the schema, must apply updates as described in the following procedure.

**To apply updates when extending the schema**

1.  Add the new attributes.
2.  Add the new classes.
3.  Add the new attributes to classes.
4.  Trigger a cache reload.

New attributes referenced in Step 3 must be referred to by its OID because the new attribute name is not present in the schema cache at this point.

Step 4 is unnecessary if the extensions will not be used immediately; the extensions will appear in the schema cache in approximately 5 minutes, depending on system load. For more information about the schema cache and how to trigger a cache reload, see [Updating the Schema Cache](updating-the-schema-cache.md).

 

 




