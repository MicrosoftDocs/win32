---
description: An IME implements a feature called &\#0034;reconversion&\#0034;.
ms.assetid: 32b20872-7e5c-487e-99bb-9447ac3aebd4
title: Using Reconversion with an IME
ms.topic: article
ms.date: 05/31/2018
---

# Using Reconversion with an IME

An IME implements a feature called "reconversion". Normally the IMM determines the lists of candidates based only on entries typed by the user. Reconversion allows the IMM to determine one or more candidates based on the containing sentence (the context). The defined reconversion types are simple, normal, and enhanced.

Reconversion is useful when a user notices a composition error in a document. The user can select the error and choose reconversion from a menu. The IME uses the context to determine the best replacement. The application can use [**ImmSetCompositionString**](/windows/desktop/api/Imm/nf-imm-immsetcompositionstringa) to support reconversion.

## Related topics

<dl> <dt>

[Using Input Method Manager](using-input-method-manager.md)
</dt> </dl>

 

 



