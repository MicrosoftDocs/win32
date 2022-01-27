---
title: Prerequisites for Installing a Schema Extension
description: To modify the schema, ensure you have the following rights and are aware of the following information You must have sufficient rights to modify the schema.
ms.assetid: f7795eac-2b95-4b6c-a2f5-8728316059ab
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Prerequisites for Installing a Schema Extension

To modify the schema, ensure you have the following rights and are aware of the following information:

-   You must have sufficient rights to modify the schema. The schema contains all of the data definitions for Active Directory Domain Services for the entire enterprise. To update the schema, a user must be a member of the Schema Administrators group, or have been delegated the rights to update the schema.
-   You can only make schema changes at the schema master. For more information, see [Detecting the Schema Master](detecting-the-schema-master.md).
-   The schema master must be writable; that is, the safety interlock in the registry must be removed. For more information, see [Enabling Schema Changes at the Schema Master](enabling-schema-changes-at-the-schema-master.md).
