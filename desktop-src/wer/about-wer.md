---
title: About WER
description: Windows Error Reporting (WER) is a flexible event-based feedback infrastructure designed to gather information about the hardware and software problems that Windows can detect, report the information to Microsoft, and provide users with any available solutions. For information about the improvements to WER, see What's New in WER.
ms.assetid: d26b3d2a-51cf-41d9-936b-f1b45778ea61
keywords:
- Windows error reporting Windows Error Reporting , about
ms.topic: article
ms.date: 05/31/2018
---

# About WER

Windows Error Reporting (WER) is a flexible event-based feedback infrastructure designed to gather information about the hardware and software problems that Windows can detect, report the information to Microsoft, and provide users with any available solutions. For information about the improvements to WER, see [What's New in WER](what-s-new-in-wer.md).

Beginning with Windows Vista, Windows provides crash, no response, and kernel fault error reporting by default without requiring changes to your application. Applications instead use the WER API to generate error reports for application-specific issues that are not related to crashes, non-responses, or kernel faults.

To generate error reports for application-specific issues, the application must create a short description of the problem using a few basic pieces of information called *report parameters*. Report parameters include information such as the application name, application version, module name, module version, and error code. The combination of these report parameters describes a unique problem.

When WER checks for a solution, it communicates with the WER server at Microsoft by first asking if the problem is already known. The server responds in one of the following ways:

-   If the problem is known and there is a solution, the server sends the solution to the client computer and WER displays this information to the user.
-   If the problem is being investigated, the server may send a response that indicates the status. If the developer needs more information to solve the problem, the server requests additional information from WER and WER asks the user for permission to send this information.
-   If the problem is not known, the server creates an issue for a developer to investigate and sends WER a response that indicates the status.

Using this process, WER gathers more information if needed or sends a solution to the user when available. On Windows Vista, the user can go to **Problem Reports and Solutions** at any time to view available solutions, check whether new solutions are available, or manage their other WER reports and settings. On Windows 7, the **Problem Reports and Solutions** is now called the **Action Center**. Click **Start** and enter "view" in **Search programs and files** and then select **View all problem reports**, **View reliability history**, or **View solutions to problems**.

## Related topics

<dl> <dt>

[Windows Error Reporting](windows-error-reporting.md)
</dt> </dl>

 

 




