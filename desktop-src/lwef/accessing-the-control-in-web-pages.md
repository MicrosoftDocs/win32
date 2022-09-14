---
title: Accessing the Control in Web Pages
description: Accessing the Control in Web Pages
ms.assetid: 0c799c60-c81a-44ea-a9e0-1a385208528f
ms.topic: article
ms.date: 05/31/2018
---

# Accessing the Control in Web Pages

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

To access the Microsoft Agent services from a webpage, use the HTML &lt;OBJECT&gt; tag within the <HEAD> or &lt;BODY&gt; element of the page, specifying the Microsoft CLSID (class identifier) for the control. In addition, use a CODEBASE parameter to specify the location of the Microsoft Agent installation file and its version number.

If Microsoft Internet Explorer (version 3.02 or later) is installed on the system, but Microsoft Agent is not yet installed and the user accesses a webpage that has the &lt;OBJECT&gt; tag with the Agent CLSID, the browser will automatically attempt to download Agent from the Microsoft website. Then, the user will be asked whether to proceed with installation. For other browsers, contact the supplier for information regarding their support or third-party support for ActiveX controls.

The following example illustrates how to use the CODEBASE parameter to autodownload the English language version 2.0 of Microsoft Agent.

``` syntax
<OBJECT
classid="clsid: D45FD31B-5C6E-11D1-9EC1-00C04FD7081F"
CODEBASE = "#VERSION=2,0,0,0"
 id=Agent
>
</OBJECT>
```

Agent can also be installed from your own HTTP server or as part of an application's installation process. To support installation from your own HTTP server, you need to post the Microsoft Agent self-installing cabinet .Exe file and specify its URL in the CODEBASE tag.

``` syntax
<OBJECT
classid="clsid: D45FD31B-5C6E-11D1-9EC1-00C04FD7081F"
CODEBASE = "https://your server/msagent.exe#VERSION=2,0,0,0"
 id=Agent
>
</OBJECT>
```

To support automatic download of a Microsoft Agent language component from a webpage, include the language component's Object tag on the page before the Agent control Object tag:

``` syntax
<OBJECT width=0 height=0
CLASSID="CLSID: C348XXXX-A7F8-11D1-AA75-00C04FA34D72"
CODEBASE = "#VERSION=2,0,0,0">
</OBJECT>
```

where XXXX is replaced with a Language ID. For the languages currently supported, check the Microsoft Agent website.

-   The &lt;OBJECT&gt; tag for a language component must precede the &lt;OBJECT&gt; tag for the Microsoft Agent core component.
-   Multiple languages can be installed on the same client.
-   Before setting the [**LanguageID**](https://www.bing.com/search?q=**LanguageID**) of a character, we recommend that your script verify that the locale of the browser, available in the [**userLanguage**](https://www.bing.com/search?q=**userLanguage**) property, matches the language being set.

To support other language versions of Agent, you use another Object tag specifying the language component. However, be aware that attempting to install multiple languages at the same time may require the user to reboot. The Agent language components can be obtained from the Agent website using the same procedure as for the Agent core component. Distribution licensing for the language components are covered in the standard Agent distribution license.To begin using a character, you must load the character using the [**Load**](/previous-versions/visualstudio/foxpro/h1tx7zt1(v=vs.71)) method. A character can be loaded from the user's local storage or an HTTP server. For more information about the syntax for loading a character, see the **Load** method. Once the character has been successful loaded you can use the methods, properties, and events exposed by the Agent control to program the character. You can also use the methods, properties, and events exposed by your programming language and the browser to program the character; for example, to program its reaction to a button click. Consult the documentation for your browser to determine what features it exposes in its scripting model. For Microsoft Internet Explorer, see the Scripting Object Model, which is available in the ActiveX SDK.

Agent's services remain loaded only when there is at least one client application with a connection. This means that when a user moves between Agent-enabled webpages, Agent will shut down and any characters you loaded will disappear. To keep Agent running between pages (and thereby keep a character visible), create another client that remains loaded between page changes. For example, you can create an HTML frameset and declare an &lt;OBJECT&gt; tag for Agent in the parent frame. You can then script the pages you load into the child frame(s), to call into the parent's script. Alternatively, you can also include an &lt;OBJECT&gt; tag on each page you load into the child frame. In this case, remember that each page will be its own client. You may need to use the [**Activate**](/previous-versions/visualstudio/foxpro/01ayxx68(v=vs.71)) method to set which client has control when the user interacts with the parent or child page.

 

 
