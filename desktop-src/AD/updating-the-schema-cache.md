---
title: Updating the Schema Cache
description: All information that is written to an Active Directory server is validated against the schema.
ms.assetid: 948f8ec5-7207-4566-bd79-60cdd54231bf
ms.tgt_platform: multiple
keywords:
- Updating the Schema Cache AD
ms.topic: article
ms.date: 05/31/2018
---

# Updating the Schema Cache

All information that is written to an Active Directory server is validated against the schema. The schema is held in memory on directory servers (domain controllers) for performance reasons. The in-memory version is updated automatically after the on-disk version has been updated. The automatic update occurs five minutes after the last change was applied; applying another change to the schema in the 5-minute window resets the timer for another 5 minutes. This behavior keeps the cache consistent, but can be confusing, because changes do not appear in the schema until the cache is updated, even though they were applied on disk.

To update the Active Directory schema cache after a schema update, or if you want to use the schema update for non-schema operations immediately, add the **schemaUpdateNow** attribute (it is an operational attribute) to the root DSE (blank DN) with value 1. A schema cache update will start immediately. The call is blocking. If the call returns with no error, the cache is updated and all schema updates are ready to be used. An error return indicates the cache update was unsuccessful. Applications that must use this feature should be designed to accommodate the blocking write, particularly in giving the user feedback, if the program or script executes interactively.

The following code example is a sample LDIFDE script that shows how to trigger a cache reload.

``` syntax
dn:
changetype: modify
add: schemaUpdateNow
schemaUpdateNow: 1
-
```

For more information about how to update the schema cache programmatically, see [Example Code for Updating the Schema Cache](example-code-for-updating-the-schema-cache.md).

 

 




