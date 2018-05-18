---
title: Creating a Cabinet File
description: Creating a cabinet file is optional; however, it is useful for deploying your troubleshooting pack because they are self-contained and require no installation. They can be deployed onto Web sites, network shares, or copied on USB keys.
ms.assetid: '401da37b-8616-4e2f-9668-a46667ee9bf3'
---

# Creating a Cabinet File

Creating a cabinet file is optional; however, it is useful for deploying your troubleshooting pack because they are self-contained and require no installation. They can be deployed onto Web sites, network shares, or copied on USB keys. Use the .diagcab file name extension for the cabinet file. The .diagcab file name extension is a registered file name extension that can be executed by WTP.

To create a DIAGCAB file, use the Makecab.exe or Cabarc.exe tool. For details, see [Microsoft Cabinet Format](http://go.microsoft.com/fwlink/p/?linkid=139747). The makecab.exe tool is located in the %Windir%\\System32 folder.

You should sign the cabinet file so if it is downloaded from the Web, the user knows that it came from a trusted source. To sign the cabinet file, use the [**Signtool.exe**](https://msdn.microsoft.com/library/windows/desktop/aa387764) tool included in the \\Bin folder of the Windows SDK. For an example on its usage, see [Signing the Security Catalog](signing-the-security-catalog.md).

 

 




