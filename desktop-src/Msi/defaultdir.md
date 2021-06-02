---
description: The DefaultDir data type is a text string containing either a valid Filename or a valid Identifier.
ms.assetid: c7c5eac1-3283-4878-9d0d-887f93fc7a35
title: DefaultDir
ms.topic: article
ms.date: 05/31/2018
---

# DefaultDir

The DefaultDir data type is a text string containing either a valid [Filename](filename.md) or a valid [Identifier](identifier.md). This is used only in the [Directory table](directory-table.md). It must be an identifier if the directory is a root directory. If the directory is a non-root, this value must be a filename or a filename:filename pair. Note that "." is allowed as a file name and has special meaning in the Directory table.

 

 



