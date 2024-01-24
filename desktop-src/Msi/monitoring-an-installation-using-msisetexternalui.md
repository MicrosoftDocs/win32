---
description: Package authors can monitor internal Windows Installer messages through the creation of an executable application that contains both a callback handler to receive the messages and functionality to initiate an installation.
ms.assetid: 0aa8a2d6-f519-4d87-a28f-a11cb546bff5
title: Monitoring an Installation Using MsiSetExternalUI
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring an Installation Using MsiSetExternalUI

Package authors can monitor internal Windows Installer messages through the creation of an executable application that contains both a callback handler to receive the messages and functionality to initiate an installation.

The callback handler conforms to the INSTALLUI\_HANDLER prototype, and a pointer to this callback handler is passed to [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia). Once the installation has been initiated by a call to [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta), installation messages are trapped by the callback handler and the package author can selectively display or ignore any or all of these messages.

For more information, see [Handling Progress Messages Using MsiSetExternalUI](handling-progress-messages-using-msisetexternalui.md), [Returning Values from an External User Interface Handler](returning-values-from-an-external-user-interface-handler.md), and [Parsing Windows Installer Messages](parsing-windows-installer-messages.md).

For more information about using a record-based external handler, see [Monitoring an Installation Using MsiSetExternalUIRecord](monitoring-an-installation-using-msisetexternaluirecord.md).

 

 



