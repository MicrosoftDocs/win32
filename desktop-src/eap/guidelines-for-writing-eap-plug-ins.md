---
title: Guidelines for Writing EAP DLLs
description: EAP DLLs or Plug-ins can be written to optimize their performance in different scenarios.
ms.assetid: 79b9bc54-6eb0-4e01-822e-af83fc475ec5
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Writing EAP DLLs

EAP DLLs or Plug-ins can be written to optimize their performance in different scenarios.

## General Guidelines

-   In order to create an encrypted connection, EAP plug-ins must generate encryption keys and return them through the Microsoft vendor-specific RADIUS Attributes MS-MPPE-Send-Keys and MS-MPPE-Recv-Keys. See the Remarks section in [**PPP\_EAP\_OUTPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_output) for more information.

## Wireless Guidelines

The following are guidelines and recommendations for writing an EAP Plug-in that supports authenticating machines in wireless (802.1X) scenarios. This section does not apply to VPN and Dial-up scenarios.

-   In order not to block unattended systems' execution, EAP plug-ins must not make any user interface calls.
-   The EAP Plug-in implementation of the machine authentication step must complete as quickly as possible so it does not hinder operating system startup.
    > [!Note]  
    > If your EAP protocol does not support machine authentication, it must check for the machine authentication flag, **RAS\_EAP\_FLAG\_MACHINE\_AUTH** used in the **fFlags** field in [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input), and return an error.

     

 

 




