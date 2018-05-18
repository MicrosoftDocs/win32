---
title: Adding HTML Help Support Implementation Details
description: Adding HTML Help Support Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1c79e2ce-3b4a-4977-a3ef-65517fcae735'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["adding HTML Help support implementation details MMC"]
---

# Adding HTML Help Support: Implementation Details

**To add HTML Help support**

1.  Implement the [**ISnapinHelp2**](isnapinhelp2.md) interface. Be aware that the snap-in's primary object, the one registered with the snap-in class ID (**CLSID**), should expose this interface.

    In the snap-in implementation of the [**GetHelpTopic**](isnapinhelp2-gethelptopic.md) method, specify the address of the null-terminated Unicode string that contains the path of the compiled Help file (.chm) for the snap-in.

    Be aware that for MMC to merge a snap-in's HTML Help file into the HTML Help collection file for the current console, the Help file must be compiled with the **Create a binary TOC** check box selected. This creates a binary contents file for the Help file.

2.  If the snap-in HTML Help file links to other Help files, implement the [**ISnapinHelp2::GetLinkedTopics**](isnapinhelp2-getlinkedtopics.md) method to specify the names and locations of these files.
3.  Handle the [**MMCN\_CONTEXTHELP**](mmcn-contexthelp.md) notification, which is sent when the user requests Help about a selected item by pressing the F1 key or clicking the Help button. In the notification handler for **MMCN\_CONTEXTHELP**, call the [**IDisplayHelp::ShowTopic**](idisplayhelp-showtopic.md) method to display the Help topic for the particular context. For property page Help topics, call [**MMCPropertyHelp**](mmcpropertyhelp.md).

## Related topics

<dl> <dt>

[Adding HTML Help Support: Interfaces](adding-html-help-support-interfaces.md)
</dt> </dl>

 

 




