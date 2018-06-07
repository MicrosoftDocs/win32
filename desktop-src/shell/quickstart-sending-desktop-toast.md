---
Description: This quickstart shows how to raise a toast notification from a desktop app.
title: 'Quickstart: Sending a toast notification from the desktop'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Quickstart: Sending a toast notification from the desktop

This quickstart shows how to raise a toast notification from a desktop app.

## Prerequisites

-   Libraries
    -   C++: Runtime.object.lib
    -   C\#: Windows.Winmd
-   A shortcut to your app, with a [System.AppUserModel.ID](https://msdn.microsoft.com/07858b3c-e601-40ec-a87a-d66612d5473a), must be installed to the Start screen. Note, however, that it does not need to be pinned to the Start screen. For more information, see [How to enable desktop toast notifications through an AppUserModelID](enable-desktop-toast-with-appusermodelid.md).
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
> You must include the [AppUserModelID](https://msdn.microsoft.com/07858b3c-e601-40ec-a87a-d66612d5473a) of your app's shortcut on the Start screen each time that you call [**CreateToastNotifier**](https://msdn.microsoft.com/Windows.UI.Notifications.ToastNotificationManager.CreateToastNotifier(System.String)). If you fail to do this, your toast will not be displayed.

 


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

[Toast XML schema](https://msdn.microsoft.com/06ae9be6-c573-4b35-83e0-371ed8299e33)
</dt> <dt>

[Toast notification overview](https://msdn.microsoft.com/14A07FCE-D631-4bad-AB99-305B703713E6)
</dt> <dt>

[Quickstart: Sending a toast notification](https://msdn.microsoft.com/098DF37C-4D40-4499-B809-CCB651DA1CBA)
</dt> <dt>

[Quickstart: Sending a toast push notification](https://www.bing.com/search?q=Quickstart:+Sending+a+toast+push+notification)
</dt> <dt>

[Guidelines and checklist for toast notifications](002951E3-3D2D-454A-A0B7-DAA5C1E7178A)
</dt> <dt>

[How to add images to a toast template](https://www.bing.com/search?q=How+to+add+images+to+a+toast+template)
</dt> <dt>

[How to check toast notification settings](https://www.bing.com/search?q=How+to+check+toast+notification+settings)
</dt> <dt>

[How to choose and use a toast template](098DF37C-4D40-4499-B809-CCB651DA1CBA)
</dt> <dt>

[How to handle activation from a toast notification](https://msdn.microsoft.com/74BA3513-0A52-46a0-8769-ED58ABE7C05A)
</dt> <dt>

[How to opt in for toast notifications](https://msdn.microsoft.com/809CDD36-6DE1-4de0-88B2-62B46CAFDB28)
</dt> <dt>

[Choosing a toast template](1A437614-4259-426b-8E3F-CA57368B2E7A)
</dt> <dt>

[Toast audio options](12185879-1F9B-4bdc-99E7-A6F2F62806CB)
</dt> </dl>

 

 



