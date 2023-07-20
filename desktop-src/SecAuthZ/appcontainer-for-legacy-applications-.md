---
title: AppContainer for legacy apps
description: The AppContainer environment is a restrictive process execution environment that can be used for legacy apps in order to provide resource security.
ms.assetid: 28498D4E-DCA4-4A85-B474-C3C328BD3022
ms.topic: article
ms.date: 07/20/2023
---

# AppContainer for legacy apps

The AppContainer environment is a restrictive process execution environment that can be used for legacy apps in order to provide resource security. An AppContainer app's process and its child processes run inside a lightweight app container where they can access only the resources that are specifically granted to them. And they're isolated using file system and registry virtualization. As a result, apps implemented in an AppContainer can't be hacked to allow malicious actions outside of the limited assigned resources.

## Packaged apps

You can take an app that's packaged using MSIX, and easily configure it to run in the AppContainer environment. Universal Windows Platform (UWP) apps are automatically AppContainer apps. But you can also configure your desktop app that's packaged with MSIX to be an AppContainer app. It's particularly easy to use AppContainer if you package using MSIX. For more info, scenarios, and configuration examples, see [MSIX AppContainer apps](/windows/msix/msix-container).

## Unpackaged apps

An unpackaged app can run in an app container, too. If you don't package your app with MSIX, then you'll need to explicitly create the AppContainer profile/definition. Most unpackaged apps that used the low integrily level now use use AppContainer as a better way to provide a constrained execution environment.

## Benefits of using an AppContainer environment

A key goal of The AppContainer environment is to separate app state from system state as much as possible, while maintaining compatibility with other apps. Windows accomplishes that by detecting and redirecting certain changes that it makes to the file system and registry at runtime (known as *virtualizing*). An AppContainer app writes to its own virtual registry and application data folder, and that data is deleted when the app is uninstalled or reset. Other apps don't have access to the virtual registry or virtual file system of an AppContainer app.

So the AppContainer environment provides secure sandboxing of apps. Isolating the app from accessing hardware, files, registry, other apps, network connectivity, and network resources without specific permission. Individual resources can be targeted without exposing other resources. Additionally, user identity is protected by using a unique identity that is a concatenation of the user and the app; and resources are granted using a least-privilege model. That further protects against an app impersonating the user to gain access to other resources.

## Example code to test for running in an app container

In a C# or C++ project, you can use the appropriate one of the code examples below to determine whether or not a process is running inside an app container. For each example, after the code has run, if the value of *isAppContainer* is non-zero (or `true`), then the process is running inside an app container.

### C# (P/Invoke)

```csharp
[DllImport("kernel32.dll", SetLastError = true)]
public static extern IntPtr GetCurrentProcess();

[DllImport("advapi32.dll", SetLastError = true)]
[return: MarshalAs(UnmanagedType.Bool)]
static extern bool OpenProcessToken(
    IntPtr ProcessHandle,
    UInt32 DesiredAccess,
    out IntPtr TokenHandle);

[DllImport("advapi32.dll", SetLastError = true)]
[return: MarshalAs(UnmanagedType.Bool)]
static extern bool GetTokenInformation(
    IntPtr TokenHandle,
    uint TokenInformationClass,
    out uint TokenInformation,
    uint TokenInformationLength,
    out uint ReturnLength);

UInt32 TOKEN_QUERY = 0x0008;
IntPtr tokenHandle;

if (!OpenProcessToken(
    GetCurrentProcess(),
    TOKEN_QUERY,
    out tokenHandle))
{
    // Handle the error.
}

uint isAppContainer;
uint TokenIsAppContainer = 29;
uint tokenInformationLength = sizeof(uint);

if (!GetTokenInformation(
    tokenHandle,
    TokenIsAppContainer,
    out isAppContainer,
    tokenInformationLength,
    out tokenInformationLength))
{
    // Handle the error.
}
```

### C++ (WIL)

This example uses the [Windows Implementation Libraries (WIL)](https://github.com/Microsoft/wil)). A convenient way to install WIL is to go to Visual Studio, click **Project** \> **Manage NuGet Packages...** \> **Browse**, type or paste **Microsoft.Windows.ImplementationLibrary** in the search box, select the item in search results, and then click **Install** to install the package for that project.

```cpp
#include <wil\token_helpers.h>
...
bool isAppContainer = wil::get_token_is_app_container();
```

The functions **wil::get_token_is_app_container_nothrow** and **wil::get_token_is_app_container_failfast** offer alternative error-handling strategies. See `wil\token_helpers.h` for more info.

### C++ (canonical)

```cpp
#include <windows.h>
...
HANDLE tokenHandle{};
DWORD isAppContainer{};
DWORD tokenInformationLength{ sizeof(DWORD) };

if (!::OpenProcessToken(
    GetCurrentProcess(),
    TOKEN_QUERY,
    &tokenHandle))
{
    // Handle the error.
}

if (::GetTokenInformation(
    tokenHandle,
    TOKEN_INFORMATION_CLASS::TokenIsAppContainer,
    &isAppContainer,
    tokenInformationLength,
    &tokenInformationLength
))
{
    // Handle the error.
}
```

## In this section

For more information about using AppContainer for legacy apps, see the following topics.

| Topic | Description |
|-|-|
| [AppContainer isolation](appcontainer-isolation.md) | Isolation is the primary goal of an AppContainer execution environment. By isolating an app from unneeded resources and other apps, opportunities for malicious manipulation are minimized. Granting access based upon least-privilege prevents apps and users from accessing resources beyond their rights. Controlling access to resources protects the process, the device, and the network. |
| [Implement an AppContainer](implementing-an-appcontainer.md) | An AppContainer is implemented by adding new information to the process token, changing [**SeAccessCheck()**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-seaccesscheck) so that all legacy, unmodified access control list (ACL) objects block access requests from AppContainer processes by default, and re-ACL objects that should be available to AppContainers. |
