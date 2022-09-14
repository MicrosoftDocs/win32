---
description: When an SSP/AP security package is functioning as an authentication package, it is loaded into the process space of the Local Security Authority (LSA) and is said to be in LSA mode.
ms.assetid: ff4e61be-dbaa-4cfa-8c72-43e99fe1c3cb
title: LSA Mode vs. User Mode
ms.topic: article
ms.date: 05/31/2018
---

# LSA Mode vs. User Mode

When an SSP/AP [*security package*](../secgloss/s-gly.md) is functioning as an [*authentication package*](../secgloss/a-gly.md), it is loaded into the process space of the [*Local Security Authority*](../secgloss/l-gly.md) (LSA) and is said to be in LSA mode. Logon applications access authentication package functionality using the [LSA Logon Functions](authentication-functions.md). Developers can use LSA support functions available only to LSA-mode security packages to implement more sophisticated authentication packages than previously supported.

When a [*security package*](../secgloss/s-gly.md) provides security services to a client/server application, it is loaded into the client and server processes and is said to be in user mode. Client/server applications access the security package's security support services using Microsoft [*Security Support Provider Interface*](../secgloss/s-gly.md) (SSPI).

LSA support for SSP/APs includes functions that the LSA-mode and user-mode instances of a security package can use to communicate. Additionally, the user-mode instance of a security package can delegate selected requests for information to the LSA-mode instance of the package.

For details about how security packages are initialized for each mode, see [LSA-mode Initialization](lsa-mode-initialization.md) and [User-mode Initialization](user-mode-initialization.md).

 

 
