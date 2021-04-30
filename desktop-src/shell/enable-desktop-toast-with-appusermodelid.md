---
description: This topic shows you how to create a shortcut for your app, assign it an AppUserModelID, and install it in the Start screen.
title: How to enable desktop toast notifications through an AppUserModelID
ms.topic: article
ms.date: 05/31/2018
ms.assetid: BB32CD0A-99E6-47dc-A913-39A7B3027314
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbSyntax

---

# How to enable desktop toast notifications through an AppUserModelID

This topic shows you how to create a shortcut for your app, assign it an [AppUserModelID](appids.md), and install it in the Start screen. We strongly recommend that you do this in the Windows Installer rather than in your app's code. Without a valid shortcut installed in the Start screen or in **All Programs**, you cannot raise a toast notification from a desktop app.

> [!Note]  
> The example methods used in this topic are taken from the [Desktop toast sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/DesktopToasts).

 

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

This example first determines the path of the user's app data folder through the [**GetEnvironmentVariable**](/windows/win32/api/processenv/nf-processenv-getenvironmentvariablea) function. It then composes the full path to the shortcut, determines that a shortcut of that name does not already exist at that location, and passes that information to another method which creates and installs the shortcut.

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

This example also retrieves the shortcut's property store and sets the required [System.AppUserModel.ID](../properties/props-system-appusermodel-id.md) property from a previously defined variable, `AppID`.


```C++
HRESULT DesktopToastsApp::InstallShortcut(_In_z_ wchar_t *shortcutPath)
{
    wchar_t exePath[MAX_PATH];
    
    DWORD charWritten = GetModuleFileNameEx(GetCurrentProcess(), nullptr, exePath, ARRAYSIZE(exePath));

    HRESULT hr = charWritten > 0 ? S_OK : E_FAIL;
    
    if (SUCCEEDED(hr))
    {
        ComPtr<IShellLink> shellLink;
        hr = CoCreateInstance(CLSID_ShellLink, nullptr, CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&shellLink));

        if (SUCCEEDED(hr))
        {
            hr = shellLink->SetPath(exePath);
            if (SUCCEEDED(hr))
            {
                hr = shellLink->SetArguments(L"");
                if (SUCCEEDED(hr))
                {
                    ComPtr<IPropertyStore> propertyStore;

                    hr = shellLink.As(&propertyStore);
                    if (SUCCEEDED(hr))
                    {
                        PROPVARIANT appIdPropVar;
                        hr = InitPropVariantFromString(AppId, &appIdPropVar);
                        if (SUCCEEDED(hr))
                        {
                            hr = propertyStore->SetValue(PKEY_AppUserModel_ID, appIdPropVar);
                            if (SUCCEEDED(hr))
                            {
                                hr = propertyStore->Commit();
                                if (SUCCEEDED(hr))
                                {
                                    ComPtr<IPersistFile> persistFile;
                                    hr = shellLink.As(&persistFile);
                                    if (SUCCEEDED(hr))
                                    {
                                        hr = persistFile->Save(shortcutPath, TRUE);
                                    }
                                }
                            }
                            PropVariantClear(&appIdPropVar);
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

As an alternative to the approach shown in this topic, you can use a framework such as the Windows Installer XML (WiX) to generate the shortcut and deploy it as part of the Windows Installer. In that case, this code should be included in the MSI rather than in the app's code. For more information, see the sample WiX configuration file included with the [Sending toast notifications from desktop apps](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Windows%208%20app%20samples/%5BC%2B%2B%5D-Windows%208%20app%20samples/C%2B%2B/Windows%208%20app%20samples/Toast%20notifications%20sample%20(Windows%208)) sample.

## Related topics

<dl> <dt>

[Quickstart: Sending a toast notification from the desktop](quickstart-sending-desktop-toast.md)
</dt> <dt>

[Sending toast notifications from desktop apps sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Windows%208%20app%20samples/%5BC%2B%2B%5D-Windows%208%20app%20samples/C%2B%2B/Windows%208%20app%20samples/Toast%20notifications%20sample%20(Windows%208))
</dt> <dt>

[Application User Model IDs (AppUserModelIDs)](appids.md)
</dt> <dt>

[How to: Install the Windows Installer XML (WiX) Tools](/previous-versions/windows/server-essentials/gg513936(v=msdn.10))
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

[How to add images to a toast template](/previous-versions/windows/)
</dt> <dt>

[How to check toast notification settings](/previous-versions/windows/)
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

 

 
