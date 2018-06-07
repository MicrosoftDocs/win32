---
Description: A logon session is a computing session that begins when a user authentication is successful and ends when the user logs off of the system.
ms.assetid: 14f0f9e7-90ba-47d7-a8d5-06f9d2f1a7a1
title: LSA Logon Sessions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LSA Logon Sessions

A [*logon session*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) is a computing session that begins when a user authentication is successful and ends when the user logs off of the system.

When a user is successfully authenticated, the authentication package creates a logon session and returns information to the [*Local Security Authority*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) (LSA) that is used to create a [*token*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f) for the new user. This token includes, among other things, a [*locally unique identifier*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) (LUID) for the logon session, called the [*logon Id*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f).

When a token is created, the [*reference count*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd) for the logon session is incremented. The reference count is also incremented whenever copies of the token are created for process creation, impersonation, or other uses. As token uses are completed and copies of the token are deleted, the reference count for the logon session is decremented. When the reference count reaches zero, the logon session is deleted.

> [!Note]  
> If authentication is not successful, the [*authentication package*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) should not create a logon session. If the authentication package must create a logon session before making a final determination about the validity of the user, and if authentication fails, the authentication package must delete the session.

 

 

 



