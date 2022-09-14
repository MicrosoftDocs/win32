---
description: You can supply all of the information needed to configure Add/Remove Programs in Control Panel by setting the values of certain installer properties in your application's Windows Installer package.
ms.assetid: 2eb00fe5-e441-4fce-9623-81a089269a2b
title: Configuring Add/Remove Programs with Windows Installer
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Add/Remove Programs with Windows Installer

You can supply all of the information needed to configure Add/Remove Programs in Control Panel by setting the values of certain installer properties in your application's Windows Installer package. Setting these properties automatically writes the corresponding values into the registry. If the installer detects that the product is marked for complete removal, operations are automatically added to the script to remove the Add/Remove Programs folder in Control Panel information for the product.

If an application is not registered, it is not listed in Add/Remove Programs in Control Panel. For more information, see [Adding and Removing an Application and Leaving No Trace in the Registry](adding-and-removing-an-application-and-leaving-no-trace-in-the-registry.md).

Applications that have been installed in the per-user [installation context](installation-context.md) are displayed in the Add/Remove Programs of the current user. Applications that have been installed in the per-machine installation context are displayed in the Add/Remove Programs of all users. Applications that have not been installed per-machine, and have only been installed as per-user applications for users other than the current user, do not appear in the Add/Remove Programs of the current user.

Note that installation packages that use the [**LIMITUI**](limitui.md) property must also contain the [**ARPNOMODIFY**](arpnomodify.md). This is required for a user to obtain the correct behavior from Add/Remove Programs in Control Panel utility when attempting to configure a product.

The installer uses the following [public properties](public-properties.md) to manage Add/Remove Programs in Control Panel.


| Property name | Brief description of property | 
|---------------|-------------------------------|
| <a href="arpauthorizedcdfprefix.md"><strong>ARPAUTHORIZEDCDFPREFIX</strong></a> | URL of the update channel for the application. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arpcomments.md"><strong>ARPCOMMENTS</strong></a> | Provides Comments for the Add/Remove Programs in the Control Panel. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arpcontact.md"><strong>ARPCONTACT</strong></a> | Provides the Contact for Add/Remove Programs in the Control Panel. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arpinstalllocation.md"><strong>ARPINSTALLLOCATION</strong></a> | Fully qualified path to the application's primary folder. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arphelplink.md"><strong>ARPHELPLINK</strong></a> | Internet address, or URL, for technical support. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arphelptelephone.md"><strong>ARPHELPTELEPHONE</strong></a> | Technical support phone numbers. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arpnomodify.md"><strong>ARPNOMODIFY</strong></a> | Prevents display of a Change button for the product in Add/Remove Programs in the Control Panel.<blockquote><b>Note:</b> This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.</blockquote><br /> | 
| <a href="arpnoremove.md"><strong>ARPNOREMOVE</strong></a> | Prevents display of a Remove button for the product in the Add/Remove Programs in the Control Panel. The product can still be removed by selecting the Change button if the installation package has been authored with a user interface that provides product removal as an option.<blockquote><b>Note:</b> This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.</blockquote><br /> | 
| <a href="arpnorepair.md"><strong>ARPNOREPAIR</strong></a> | Disables the Repair button in the Add/Remove Programs in the Control Panel.<blockquote><b>Note:</b> This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.</blockquote><br /> | 
| <a href="arpproducticon.md"><strong>ARPPRODUCTICON</strong></a> | Identifies the icon displayed in Add/Remove Programs. If this property is not defined, Add/Remove Programs specifies the display icon. | 
| <a href="arpreadme.md"><strong>ARPREADME</strong></a> | Provides the ReadMe for Add/Remove Programs in Control Panel. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arpsize.md"><strong>ARPSIZE</strong></a> | Estimated size of the application in KB. | 
| <a href="arpsystemcomponent.md"><strong>ARPSYSTEMCOMPONENT</strong></a> | Prevents display of the application in the Programs List of the Add/Remove Programs in the Control Panel.<blockquote><b>Note:</b> This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.</blockquote><br /> | 
| <a href="arpurlinfoabout.md"><strong>ARPURLINFOABOUT</strong></a> | URL for application's home page. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 
| <a href="arpurlupdateinfo.md"><strong>ARPURLUPDATEINFO</strong></a> | URL for application update information. The value the installer writes under the <a href="uninstall-registry-key.md">Uninstall Registry Key</a>. | 


> [!Note]  
> For information regarding the Set Program and Defaults tool, refer to the section [Working with Set Program Access and Computer Defaults](/previous-versions//bb776877(v=vs.85)).

## Related topics

<dl> <dt>

[Uninstall Registry Key](uninstall-registry-key.md)
</dt> </dl>
