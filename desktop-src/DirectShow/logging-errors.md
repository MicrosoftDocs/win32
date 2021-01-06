---
description: Logging Errors
ms.assetid: 690ea91b-5bc0-45f0-8354-ec625709f7bd
title: Logging Errors
ms.topic: article
ms.date: 05/31/2018
---

# Logging Errors

\[This API is not supported and may be altered or unavailable in the future.\]

[DirectShow Editing Services](directshow-editing-services.md) (DES) provides a built-in mechanism for logging errors that occur when loading, constructing, or rendering a DES project. This article presents a sample console application that loads an XML project file and attempts to render it. If an error occurs, the application prints an error message in the console window. The sample code presented in this article builds on the example given in [Loading and Previewing a Project](loading-and-previewing-a-project.md).

> [!Note]  
> Your application is not required to implement error logging. DES does not log errors unless you explicitly request it.

 

This article assumes that you understand COM client programming and the DES timeline model. In addition, you need to understand the basics of COM object programming. For information about timelines in DES, see [The Timeline Model](the-timeline-model.md).

This article contains the following sections.

-   [Overview of Error Logging](overview-of-error-logging.md)
-   [Creating an Error Logging Class](creating-an-error-logging-class.md)
-   [Implementing IAMErrorLog](implementing-iamerrorlog.md)
-   [Setting the Error Log](setting-the-error-log.md)
-   [DES Error Logging: Example Code](des-error-logging--example-code.md)

## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 



