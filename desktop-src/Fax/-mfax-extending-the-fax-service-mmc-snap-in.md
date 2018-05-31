---
Description: The fax service administration console application is a Microsoft Management Console snap-in component that the system administrator can use to manage the fax service.
ms.assetid: bab76c94-e69e-4de7-b793-5655356412c2
title: Extending the Fax Service MMC Snap-in
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extending the Fax Service MMC Snap-in

The fax service administration console application is a [Microsoft Management Console](http://msdn.microsoft.com/library/en-us/mmc/mmc/microsoft_management_console_start_page.asp) snap-in component that the system administrator can use to manage the fax service. The snap-in can operate as a stand-alone snap-in or as an extension to the Computer Management snap-in application.

Third-party vendors can extend the functionality of the fax service administration snap-in by writing Microsoft Management Console (MMC) extensions to specific node types in the snap-in namespace. Information about the node types is provided in the topic [MMC Snap-in Node Types](-mfax-mmc-snap-in-node-types.md).

For example, an fax service provider (FSP) that provides support for fax-over-Internet Protocol (FoIP) transmissions could write an MMC property sheet extension to extend the default **Device Properties** dialog box. The property sheet extension could include property pages to use when an administrator configures the properties of the FSPs FoIP devices. The administration console snap-in for the fax service provides information that lets the third-party extension know when to display the property pages and how to access the fax server.

For information about registering your snap-in, see [Registering and Unregistering a Snap-in](http://msdn.microsoft.com/library/en-us/mmc/mmc/registering_and_unregistering_a_snap_in.asp).

 

 



