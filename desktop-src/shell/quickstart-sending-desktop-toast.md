---
description: This quickstart shows how to raise a toast notification from a desktop app.
title: Sending a toast notification from the desktop
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 1D20ED75-E24A-4e60-91AB-CFCBE902A68E
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbSyntax

---

# Quickstart: Sending a toast notification from the desktop

This quickstart shows how to raise a toast notification from a desktop app.

## Prerequisites

-   Libraries
    -   C++: Runtime.object.lib
    -   C\#: Windows.Winmd
-   A shortcut to your app, with a [System.AppUserModel.ID](../properties/props-system-appusermodel-id.md), must be installed to the Start screen. Note, however, that it does not need to be pinned to the Start screen. For more information, see [How to enable desktop toast notifications through an AppUserModelID](enable-desktop-toast-with-appusermodelid.md).
-   A version of Microsoft Visual Studio that supports at least Windows 8

## Instructions

### 1. Create your toast content

> [!Note]  
> When you specify a toast template that includes an image, be aware that desktop apps can use only local images; web images are not supported. Also, the path to the local image file must be provided as an absolute (not relative) path.

 


```csharp
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


```csharp
toast.Activated += ToastActivated;
toast.Dismissed += ToastDismissed;
toast.Failed += ToastFailed;
```



### 3. Send the toast

> [!IMPORTANT]
> You must include the [AppUserModelID](../properties/props-system-appusermodel-id.md) of your app's shortcut on the Start screen each time that you call [**CreateToastNotifier**](/uwp/api/Windows.UI.Notifications.ToastNotificationManager). If you fail to do this, your toast will not be displayed.

 


```csharp
ToastNotificationManager.CreateToastNotifier(appID).Show(toast);
```



### 4. Handle the callbacks

Bring your app's window to the foreground if it receives an "activated" callback from the toast notification. When a user selects a toast, the expectation is that the app will be launched to a view related to the content of that toast..

## Related topics

<dl> <dt>

[Sending toast notifications from desktop apps sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/DesktopToasts)
</dt> <dt>

[How to enable desktop toast notifications through an AppUserModelID](enable-desktop-toast-with-appusermodelid.md)
</dt> <dt>

[Toast XML schema](/uwp/schemas/tiles/toastschema/schema-root)
</dt> <dt>

[Toast notification overview](/previous-versions/windows/apps/hh779727(v=win.10))
</dt> <dt>

[Quickstart: Sending a toast notification](/previous-versions/windows/apps/hh465448(v=win.10))
</dt> <dt>

[Quickstart: Sending a toast push notification](/previous-versions/windows/hh761487(v=win.10))
</dt> <dt>

[Guidelines and checklist for toast notifications](/windows/uwp/design/shell/tiles-and-notifications/)
</dt> <dt>

[How to choose and use a toast template](/previous-versions/windows/apps/hh465448(v=win.10))
</dt> <dt>

[How to handle activation from a toast notification](/previous-versions/windows/apps/hh761468(v=win.10))
</dt> <dt>

[How to opt in for toast notifications](/previous-versions/windows/apps/hh781238(v=win.10))
</dt> <dt>

[Choosing a toast template](/previous-versions/windows/apps/hh761494(v=win.10))
</dt> <dt>

[Toast audio options](/previous-versions/windows/apps/hh761492(v=win.10))
</dt> </dl>

 

 
