---
description: All authentication settings are made through the Internet Services Manager.
ms.assetid: 9b118120-f0cb-4973-b537-dd3d12a7a6d5
ms.tgt_platform: multiple
title: Configuring IIS 5.0 and Later for WMI ASP Scripting
ms.topic: article
ms.date: 05/31/2018
---

# Configuring IIS 5.0 and Later for WMI ASP Scripting

All authentication settings are made through the Internet Services Manager.

When configuring Internet Information Server (IIS) 5.0 and IIS 6.0 security for WMI ASP scripts, consider the following issues:

-   [Authentication level](#authentication-level)

    You can configure at the server, directory, or file level.

-   [Authentication setting](#authentication-setting)

    You can set authentication to Anonymous, Integrated Windows, or both.

-   [Protection](#protection)

    You can set the ASP to run in-process (low protection), or out-of-process by using Dllhost.exe (medium or high protection).

## Authentication Level

For added security, you can configure the authentication at the directory or file level.

If authentication is set at the server level, all subsequent directories and files adhere to the server authentication unless explicitly altered at the directory or file level. You can create a directory structure to contain all WMI ASP scripts where HTML pages and ASPs specific to WMI can be configured independently from the rest of the server. Perform the following procedure to change the authentication level of a server, directory, or file.

**To set the authentication at any level**

1.  In Control Panel, double-click **Administrative Tools**, and then double-click the IIS snap-in.

2.  Locate the ASP page icon, and then open the properties for the level to set, which can be server, directory, or file.

    > [!Note]  
    > Authentication settings are located on either the **Directory Security** or **File Security** tab of the **Properties**sheet.

     

## Authentication Setting

For WMI ASP scripts, the combination of Anonymous authentication turned off (unchecked), and Integrated Windows authentication turned on (checked) provides greater opportunity to set security. To use NT LAN Manager (NTLM), Passport, or Digest IIS authentication settings, you must turn on the remote enable privileges, because the user is treated as a network identity and logged remotely. The remote enable setting is not required for Anonymous and Basic authentication. However, the system is much less secure when you are using Anonymous and Basic authentication.

If Anonymous authentication is used with or without Integrated Windows authentication, the most secure approach is to use a logon that requires a user to enter a username and password. The default logon is the IIS identity, but a logon can be created by using specific permissions suited for the WMI ASP Scripts that can be used as the account for the anonymous or guest connections.

If you choose a logon identifier that is not an IIS identity, then clear the **Allow IIS to control password** check box, and enter the correct password. This forces all anonymous or guest connections to use the logon identifier. By creating a logon separate from the IIS identity, the privileges of an account accessing WMI can be controlled without affecting the other directories or files on the IIS server—unless the authentication is set at the server level.

Perform the following procedure to set the authentication requirements for the ASP page using the IIS snap-in in the Control Panel.

**To get to the account setting**

1.  In Control Panel, double-click the **Administrative Tools** icon, open the IIS snap-in, locate your ASP page, and open the properties of the level to set, which can be server, directory, or file.

    Authentication settings can be found on either the **Directory Security** or **File Security** tab of the **Properties** sheet.

2.  In the Anonymous authentication area, click **Edit**.

3.  If a logon identifier other than the IIS identity is selected, then clear the **Allow IIS to control password**check box, and enter the correct password. This forces all anonymous or guest connections to use the logon identifier.

By using a logon different from the IIS identity, the privileges of the account accessing WMI can be controlled without affecting the other directories or files on the IIS server—unless the authentication is set at the server level.

The previous configuration allows the IIS server to use Anonymous authentication in some areas, and Integrated Windows or mixed authentication in others.

## Protection

The last consideration when configuring the IIS server is which protection to use when executing an ASP.

You can set an ASP to run the following:

-   In-process to IIS (low protection).

-   External to IIS with Dllhost.exe as pooled or out-of-process (pooled medium protection).

-   Out-of-process self-host (high protection).

> [!Note]  
> For the best balance of security and performance, use pooled host.

 

 

 



