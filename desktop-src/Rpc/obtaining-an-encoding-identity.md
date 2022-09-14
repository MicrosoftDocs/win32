---
title: Obtaining an Encoding Identity
description: An application that is decoding encoded data can obtain the identity of the routine used to encode the data, prior to calling a routine to decode it. The MesInqProcEncodingId routine provides this identity.
ms.assetid: 53cbd6c5-b267-4ff1-a45b-7e22093f41a5
keywords:
- Remote Procedure Call RPC , tasks, obtaining encoding identity
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining an Encoding Identity

An application that is decoding encoded data can obtain the identity of the routine used to encode the data, prior to calling a routine to decode it. The [**MesInqProcEncodingId**](/windows/desktop/api/Midles/nf-midles-mesinqprocencodingid) routine provides this identity.

Each procedure in an interface is assigned an integer identification number, called a *procedure identifier* or a *proc ID*, by the MIDL compiler. Numbering begins with zero. The RPC run-time libraries are not involved in translating the procedure ID into an actual procedure call. Given a proc ID, your application must provide a means of calling the correct procedure. Typically, application developers use a series of **if** statements, or (when using C/C++) a **switch** statement for this purpose.

 

 




