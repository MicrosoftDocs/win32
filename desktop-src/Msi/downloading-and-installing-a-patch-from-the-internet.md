---
description: Microsoft Windows Installer accepts a Uniform Resource Locator (URL) as a valid source for a patch.
ms.assetid: 11a65123-a8bd-46d8-a416-4fc2f2f1e121
title: Downloading and Installing a Patch From the Internet
ms.topic: article
ms.date: 05/31/2018
---

# Downloading and Installing a Patch From the Internet

Microsoft Windows Installer accepts a Uniform Resource Locator (URL) as a valid source for a [patch](patch-packages.md). To install a patch located on a web server at https://MyWeb/MyPatch.msp, use the following command line:

**msiexec /p https://MyWeb/MyPatch.msp**

To avoid unexpected results, do not launch a patch by clicking the link on the webpage showing the patch file's URL. You can also install a patch by using a script like the following:


```VB
<SCRIPT LANGUAGE="VBScript"> 
<!-- 
Dim Installer
On Error Resume Next
set Installer=CreateObject("WindowsInstaller.Installer")
Installer.ApplyPatch "https://server/share/patch.msp", "", 0, "REINSTALL=ALL REINSTALLMODE=omus"
set Installer=Nothing
-->
</SCRIPT>
```



Note that because the [**Installer**](installer-object.md) object is not marked as [SafeForScripting](safeforscripting.md) on the user's computer, users need to adjust their browser security settings for the example to work correctly.

For more information, see [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md) and [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md).

## Related topics

<dl> <dt>

[Patch Packages](patch-packages.md)
</dt> <dt>

[Creating a Patch Package](creating-a-patch-package.md)
</dt> <dt>

[Patching Customized Applications](patching-customized-applications.md)
</dt> <dt>

[Downloading an Installation From the Internet](downloading-an-installation-from-the-internet.md)
</dt> </dl>

 

 



