---
description: Application Verifier (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.assetid: edf719b7-9bd9-4e23-9bba-d0d7c3c5dbf5
title: Application Verifier (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.topic: article
ms.date: 05/31/2018
---

# Application Verifier (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)

## Affected Platforms

**Clients** - Windows XP, Windows Vista, Windows 7  
**Servers** - Windows Server 2003, Windows Server 2008, Windows Server 2008 R2  


## Description

Promote and enforce Application Verifier as a quality gate for all development. It includes several improvements:

-   We have provided additional checks to address issues that the Windows Error Reporting team discovered during thread-pool usage.
-   We combined 32- and 64-bit versions of the package to address changes in Windows 7, including the needs for testing 32-bit components under a 64-bit version of Windows, as well as for general simplification.
-   We have included additional checks for multithreaded applications, running 32-bit applications on 64-bit Windows, as well as many bug fixes.

These changes should have no negative impact on users who do not enable the Thread Checks; those who do should receive additional support in discovery and diagnosis of existing thread-pool usage problems. Whether or not you enable Thread Checks, you will benefit from the other improvements and bug fixes in this service.

While there is a slight performance penalty when using this service, the performance levels should remain acceptable because it does not typically run in retail environments.

## Usage

**General Information**

To deliver reliable Windows applications:

1.  Test applications written in unmanaged (native) code with Application Verifier under the debugger and with full-page heap before releasing it to customers.
2.  Follow the steps provided by Application Verifier to resolve errant conditions.
3.  Once your application is released, regularly monitor the application failure reports collected by Windows Error Reporting.

Thread-pool checks are enabled by default under the "Basics" check heading. As this is included in the default setting, users need only to run Application Verifier on their code with the default settings to leverage the new checks.

**Details**

At a minimum, you should run Application Verifier with the Basics setting selected. This is required for WinLogo and WinQual. The Basics setting checks for the following:

-   **Exceptions Stop Details** - Ensures that applications do not hide access violations using structured exception handling
-   **Handles Stop Details** - Tests to ensure the application is not attempting to use invalid handles
-   **Heaps Stop Details** - Checks for memory corruptions issues in the heap
-   **Input/Output Stop Details** - Monitors the execution of asynchronous IO, and performs various validations
-   **Leak Stop Details** - Detects leaks by tracking the resources made by a dll that are not freed by the time the dll was unloaded
-   **Locks Stop Details** - Verifies the correct usage for critical sections
-   **Memory Stop Details** - Ensures APIs for virtual space manipulations are used correctly (for example, VirtualAlloc, MapViewOfFile)
-   **TLS Stop Details** - Ensures that Thread Local Storage APIs are used correctly
-   **Threadpool Stop Details** - Ensures correct usage of threadpool APIs and enforces consistency checks on worker-thread-states after a callback

If your application is migrating from a "Pre-Vista" application, you will want to leverage the "LuaPriv" (also known as UAC checks). The Limited User Account Privilege Predictor (LuaPriv) has two primary goals:

-   **Predictive**: While running an application with administrative privilege, predict whether that application would work as well if run with less privilege (generally, as a normal user). For example, if the application writes to files that only allow Administrators access, then that application will not be able to write to the same file if run as a non-administrator.
-   **Diagnostic**: While running with non-administrator privilege, identify potential problems that may already exist with the current run. Continuing the previous example, if the application tries to write to a file that grants only Administrator group members access, the application will get an ACCESS\_DENIED error. If the application does not operate correctly, this operation may be the culprit.

LuaPriv identifies the following types of problems:



| **Potential Issue**       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Restricted Namespaces     | Creating a named synchronization object (Event, Semaphore, Mutex, etc) without a namespace may complicate running without privilege on some operating systems because the operating system may choose to place the object in a restricted namespace. Creating such an object in a restricted namespace (such as the Global namespace) requires SeCreateGlobalPrivilege, which is granted only to administrators.<br/> LuaPriv flags both these issues if it detects them.<br/> |
| Hard Administrator Checks | Some applications interrogate the user's security token to find out how much privilege he/she has. In those cases, the application may change its behavior depending on how much power it thinks the user has. <br/> LuaPriv flags API calls that return this information.<br/>                                                                                                                                                                                                |
| Requesting Privileges     | An application may attempt to enable a security-relevant privilege (such as SeTcbPrivilege or SeSecurityPrivilege) prior to performing an operation that requires it. <br/> LuaPriv flags attempts to enable security-relevant privileges. <br/>                                                                                                                                                                                                                               |
| Missing Privileges        | If an application attempts to enable a privilege that the user does not have, it probably signals that the application expects the privilege, which can cause behavior differences. <br/> LuaPriv flags failed privilege requests. <br/>                                                                                                                                                                                                                                       |
| INI-File Operations       | Attempts to write to mapped INI files (WritePrivateProfileSection and similar APIs) can fail as a non-administrator user. <br/> LuaPriv flags such operations.<br/>                                                                                                                                                                                                                                                                                                            |
| Access Denied             | If the application attempts to access an object (File, registry key, etc) but the attempt fails due to insufficient access, then the application probably expects to be running with more privilege than it has. <br/> LuaPriv flags object-open attempts that fail with ACCESS\_DENIED and similar errors.<br/>                                                                                                                                                               |
| Deny ACEs                 | If an object has Deny ACEs in its DACL, then it explicitly denies access to specific entities. <br/> This is uncommon, and makes prediction difficult, so LuaPriv flags Deny ACEs when it finds them.<br/>                                                                                                                                                                                                                                                                     |
| Access Restricted         | If an application attempts to open an object for rights that are not granted to normal users (for example, trying to write to a file that is only writeable by administrators), then the application probably will not work the same when run as a normal user. <br/> LuaPriv flags such operations.<br/>                                                                                                                                                                      |
| MAXIMUM\_ALLOWED          | If an application opens an object for MAXIMUM\_ALLOWED, then the actual access check on the object will occur elsewhere. Most code that does this does not work correctly, and will almost certainly work differently when run without privilege. <br/> LuaPriv thus flags all incidents of MAXIMUM\_ALLOWED. <br/>                                                                                                                                                            |



 

Commonly overlooked issues are captured in the nebulous Misc Checks:

-   Dangerous APIs Stop Details
-   Dirty Stacks Stop Details
-   Time Rollover

We have added a new Print Verifier. This layer helps find and troubleshoot issues that may result when an application calls the print subsystem. Print Verifier targets the two layers of the print subsystem, the PrintAPI layer and the PrintDriver layer.

*Print API Layer*

Print Verifier tests the interface between a program and Winspool.drv and prntvpt.dll and tests the interfaces of those DLLs. You can review the rules for calling functions in this interface in the MSDN help section for APIs exported by winspool.drv and prntvpt.dll.

*Print Driver Layer*

Print Verifier also tests the interface between a core print driver such as UNIDRV.DLL, UNIDRUI.DLL, PSCRIPT5.DLL, PS5UI.DLL, or MXDWDRV.DLL, and the print driver plug-ins. You can find information about this interface in the MSDN and the WDK.

Note that some of these checks are for Windows 7 only, and others will simply perform better under Windows 7.

Typically, only debug versions run the Application Verifier, so performance is not generally an issue. If performance issues arise from the use of this, or any other Application Verifier check, run one check at a time until you have performed all needed checks.

Nearly 10% of application crashes on Windows systems are due to heap corruption. These crashes are nearly impossible to debug after the fact. The best way to avoid these issues is to test with the Page Heap features found in Application Verifier. There are two flavors of Page Heap: "Full" and "Light." Full is the default; it will force a debugger stop instantly upon detecting corruption. This feature MUST be run while under the debugger. However, it is also the most resource demanding. If a user is having timing issues and has already run a scenario under "Full" Page Heap, setting it to "Light" will likely address these issues. Additionally, Light Page Heap does not crash until the process exits. It does provide a stack trace to the allocation, but can take considerably longer to diagnose than leveraging its Full counterpart.

Monitor the reliability status of the applications via the Winqual web portal. This portal shows the error reports collected via Windows Error Reporting, so it is easy to identify the most frequent failures. Learn about this at Windows Error Reporting: Getting Started. Microsoft does not charge for this service.

To take advantage of WinQual, you must:

1.  Register your company for WinQual, which requires a VeriSign ID. You can find Windows 7 information about WinQual in the developer portal grouped under Windows Vista SP1 \\ Windows Server 2008. It will have a Windows 7 location soon.
2.  Map the ISV applications to a product name and the ISV name, which links the failure reports to the company. Other ISVs cannot view your error reports.
3.  Use the portal to identify top issues. ISVs can also create responses that inform customers what steps to take after a failure. The response system supports over 10 languages worldwide.

One further note: Application Verifier is only as good as the code paths you run it against. The value of combining this tool with a code coverage tool cannot be overstated.

## Links to Other Resources

**Debugging Tools for Windows:**

-   [Overview and download site](https://msdn.microsoft.com/windows/hardware/bg127145)
-   [MSDN online documentation](/windows-hardware/drivers/debugger/)

**Application Verifier:**

-   [Overview](/previous-versions/ms220948(v=vs.80))
-   [Download](https://www.microsoft.com/downloads/details.aspx?FamilyID=c4a25ab9-649d-4a1b-b4a7-c9d8b095df18&amp;DisplayLang=en)
-   [Application Verifier for Microsoft Visual Studio 2008/.NET Framework 3.5](/previous-versions/ms220948(v=vs.80))

    **Note:** the Application Verifier version that ships in Visual Studio is quite dated. If possible, use the standalone package instead. For this reason, future versions of Visual Studio will no longer have embedded Application Verifier.

**WinQual:**

-   [Create a WLK hardware submission package - Winqual tool](/windows-hardware/drivers/dashboard/hardware-submission-wlk)
-   [Windows Error Reporting: Getting Started](../wer/using-wer.md)

 

 
