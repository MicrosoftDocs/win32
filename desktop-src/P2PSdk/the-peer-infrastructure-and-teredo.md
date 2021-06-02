---
description: A user can check the status of the Teredo interface from the command prompt by typing netsh interface teredo show state and examining the output.
ms.assetid: b6ac1708-fb8a-449b-b30f-c889688a4bac
title: The Peer Infrastructure and Teredo
ms.topic: article
ms.date: 05/31/2018
---

# The Peer Infrastructure and Teredo

A user can check the status of the [Teredo](https://msdn.microsoft.com/library/ms819742.aspx) interface from the command prompt by typing **netsh interface teredo show state** and examining the output. If the state is "offline", Teredo is not active, which prevents the user from connecting to other users via their Teredo addresses. It is possible Teredo may be offline because your firewall is disabled or does not support [IPv6](/previous-versions/windows/embedded/ms898970(v=msdn.10)).

 

 
