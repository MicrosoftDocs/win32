---
title: Nesting in Native Mode
description: The following list describes what can be contained in a group that exists in a native-mode domain.
ms.assetid: 7992ef2d-9dcf-4087-b09a-35235b23e499
ms.tgt_platform: multiple
keywords:
- Nesting in Native Mode AD
ms.topic: article
ms.date: 05/31/2018
---

# Nesting in Native Mode

The following list describes what can be contained in a group that exists in a native-mode domain. This same list also applies to distribution groups in mixed-mode domains. The scope of the group determines these containment rules.

-   A universal group can contain other universal groups, global groups and accounts from any domain within the forest in which this Universal Group resides.
-   A global group can contain other global groups and accounts from the same domain that the group belongs to. A global group cannot contain any universal groups, or any global group or account from another domain.
-   A domain local group can contain universal groups, global groups and accounts from any domain or forest. A domain local group can also contain other domain local groups from the same domain that the group belongs to. A domain local group cannot contain other domain local groups from any other domain or forest.

 

 




