---
Description: This topic shows you how to create a shortcut for your app, assign it an AppUserModelID, and install it in the Start screen.
title: How to enable desktop toast notifications through an AppUserModelID
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to enable desktop toast notifications through an AppUserModelID

This topic shows you how to create a shortcut for your app, assign it an [AppUserModelID](appids.md), and install it in the Start screen. We strongly recommend that you do this in the Windows Installer rather than in your app's code. Without a valid shortcut installed in the Start screen or in **All Programs**, you cannot raise a toast notification from a desktop app.

> [!Note]  
> The example methods used in this topic are taken from the [Desktop toast sample](http://go.microsoft.com/fwlink/p/?linkid=242463).

 

## What you need to know

### Technologies

-   COM

### Prerequisites

-   Libraries
    -   C++: Runtime.object.lib
    -   C\#: Windows.Winmd
-   C\#: Windows API Code Pack for Microsoft .NET Framework
-   A version of Microsoft Visual Studio that supports at least Windows 8

## Instructions

### Step 1: Prepare the shortcut to be created

This example first determines the path of the user's app data folder through the [**GetEnvironmentVariable**](base.getenvironmentvariable) function. It then composes the full path to the shortcut, determines that a shortcut of that name does not already exist at that location, and passes that information to another method which creates and installs the shortcut.

Note that the shortcut can be deployed per-user or per-app.


```C++
HRESULT DesktopToastsApp::TryCreateShortcut()
{
    wchar_t shortcutPath[MAX_PATH];
    DWORD charWritten = GetEnvironmentVariable(L"APPDATA", shortcutPath, MAX_PATH);
    HRESULT hr = charWritten > 0 ? S_OK : E_INVALIDARG;

    if (SUCCEEDED(hr))
    {
        errno_t concatError = wcscat_s(shortcutPath, ARRAYSIZE(shortcutPath), L"\\Microsoft\\Windows\\Start Menu\\Programs\\Desktop Toasts App.lnk");
 
        hr = concatError == 0 ? S_OK : E_INVALIDARG;
        if (SUCCEEDED(hr))
        {
            DWORD attributes = GetFileAttributes(shortcutPath);
            bool fileExists = attributes < 0xFFFFFFF;

            if (!fileExists)
            {
                hr = InstallShortcut(shortcutPath);  // See step 2.
            }
            else
            {
                hr = S_FALSE;
            }
        }
    }
    return hr;
}
```



### Step 2: Create the shortcut and install it in the Start screen

This example also retrieves the shortcut's property store and sets the required [System.AppUserModel.ID](properties.props_System_AppUserModel_Id) property from a previously defined variable, `AppID`.


```C++
HRESULT DesktopToastsApp::InstallShortcut(_In_z_ wchar_t *shortcutPath)
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
                hr = shellLink->SetArguments(L"");
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
                                hr = propertyStore->Commit();
                                if (SUCCEEDED(hr))
                                {
                                    ComPtr<IPersistFile> persistFile;
                                    hr = shellLink.As(&amp;persistFile);
                                    if (SUCCEEDED(hr))
                                    {
                                        hr = persistFile->Save(shortcutPath, TRUE);
                                    }
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



## Remarks

As an alternative to the approach shown in this topic, you can use a framework such as the Windows Installer XML (WiX) to generate the shortcut and deploy it as part of the Windows Installer. In that case, this code should be included in the MSI rather than in the app's code. For more information, see the sample WiX configuration file included with the [Sending toast notifications from desktop apps](http://go.microsoft.com/fwlink/p/?linkid=242463) sample.

## Related topics

<dl> <dt>

[Quickstart: Sending a toast notification from the desktop](quickstart-sending-desktop-toast.md)
</dt> <dt>

[Sending toast notifications from desktop apps sample](http://go.microsoft.com/fwlink/p/?linkid=242463)
</dt> <dt>

[Application User Model IDs (AppUserModelIDs)](appids.md)
</dt> <dt>

[How to: Install the Windows Installer XML (WiX) Tools](d02c70e2-3eea-46ea-b100-53e776852dde)
</dt> <dt>

[Sending toast notifications from desktop apps sample](http://go.microsoft.com/fwlink/p/?linkid=231503)
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

 

 



