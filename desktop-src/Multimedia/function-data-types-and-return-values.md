---
title: Function Data Types and Return Values
description: Function Data Types and Return Values
ms.assetid: a17ec8bb-4369-463f-8c67-11457a18595b
ms.topic: article
ms.date: 05/31/2018
---

# Function Data Types and Return Values

The AVIFile functions and macros use file and stream handlers implemented with OLE technology. The standard data type of an OLE function is **STDAPI**, and the function returns an **HRESULT** value (zero for success or an error otherwise). If a function returns a value other than an **HRESULT**, the type of the function's prototype has a slightly different syntax that embeds the return value type in parentheses following "STDAPI\_". For example, a function that returns a **LONG** data value uses **STDAPI\_(LONG)** in the prototype statement.

 

 




