---
title: Merging Help Files at Run Time
description: Merging Help Files at Run Time
ms.assetid: DCEA8057-3DCA-4df9-A2F4-48A4C38044BC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Merging Help Files at Run Time

When you merge help files, information from the index and full-text search of multiple compiled help (.chm) files is combined at run time. A unified index and full-text search information appears in the Navigation pane of the Help Viewer.

To combine the tables of contents from multiple help files, you need to [link to the contents files](creating-links-from-one-contents-file-to-another.md) that need to be merged.

This is a very useful feature when you need to [merge multiple help files](to-merge-multiple-help-files-at-run-time.md) that are designed as components of a larger help system. For example, the Professional edition of a software product might contain four programs, each with a separate help file; while the Student edition of the same product might contain only two programs and related help files.

When a help author creates a project file that specifies which files to merge at run time, the help compiler will find and merge only those files on a user's computer.

There are special considerations when [linking between merged help files](linking-between-merged-help-files.md).

## Related topics

<dl> <dt>

[About Managing Large Document Sets](manage-large-document-sets.md)
</dt> </dl>

 

 




