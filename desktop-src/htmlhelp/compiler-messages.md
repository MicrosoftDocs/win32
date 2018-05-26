---
title: Compiler Messages
description: Compiler Messages
ms.assetid: B44CDF75-8FEA-405d-9183-CF487CBFF2CF
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Compiler Messages

When you [compile a help project](to-compile-a-help-project-file.md), HTML Help Workshop notifies you if there are basic problems in the project files by creating compiler messages. You can [monitor these messages](monitoring-help-messages.md) to see whether any problems, such as missing links or graphics, exist in your help files.

HTML Help Workshop reports these compiler messages:

> [!Note]  
> A condition you should be aware of, which will probably not cause serious problems when you open your help file. Note error messages have a number range from 1000 through 2999. For example, a broken link causes this type of message: The file "c:\\htmlhelp\\httempex.htm" has a link to a non-existent file: "tmplstep.htm".

 

<dl> <dt>

<span id="Warning_"></span><span id="warning_"></span><span id="WARNING_"></span>**Warning** 
</dt> <dd>

A condition that results in a defective help file. Warning error messages have a number range from 3000 through 4999. For example, an invalid DLL causes this type of message: HHW4000: Warning: Unable to initialize for full-text search. The .dll may not be installed or is invalid.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error**
</dt> <dd>

A condition that prevents the help file from being built. Error messages have a number range from 5000 through 6999.

</dd> <dt>

<span id="Internal_Error"></span><span id="internal_error"></span><span id="INTERNAL_ERROR"></span>**Internal Error**
</dt> <dd>

An error caused by the HTML Help Workshop program. Internal Error messages have a number greater than 7000.

</dd> </dl>

> [!Note]  
> HTML Help Workshop can display up to 64K of messages on the screen in Microsoft Windows 95 and 1 MB in Windows 2000, but there is no practical limit to how many [compiler messages can be saved to a file](to-save-compiler-messages-to-a-file.md).

 

## Related topics

<dl> <dt>

[About Compiling a Help Project](compile-a-help-project.md)
</dt> </dl>

 

 




