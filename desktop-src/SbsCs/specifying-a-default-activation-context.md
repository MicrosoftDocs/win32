---
description: Specifying a Default Activation Context
ms.assetid: 4d9a8552-7098-458d-a592-45524871cce5
title: Specifying a Default Activation Context
ms.topic: article
ms.date: 05/31/2018
---

# Specifying a Default Activation Context

When your application or component creates a new process, Windows searches for a default application manifest. Note that a manifest included as a resource in the application takes precedence over an external manifest. The default activation context is the first activation context that is active before any other activation context has been activated. This activation context is always active unless you activate other contexts. If you define ISOLATION\_AWARE\_ENABLED when you compile your application or component, calls like [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance), [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya), and [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) can perform automatic context management.

The loader allows an application to specify its default activation context by two methods. You can put the manifest file in the resources of the executable and the loader will find it. This is the same as putting the manifest file in the executable's resource table. You can place the manifest in a file named *Myapp*.exe.Manifest in the same directory as *Myapp*.exe, and the loader finds it while looking for *Myapp*.exe.

If you use none of these methods, the application starts with the system default activation context, which contains a minimal set of assemblies.

A better way of using automatic context management is by compiling your application with ISOLATION\_AWARE\_ENABLED defined. The recommended method is to set this on the compiler's command line for the entire project being built rather than being set in individual source files or headers. This makes most Win32 APIs aware of activation contexts and how to manage them. Instead of having to do your own activation context management, you simply need to place a manifest in your resource table at resource ID ISOLATIONAWARE\_MANIFEST\_RESOURCE\_ID (numeric value 2), of type RT\_MANIFEST (numeric value 24.) Functions such as [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa), [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance), and [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) then automatically activate this context before making the actual call.

Note that if you compile with ISOLATION\_AWARE\_ENABLED defined, you cannot also do your own activation context management. With ISOLATION\_AWARE\_ENABLED defined, Windows ignores any dynamic activation context creation your application may attempt to do between [**ActivateActCtx**](/windows/desktop/api/Winbase/nf-winbase-activateactctx) and [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) calls. This means that when your application uses ISOLATION\_AWARE\_ENABLED you must make sure that the manifest contains a complete list of all assemblies that your component requires.

 

 
