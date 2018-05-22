---
title: Chaining Multiple Third-Party DLLs
description: It is important to recognize that Microsoft DHCP Server stops searching for additional third-party DLLs once a DLL has been successfully loaded.
ms.assetid: '782dd73a-7f32-4001-859b-21379f1e80d4'
keywords: ["Server API DHCP , chaining DLLs", "chaining DHCP", "Dynamic Host Configuration Protocol DHCP , tasks"]
---

# Chaining Multiple Third-Party DLLs

It is important to recognize that Microsoft DHCP Server stops searching for additional third-party DLLs once a DLL has been successfully loaded. To facilitate multiple simultaneous DLL calls from a given event, Microsoft DHCP Server passes the remaining list of third-party DLLs in its call to the [**DhcpServerCalloutEntry**](dhcpservercalloutentry.md) function, and expects the loaded third-party DLL to perform the necessary processing of additional third-party DLLs, and then return a cumulative set of requested calls.

For example, if one third-party DLL is registered for notification upon the arrival of a new DHCP packet, and another DLL is being called upon the deletion of a client and the sending of a packet, the [**DHCP\_CALLOUT\_TABLE**](dhcp-callout-table.md) function returned to Microsoft DHCP Server would include pointers in these members:

-   [**DhcpNewPktHook**](dhcpnewpkthook.md)
-   [**DhcpPktSendHook**](dhcppktsendhook.md)
-   [**DhcpDeleteClientHook**](dhcpdeleteclienthook.md)

If those were the only events for which notification was required, those three members of [**DHCP\_CALLOUT\_TABLE**](dhcp-callout-table.md) would contain function pointers to the appropriate third-party DLL, and the rest of the members would be **NULL**.

Another situation that third-party DLL developers must accommodate is notification of multiple third-party DLLs for the same event. This situation requires the initially loaded third-party DLL to maintain a table of its own — similar in functionality to the internal table maintained by Microsoft DHCP Server — that lists additional functions to be called upon notification of a given DHCP Server event. The initially loaded third-party DLL is expected to call all other third-party DLLs requesting notification for a given event, and then return their function call, as appropriate.

For example, three properly registered third-party DLLs have been developed to register for notification upon the arrival of a new DHCP packet. The initially loaded third-party DLL, firstDLL,is the only third-party DLL loaded by the Microsoft DHCP Server.

Upon loading, Microsoft DHCP Server provided information about the other two third-party DLLs, secondDLL and thirdDLL, and firstDLL was able to load them and retrieve their requested notification information.

Upon notification of the arrival of a new packet, that Microsoft DHCP Server provides by calling firstDLL's [**DhcpNewPktHook**](dhcpnewpkthook.md) function, firstDLL consults its table and finds that secondDLL and thirdDLL also require notification of the arrival of a new packet. Before returning to Microsoft DHCP Server, firstDLL can call the **DhcpNewPktHook** function for secondDLL and thirdDLL, and then return from its own function to Microsoft DHCP Server.

 

 




