---
title: Multilink and Callback Connections
description: For the first link in a multilink connection, the authentication service sets the RAS\_EAP\_FLAG\_FIRST\_LINK flag in the fFlags member of the PPP\_EAP\_INPUT structure.
ms.assetid: a6aee73b-43b2-43b4-a6f1-ac7b293c44ad
ms.topic: article
ms.date: 05/31/2018
---

# Multilink and Callback Connections

For the first link in a multilink connection, the authentication service sets the RAS\_EAP\_FLAG\_FIRST\_LINK flag in the **fFlags** member of the [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) structure. The authentication protocol can use the presence of this flag to determine whether to present a user interface specifically for the first link of a multilink connection.

If the connection is configured so that the server calls back the client computer, the RAS\_EAP\_FLAG\_FIRST\_LINK flag will not be set on the callback.

If the authentication protocol sets the **fSaveConnectionData** member of [**PPP\_EAP\_OUTPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_output) to **TRUE**, subsequent links in the multilink connection receive the new connection-specific data. In the case of user-specific data, however, the authentication protocol continues to get the original user-specific data even if it sets the **fSaveUserData** member of **PPP\_EAP\_OUTPUT** to **TRUE**.

The authentication protocol may use an [interactive user interface](interactive-user-interface.md) to collect data for a particular link of a multilink connection. In this case, the authentication service makes the resulting data available to the authentication protocol during subsequent links. However, this data is never saved to persistent storage.

 

 




