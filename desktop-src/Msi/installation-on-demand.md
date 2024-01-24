---
description: With traditional installation technology, it is necessary to exit an application and rerun setup to perform an installation task.
ms.assetid: 94c3d5a8-a560-4a1d-b40e-7ebc92d659f3
title: Installation-On-Demand
ms.topic: article
ms.date: 05/31/2018
---

# Installation-On-Demand

With traditional installation technology, it is necessary to exit an application and rerun setup to perform an installation task. This commonly occurred when a user wanted a feature or product not chosen during the first run of setup. This often made the process of product configuration inefficient because it required the user to anticipate the functionality required before they ever used the product.

Installation-on-demand makes it possible to offer functionality to users and applications in the absence of the files themselves. This notion is known as advertisement. The Windows Installer has the capability of advertising functionality and to make installation-on-demand of application features or entire products possible. When a user or application activates an advertised feature or product, the installer proceeds with installation of the needed components. This shortens the configuration process because additional functionality can be accessed without having to exit and rerun another setup procedure.

When a product uses the installer, a user can choose at setup time which features or applications to install and which to advertise. Then if while running an application the user requests an advertised feature that has not yet been installed, the application calls the installer to enact a just-in-time feature level installation of the necessary files. If the user activates an advertised product that has not yet been installed, the operating system calls the installer to enact a just-in-time product level installation.

[Advertisement](advertisement.md) and installation-on-demand can also facilitate system management by enabling administrators to designate applications as required or optional for different groups of users. There are two types of advertising known as "assigning" and "publishing." If an administrator assigns an application to a group, then these users can install the application on-demand. If, however, the administrator publishes the application to the group, no entry points appear to these users and installation-on-demand is only activated if another application activates the published application.

 

 



