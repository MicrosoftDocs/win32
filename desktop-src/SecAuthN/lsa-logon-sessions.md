---
description: A logon session is a computing session that begins when a user authentication is successful and ends when the user logs off of the system.
ms.assetid: 14f0f9e7-90ba-47d7-a8d5-06f9d2f1a7a1
title: LSA Logon Sessions
ms.topic: article
ms.date: 05/31/2018
---

# LSA Logon Sessions

A [*logon session*](../secgloss/l-gly.md) is a computing session that begins when a user authentication is successful and ends when the user logs off of the system.

When a user is successfully authenticated, the authentication package creates a logon session and returns information to the [*Local Security Authority*](../secgloss/l-gly.md) (LSA) that is used to create a [*token*](../secgloss/t-gly.md) for the new user. This token includes, among other things, a [*locally unique identifier*](../secgloss/l-gly.md) (LUID) for the logon session, called the [*logon Id*](../secgloss/l-gly.md).

When a token is created, the [*reference count*](../secgloss/r-gly.md) for the logon session is incremented. The reference count is also incremented whenever copies of the token are created for process creation, impersonation, or other uses. As token uses are completed and copies of the token are deleted, the reference count for the logon session is decremented. When the reference count reaches zero, the logon session is deleted.

> [!Note]  
> If authentication is not successful, the [*authentication package*](../secgloss/a-gly.md) should not create a logon session. If the authentication package must create a logon session before making a final determination about the validity of the user, and if authentication fails, the authentication package must delete the session.

 

 

 
