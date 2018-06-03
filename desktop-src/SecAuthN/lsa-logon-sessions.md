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

A [*logon session*](https://www.bing.com/search?q=*logon session*) is a computing session that begins when a user authentication is successful and ends when the user logs off of the system.

When a user is successfully authenticated, the authentication package creates a logon session and returns information to the [*Local Security Authority*](https://www.bing.com/search?q=*Local Security Authority*) (LSA) that is used to create a [*token*](https://www.bing.com/search?q=*token*) for the new user. This token includes, among other things, a [*locally unique identifier*](https://www.bing.com/search?q=*locally unique identifier*) (LUID) for the logon session, called the [*logon Id*](https://www.bing.com/search?q=*logon Id*).

When a token is created, the [*reference count*](https://www.bing.com/search?q=*reference count*) for the logon session is incremented. The reference count is also incremented whenever copies of the token are created for process creation, impersonation, or other uses. As token uses are completed and copies of the token are deleted, the reference count for the logon session is decremented. When the reference count reaches zero, the logon session is deleted.

> [!Note]  
> If authentication is not successful, the [*authentication package*](https://www.bing.com/search?q=*authentication package*) should not create a logon session. If the authentication package must create a logon session before making a final determination about the validity of the user, and if authentication fails, the authentication package must delete the session.

 

 

 



