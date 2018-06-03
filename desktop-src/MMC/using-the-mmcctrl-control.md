---
title: Using the MMCCtrl Control
description: To use the MMCCtrl control on a custom taskpad's DHTML page, embed the object using the object tag, placing it between the head and /head tags.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4223199-0c3f-4d62-8418-a19d180a963a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Using the MMCCtrl Control
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the MMCCtrl Control

To use the MMCCtrl control on a custom taskpad's DHTML page, embed the object using the object tag, placing it between the &lt;head&gt; and &lt;/head&gt; tags.


```C++
<head>
<object id="taskctrl"
    classid="CLSID:545AE700-50BF-11D1-9FE9-00600832DB4A">
</object>
</head>
```



When the MMCCtrl control is embedded as an object on the page, scripts can call methods on the control.

The following code example gets the title string by calling the GetTitle method on an MMCCtrl object with an ID of taskctrl.


```C++
var mszTaskpadTitle;
var hash = location.hash;
if (hash != "") {
    hash = hash.substr(1);
}
 
// Get the taskpad title.
mszTaskpadTitle = taskctrl.GetTitle (hash);
```



 

 




