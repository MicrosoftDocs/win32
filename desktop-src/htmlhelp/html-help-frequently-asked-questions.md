---
title: HTML Help Frequently Asked Questions
description: This topic contains the answers to several frequently asked questions.
ms.assetid: A91DE043-3A0E-440c-BB80-2EF960E57C0F
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTML Help Frequently Asked Questions

This topic contains the answers to several frequently asked questions.

-   [How can I use Visual Basic with HTML Help?](#how-can-i-use-visual-basic-with-html-help)
-   [What files need to be distributed with my compiled HTML Help (.chm) file?](#what-files-need-to-be-distributed-with-my-compiled-html-help-chm-file)
-   [If there's an old version of Microsoft Internet Explorer on the user's computer, will the HTML Help ActiveX control (Hhctrl.ocx) be updated?](#if-theres-an-old-version-of-microsoft-internet-explorer-on-the-users-computer-will-the-html-help-activex-control-hhctrlocx-be-updated)
-   [What if my user wants to use a browser other than Internet Explorer?](#what-if-my-user-wants-to-use-a-browser-other-than-internet-explorer)
-   [Why can't I read the text in my Help file when using Windows 98?](#why-cant-i-read-the-text-in-my-help-file-when-using-windows-98)
-   [Why is there an "X" where my graphic should be in my help topic?](#why-is-there-an-x-where-my-graphic-should-be-in-my-help-topic)
-   [Why does HTML Help Workshop sometimes "hang" when I edit the \[ALIAS\] and \[MAP\] sections?](#why-does-html-help-workshop-sometimes-hang-when-i-edit-the-alias-and-map-sections)
-   [If I compile my HTML Help project using HTML Help Workshop, are all my internal links tested during compilation?](#if-i-compile-my-html-help-project-using-html-help-workshop-are-all-my-internal-links-tested-during-compilation)
-   [I get the following message when I try to run my recently compiled HTML Help project:](#i-get-the-following-message-when-i-try-to-run-my-recently-compiled-html-help-project)
-   [Why don't my graphics print when I print all topics under a heading?](#why-dont-my-graphics-print-when-i-print-all-topics-under-a-heading)
-   [Is there a registry key that enables me to find out if HTML Help is set up on a computer?](#is-there-a-registry-key-that-enables-me-to-find-out-if-html-help-is-set-up-on-a-computer)
-   [It has been mentioned that you will implement an interface called **IHHWindow** that will offer Visual Basic Scripting Edition developers a more natural programming interface. When will this be implemented?](#it-has-been-mentioned-that-you-will-implement-an-interface-called-ihhwindow-that-will-offer-visual-basic-scripting-edition-developers-a-more-natural-programming-interface-when-will-this-be-implemented)
-   [I'm using Microsoft Internet Explorer 3.x on a Windows 95 operating system. When I try to look at the help for HTML Help Workshop, I don't see anything. What's wrong?](#im-using-microsoft-internet-explorer-3x-on-a-windows-95-operating-system-when-i-try-to-look-at-the-help-for-html-help-workshop-i-dont-see-anything-whats-wrong)
-   [How are full-text search hits ranked?](#how-are-full-text-search-hits-ranked)
-   [I need to put an older version of Hhctrl.ocx on my machine. How do I install an older version successfully?](#i-need-to-put-an-older-version-of-hhctrlocx-on-my-machine-how-do-i-install-an-older-version-successfully)
-   [On the Search tab in a compiled help file there is a **Match similar words** check box. What does this option do?](#on-the-search-tab-in-a-compiled-help-file-there-is-a-match-similar-words-check-box-what-does-this-option-do)
-   [How do I link from a WinHelp topic to an HTML Help topic?](#how-do-i-link-from-a-winhelp-topic-to-an-html-help-topic)
-   [What files make up the HTML Help client? Where are they installed? Are they registered?](#what-files-make-up-the-html-help-client-where-are-they-installed-are-they-registered)
-   [What HTML Help functionality do I lose if I use Microsoft Internet Explorer 3.02 instead of later versions?](#what-html-help-functionality-do-i-lose-if-i-use-microsoft-internet-explorer-302-instead-of-later-versions)
-   [What backwards compatibility can I count on as new versions of HTML Help are released? Will my compiled help files work with new versions of the Help Viewer? Can I create compiled help files with new versions of the Workshop that will work with older versions of the Help Viewer?](#what-backwards-compatibility-can-i-count-on-as-new-versions-of-html-help-are-released-will-my-compiled-help-files-work-with-new-versions-of-the-help-viewer-can-i-create-compiled-help-files-with-new-versions-of-the-workshop-that-will-work-with-older-versions-of-the-help-viewer)
-   [What's the best source of documentation for HTML Help?](#whats-the-best-source-of-documentation-for-html-help)
-   [Is HTML Help always going to be free on the Web?](#is-html-help-always-going-to-be-free-on-the-web)
-   [Do I need Microsoft Internet Explorer to use HTML Help?](#do-i-need-microsoft-internet-explorer-to-use-html-help)
-   [What HTML Help functionality do I lose if I use Microsoft Internet Explorer 3.0 instead of later versions?](#what-html-help-functionality-do-i-lose-if-i-use-microsoft-internet-explorer-30-instead-of-later-versions)
-   [Using WinHelp I could create a formatted pop-up window. How can I do this in HTML Help?](#using-winhelp-i-could-create-a-formatted-pop-up-window-how-can-i-do-this-in-html-help)
-   [Is it possible to open a specific topic from the Hh.exe command line?](#is-it-possible-to-open-a-specific-topic-from-the-hhexe-command-line)
-   [How can I make the HTML Help window remain even though the calling process has been terminated?](#how-can-i-make-the-html-help-window-remain-even-though-the-calling-process-has-been-terminated)
-   [We tried to implement embedded window help, but kept getting crashes in Hh.exe. Is there a workaround?](#we-tried-to-implement-embedded-window-help-but-kept-getting-crashes-in-hhexe-is-there-a-workaround)

## How can I use Visual Basic with HTML Help?

There are several Microsoft Knowledge Base articles about using Visual Basic with HTML Help. The following is a partial list of available topics with article ID numbers:

-   How to Use HTML Help API in a Visual Basic 5.0 Application (Q183434)
-   How to Create Context-Sensitive HTML Help in a Visual Basic Application (Q 189086)

To locate one of the above topics, on the [microsoft knowledge base search page](/isapi/gosupport.asp?target=/support/c.asp?pr=chs&fr=0)![non-msdn online link](images/leave-site.gif), select the **Specific article ID number** option, and then type the ID number in the box. To see all of the articles related to HTML Help, search the Microsoft Knowledge Base for the phrase "html AND help."

## What files need to be distributed with my compiled HTML Help (.chm) file?

The HTML Help Installation and Update package (Hhupd.exe), your compiled help file, and if Internet Explorer is not already set up on the user's computer, Microsoft Internet Explorer (version 3.02 or later). Hhupd.exe can be found on your local drive, in the HTML Help Workshop\\redist directory. You can find out more about redistributing Microsoft Internet Explorer at [http:/ /www.microsoft.com/windows/ieak/en/default.asp](/isapi/gomscom.asp?target=/windows/ieak/en/default.asp)![non-msdn online link](images/leave-site.gif).

## If there's an old version of Microsoft Internet Explorer on the user's computer, will the HTML Help ActiveX control (Hhctrl.ocx) be updated?

Yes.

## What if my user wants to use a browser other than Internet Explorer?

They can continue to use any browser they want. However, the HTML Help Java Applet, which is supported across browsers, only works with a subset of the navigation features supported by the HTML Help ActiveX control. The applet supports:

-   Table of contents
-   Index
-   Related Topics

## Why can't I read the text in my Help file when using Windows 98?

If Windows 98 is configured to use the high contrast black color scheme an end user may not be able to read the text in Windows Help. The background will blend closely with the color of the font. An end user can fix this problem in the following way: Go to the **Control Panel**, **Internet**, Click **General**, **Accessibility**, and then click the **Ignore Colors Specified on Web pages**.

Help authors can help prevent this problem by not shipping a style sheet (.css file) or in line styles where the background color is defined as white.

## Why is there an "X" where my graphic should be in my help topic?

This usually means that your graphics file cannot be found. Check the path.

## Why does HTML Help Workshop sometimes "hang" when I edit the \[ALIAS\] and \[MAP\] sections?

There is a bug that makes the editing of these sections very unstable. If you have trouble editing them, use Notepad (Notepad.exe) or another text editor to open your project (.hhp) file, and then edit the source.

## If I compile my HTML Help project using HTML Help Workshop, are all my internal links tested during compilation?

The compiler will pull in topics referred to by HREF and SRC attributes. It will report any missing files in the error log. Referring to files through script or Dynamic HTML (DHTML) tags is not supported and those files will have to be manually added to the \[FILES\] section of your project (.hhp) file.

## I get the following message when I try to run my recently compiled HTML Help project:

Internet Explorer cannot open the Internet site mk:MSITStore:c:\\&lt;path&gt;\\&lt;project.chm&gt;::/default.htm.

An unexpected error has occurred.

What does it mean?

HTML Help instructed Microsoft Internet Explorer to look for a particular file within the compiled help title, and it couldn't be found. You should have received an error when you compiled your project (.hhp) file warning that a file was missing, or that no default file was specified.

If you don't specify a default file in your project options, HTML Help will attempt to open Default.htm (but there shouldn't be a path). Please note that default files must be set for each window you define. If you are not using window definitions, then the default file must be specified in the **Project Options** dialog box.

## Why don't my graphics print when I print all topics under a heading?

This is a known bug. It will be fixed in a later release.

## Is there a registry key that enables me to find out if HTML Help is set up on a computer?

You can look for the CLSID of Hhctrl.ocx in **HKEY\_CLASSES\_ROOT\\CLSID**. The CLSID is: **52A2AAAE-085D-4187-97EA-8C30DB990436**. This key is registered by the system during setup.

> [!Note]  
> The CLSID given here was introduced in Windows XP SP1. For earlier versions of Windows, the CLSID of the HTML Help ActiveX Control is ADB880A6-D8FF-11CF-9377-00AA003B7A11.

 

## It has been mentioned that you will implement an interface called **IHHWindow** that will offer Visual Basic Scripting Edition developers a more natural programming interface. When will this be implemented?

This work has been delayed until the next major release of HTML Help (2.0) which will be COM+ based.

## I'm using Microsoft Internet Explorer 3.x on a Windows 95 operating system. When I try to look at the help for HTML Help Workshop, I don't see anything. What's wrong?

You need to install DCOM95 version 1.2 for Windows 95. You can download it from [http://www.microsoft.com/cominfo/dcom95/](/isapi/gomscom.asp?target=/cominfo/dcom95/)![non-msdn online link](images/leave-site.gif).

## How are full-text search hits ranked?

For a single compiled help (.chm) file, results are ranked by the number of hits within each topic (the number of times the search term is found within a topic). For a multiple-title help system, it's a little more complex.

If you have, for example, 5 compiled help files in your help system, the top-ranking hit from each title will be listed, followed by the second-ranking hit for each title, followed by the third, and so on. This process is followed until all the results are returned, or a total of 500 topic titles are listed.

## I need to put an older version of Hhctrl.ocx on my machine. How do I install an older version successfully?

It is not easy to remove Hhctrl.ocx because it is considered to be a system component. To remove your current version of Hhctrl.ocx and install an older version, type the following from the command line:

1.  cd %windir%\\system (win95) or cd %windir%\\system32 (NT4)
2.  regsvr32 -u hhctrl.ocx
3.  del hhctrl.ocx
4.  del itss.dll
5.  del itircl.dll

Now that you have removed the newer run-time components, you can get the older components by installing either an older version of HTML Help Workshop, or an older version of the HTML Help Installation and Update package (Hhupd.exe).

## On the Search tab in a compiled help file there is a **Match similar words** check box. What does this option do?

The **Match similar words** option uses Western-language rules for determining suffixes and finds all occurrences of a given word that include common suffixes. For example, a search for "run" will find words such as "run," running," and "runner." The word "runtime" will not be found.

## How do I link from a WinHelp topic to an HTML Help topic?

Here's the correct syntax for jumping from a WinHelp topic link to a topic in a compiled HTML Help (.chm) file: **!execfile(hh.exe, filename.chm::/topic.htm)**

where **!execfile** is the name of the WinHelp macro, hh.exe is the HTML Help executable program, filename.chm is the name of the compiled help file, and topic.htm is the name of the HTML topic file.

## What files make up the HTML Help client? Where are they installed? Are they registered?

The client files are:

-   %windir%\\HH.EXE (not registered)
-   %windir%\\system(32)\\HHCTRL.OCX (registered)
-   %windir%\\system(32)\\ITSS.DLL (registered)
-   %windir%\\system(32)\\ITIRCL.DLL (registered)

## What HTML Help functionality do I lose if I use Microsoft Internet Explorer 3.02 instead of later versions?

Full-text search highlighting.

## What backwards compatibility can I count on as new versions of HTML Help are released? Will my compiled help files work with new versions of the Help Viewer? Can I create compiled help files with new versions of the Workshop that will work with older versions of the Help Viewer?

Your compiled help files will work with new versions of the Help Viewer and you will be able to create compiled help files with new versions of the workshop that will work with older versions of the Help Viewer.

## What's the best source of documentation for HTML Help?

Aside from the general information contained on this Web site, the best source of documentation for HTML Help is the help that ships with HTML Help Workshop. Set up HTML Help Workshop, click the **Help** menu, and then click **Help Topics**.

The Microsoft Press book, the Official HTML Help Authoring Kit is also a good source of information. Updated companion files, information about how to set up the sample programs, and other late-breaking news about this book is available from the [microsoft press web site](http://www.microsoft.com/mspress/default.asp)![non-msdn online link](images/leave-site.gif).

## Is HTML Help always going to be free on the Web?

Yes, that's the plan.

## Do I need Microsoft Internet Explorer to use HTML Help?

The HTML Help ActiveX control requires that Internet Explorer be set up on a user's computer. HTML Help works with Microsoft Internet Explorer 3.02, but to take advantage of the full functionality of HTML Help, you should use the latest release of Internet Explorer. HTML Help does not require that you use Internet Explorer as your default browser.

## What HTML Help functionality do I lose if I use Microsoft Internet Explorer 3.0 instead of later versions?

Internet Explorer 4.0 or later is needed to get highlighting of full-text search terms, to get the auto-underlining and auto-expand/collapse of the table of contents, to be able to access compiled HTML Help (.chm) files over a Hypertext Transfer Protocol (HTTP) connection, and to be able to display some multimedia file types (such as AVI) within a compiled help file. In addition, anything authored on an HTML page that takes advantage of Dynamic HTML (DHTML) will work only with Internet Explorer 4.0 or later.

## Using WinHelp I could create a formatted pop-up window. How can I do this in HTML Help?

For now, HTML Help supports only simple text-only pop-up windows with no formatting. For more sophisticated formatting you need to use regular HTML-based topics instead of pop-up windows. Alternatively, you can continue to use WinHelp for your pop-up windows.

## Is it possible to open a specific topic from the Hh.exe command line?

Yes, try:

**hh mk:@MSITStore:/path/filename.chm::/path\\topicname.htm**

For example, with the compiled help file htmlhelp.chm, you can use:

**hh mk:@MSITStore:htmlhelp.chm::/api.htm**

**hh mk:@MSITStore:c:\\windows\\help\\htmlhelp.chm::/flash\\browse.htm**

## How can I make the HTML Help window remain even though the calling process has been terminated?

There is more than one way to solve this problem.

HTML Help is implemented as a DLL and is, therefore, always in-process. It terminates when the process that creates it terminates. To keep HTML Help around, the process that creates it must stay around.

One way to do this is to create an executable (.exe) file that calls HTML Help. This .exe file should stay running until HTML Help is closed by the user. You will also have to implement a method for communicating between this .exe file and the executable file of your program.

Another solution is to load your title under Hh.exe. If you WinExec your title, then the standard Windows file association code will load it using Hh.exe and it will remain running until the user closes Hh.exe.

## We tried to implement embedded window help, but kept getting crashes in Hh.exe. Is there a workaround?

There are several key limitations to using embedded windows. This is because an HTML Help window is not designed to be a child window of an application. Control over the appearance of the help window is somewhat limited, and painting/resizing of the window is unpredictable. In addition, you will have to run Hhctrl.ocx in single-threaded mode. The following topic explains the problem and its solution in detail:

-   Embedded windows: issues and workarounds (Q194116)

To locate the above topic, on the [microsoft knowledge base search page](/isapi/gosupport.asp?target=/support/c.asp?pr=chs&fr=0)![non-msdn online link](images/leave-site.gif), select the **Specific article ID number** option, and then type the ID number in the box. To see all of the articles related to HTML Help, search the Microsoft Knowledge Base for the phrase "html AND help."

 

 




