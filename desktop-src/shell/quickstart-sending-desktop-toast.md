---
Description: This quickstart shows how to raise a toast notification from a desktop app.
title: Quickstart Sending a toast notification from the desktop
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Quickstart: Sending a toast notification from the desktop

This quickstart shows how to raise a toast notification from a desktop app.

## Prerequisites

-   Libraries
    -   C++: Runtime.object.lib
    -   C\#: Windows.Winmd
-   A shortcut to your app, with a [System.AppUserModel.ID](properties.props_System_AppUserModel_Id), must be installed to the Start screen. Note, however, that it does not need to be pinned to the Start screen. For more information, see [How to enable desktop toast notifications through an AppUserModelID](enable-desktop-toast-with-appusermodelid.md).
-   A version of Microsoft Visual Studio that supports at least Windows 8

## Instructions

### 1. Create your toast content

> [!Note]  
> When you specify a toast template that includes an image, be aware that desktop apps can use only local images; web images are not supported. Also, the path to the local image file must be provided as an absolute (not relative) path.

 


```CSharp
// Get a toast XML template
XmlDocument toastXml = ToastNotificationManager.GetTemplateContent(ToastTemplateType.ToastImageAndText04);

// Fill in the text elements
XmlNodeList stringElements = toastXml.GetElementsByTagName("text");
for (int i = 0; i < stringElements.Length; i++)
{
    stringElements[i].AppendChild(toastXml.CreateTextNode("Line " + i));
}

// Specify the absolute path to an image
String imagePath = "file:///" + Path.GetFullPath("toastImageAndText.png");
XmlNodeList imageElements = toastXml.GetElementsByTagName("image");

ToastNotification toast = new ToastNotification(toastXml);
```



### 2. Create and attach the event handlers

Register handlers for the toast events: Activated, Dismissed, and Failed. A desktop app must at least subscribe to the Activated event so that it can handle the expected activation of the app from the toast when the user selects it.


```CSharp
toast.Activated += ToastActivated;
toast.Dismissed += ToastDismissed;
toast.Failed += ToastFailed;
```



### 3. Send the toast

> \[!Important\]  
> You must include the [AppUserModelID](properties.props_System_AppUserModel_Id) of your app's shortcut on the Start screen each time that you call [**CreateToastNotifier**](w_ui_notif.toastnotificationmanager_createtoastnotifier_163337301). If you fail to do this, your toast will not be displayed.

 


```CSharp
ToastNotificationManager.CreateToastNotifier(appID).Show(toast);
```



### 4. Handle the callbacks

Bring your app's window to the foreground if it receives an "activated" callback from the toast notification. When a user selects a toast, the expectation is that the app will be launched to a view related to the content of that toast..

## Summary and next steps

## Related topics

<dl> <dt>

[Sending toast notifications from desktop apps sample](http://go.microsoft.com/fwlink/p/?linkid=242463)
</dt> <dt>

[How to enable desktop toast notifications through an AppUserModelID](enable-desktop-toast-with-appusermodelid.md)
</dt> <dt>

[Toast notifications sample](http://go.microsoft.com/fwlink/p/?linkid=231503)
</dt> <dt>

[Toast XML schema](toast.Schema_Root)
</dt> <dt>

[Toast notification overview](m_ca_tiles.toast_ovw)
</dt> <dt>

[Quickstart: Sending a toast notification](m_ui_tiles.quickstart_sending_a_toast)
</dt> <dt>

[Quickstart: Sending a toast push notification](m_ui_tiles.quickstart_sending_a_toast_push)
</dt> <dt>

[Guidelines and checklist for toast notifications](m_ui_tiles.guidelines_and_checklist_for_toast)
</dt> <dt>

[How to add images to a toast template](m_ui_tiles.howto_use_images_toast)
</dt> <dt>

[How to check toast notification settings](m_ui_tiles.howto_check_toast_notification_settings)
</dt> <dt>

[How to choose and use a toast template](m_ui_tiles.howto_specify_a_toast_template)
</dt> <dt>

[How to handle activation from a toast notification](m_ui_tiles.howto_handle_activation_from_toast)
</dt> <dt>

[How to opt in for toast notifications](m_ui_tiles.howto_optin_for_toast)
</dt> <dt>

[Choosing a toast template](m_ui_tiles.toast_template_catalog)
</dt> <dt>

[Toast audio options](m_ui_tiles.toast_audio_options)
</dt> </dl>

 

 



