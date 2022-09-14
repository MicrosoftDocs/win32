---
title: Session-to-Session Activation with a Session Moniker
description: Session-to-session activation (also called cross-session activation) allows a client process to start (activate) a local server process on a specified session.
ms.assetid: d405c276-040b-4cde-aeb2-482a25e2867f
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Session-to-Session Activation with a Session Moniker

Session-to-session activation (also called cross-session activation) allows a client process to start (activate) a local server process on a specified session. This feature is available for applications that are configured to run in the security context of the interactive user, also known as the "RunAs Interactive User" object activation mode. For more information about security contexts, see [The Client's Security Context](/windows/desktop/SecAuthZ/the-client-security-context).

Distributed COM (DCOM) enables object activation on a per-session basis by using a system-supplied [Session Moniker](session-monikers.md). Other system-supplied monikers include [file monikers](../com/file-monikers.md), [item monikers](../com/item-monikers.md), generic [composite monikers](../com/composite-monikers.md), [anti-monikers](../com/anti-monikers.md), [pointer monikers](../com/pointer-monikers.md), and [URL monikers](../com/url-monikers.md).

To be able to use the session moniker, the DCOM application must be set to run as the interactive user. This can be set by using the Component Services Administrative tool, viewing the Properties of the DCOM application, and selecting **The interactive user** on the **Identity** tab. For more information about the possible security risks associated with setting a DCOM application to run as the interactive user in a Remote Desktop Services environment, see the "Application Identity (COM)" section of the COM documentation in the Platform Software Development Kit (SDK).

If any other type of user is selected to run the application, the session moniker will be ignored by the application. The session moniker is also ignored by COM+ server applications. For more information about other methods for selecting the type of user to run the application, see the COM documentation in the Platform SDK.

To create a session moniker, you must compose the session ID of the Remote Desktop Services session with a class moniker that specifies the process server's class ID.

**To create a session moniker**

1.  Prefix the display name of the class moniker with the display name of the session moniker by using the following syntax:

    ``` syntax
    "Session:[digits]!clsid:[class id]"
    ```

    where *digits* represents the session ID of the session on which the server process will be started, and where *class id* represents the class ID of the server. Note that the session ID is a base-10 number.

    For computers that are running Windows XP or later, using the following syntax will result in COM sending the activation to the currently active physical console session, whatever its session ID is:

    ``` syntax
    "Session:Console!clsid:[class id]"
    ```

2.  After you have created the session moniker, you can pass the result to either the [**MkParseDisplayName**](/windows/desktop/api/objbase/nf-objbase-mkparsedisplayname) function or the [MkParseDisplayNameEx](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775113(v=vs.85)) function.

You can use a session moniker in the same way as you would use any other moniker.

For a code sample that demonstrates how to activate a local server process on a specified session, see [Using a Session Moniker](using-a-session-moniker.md).

For more information about object activation, system-supplied monikers and class monikers, see the COM documentation in the Platform SDK.

> [!Note]  
> Processes that are created across sessions have an upper limit on the size of the environment block. This limit is around 4 KB, but it can be larger or smaller depending on what other information is needed to create the process (for example file names, directories, and parameters for the new process).

 

 

 