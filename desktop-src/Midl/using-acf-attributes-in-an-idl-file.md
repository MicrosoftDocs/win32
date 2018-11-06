---
title: Using ACF Attributes in an IDL File
description: You can use the /app\_config MIDL compiler option to specify binding handle attributes in the IDL file rather than in a separate ACF file.
ms.assetid: 3558e818-b39f-42a4-842f-05970296da0e
keywords:
- ACF MIDL , attributes, using ACF in IDL
- IDL MIDL , using ACF
ms.topic: article
ms.date: 05/31/2018
---

# Using ACF Attributes in an IDL File

You can use the /[**app\_config**](-app-config.md) MIDL compiler option to specify binding handle attributes in the IDL file rather than in a separate ACF file. Specifically, you can apply the [**auto\_handle**](auto-handle.md), [**implicit\_handle**](implicit-handle.md), and [**explicit\_handle**](explicit-handle.md) attributes to the header of an RPC interface in an IDL file. Consider using this option if your RPC application does not require other ACF attributes, and if you do not require strict OSF-DCE compatibility.

 

 




