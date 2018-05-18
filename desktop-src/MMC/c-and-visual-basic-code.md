---
title: C++ and Visual Basic Code
description: Provides test considerations that apply to both C++ and VB developers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '445220f0-38d2-440b-a91f-c7f3bcc27e1f'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["snap-in testing MMC , C++ and VB"]
---

# C++ and Visual Basic Code

The following considerations apply to both C++ and Visual Basic developers:

-   Publish your clipboard formats and node types to allow extensions to be written to your snap-in. For more information about gaining free exposure for your snap-in on the Microsoft website, send email to: snapreq@microsoft.com.
-   Do not change the node selected in the scope pane when your snap-in receives a selection or expand notification.
-   For Visual Basic developers: If you add a childless node, ensure that HasChildren is set to False so that the plus sign (+) is hidden in the console tree.

    For C++ developers: If you add a childless scope pane node, ensure that the SCOPEDATAITEM.cChildren member is set to 0 so that the plus sign is hidden in the console tree.

 

 




