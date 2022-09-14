---
title: Multiple-user guidelines
description: Guidelines for developing applications for multiple users in a Remote Desktop Services environment.
ms.assetid: c7acbedb-3bf2-4519-ab11-a50bf071e757
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Multiple-user guidelines

The following sections provide guidelines for developing applications for multiple users in a Remote Desktop Services environment.

## In this section

<dl> <dt>

[Application setup](application-setup-in-a-terminal-services-environment.md)
</dt> <dd>

Installing an application for a single user can create problems in a multiuser Remote Desktop Services environment.

</dd> <dt>

[Storing user-specific information](storing-user-specific-information.md)
</dt> <dd>

Applications should store user-specific information in user-specific locations, separately from global information that applies to all users.

</dd> <dt>

[Kernel object namespaces](kernel-object-namespaces.md)
</dt> <dd>

Remote Desktop Services uses multiple namespaces for kernel objects; a global namespace is used primarily by services in client/server applications.

</dd> <dt>

[IP addresses and computer names](ip-addresses-and-computer-names.md)
</dt> <dd>

It is not safe to assume that the computer name or the IP address assigned to the computer are associated with a single user because multiple users can be logged on simultaneously to a Remote Desktop Session Host (RD Session Host) server.

</dd> </dl>

As always, lock files and databases while making changes to prevent inadvertent loss of data.

Your application must not lock any run-time application files that are not per-user files. Locked run-time files can keep multiple instances of the application, or processes under the application such as wizards, from running. A good way to test which files are run-time application files is to track which files are installed by the application setup. Per-user files are rarely installed by setup; therefore, most files installed by setup are run-time application files.

 

 




