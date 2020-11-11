---
title: App (executable) manifest
description: App (executable) manifest
ms.assetid: F46F33A6-0B2F-4086-9C6D-4AD43C26BCD3
ms.topic: article
ms.date: 05/31/2018
---

# App (executable) manifest

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

The compatibility section of the app (executable) manifest introduced in Windows helps the operating system determine the versions of Windows an app was designed to target. Additionally, the app manifest enables Windows to provide the behavior that the app expects based on the version of Windows that the app targeted.

The compatibility section of the manifest allows Windows to provide new behavior to newly created software while maintaining the compatibility for existing software. This section helps Windows deliver greater compatibility in future versions of Windows as well. For example, an app declaring support for only Windows 8 in the compatibility section will continue to receive Windows 8 behavior in future versions of Windows.

## Manifestation

Apps without a compatibility section in their manifest will have Windows Vista behavior by default on Windows 7 and Windows 8 and future Windows versions. Be aware that Windows XP and Windows Vista ignore this manifest section and it has no impact on them.

These Windows components provide divergent behavior based on the compatibility section:

**Remote procedure call (RPC) default thread pool**

-   Windows 8 and Windows 7: To improve scalability and reduce thread counts, RPC switched to the NT thread pool (default pool). For Windows Vista, RPC used a private thread pool:

    -   For binaries compiled for Windows 7 and later versions of Windows, the default pool is used.
    -   If I\_RpcMgmtEnableDedicatedThreadPool is called before any RPC API is called, the private thread pool is used (Vista behavior).
    -   If I\_RpcMgmtEnableDedicatedThreadPool is called after an RPC call, the default pool is used, I\_RpcMgmtEnableDedicatedThreadPool returns the error 1764, and the requested operation is not supported.

-   Windows Vista (default): For binaries compiled for Windows Vista and earlier versions of Windows, the private pool is used.

**DirectDraw lock**

-   Windows 8 and Windows 7: Apps manifested for Windows 7 and later versions of the operating system cannot call Lock API in DDRAW to lock the primary desktop video buffer; doing so will result in an error, and a NULL pointer for the primary is returned. This behavior is enforced even if Desktop Window Manager Composition is not turned on. Apps with compatibility declared for Windows 7 and later must not lock the primary video buffer to render.
-   Windows Vista (default): Apps can acquire a lock on the primary video buffer, as legacy apps depend on this behavior; running the app turns off Desktop Window Manager.

**DirectDraw bit-block transfer (bitblt) to primary without clipping window**

-   Windows 8 and Windows 7: Apps manifested for Windows 7 and later versions of Windows are prevented from performing a bitblt to the primary Desktop video buffer without a clipping window; doing so results in an error and the bitblt area will not be rendered. Windows enforces this behavior even if you do not turn on Desktop Window Manager Composition. Apps with compatibility declared for Windows 7 and later must perform a bitblt to a clipping window.
-   Windows Vista (default): Apps must be able to perform a bitblt to the primary without a clipping window, as legacy apps depend on this behavior; running this app turns off the Desktop Window Manager.

**GetOverlappedResult API**

-   Windows 8 and Windows 7: Resolves a race condition where a multithreaded app using **GetOverlappedResult** can return without resetting the event in the overlapped structure, causing the next call to this function to return prematurely.
-   Windows Vista (default): Provides the behavior with the race condition that apps might have a dependency on. Apps that must avoid this race prior to the Windows 7 behavior should wait on the overlapped event and, when signaled, call GetOverlappedResult with bWait == FALSE.

**Shell themes status in high contrast mode**

-   Windows 8: Returns the real theming status for when in high contrast mode.
-   Windows 7: Returns theming as unavailable when in high contrast mode because DWM is still on.
-   Windows Vista (default): Returns theming as unavailable when in high contrast mode because DWM is still on.

**Shell iPersistFile::Save method**

-   Windows 8: CShellLink::Save now determines if the IPersistFile handler is called with a relative path argument and fails the call if it is.

    The [public documentation](/windows/win32/api/objidl/nf-objidl-ipersistfile-save) describing this behavior indicates that path argument has to be an absolute path:

-   Windows 7 and earlier (default): CShellLink::Save does not determine if the iPersistFile handler sends a relative path check and allows apps to continue working with absolute or relative paths.

**Program Compatibility Assistant (PCA)**

-   Windows 8: Apps with the compatibility section do not get the PCA mitigation.
-   Windows 7: Apps with the compatibility section are tracked for potential compatibility issues for Windows 8 changes (described in this document).
-   Windows Vista (default): Apps that fail to install properly or crash during runtime under some specific circumstances get the PCA mitigation. For more info, see the Resources section.

## Leveraging feature capabilities

Update the app manifest with the latest compatibility info for operating system support. This section describes the additions to the manifest:

**Namespace:** Compatibility.v1 (xmlns="urn:schemas-microsoft-com:compatibility.v1">)

**Section name:** Compatibility (new section)

**SupportedOS:** GUID of supported operating system - The GUIDs that map to the supported operating systems are:

-   {e2011457-1546-43c5-a5fe-008deee3d3f0}

    for **Windows Vista**: This is the default value for the switchback context

-   {35138b9a-5d96-4fbd-8e2d-a2440225f93a}

    for **Windows 7**: Apps that set this value in the app manifest get the Windows 7 behavior

-   {4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}

    for **Windows 8**: Apps that set this value in the application manifest get the Windows 8 behavior

Microsoft will generate and post GUIDs for future Windows versions as needed.

An XML example of an updated manifest:

> [!Note]  
> The attribute and tag names in the app manifest are case sensitive.

 


```XML
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0"> 
<compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1"> 
    <application> 
        <!--The ID below indicates app support for Windows Vista -->
        <supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/> 
        <!--The ID below indicates app support for Windows 7 -->
        <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>
        <!--The ID below indicates app support for Windows 8 -->
        <supportedOS Id="{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}"/>
    </application> 
</compatibility>
</assembly>
```



The GUIDs for all the operating systems in the previous example provide down-level support. Apps that support multiple platforms do not need separate manifests for each platform.

## Tests

An app can specify multiple supported operating system IDs. You should add a supported operating system ID if you have tested, or are in the process of testing, the app on that operating system. Windows Vista and prior operating system versions do not pay attention to these entries. Starting with Windows 7, Windows will choose the highest version GUID in the manifest up to the running Windows version, and give the app support at that level. To verify that the app works with the new app manifest compatibility section:

1.  Test the app with the new compatibility section and SupportedOS ID = { 4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38} to ensure that the app works properly using the latest Windows 8 behavior.
2.  Test the app with the new compatibility section and SupportedOS ID = {35138b9a-5d96-4fbd-8e2d-a2440225f93a} to ensure that the app works properly using the Windows 7 behavior.
3.  Test the app with the new compatibility section and SupportedOS ID = {e2011457-1546-43c5-a5fe-008deee3d3f0} to ensure that the app works properly using the Windows Vista behavior.

## Resources

-   [QueryActCtxW Function](../sbscs/application-manifests.md)
-   [UAC manifest](/previous-versions/bb756929(v=msdn.10))
-   [Application Manifests for Windows Applications](../sbscs/application-manifests.md)
-   [Desktop Window Manager (DWM)](../dwm/dwm-overview.md)
-   [Context Mismatch Update](https://support.microsoft.com/kb/978637)
-   [Program Compatibility Assistant](/previous-versions/bb756937(v=msdn.10))

 

 