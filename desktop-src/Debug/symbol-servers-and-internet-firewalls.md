---
description: Some systems use Internet firewalls or proxy servers that require authentication for all Internet traffic.
ms.assetid: b79e9a6f-2ffb-4ec0-ac2d-63e79ecfc26c
title: Symbol Server and Internet Firewalls
ms.topic: article
ms.date: 05/31/2018
---

# Symbol Server and Internet Firewalls

Some systems use Internet firewalls or proxy servers that require authentication for all Internet traffic. Early versions of the symbol server could not access symbols from the Internet unless the system used a firewall client that handled the authentication transparently.

Starting with Dbghelp 6.1, the symbol server supports proxy servers that require such authentication. The symbol server uses whatever server is configured as the default in the computer's LAN settings. To find this, open the **Internet Options** item in Control Panel, click the **Connections** tab and click **LAN Settings**. This can also be done from Internet Explorer by clicking **Internet Options** on the **Tools** menu. The symbol server has been tested on many brands of proxy servers using both basic and challenge-response methods of authentication.

To define a specific proxy server for symbol server to use, set the \_NT\_SYMBOL\_PROXY environment variable to the name (or IP address) of the proxy server, followed by the port number. Separate the two values with a colon. For example:

**set \_NT\_SYMBOL\_PROXY=***myproxyserver***:80**

When using the windbg debugger, configure your symbol path to point to the symbol store that you want to use. The one difference is that the system will display a dialog box in which you need to enter your user ID and password to pass to the proxy server. If you enter incorrect information, the dialog box will be redisplayed. If you click the **Cancel** button, the dialog box is dismissed and the symbol server will be disabled for use through the Internet.

When using the latest versions of cdb.exe or ntsd.exe, this functionality is turned off by default. However you can enable or disable this functionality using the !sym extension command as follows:

-   To turn on prompting for user ID and password: **!sym prompts**.
-   To turn off prompting for user ID and password: **!sym prompts off**.

If you turn on prompting, you will need to reload symbols with the .reload command.

The DbgHelp API has been expanded to support these changes. The [**SymbolServerSetOptions**](/previous-versions//ms680676(v=vs.85)) function supports the SSRVOPT\_PROXY option. If the data parameter is **NULL**, the default proxy defined in **Internet Options** is used. Otherwise a zero-terminated string is passed specifying the name and port number of the proxy server. The name and port are separated by a colon as follows: *myproxyserver*:80. The [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) function supports the SYMOPT\_NO\_PROMPTS option. This turns off all prompting for validation from the symbol server.

 

 
