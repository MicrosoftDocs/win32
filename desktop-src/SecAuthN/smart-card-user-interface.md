---
description: The smart card user interface (UI) is a single common dialog box that lets the user specify or search for a smart card to open (that is, connect to and use in an application).
ms.assetid: a64a617a-b2ae-471f-a88f-a73f0fc3a791
title: Smart Card User Interface
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card User Interface

The smart card [*user interface*](../secgloss/u-gly.md) (UI) is a single [*common dialog box*](../secgloss/s-gly.md) that lets the user specify or search for a smart card to open (that is, connect to and use in an application).

Following are two ways you can use the common dialog box. Both assume that the dialog box UI will be displayed. For more information, see [**OPENCARDNAME**](/windows/desktop/api/Winscard/ns-winscard-opencardnamea).

**To select a smart card to open**

1.  Declare a variable of type **OPENCARDNAME**.
2.  Provide enough information in the common dialog box to narrow the search for a smart card that the calling application is looking for. This includes specifying **lpstrGroupNames**, **lpstrCardNames**, and **rgguidInterfaces**. This also includes specifying a preferred share mode and protocol to use when the common dialog box connects to the card by using the **dwShareMode** and **dwPreferredProtocols** members of the [**OPENCARDNAME**](/windows/desktop/api/Winscard/ns-winscard-opencardnamea) structure.
3.  Call the [**GetOpenCardName**](/windows/desktop/api/Winscard/nf-winscard-getopencardnamea) function to display the common dialog box to the user. A simple help information line will be displayed, and if one of the cards being requested is found, the card will be highlighted in the display. For multiple card name searches, the first reader that contains one of the preferred cards will be highlighted.
4.  The user then selects a card, clicks **OK**, and connects to the smart card.

**To search for a specific card**

1.  Declare a variable of type **OPENCARDNAME**.
2.  Provide enough information in the common dialog box to narrow the search for a smart card that the calling application is looking for. This includes specifying **lpstrGroupNames**, **lpstrCardNames**, and **rgguidInterfaces**.
3.  Create the **Connect**, **Check**, and **Disconnect** callback functions, and set the **lpfnConnect**, **lpfnCheck**, and **lpfnDisconnect** data members appropriately.
    > [!Note]  
    > All three functions and members must be available when using the common dialog box in this way.

     

4.  Call the [**GetOpenCardName**](/windows/desktop/api/Winscard/nf-winscard-getopencardnamea) common dialog box function.
5.  The common dialog box will then search for the requested cards. If a matching card name or [*ATR string*](../secgloss/a-gly.md) is found, the **Connect**, **Check**, and **Disconnect** callback functions will be called in sequence. If a card passes the **Check** routine (that is, the **Check** callback returns **TRUE**), this card is highlighted in the display to the user.
    > [!Note]  
    > If multiple card names are given, the first reader that contains one of the requested cards and passes the **Check** routine will be the selected card.

     

6.  If no matches are found, a common dialog box will appear.

 

 
