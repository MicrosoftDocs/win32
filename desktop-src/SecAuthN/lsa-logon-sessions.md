---
Description: 'A logon session is a computing session that begins when a user authentication is successful and ends when the user logs off of the system.'
ms.assetid: '14f0f9e7-90ba-47d7-a8d5-06f9d2f1a7a1'
title: LSA Logon Sessions
---

# LSA Logon Sessions

A [*logon session*](security.l_gly#-security-logon-session-gly) is a computing session that begins when a user authentication is successful and ends when the user logs off of the system.

When a user is successfully authenticated, the authentication package creates a logon session and returns information to the [*Local Security Authority*](security.l_gly#-security-local-security-authority-gly) (LSA) that is used to create a [*token*](security.t_gly#-security-token-gly) for the new user. This token includes, among other things, a [*locally unique identifier*](security.l_gly#-security-locally-unique-identifier-gly) (LUID) for the logon session, called the [*logon Id*](security.l_gly#-security-logon-identifier-gly).

When a token is created, the [*reference count*](security.r_gly#-security-reference-count-gly) for the logon session is incremented. The reference count is also incremented whenever copies of the token are created for process creation, impersonation, or other uses. As token uses are completed and copies of the token are deleted, the reference count for the logon session is decremented. When the reference count reaches zero, the logon session is deleted.

> [!Note]  
> If authentication is not successful, the [*authentication package*](security.a_gly#-security-authentication-package-gly) should not create a logon session. If the authentication package must create a logon session before making a final determination about the validity of the user, and if authentication fails, the authentication package must delete the session.

 

 

 



