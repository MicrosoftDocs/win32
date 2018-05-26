---
title: Windows Messenger
description: This is the entry page to the reference documentation for Windows Messenger. This section includes information about the Messenger service APIs and the Messenger client APIs. The documentation consists of API reference and conceptual overviews.
ms.assetid: 25517c5a-fd5e-4634-a001-6970e901c871
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Messenger

\[Windows Messenger is no longer available for use as of Windows Vista. \]

This is the entry page to the reference documentation for Windows Messenger. This section includes information about the Messenger service  APIs and the Messenger client APIs. The documentation consists of API reference and conceptual overviews.

## In this section



| Topic                                                                         | Description                                                     |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [Windows Messenger Overviews](im-ovw-entry.md)<br/>                    | Overview information for Windows Messenger.<br/>          |
| [Windows Messenger Client Reference](im-client-cppref-entry.md)<br/>   | Client reference information for Windows Messenger.<br/>  |
| [Windows Messenger Service Reference](im-service-cppref-entry.md)<br/> | Service reference information for Windows Messenger.<br/> |



 

## Windows Messenger Is No Longer Available

Windows Vista does not include the APIs for Windows Messenger. They are included with Windows Live Messenger to ensure continued support for applications that use the Windows Messenger APIs. You can download Messenger from the [Windows Live Messenger](http://get.live.com/messenger/overview) site.

Applications developed with the Windows Messenger SDK are compatible with Messenger; however, Messenger does not support script that uses Windows Messenger objects. Applications that require Messenger functionality should be developed with the appropriate Live SDK. More information about the Live SDKs can be found on [Windows Live Dev](http://dev.live.com).

## What's New in Windows Messenger 5.0

The Windows Messenger Add-In APIs are no longer available. For information about branding Windows Messenger, see [Personalizing Microsoft Windows Messenger 5.0](http://www.microsoft.com/technet/treeview/default.asp?url=/technet/prodtechnol/winxppro/deploy/WMsngrBr.asp).

Five properties of the [**IMessenger**](im-imessenger.md) interface have been deprecated in favor of properties in the [**IMessengerService**](im-imessengerservice.md) interface.

-   Use [**MyFriendlyName**](im-imessengerservice-myfriendlyname.md) instead of [**MyFriendlyName**](im-imessenger-myfriendlyname.md).
-   Use [**ServiceID**](im-imessengerservice-serviceid.md) instead of [**MyServiceId**](im-imessenger-myserviceid.md).
-   Use [**ServiceName**](im-imessengerservice-servicename.md) instead of [**MyServiceName**](im-imessenger-myservicename.md).
-   Use [**MySigninName**](im-imessengerservice-mysigninname.md) instead of [**MySigninName**](im-imessenger-mysigninname.md).
-   Use [**MyStatus**](im-imessengerservice-mystatus.md) instead of [**MyStatus**](im-imessenger-mystatus.md).

## Windows Messenger Add-In APIs

The documentation for the Add-In APIs shows you how to create add-in components for the Windows Messenger client on Windows XP. The Add-In APIs are not available with any version of Windows Messenger other than 4.6 or 4.7. To download this documentation, see [Windows Messenger Add-In APIs](http://download.microsoft.com/download/6/8/3/683DB9FE-8D61-4A3C-B7B8-3169FF70AE9F/WinMsgr.msi).

## What's New in Windows Messenger 4.7

A new overview [Using the Registration Mechanism](im-registration-mechanism.md) has been added.

 

 





