---
description: With a connection-oriented context, the function's caller is responsible for formatting messages. The caller relies on the security package to authenticate connections and to ensure the integrity of specific parts of the message.
ms.assetid: 82c6b1aa-304c-47f9-8e0f-ad70a89772aa
title: Connection-Oriented Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Connection-Oriented Contexts

With a connection-oriented [*context*](/windows/desktop/SecGloss/c-gly), the function's caller is responsible for formatting messages. The caller relies on the [*security package*](/windows/desktop/SecGloss/s-gly) to authenticate connections and to ensure the integrity of specific parts of the message.

Most context options are available to connection-oriented contexts. These options include mutual authentication, replay detection, and sequence detection, as described in [Context Requirements](context-requirements.md).

A security package sets the SECPKG\_FLAG\_CONNECTION flag to indicate that it supports connection-oriented semantics.

 

 
