---
title: Identifiers
description: Identifiers can be up to 255 characters long, and must conform to C-style syntax.
ms.assetid: a802d92e-2116-4d7e-9a16-df3d889337a2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Identifiers

Identifiers can be up to 255 characters long, and must conform to C-style syntax. MIDL is case sensitive, but it generates type libraries that are case insensitive. It is therefore possible to define a user-defined type whose name differs from that of a built-in type only by case. User-defined type names (and member names) that differ only in case refer to the same type or member. Except for property accessor functions, it is invalid for two members of a type to have the same name, regardless of case.

 

 




