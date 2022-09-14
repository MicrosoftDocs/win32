---
description: Explains the means by which an application or service provider can connect to a smart card by using the smart card subsystem.
ms.assetid: 27f8f25f-1883-4070-94a4-0d3c51032378
title: Accessing a Smart Card
ms.topic: article
ms.date: 05/31/2018
---

# Accessing a Smart Card

The [*smart card*](/windows/desktop/SecGloss/s-gly) subsystem provides several means for an application or [*service provider*](/windows/desktop/SecGloss/c-gly) to connect to a smart card:

-   An application can call [**SCardConnect**](/windows/desktop/api/Winscard/nf-winscard-scardconnecta) to connect to a card that resides in a given reader. This is the simplest way to establish communication with a smart card.
-   An application can search for a specific smart card within a given reader group. The application identifies the card by its display name, and specifies a list of readers in which the card may appear. The [*resource manager*](/windows/desktop/SecGloss/r-gly) searches the list of readers for any cards with an [*ATR string*](/windows/desktop/SecGloss/a-gly) that matches the named card, and returns status information to the application. The [*smart card subsystem*](/windows/desktop/SecGloss/s-gly) never puts up a GUI or interacts with the card beyond obtaining the ATR string. It does, however, supply sufficient information for the application or a common control to be able to walk the user through locating the desired card or card type. This results in mapping the request to a specific reader, to which further I/O is directed.
-   An application can request a list of cards supporting a given set of smart card interfaces. The application can then use the list in the previous case. This allows applications to connect to cards based on their capabilities, without regard to their names.

When an application looks for a card, it supplies an array of reader names in which to look. For each reader element in the array, the resource manager supplies the following information:

-   Whether the reader is available for use by this application.
-   Whether there is a card inserted into this reader, and if so, what its ATR string is.
-   Whether the card's ATR string matches any of the requested cards' ATR strings.

The application uses the returned information to apply further filters to the cards or to prompt the user to select the desired card. Note that one or more of the returned list of readers may be opened for exclusive use by other applications, so access to this list of readers is not guaranteed.

 

 
