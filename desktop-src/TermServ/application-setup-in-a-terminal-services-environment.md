---
title: Application setup
description: Installing an application for a single user can create problems in a multiuser Remote Desktop Services environment.
ms.assetid: 3e60e95a-3580-48aa-a9f9-8fd899aa7fca
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Application setup

The automated setup procedure for many existing applications assumes that the application is being installed for a single user. In a multiuser Remote Desktop Services environment, this assumption can create the following problems:

-   If the setup procedure updates the registry and desktop environment for just one user, additional users must reinstall the entire package or an administrator must manually copy information from the registry and desktop of one user to the other users.
-   With some setup procedures, you can customize the application at installation time by excluding features. If the initial installer excludes part of the application, additional users must reinstall the application to get the excluded features.

To avoid these problems, setup procedures should use the following guidelines when installing an application on a Remote Desktop Session Host (RD Session Host) server:

-   Install applications into the default user environment common to all users. Before installing the application, execute the **change user /install** console command, and after installation is complete, execute the **change user /execute** console command. Use a Remote Desktop Services compatibility script for the installation.
-   Support user-specific customization through the use of user profiles. To do this, create an [Administrative Template File Format](/previous-versions/windows/desktop/Policy/administrative-template-file-format) so an administrator can configure the registry to indicate the features available to each user. Then, at run time, the application can enable or disable features depending on the settings in the current user's registry settings. The application can store the per user configuration in the **HKEY CURRENT USER** registry hive and let every user configure the application according to their preferences.

 

 