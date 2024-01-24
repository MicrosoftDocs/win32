---
description: Naming mailslots and putting messages into mailslots.
ms.assetid: 1ef522a4-9786-427c-a18a-ae1f0a05cc50
title: Mailslot Names
ms.topic: article
ms.date: 05/31/2018
---

# Mailslot Names

When a process creates a mailslot, the mailslot name must have the following form.

\\\\.\\mailslot\\\[*path*\\\]*name*

A mailslot name requires the following elements: two backslashes to begin the name, a period, a backslash following the period, the word "mailslot", and a trailing backslash. Names are not case sensitive. A mailslot name can be preceded by a path consisting of the names of one or more directories, separated by backslashes. For example, if a user expects messages on the subject of taxes from Bob, Pete, and Sue, the user's mailslot application might allow the user to create individual mailslots for each sender, as shown here:<dl> \\\\.\\mailslot\\taxes\\bobs\_comments  
\\\\.\\mailslot\\taxes\\petes\_comments  
\\\\.\\mailslot\\taxes\\sues\_comments  
</dl>

To put a message into a mailslot, a process opens a mailslot by name. To write to a mailslot on the local computer, a process can use a mailslot name that has the same form used for creating a mailslot. This situation, however, is relatively uncommon. More frequently, you would use the following form to write to a mailslot on a specific remote computer:

\\\\*ComputerName*\\mailslot\\\[*path*\\\]*name*

To put a message into every mailslot in the specified domain with a given name, use the following form:

\\\\*DomainName*\\mailslot\\\[*path*\\\]*name*

To put a message into every mailslot with a given name in the system's primary domain, use the following form:

\\\\\*\\mailslot\\\[*path*\\\]*name*

 

 



