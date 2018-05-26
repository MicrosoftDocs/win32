---
title: About Working with KLinks
description: About Working with KLinks
ms.assetid: A9923007-5A33-4353-8B15-3502F6956EA2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Working with KLinks

Keyword links (KLinks), are based on keywords that you add to your HTML files. When a user clicks a button or link that is associated with a KLink keyword, a **Topics Found** dialog box appears displaying the titles of all the topics that contain the keyword. You can use a KLink to jump to topics in the same or other help files. KLink keywords also appear in the index.

KLinks are automatically updated as keywords are added to or deleted from HTML files. As you author topics that contain these keywords, the topics are added to the **Topics Found** dialog box.

KLinks also enable you to specify jumps to topics in help files that won't be on a user's hard disk or a Web site until some future time. You might, for example, plan to distribute an updated help file that contains more topics but uses the same keywords as the earlier version.

When creating KLinks, first you add keywords to the HTML files that are the target for the link. Then you add the KLink object to the topic files you want to link to that target. For example, add the keyword "fonts" to several HTML files. Then add the KLink object with "fonts" specified in the keyword search to a file you want to link to those files. The keyword will appear in the index and in the **Topics Found** dialog box. You can also specify that the [target list appears on a pop-up menu](to-have-alink-or-klink-target-topics-appear-on-a-pop-up-menu.md) instead of in the **Topics Found** dialog box. For detailed information about KLinks, see the [HTML Help ActiveX control reference](klink.md).

## Related topics

<dl> <dt>

[Work with Klinks](working-with-klinks.md)
</dt> </dl>

 

 




