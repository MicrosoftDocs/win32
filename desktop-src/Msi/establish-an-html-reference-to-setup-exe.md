---
description: The final step is to place a reference to the Setup.exe on the hypothetical MySetup webpage (MySetup.html) described in A URL Based Windows Installer Installation Example.
ms.assetid: 1a040bd9-242b-4528-858a-2218099acbe3
title: Establish an HTML Reference to Setup.exe
ms.topic: article
ms.date: 05/31/2018
---

# Establish an HTML Reference to Setup.exe

The final step is to place a reference to the Setup.exe on the hypothetical MySetup webpage (MySetup.html) described in [A URL Based Windows Installer Installation Example](a-url-based-windows-installer-installation-example.md). Use the following HTML script:

``` syntax
[MySetup Installation](https://www.blueyonderairlines.com/Products/MySetup/setup.exe)
```

Clicking on the "MySetup Installation" link presents users with the option to save or run from that location. If the user selects run from that location, the Setup.exe upgrades the version of Windows Installer on the computer, if necessary, verifies the digital signature on the installer package, and installs the package on their computer.

This completes the example.

 

 



