---
title: Using the Registration Mechanism
description: This topic provides basic information about registering a non-Microsoft messenger application.
ms.assetid: 0d1d87ba-a640-4448-8f23-efa45ec68e8b
keywords:
- Windows Messager,loading
- Windows Messager,opening
- Windows Messager,registry entries
- opening Windows Messenger
- loading Windows Messenger
- Windows Messager,calls to multiple clients
- registering non-Microsoft messenger applications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Registration Mechanism

This topic provides basic information about registering a non-Microsoft messenger application.

Windows Messenger supports a mechanism that helps you register your communications application when it is loaded. Windows Messenger can be loaded as an **InProc** or **Local** server. See [Local vs. InProc Objects in OLE](http://msdn.microsoft.com/library/dnolegen/html/msdn_inproc.asp) for information on InProc and Local servers.

This topic contains the following sections.

-   [Steps in Loading Windows Messenger](#steps-in-loading-windows-messenger)
-   [Opening Windows Messenger](#opening-windows-messenger)
-   [Registry Settings](#registry-settings)
-   [Calls to Multiple Clients](#calls-to-multiple-clients)
-   [Related topics](#related-topics)

## Steps in Loading Windows Messenger

When an application loads Windows Messenger, the following actions take place.

-   The client checks the registry to determine whether other clients are installed.
-   Windows Messenger is set as the primary client on the system, if there are no other clients.
-   Microsoft .NET Messenger Service can be disabled if any other client is installed on the system. The Microsoft .NET Messenger Service is disabled only if the previously installed client has the registry flag *isDotNetProvider* enabled in the registry. If a client has the *isDotNetProvider* flag set, that client is the Microsoft .NET provider.

## Opening Windows Messenger

In case Windows Messenger is not the .NET provider and does not have the Session Initiation Protocol (SIP) enabled, the Windows Messenger icon in the system tray is deactivated. To open Windows Messenger, use the Windows Messenger executable or open it from the **Start Menu**. When Windows Messenger opens, an icon is placed in the system tray and the user can click the icon to exit Windows Messenger.

> [!Note]  
> If SIP is enabled and two clients are installed, the system tray will contain two icons.

 

## Registry Settings

If you write a messenger application you must register your application using the following registry settings.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         MessengerService
            Clients
               My Messenger
                  MessengerGuid = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
                  MessengerPrivateGuid = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
                  MsgrSessionManagerGuid = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
                  isDotNetProvider = dword:00000001
```

Notice in the preceding registry settings that you must make the following entries.

-   My Messenger (your application) is set on the client's key.
-   The Messenger GUID entry that implements [**IMessenger**](im-imessenger.md), [**IMessenger2**](im-imessenger2.md), and [**IMessenger3**](im-imessenger3.md).
    > [!Note]  
    > The format of a GUID is *xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx*. You must generate your own GUIDs for the three GUID entries.

     

-   The Messenger Private GUID entry that implements [**IMessengerPrivate**](im-imessengerprivate.md).
-   The Messenger Session Manager GUID entry that implements [**IMsgrSessionManager**](im-imsgrsessionmanager.md).
-   A flag to specify whether the application is a .NET provider. `00000001` means true and `00000000` false.

## Calls to Multiple Clients

All messenger clients must implement the same interfaces as Windows Messenger and the interfaces must respond to the same UUIDs. When a call is made to Windows Messenger, the proxy distributes the call to all installed clients and responds to the calling application by transparently providing a response as if it were one client. For example, if [**AutoSignin**](im-imessenger-autosignin.md) is called the proxy makes a call to **AutoSignin** on all the clients. When a method call is made to [**MyContacts**](im-imessenger-mycontacts.md) the method returns the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) of an object that implements [**IMessengerContact**](im-imessengercontact.md). This object contains a reference to all the contacts of all the installed clients. All groups, contacts, and services from all clients are wrapped before sending them to the application. The application unwraps them before the proxy calls any of the clients. Events are treated the same way as the method calls. They are distributed to all the clients.

Another important aspect of the proxy is the [IDispatch::Invoke](http://msdn.microsoft.com/library/automat/html/964ade8e-9d8a-4d32-bd47-aa678912a54d.asp) method call. This call forwards the method call to all the clients on the system without determining if the calls are allowed. It is up to the client to determine if IDispatch::Invoke should be called. Script safety must be implemented on each client and it is up to the client to determine what is scriptable.

When Windows Messenger and another client are running, the other client can disable autosignin. Apply the bitmask 0x00040000 to the 4-byte registry value **AppSettings** to turn autosignin off. For example, if the current registry setting is 62 03 00 80, changing the value to 62 07 00 80 disables autosignin.

```
HKEY_CURRENT_USER
   Software
      Microsoft
         MessengerService
            AppSettings (REG_BINARY)
```

## Related topics

<dl> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Windows Messenger](im-messenger-entry.md)
</dt> </dl>

 

 




