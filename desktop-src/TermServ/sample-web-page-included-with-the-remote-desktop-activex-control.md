---
title: Sample webpage included with the Remote Desktop ActiveX control
description: A sample webpage (Default.htm) is in the directory where Remote Desktop Web Connection is installed.
ms.assetid: 3137f58b-1aec-4bd6-a3b2-d1db6c8b96e4
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Sample webpage included with the Remote Desktop ActiveX control

When you install the Remote Desktop ActiveX control of Remote Desktop Web Connection, a sample webpage (Default.htm) is copied to the directory where Remote Desktop Web Connection is installed. This page can be run as-is or customized to fit the needs of a user or an organization.

The sample webpage must be installed on a web server running Windows Server and Internet Information Server 4.0 or later. Also, the browser on the client computer should be Internet Explorer version 4.0 or later. For more information, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

Default.htm is a default logon webpage that collects connection information from the user. The logon page contains one required field into which the user enters the name of the Remote Desktop Session Host (RD Session Host) server or remote computer to connect to. The logon page also includes optional fields for screen size and user logon information, including user name and domain.

After collecting the user data, Default.htm passes it to the Remote Desktop ActiveX control (Msrdp.ocx) to initiate a remote desktop session. The steps involved in initiating the session are the following:

1.  If necessary, Internet Explorer downloads the .cab file and installs it on the user's computer.
2.  The user enters the fully qualified domain name or IP address of the remote computer in the appropriate field.

    -   The user can optionally specify a screen size for the connection. If the user does not specify a screen size, the session opens in full-screen mode if the user is in a trusted URL security zone. Otherwise, the session opens in window mode.
    -   The user can optionally supply automatic logon information (user name, domain) for the remote session.

3.  When the user clicks the **Connect** button, Default.htm passes the user-supplied data as parameters to the Remote Desktop ActiveX control.
4.  The remote desktop opens in the browser window or in full-screen mode, as specified by the user.

When Default.htm opens for the first time using Internet Explorer, a dialog box appears giving the user the option to download the Remote Desktop ActiveX control (Msrdp.ocx). The dialog box appears under the following conditions:

-   The computer that accessed the webpage does not have a full installation of the Remote Desktop Web Connection client (or the Remote Desktop Services Advanced Client) with web support.
-   The installed version of the .cab file on the client computer is older than the version on the Default.htm webpage.

The size of the remote desktop session that appears in the browser window is the size specified in the Default.htm webpage. To change the screen size, the user must disconnect from the session, return to the Default.htm webpage and edit the connection information. If no screen size was specified, the session opens in the browser window in the default full-screen mode. At this resolution the remote desktop expands to match the full dimensions of the user's screen and the Internet Explorer browser toolbars and window frames do not display. As with the full Remote Desktop Connection client, the user can toggle between full-screen and window mode by pressing the full-screen mode [shortcut key](terminal-services-shortcut-keys.md) combination (CTRL+ALT+BREAK).

For security reasons, some options that are available in the Remote Desktop Services Connection Manager are restricted in the Remote Desktop ActiveX control to certain Internet Explorer URL security zones. Refer to [Providing for RDP Client Security](providing-for-rdp-client-security.md) for more information about these options and about specifying a program to run upon connection.

 

 




