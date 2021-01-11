---
description: When you provide a preview, the following guidelines should be followed.
title: Preview Handler Guidelines
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 3538cc5d-afb6-4d43-b527-6c6e1d773b41
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Preview Handler Guidelines

When you provide a preview, the following guidelines should be followed.

-   A preview should contain minimal UI—it is simply a preview. It should display only the file content. It should not display dialogs, splash screens, toolbars, or task panes. The reading pane will commonly be used in conjunction with search to quickly identify a file. Anything that clutters the reading pane or otherwise detracts from file content or causes delays in preview display should be avoided.
-   The preview should allow the user to navigate in the document. The user should also be able to select and copy text.
-   The preview should not be memory-intensive, should consume minimal resources, and should have a fast startup time.
-   All script and macros in the file being previewed should be blocked from running for security and privacy purposes.
-   The preview should support keyboard accelerators for navigation and selection as supported by the application. It should also display a context menu when right-clicked.
-   When a file is displayed as a preview, the preview should not lock the file itself. A file can be previewed and opened in its associated application at the same time.

## Related topics

<dl> <dt>

[Preview Handlers and Shell Preview Host](preview-handlers.md)
</dt> <dt>

[Building Preview Handlers](building-preview-handlers.md)
</dt> </dl>

 

 



