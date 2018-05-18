---
title: Troubleshooting GUID Errors in Automation
description: Describes how to troubleshooting GUID errors in Automation.
ms.assetid: '5b533c95-517e-4a88-8c2b-f2e26f5f256b'
---

# Troubleshooting GUID Errors in Automation

The following problems are common with GUIDs.

## Problem

**GetObject** can't seem to create an instance of my application.

## Solution

Visual Basic uses the OLE calls listed in Appendix C to find the .exe file that creates an application instance.

Visual Basic proceeds as follows

1.  Looks up the GUID for the object. (For the Hello application, Visual Basic maps the programmatic ID (ProgID) Hello.Application into a GUID).

2.  Finds the object's server (the Hello.exe for the Hello application).

3.  Launches the application.

If an error occurs, check the following:

-   Has the .reg file been run?

-   Are the entries in the registry correct?

-   Do all of the GUIDs match?

-   Can the application be launched? The .exe file for the application, listed in the LocalServer entry, should either be on the path or it should be fully specified. For example:


```C++
c:\ole2\sample\hello\hello.bin
```



## Problem

When I use **GetObject**, the application launches, but the **GetObject** call fails.

## Solution

Normally, when an application is started, a class factory is registered using **CoRegisterClassObject**. Some applications register their class factories only when launched with the **/Automation** switch. If code was inherited, or a sample was copied, determine whether it checks for this switch. The **/Automation** option might appear in the .reg file, the registry, or in the development environment.

## Problem

**GetTypeInfoOfGuid()** fails to get the type information from my type library.

## Solution

When [**GetTypeInfoOfGuid**](itypelib-gettypeinfoofguid.md) is called, a GUID is provided. If this GUID does not match the GUID in the .tlb file, no type information will be returned. The GUID in the code may be declared in a header file. The GUID in the .tlb file can be checked by using Browse.exe, which is provided with OLE, or with the Visual Basic Object Browser.

 

 




