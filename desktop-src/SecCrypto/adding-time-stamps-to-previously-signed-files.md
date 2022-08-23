---
description: Time stamps are normally included when a file is signed using SignTool with the -t option.
ms.assetid: ca22d055-dc34-447c-991b-27ff21ca3afc
title: Adding Time Stamps to Previously Signed Files
ms.topic: article
ms.date: 05/31/2018
---

# Adding Time Stamps to Previously Signed Files

Time stamps are normally included when a file is signed using SignTool with the `-t` option. In addition, time stamps can be added to files that were signed without a time stamp. The following command adds a time stamp to a previously signed file:

```console
signtool timestamp -t https://timestamp.digicert.com MyControl.exe
```

> [!Note]  
> The file to be time stamped must have previously been signed.

 

For more information about SignTool, see [SignTool](signtool.md).

 

 



