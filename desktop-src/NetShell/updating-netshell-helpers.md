---
title: Updating NetShell Helpers
description: After a helper command has been implemented and released, updated versions should avoid changing the original syntax of the command in order to prevent errors.
ms.assetid: 47dde8e2-36e4-4c9e-9910-e62e962b9c71
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Updating NetShell Helpers

After a helper command has been implemented and released, updated versions should avoid changing the original syntax of the command in order to prevent errors. For example, deleting or renaming the **dump** command's tag will cause a dump script to fail. However, extending the name of a command or tag would not cause failure since abbreviations are acceptable.

Changing the syntax of a command can also cause a command to be interpreted differently between different releases of a helper. Specifically, tags should not be reordered. For example, if the original version of a command's syntax is "show object \[name=\]&lt;string&gt; \[index=\]&lt;integer&gt;", an updated release should not switch the tags to "show object \[index=\]&lt;integer&gt; \[name=\]&lt;string&gt;". Doing so will cause users familiar with the old syntax to make errors, and will break existing scripts.

 

 




