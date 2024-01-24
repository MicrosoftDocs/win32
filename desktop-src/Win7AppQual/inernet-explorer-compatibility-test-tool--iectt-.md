---
description: Internet Explorer Compatibility Test Tool (IECTT)
ms.assetid: 11169540-555A-48A9-A4CD-535D5765C005
title: Internet Explorer Compatibility Test Tool (IECTT)
ms.topic: article
ms.date: 05/31/2018
---

# Internet Explorer Compatibility Test Tool (IECTT)

The Internet Explorer Compatibility Test Tool (IECTT) is a component of the [Microsoft Application Compatibility Toolkit](/windows-hardware/get-started/adk-install). This tool can help you diagnose issues in your web applications by displaying issues in real time and optionally uploading the results to an ACT database. The results include details about possible compatibility issues and links for more information about each compatibility issue. IECTT also enables you to exclude issues and modify available attributes.

## To open IECTT

1.  Install the [Microsoft Application Compatibility Toolkit](/windows-hardware/get-started/adk-install).
2.  Click **Start**, point to **Programs**, point to **Microsoft Application Compatibility Toolkit 5.6**, point to **Developer and Tester Tools**, and then click **Internet Explorer Compatibility Test Tool**.

The following sections describe common IECTT scenarios.

## View Issues in Real Time

You can locate and view your web-based issues in real time, while you are testing your websites and web applications against Windows Internet Explorer 7 and Windows Internet Explorer 8. After you complete your testing, you can view your results in the **Live Data** screen of the IECTT.

## Upload Issues to Your ACT Database

You can upload your web-based issues to the ACT database, which processes the information and enables you to view your results on the **Analyze** screen of the Application Compatibility Manager.

## Collect Your Compatibility Data

You can collect your website and web application-related compatibility data by using the IECTT tool with either Internet Explorer 7 or Internet Explorer 8.
**To collect your compatibility data**

1.  Close all of your active Windows Internet Explorer windows.
2.  In IECTT, on the **Internet Explorer Compatibility Test Tool** toolbar, click **Enable**.
3.  Open an Internet Explorer 7 or Internet Explorer 8 window.

    A message appears and states that compatibility evaluation logging is turned on.

4.  Visit the websites or web applications that are required for use by your organization. As you visit each site, the IECTT tool displays, in real-time, your potential compatibility issues.
5.  On the **Internet Explorer Compatibility Test Tool** toolbar, click **Disable** when you are done.

    The compatibility logging process finishes and stops.

## Filter Your Issue Results

You can filter any of your IECTT results by object name, by issue type, or by both.

**To filter your issue results**

1.  On the **Internet Explorer Compatibility Test Tool** screen, click **Filter**.

    The **Issues Filter** dialog box appears.

2.  Enter the name of the object that you intend to view in the **Enter the name of the object to view issues for** box.

For more information about this tool and other developers tools, see [What is the Internet Explorer Compatibility Test Tool?](/previous-versions/windows/it-pro/windows-7/cc721989(v=ws.10)) in the MSDN Library and the [Application Compatibility Logging in IE8](/archive/blogs/ie/application-compatibility-logging-in-ie8) blog post.

## Related topics

<dl> <dt>

[Tools for Debugging Web Applications and Add-Ons](tools-for-debugging-web-applications-and-add-ons.md)
</dt> </dl>

 

 
