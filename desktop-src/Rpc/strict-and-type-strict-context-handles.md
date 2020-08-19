---
title: Strict and Type Strict Context Handles
description: Use the strict\_context\_handle attribute for all context handles.
ms.assetid: 2483aa76-0814-4f63-9c38-0aa050d73772
ms.topic: article
ms.date: 05/31/2018
---

# Strict and Type Strict Context Handles

Use the [**strict\_context\_handle**](/windows/desktop/Midl/strict-context-handle) attribute for all context handles. By default, a context handle is not associated with an interface, which means a context handle can be created on one interface, then passed to another. This is an easy attack, and many RPC servers fail to prevent it.

If two interfaces coexist in the same process, an attacker can open a context handle on one interface, and pass it to another, which may trip over the unexpected data. Many developers believe their software is the only interface in a process, but very often that is not the case, because both the system and many third-party components use RPC internally, and those interfaces can create context handles. When the [**strict\_context\_handle**](/windows/desktop/Midl/strict-context-handle) attribute is used, the RPC run time ensures that a context created on one interface can be passed as an argument only to methods of that interface.

In situations where an application is developed for Windows Vista, the use of [**type\_strict\_context\_handle**](/windows/desktop/Midl/type-strict-context-handle) is available and recommended. Context handles are not associated with a specific type by default. When multiple types of context handles are used in the same process, it is possible for a malicious client to pass a context handle in place of another to produce undesirable results. The use of **type\_strict\_context\_handle** allows applications to enforce context handle type consistency and prevent any mismatched context handle type usage.

 

 