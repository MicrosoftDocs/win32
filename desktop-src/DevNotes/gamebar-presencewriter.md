---
title: Game Bar Presence Writer
description: Game Bar Presence Writer
ms.assetid: 87e04f78-d2d1-42f7-8d9f-2d46d7fd226d
ms.topic: reference
ms.date: 02/22/2024
---

# Game Bar Presence Writer

## Purpose

Game Bar Presence Writer is a component that is notified when a game's "presence" state (i.e. is a game running in the foreground) changes.  This functionality is available in Windows 10 and later operating systems.  By default, the existing Game Bar Presence Writer will set a user's Xbox Live presence state for a running game if the Xbox App is installed, the user is signed into their Xbox account, and the user has enabled Xbox Live presence to be set when they run a game on their PC.  It is possible for Windows Application developers to override this default behavior with their own implemention.

> [!Important]
> By providing a custom implementation of the Game Bar Presence Writer, the default behavior of a user's Xbox Live presence state being set when they run a game will no longer be available.

## Implement an out of proc COM server that implements Game Bar Presence Writer functionality

In order to provide a Game Bar Presence Writer implementation, you must implement an out of proc COM server that implemented the following COM interfaces:

``` syntax
import "oaidl.idl";
import "Inspectable.idl";

#include <sdkddkver.h>

namespace Windows.Gaming.GameBar.PresenceServer.Internal
{
    // typedefs
    typedef enum GameNotificationEvent GameNotificationEvent;
    typedef enum AppIdType AppIdType;

    typedef UINT64 WindowId;

    interface IPresenceWriter;
    runtimeclass PresenceWriter;

    // enums
    enum GameNotificationEvent
    {
        None = 0,
        GotFocus,
        LostFocus,
        AppClose
    };

    // enums
    enum AppIdType
    {
        Aumid = 0,  // Application User Model Id
        TitleId     // Xbox Live Title Id
    };

    [uuid(782674D9-5CBB-4FCA-AD72-D9AC5F7AE963)]
    [exclusiveto(PresenceWriter)]
    interface IPresenceWriter : IInspectable
    {
        HRESULT UpdatePresence([in] WindowId hWnd, [in] GameNotificationEvent @event, [in] HSTRING appId, [in] AppIdType appIdType);
    }

    [marshaling_behavior(agile)] 
    runtimeclass PresenceWriter 
    {
        [default] interface IPresenceWriter; 
    }
}
```
When a game is ran on the user's machine, UpdatePresence will be called with the following parameters:

<dl> <dt>

*hWnd* \[in\]
</dt> <dd>

A handle to the window of the running game.
</dd> <dt>

*event* \[in\]
</dt> <dd>

Event that correpsonds to whether the game got focus (**GotFocus**), lost focus (**LostFocus**), or the game as was closed (**AppClose**).
</dd> <dt>

*appId* \[in\]
</dt> <dd>

Application Identifier of the game.  If *appIdType* is **Aumid** then *appId* is the Application User Model Id.  If *appId* is **TitleId** then *appId* is the Xbox Live Title Id.
</dd> <dt>

*appIdType* \[in\]
</dt> <dd>

Specifies if *appId* corresponds to the Application User Model Id (**Aumid**) of the game of the Xbox Live Title Id (**TitleId**) of the game.
</dd></dl>

## Register COM server implementation for Presence Writer

In order for your implementation of Game Bar Presence Writer to run, it must ensure the following registry value is set:

**HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsRuntime\Server\Windows.Gaming.GameBar.Internal.PresenceWriterServer\ExePath**



| Data type | Range                    | Default value |
|-----------|--------------------------|---------------|
| REG\_SZ   | *Path to the executable* |               |

