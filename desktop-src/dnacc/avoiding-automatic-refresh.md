---
Description: Microsoft Corporation
ms.assetid: c1a4c1ef-9078-4495-a084-17922c1cfb3c
title: Avoiding Automatic Refresh
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Avoiding Automatic Refresh

Microsoft Corporation

September 2003

**Summary**: Describes an alternative to automatic page refresh in HTML. Automatic page refresh can confuse users with cognitive disabilities when a page reloads without the user's request. This article provides you with instructions on how to apply explicit manual control of page refreshing. (2 printed pages)

-   [Introduction](#introduction)
    -   [How Automatic Refresh Works](#how-automatic-refresh-works)
-   [Full Control Script](#full-control-script)
-   [Conclusion](#conclusion)
-   [Related Resources](#related-resources)

## Introduction

Checkpoint 7.4 in the W3C Web Content Authoring Guide recommends avoiding automatic periodic refresh for the following reason. When certain assistive technology products, such as screen readers, encounter a page that reloads itself without user input, the screen reader re-reads the entire page to the user on every reload.

This can confuse the user with cognitive disabilities who has not requested a page refresh.

### How Automatic Refresh Works

Automatic refreshing is typically done in one of two ways:

-   **HTML Header Code**. The following markup code in the header of the HTML document provides automatic page refresh ("600" is the number of seconds between automatic reloads of the document).

    &lt;meta http-equiv="refresh" content="600"&gt;

    > [!Note]  
    > Avoid this technique whenever possible because it does not give the user any control over the refresh rate.

     

-   **Script Using Timer(s)**. This is becoming a more common technique when the author wants to periodically refresh an image, but not the entire page. It is often set up to give the user no control over the refresh rate or to allow the user to select one of several refresh intervals.

## Full Control Script

You can give full control back to users by either providing a button that allows them to manually refresh the page or by providing a range of refresh timing options that include manual refresh or refresh on demand using a script with a timer

The following code shows how to provide a button that enables the user to manually reload the page. Many elements support this technique.

``` syntax
<html>
<body>
   <img id="TrafficPhoto" src="http://webapp.metrokc.gov/trafficcamdata/current-10.jpg">
   <br>
   <button onclick="top.location.reload();">Update Image</button>
</body>
</html>
```

## Conclusion

By using the techniques described in this article, you provide users with cognitive disabilities the means to control automatic page refreshing and thereby significantly enrich their computing experience.

## Related Resources

To get additional suggestions for web content design standards for page refresh, see the [W3C Web Content Authoring Guide, checkpoint 7.4](http://go.microsoft.com/fwlink/p/?linkid=208744), at the W3C Recommendation website.

 

 



