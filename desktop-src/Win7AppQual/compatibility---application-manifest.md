---
description: Application Manifest
ms.assetid: f022374d-ea3f-477f-9b59-3188b775ed64
title: Application Manifest
ms.topic: article
ms.date: 05/31/2018
---

# Application Manifest

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

Windows 7 introduces a new section in the application manifest called "Compatibility." This section helps Windows determine the versions of Windows that an application was designed to target, and enables Windows to provide the behavior that the application expects based on the version of Windows that the application targeted.

The Compatibility section allows Windows to provide new behavior to new developer-created software while maintaining the compatibility for existing software. This section also helps Windows deliver greater compatibility in future versions of Windows as well. For example, an application declaring support only for Windows 7 in the Compatibility section will continue to receive Windows 7 behavior in future version of Windows.

## Manifestation of Change

Applications without a Compatibility section in their manifest will receive Windows Vista behavior by default on Windows 7 and future Windows versions. Note that Windows XP and Windows Vista ignore this manifest section and it has no impact on them.

The following Windows components provide divergent behavior based on the Compatibility section in Windows 7:

**RPC Default Thread Pool**

-   **Windows 7:** To improve scalability and reduce thread counts, RPC switched to the NT thread pool (default pool). For Windows Vista, RPC used a private thread pool.
    -   For binaries compiled for Win7 the default pool is used
    -   If I\_RpcMgmtEnableDedicatedThreadPool is called before any RPC API is called, the private thread pool is used (Vista behavior)
    -   If I\_RpcMgmtEnableDedicatedThreadPool is called after an RPC call, the default pool is used, I\_RpcMgmtEnableDedicatedThreadPool returns the error 1764, and the requested operation is not supported
-   **Windows Vista (default):** For binaries compiled for Windows Vista and below, the private pool is used.

**DirectDraw Lock**

-   **Windows 7:** Applications manifested for Windows 7 cannot call Lock API in DDRAW to lock the primary Desktop video buffer. Doing so will result in error, and **NULL** pointer for the primary will be returned. This behavior is enforced even if Desktop Window Manager Composition is not turned on. Windows 7 compatible applications must not lock the primary video buffer to render.
-   **Windows Vista (default):** Applications will be able to acquire a lock on the primary video buffer as legacy applications depend on this behavior. Running the application turns off Desktop Window Manager.

**DirectDraw Bit Block Transfer (Blt) to Primary without Clipping Window**

-   **Windows 7:** Applications manifested for Windows 7 are prevented from performing Blt's to the primary Desktop video buffer without a clipping window. Doing so will result in error and the Blt area will not be rendered. Windows enforces this behavior even if you do not turn on Desktop Window Manager Composition. Windows 7 compatible applications must Blt to a clipping window.
-   **Windows Vista (default):** Applications must be able to Blt to the primary without a clipping window as legacy applications depend on this behavior. Running this application turns off the Desktop Window Manager.

**GetOverlappedResult API**

-   **Windows 7:** Resolves a race condition where a multithreaded app using GetOverlappedResult can return without resetting the event in the overlapped structure, causing the next call to this function to return prematurely.
-   **Windows Vista (default):** Provides the behavior with the race condition that applications may have a dependency on. Applications wishing to avoid this race prior to the Windows 7 behavior should wait on the overlapped event and when signaled, call GetOverlappedResult with bWait == **FALSE**.

**Program Compatibility Assistant (PCA)**

-   **Windows 7:** Applications with Compatibility section will not get the PCA mitigation.
-   **Windows Vista (default):** Applications that fail to install properly or crash during runtime under some specific circumstances will get the PCA mitigation. For more details, see the reference section.

## Leveraging Feature Capabilities

Update the application manifest with the latest Compatibility information for operating system support. The section describes the additions to the manifest:

-   **Namespace:** Compatibility.v1 (xmlns="urn:schemas-microsoft-com:compatibility.v1">)

-   **Section Name:** Compatibility (new section)

-   **SupportedOS:** GUID of supported operating system - The GUIDs that map to the supported operating systems are:

    -   {e2011457-1546-43c5-a5fe-008deee3d3f0} for Windows Vista: This is the default value for the switchback context.
    -   {35138b9a-5d96-4fbd-8e2d-a2440225f93a} for Windows 7: Applications that set this value in the application manifest get the Windows 7 behavior.

    > [!Note]  
    > Microsoft will generate and post GUIDs for future Windows versions as needed.

     

The following is an example of an updated manifest.

> [!Note]  
> The attribute and tag names in the application manifest are case sensitive.

 


```XML
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
  <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0"> 
    <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1"> 
      <application> 
        <!--The ID below indicates application support for Windows Vista --> 
          <supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/> 
        <!--The ID below indicates application support for Windows 7 --> 
          <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/> 
      </application> 
    </compatibility>
  </assembly>
```



The value of adding GUIDs for both operating systems in the above example is to provide down-level support. Applications that support both platforms would not need separate manifests for each platform.

## Compatibility, Performance, Reliability, and Usability Testing

1.  Test the application with the new compatibility section and `SupportedOS ID ={35138b9a-5d96-4fbd-8e2d-a2440225f93a}` to ensure that the application works properly using the latest Windows 7 behavior
2.  Test the application with the new compatibility section and `SupportedOS ID ={e2011457-1546-43c5-a5fe-008deee3d3f0}` (or without this section entirely) to ensure that the application works properly using the Windows Vista behaviors on Windows 7

## Known Issues

**Context Mismatch** An application runs in a Windows Vista context instead of in a Windows 7 context on a computer that is running an x64 edition of either Windows 7 or Windows Server 2008 R2.

**Solution** Updates are available to correct this for all supported x64-based versions of Windows 7 and Windows Server 2008 R2, as well as for all supported Itanium-based versions of Windows Server 2008 R2. Go to the Microsoft Support page for [KB 978637: An application runs in a Windows Vista context instead of in a Windows 7 context on a computer that is running an x64 edition of Windows 7 or of Windows Server 2008 R2](https://support.microsoft.com/kb/978637) for additional details and to download the correct version for your system.

**Crash dump diagnosis blocked**

**Solution** Go to the Microsoft Support page for KB 976038: Exceptions that are thrown from an application that runs in a 64-bit version of Windows are ignored  for additional details.

## Links to Other Resources

-   [**QueryActCtxW Function**](/windows/win32/api/winbase/nf-winbase-queryactctxw)
-   [UAC manifest](/previous-versions/bb756929(v=msdn.10))
-   [Application manifests for Windows applications](../sbscs/application-manifests.md)
-   [Desktop Window Manager (DWM)](../dwm/dwm-overview.md)
-   [Context Mismatch Update](https://support.microsoft.com/kb/978637)

 

 
