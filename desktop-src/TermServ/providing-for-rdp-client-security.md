---
title: Providing for RDP client security
description: Some properties of the Remote Desktop ActiveX control object are restricted to specific Internet Explorer URL security zones.
ms.assetid: fd20ec03-a5e4-4c3e-9bf5-5fa841e869c3
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Providing for RDP client security

To allow clients to protect themselves from potentially untrustworthy servers, some properties of the Remote Desktop ActiveX control object are restricted to specific Internet Explorer URL security zones. This means that, when a user browsing the web accesses the page and the page is in a higher URL security zone than the computer they are browsing the web with, these properties are disabled. These restricted properties are accessed using the [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface and the [**IMsRdpClientSecuredSettings**](imsrdpclientsecuredsettings-interface.md) interface, and are available in the following Internet Explorer URL security zones:

-   My computer
-   Local intranet
-   Trusted sites

They are disabled in these zones:

-   Internet
-   Restricted sites

If you call these restricted properties within your Remote Desktop Services web application, you should call [**IMsTscAx::get\_SecuredSettings**](imstscax-securedsettings.md) and [**IMsTscAx::get\_SecuredSettingsEnabled**](imstscax-securedsettingsenabled.md) to access the Secured Settings properties.

The restricted properties that the **IMsTscSecuredSettings** interface accesses are the following:

-   [**StartProgram**](imstscsecuredsettings-startprogram.md). This property specifies the program that will be started upon connection.
-   [**WorkDir**](imstscsecuredsettings-workdir.md). This property specifies the working directory of the program specified in [**StartProgram**](imstscsecuredsettings-startprogram.md).
-   [**FullScreen**](imstscsecuredsettings-fullscreen.md). This property specifies whether the state of the control upon connection will be in full-screen or window mode. If the value of this property is **TRUE**, the connection will be opened in full-screen mode. Although the use of the **FullScreen** property is restricted to the Internet Explorer URL security zones listed earlier, a user can always change to full-screen mode after connection by pressing the full-screen mode [shortcut key](terminal-services-shortcut-keys.md) combination (CTRL+ALT+BREAK).

The properties that the **IMsRdpClientSecuredSettings** interface accesses are the following:

-   [**AudioRedirectionMode**](imsrdpclientsecuredsettings-autoredirectionmode.md). This property specifies whether to redirect sounds, or play sounds at the Remote Desktop Session Host (RD Session Host) server.
-   [**KeyboardHookMode**](imsrdpclientsecuredsettings-keyboardhookmode.md). This property specifies how and when to apply Windows key combinations; for example, ALT+TAB.

The following script launches Microsoft Notepad.exe upon connection. Run this script before calling the [**IMsTscAx::Connect**](imstscax-connect.md) method.

``` syntax
if MsRdpClient.SecuredSettingsEnabled then
    MsRdpClient.SecuredSettings.StartProgram = "notepad.exe"
else
    msgbox "Cannot access secured setting (startprogram) in the current browser zone"
end if
```

 

 




