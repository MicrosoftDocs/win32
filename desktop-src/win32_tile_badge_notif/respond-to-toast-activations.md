---
title: Respond to toast activations
description: In order for Win32 applications to respond to toast notifications, there are several steps they need to take. This topic explains how to have your app respond to those notifications.
ms.assetid: '050E6944-6727-4632-85E8-8E68887D4786'
---

# Respond to toast activations

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

In order for Win32 applications to respond to toast notifications, there are several steps they need to take. This topic explains how to have your app respond to those notifications. Modern applications have a different activation model, which is why these steps are not necessary if you are creating a modern app.

Notifications in the action center can stay around for several days before they are seen by the user and processed. Because of this, you can't assume that your app will be running when the user responds to a notification. In order to get around this, you will need to create a local Component Object Model (COM) server that can be invoked when users interact with the toast. By following this paradigm, your app can respond to toasts at any time.

## Creating a shortcut

In order for your app to be able to be activated at any time, you will need to create a shortcut and have it installed on the Start menu. This should happen as part of the install process for your application. The shortcut needs to contain the following pieces of information.

-   A **System.AppUserModel.ID** that is a unique identifier for your application. This is necessary so that the system knows the notification endpoint for your app. This is also needed in order to send toast notifications. For more information about this identifier, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/library/windows/desktop/dd378459).
-   A CLSID that points to your COM component that implements [**INotificationActivationCallback**](inotificationactivationcallback.md).

The following sample code demonstrates how to install this shortcut.


```C++
HRESULT DesktopToastsApp::InstallShortcut(_In_ PCWSTR shortcutPath)
{
    wchar_t exePath[MAX_PATH];
     
    DWORD charWritten = GetModuleFileNameEx(GetCurrentProcess(), nullptr, exePath, ARRAYSIZE(exePath));
  
    HRESULT hr = charWritten > 0 ? S_OK : E_FAIL;
     
    if (SUCCEEDED(hr))
    {
        ComPtr<IShellLink> shellLink;
        hr = CoCreateInstance(CLSID_ShellLink, nullptr, CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&amp;shellLink));
  
        if (SUCCEEDED(hr))
        {
            hr = shellLink->SetPath(exePath);
            if (SUCCEEDED(hr))
            {
                ComPtr<IPropertyStore> propertyStore;
                hr = shellLink.As(&amp;propertyStore);
                if (SUCCEEDED(hr))
                {
                    PROPVARIANT appIdPropVar;
                    hr = InitPropVariantFromString(AppId, &amp;appIdPropVar);
                    if (SUCCEEDED(hr))
                    {
                        hr = propertyStore->SetValue(PKEY_AppUserModel_ID, appIdPropVar);
                        if (SUCCEEDED(hr))
                        {
                            PropVariantClear(&amp;appIdPropVar);
                            appIdPropVar.vt = VT_CLSID;
                            appIdPropVar.puuid = const_cast<CLSID*>(&amp;__uuidof(NotificationActivator));
                            hr = propertyStore->SetValue(PKEY_AppUserModel_ToastActivatorCLSID, appIdPropVar);
                            if (SUCCEEDED(hr))
                            {
                                ComPtr<IPersistFile> persistFile;
                                hr = shellLink.As(&amp;persistFile);
                                if (SUCCEEDED(hr))
                                {
                                    hr = persistFile->Save(shortcutPath, TRUE);
                                }
                            }
                            PropVariantClear(&amp;appIdPropVar);
                        }
                    }
                }
            }
        }
    }
    return hr;
}
```



## Registering a COM activator

Once you have overwritten the [**INotificationActivationCallback**](inotificationactivationcallback.md) interface in your COM component, you will need to tell COM how to start your app when it is necessary. In order to do this, you will need to update the registry. The following line will modify the registry

> \[!Important\]  
> The identifier provided (23A5B06E-20BB-4E7E-A0AC-6982ED6A6041) in this step is just used as a sample. You will need to change this to your unique CLSID. In addition, you will need to update the install path (C:\\Users\\Sample\\Desktop\\DesktopToastsSample.exe) to point to the exe for your application.

 

**reg add "HKEY\_CURRENT\_USER\\SOFTWARE\\Classes\\CLSID\\{23A5B06E-20BB-4E7E-A0AC-6982ED6A6041}\\LocalServer32" /d C:\\Users\\Sample\\Desktop\\DesktopToastsSample.exe**

In addition, you need to make sure to add the following line of code to your application when it starts. This will register your COM object so that it can be found by the system.


```C++
Module::GetModule().RegisterObjects();
```



## Handling the notification

In order to respond to the notification, you will need to implement [**Activate**](inotificationactivationcallback-activate.md). In this method, you can respond to both non-interactive and interactive toasts however you see fit. If your app is not running, it will be launched by your local COM service defined in the previous section. If you are responding to interactive toasts, the UI could be waiting for the callback to return by showing an indeterminate progress UI, so you need to make sure your callback returns at the appropriate time to indicate that the action is complete. If you want to respond to the interactive toast without showing any additional UI, you will need to register a non-UI process as the COM server. One example where this could be useful is replying to a message without bring your app to the foreground.

The following code demonstrates a simple way to handle the toast notification.


```C++
HStringReference toastXML(
    L"<toast>"
    L" <visual>"
    L" <binding template='ToastGeneric'>"
    L" <text>Press Reply</text>"
    L" </binding>"
    L" </visual>"
    L" <actions>"
    L" <action content='reply'"
    L" arguments='replyToComment'"
    L" activationKind='Background'/>"
    L" </actions>"
    L"</toast>");
 
...
 
hr = DocumentIO->LoadXml(toastXML.Get());
 
...
 
ComPtr<IToastNotification> toast;
hr = factory->CreateToastNotification(xml, &amp;toast);
 
...
 
hr = notifier->Show(toast.Get());
 
 
 
HRESULT NotificationActivator::Activate(PCWSTR /*appUserModelId*/, PCWSTR invokedArgs,
    const NOTIFICATION_USER_INPUT_DATA* data, ULONG count)
{
    if (invokedArgs == nullptr)
    {
      // Start my app or just do nothing because COM started the app already.
    }
    else if (::wcscmp(invokedArgs, L"replyToComment") == 0)
    {
        ASSERT(count == 1);
        ASSERT(::wcscmp(data[0].Key, L"replyToComment") == 0);
                
        DoWorkToReply(data[0].Data);
    }
 
    return S_OK;
}
```



## Related topics

<dl> <dt>

[Tiles, badges, and notifications for UWP apps](https://msdn.microsoft.com/library/windows/apps/mt185606)
</dt> </dl>

 

 




