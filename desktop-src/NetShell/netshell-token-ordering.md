---
title: NetShell Token Ordering
description: Tokens are equivalent to the command-line command a user executes within the helper context.
ms.assetid: '5aa4be89-ddcf-400d-83e0-9972c0d2dff8'
keywords: ["helper NetSh , implementing, token ordering", "token ordering NetSh", "NetShell NetSh , described, token ordering"]
---

# NetShell Token Ordering

Tokens are equivalent to the command-line command a user executes within the helper context.

When creating tokens, such as a table of [**CMD\_ENTRY**](cmd-entry.md) entries or [**TAG\_TYPE**](tag-type.md) entries, the order in which tokens are created is significant. If one token is a possible abbreviation of another token, the shorter token must come first. For example, if two fictional commands **start** and **startrunning** are tokens in a helper, the **start** token must be defined first. This constraint is a result of NetShell token abbreviation capabilities.

 

 




