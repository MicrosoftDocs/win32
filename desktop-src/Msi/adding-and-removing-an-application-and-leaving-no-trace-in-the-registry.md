---
description: If an application must be registered, author the installation package as described in the section Adding and Removing Registry Keys on the Installation or Removal of Components.
ms.assetid: d2c6afde-cede-4ed1-ac1a-8ddb1bc73ec2
title: Adding and Removing an Application and Leaving No Trace in the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Adding and Removing an Application and Leaving No Trace in the Registry

If an application must be registered, author the installation package as described in the section [Adding and Removing Registry Keys on the Installation or Removal of Components](adding-or-removing-registry-keys-on-the-installation-or-removal-of-components.md). Registration is used by the installer for advertisement and by the Add or Remove Programs feature in Control Panel. If an application is not registered, it cannot be advertised, and is not listed in the Add or Remove Programs feature in Control Panel.

You can omit registering an application by removing the [RegisterProduct Action](registerproduct-action.md), [RegisterUser Action](registeruser-action.md), [PublishProduct Action](publishproduct-action.md), and [PublishFeatures Action](publishfeatures-action.md) from the [InstallExecuteSequence Table](installexecutesequence-table.md) and [AdvtExecuteSequence Table](advtexecutesequence-table.md). All of these actions must be removed, or some trace of the application may remain in the registry. Removing all of these actions prevents the application from being listed in the Add or Remove Programs feature in Control Panel, and prevents the advertisement of the application. Removing all of these actions also prevents the application from being registered with the Windows Installer configuration data. This means that you cannot remove, repair, or reinstall the application by using the Windows Installer [Command-Line Options](command-line-options.md), or the Windows Installer application programming interface (API).

To hide an application from the Add or Remove Programs feature in Control Panel and still be able to use the Windows Installer to manage an application, leave the registration actions in the sequence tables, and set the [**ARPSYSTEMCOMPONENT Property**](arpsystemcomponent.md) in the [Property Table](property-table.md) to 1 (one). The application does not appear in the Add or Remove Programs feature, but you can use the Windows Installer to install-on-demand, uninstall, repair, and reinstall the application.

 

 



