---
title: Nesting in Mixed Mode
description: This topic lists the restrictions of security groups in a mixed-mode domain.
ms.assetid: e9f50485-db09-4d8c-8cf4-0ee7e78cb133
ms.tgt_platform: multiple
keywords:
- Nesting in Mixed Mode AD
ms.topic: article
ms.date: 05/31/2018
---

# Nesting in Mixed Mode

This topic lists the restrictions of security groups in a mixed-mode domain.

Security groups in a mixed-mode domain have the following restrictions:

-   Universal groups cannot be created in mixed-mode domains because the universal scope is supported only in Windows 2000 native-mode domains.
-   A global group can contain accounts from the same domain to which the group belongs. A global group cannot contain any universal groups, any global group, or an account from another domain.
-   A domain local group can contain global groups and accounts from any domain or forest. A domain local group cannot contain any other domain local group.

Be aware that distribution groups can be nested according to the nesting rules for native mode.

 

 




