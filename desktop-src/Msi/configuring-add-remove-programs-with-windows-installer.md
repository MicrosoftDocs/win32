---
Description: You can supply all of the information needed to configure Add/Remove Programs in Control Panel by setting the values of certain installer properties in your application's Windows Installer package.
ms.assetid: 2eb00fe5-e441-4fce-9623-81a089269a2b
title: Configuring Add/Remove Programs with Windows Installer
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Add/Remove Programs with Windows Installer

You can supply all of the information needed to configure Add/Remove Programs in Control Panel by setting the values of certain installer properties in your application's Windows Installer package. Setting these properties automatically writes the corresponding values into the registry. If the installer detects that the product is marked for complete removal, operations are automatically added to the script to remove the Add/Remove Programs folder in Control Panel information for the product.

If an application is not registered, it is not listed in Add/Remove Programs in Control Panel. For more information, see [Adding and Removing an Application and Leaving No Trace in the Registry](adding-and-removing-an-application-and-leaving-no-trace-in-the-registry.md).

Applications that have been installed in the per-user [installation context](installation-context.md) are displayed in the Add/Remove Programs of the current user. Applications that have been installed in the per-machine installation context are displayed in the Add/Remove Programs of all users. Applications that have not been installed per-machine, and have only been installed as per-user applications for users other than the current user, do not appear in the Add/Remove Programs of the current user.

Note that installation packages that use the [**LIMITUI**](limitui.md) property must also contain the [**ARPNOMODIFY**](arpnomodify.md). This is required for a user to obtain the correct behavior from Add/Remove Programs in Control Panel utility when attempting to configure a product.

The installer uses the following [public properties](public-properties.md) to manage Add/Remove Programs in Control Panel.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Brief description of property</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>ARPAUTHORIZEDCDFPREFIX</strong>](arpauthorizedcdfprefix.md)</td>
<td>URL of the update channel for the application. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="even">
<td>[<strong>ARPCOMMENTS</strong>](arpcomments.md)</td>
<td>Provides Comments for the Add/Remove Programs in the Control Panel. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="odd">
<td>[<strong>ARPCONTACT</strong>](arpcontact.md)</td>
<td>Provides the Contact for Add/Remove Programs in the Control Panel. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="even">
<td>[<strong>ARPINSTALLLOCATION</strong>](arpinstalllocation.md)</td>
<td>Fully qualified path to the application's primary folder. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="odd">
<td>[<strong>ARPHELPLINK</strong>](arphelplink.md)</td>
<td>Internet address, or URL, for technical support. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="even">
<td>[<strong>ARPHELPTELEPHONE</strong>](arphelptelephone.md)</td>
<td>Technical support phone numbers. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="odd">
<td>[<strong>ARPNOMODIFY</strong>](arpnomodify.md)</td>
<td>Prevents display of a Change button for the product in Add/Remove Programs in the Control Panel.
<blockquote>
[!Note]<br />
This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ARPNOREMOVE</strong>](arpnoremove.md)</td>
<td>Prevents display of a Remove button for the product in the Add/Remove Programs in the Control Panel. The product can still be removed by selecting the Change button if the installation package has been authored with a user interface that provides product removal as an option.
<blockquote>
[!Note]<br />
This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ARPNOREPAIR</strong>](arpnorepair.md)</td>
<td>Disables the Repair button in the Add/Remove Programs in the Control Panel.
<blockquote>
[!Note]<br />
This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ARPPRODUCTICON</strong>](arpproducticon.md)</td>
<td>Identifies the icon displayed in Add/Remove Programs. If this property is not defined, Add/Remove Programs specifies the display icon.</td>
</tr>
<tr class="odd">
<td>[<strong>ARPREADME</strong>](arpreadme.md)</td>
<td>Provides the ReadMe for Add/Remove Programs in Control Panel. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="even">
<td>[<strong>ARPSIZE</strong>](arpsize.md)</td>
<td>Estimated size of the application in kilobytes.</td>
</tr>
<tr class="odd">
<td>[<strong>ARPSYSTEMCOMPONENT</strong>](arpsystemcomponent.md)</td>
<td>Prevents display of the application in the Programs List of the Add/Remove Programs in the Control Panel.
<blockquote>
[!Note]<br />
This only affects the display in the ARP. The Windows Installer is still capable of repairing, installing-on-demand, and uninstalling applications through a command line or the programming interface.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ARPURLINFOABOUT</strong>](arpurlinfoabout.md)</td>
<td>URL for application's home page. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
<tr class="odd">
<td>[<strong>ARPURLUPDATEINFO</strong>](arpurlupdateinfo.md)</td>
<td>URL for application update information. The value the installer writes under the [Uninstall Registry Key](uninstall-registry-key.md).</td>
</tr>
</tbody>
</table>



 

> [!Note]  
> For information regarding the Set Program and Defaults tool, please refer to the section [Working with Set Program Access and Computer Defaults](Http://go.microsoft.com/fwlink/p/?linkid=83959).

 

## Related topics

<dl> <dt>

[Uninstall Registry Key](uninstall-registry-key.md)
</dt> </dl>

 

 




