---
Description: Before the smart card subsystem can find a smart card, the smart card must be introduced to the system.
ms.assetid: 5b331d7d-9440-4e0d-a73b-48a2a556c31c
title: Introducing Smart Cards to the System
ms.topic: article
ms.date: 05/31/2018
---

# Introducing Smart Cards to the System

Before the [*smart card subsystem*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx) can find a [*smart card*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx), the smart card must be introduced to the system. This is typically done with a smart card setup tool provided by the card manufacturer. The tool could come as a program on a floppy disk (with the smart card), an ActiveX control available on a website, and so on.

The setup tool must provide the following pieces of information about the card:

-   Its [*ATR string*](https://msdn.microsoft.com/library/ms721532(v=VS.85).aspx), and an optional mask to use as an aid in identifying the card.
-   A list of smart card interfaces supported by the card.
-   A display name for the card, to be used in identifying the card to the user. In most cases, the user will supply this to the setup tool.
-   The [*primary service provider*](https://msdn.microsoft.com/library/ms721603(v=VS.85).aspx) associated with the card (optional), to be used when accessing the card through COM interfaces.

To simplify setup tools, and to ensure the integrity of the [*smart card database*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx), the smart card subsystem provides the following two functions. [**SCardIntroduceCardType**](/windows/desktop/api/Winscard/nf-winscard-scardintroducecardtypea) introduces a smart card into the database and [**SCardForgetCardType**](/windows/desktop/api/Winscard/nf-winscard-scardforgetcardtypea) removes it from the database.

 

 



