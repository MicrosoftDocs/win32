---
title: Adding About Information
description: The standard method for providing version and provider information within most applications that run on Windows platforms is the About menu selection item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 96a15e76-3918-45bd-b78c-b88297fa6cb9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- adding About information MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding About Information

The standard method for providing version and provider information within most applications that run on Windows platforms is the **About** menu selection item. MMC supports snap-in applications in providing this type of information. The information is displayed on a property page and is made available by using the [**ISnapinAbout**](isnapinabout.md) interface.

The snap-in About information is only displayed in the [Add/Remove Snap-in dialog box](add-remove-snap-in-dialog-box.md). Be aware that this information is not available to the user of a console file. Only the authors of saved console files can access the snap-in About information.

MMC also calls the snap-in [**ISnapinAbout**](isnapinabout.md) implementation to obtain custom folder images for the snap-in static node. If a snap-in does not implement **ISnapinAbout**, MMC uses default folder images instead. Be aware that snap-ins can also programmatically specify the static node's folder images when the static node is selected and the snap-in receives an [**MMCN\_EXPAND**](mmcn-expand.md) notification message. However, implementing **ISnapinAbout** is the recommended method for specifying the static folder images.

Methods belonging to [**ISnapinAbout**](isnapinabout.md) include [**GetSnapinDescription**](isnapinabout-getsnapindescription.md), which provides text for the snap-in description box. [**GetProvider**](isnapinabout-getprovider.md) handles the name of the provider, and [**GetSnapinVersion**](isnapinabout-getsnapinversion.md) obtains the snap-in version number. [**GetSnapinImage**](isnapinabout-getsnapinimage.md) gets the main icon for the About property page, and [**GetStaticFolderImage**](isnapinabout-getstaticfolderimage.md) gets the static folder images for the scope and result panes.

In the following procedure, be aware that {CLSID} and {snapinCLSID} indicate string representations of the specified CLSIDs. The strings must begin with an open brace ({) and end with a close brace (}).

**To add About information**

1.  Implement the [**ISnapinAbout**](isnapinabout.md) interface in the snap-in.
2.  Use a COM object other than the snap-in's primary object (the one that exposes the snap-in's [**IComponentData**](icomponentdata.md) interface) to expose the [**ISnapinAbout**](isnapinabout.md) interface. This is so that, for performance reasons, MMC is not required to create an instance of the entire snap-in to access its About information.
3.  Register the CLSID of this object under the HKEY\_CLASSES\_ROOT\\CLSID key in the {CLSID} subkey as an in-process server DLL. Also register an apartment threading model for the object. This allows the snap-in's [**ISnapinAbout**](isnapinabout.md) interface to be marshaled by COM to MMC.

    For more information about the HKEY\_CLASSES\_ROOT\\CLSID key, see [CLSID Key](_com_CLSID_Key). For more information and a code example, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

4.  Also register the CLSID of the object under the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID} key. Be aware that the {snapinCLSID} key is the string representation of the snap-in's CLSID. In the About named value of the {snapinCLSID} key, specify the string representation of the CLSID of the object. For more information about the SnapIns Key, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

 

 




