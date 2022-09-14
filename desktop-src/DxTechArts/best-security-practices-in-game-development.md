---
title: Best Security Practices in Game Development
description: Describes best security practices to use in game development and provides examples of insecure code.
ms.assetid: 20956529-42ed-722b-cfa3-e3230d89fdd7
ms.topic: article
ms.date: 05/31/2018
---

# Best Security Practices in Game Development

This article discusses best practices to use in game development.

-   [Introduction](#introduction)
-   [Examples of Insecure Code](#examples-of-insecure-code)
-   [Ways to improve security](#ways-to-improve-security)
-   [Summary](#summary)

## Introduction

An increasing number of people play online games and games with user-made content. This, combined with the increasing security of the Microsoft Windows Operating System, means that games are a growing and more tempting target for attackers to exploit. Game developers should place a strong emphasis on making sure that the games they release aren't creating new security holes for attackers to exploit. Game developers have a responsibility and a vested interest in helping to prevent their customers' computers from being hacked by malicious network data, user modifications, or tampering. If a vulnerability is exploited, it could result in losing customers and/or money. This article outlines and explains some common methods and tools to increase code security without over-inflating development time.

The three most common mistakes made by a development team when releasing a product are:

-   Requiring administrative privileges. Games should not require administrative privileges. For more details, see [User Account Control for Game Developers](./user-account-control-for-game-developers.md).
-   Not using automated protection. Developers are generally not using **/GS**, **/SAFESEH**, or **/NX**. Using these compile/link flags can spot or eliminate many basic security holes without significantly increasing workload. These flags are discussed later in this article.
-   Using forbidden APIs. There are many APIs (**strcpy**, **strncpy**, and so on) that are prone to programmer error and easily generate security holes. Developers should replace these APIs with the safe versions. Visual Studio 2005 comes with a tool for analyzing binary files that can automatically check object files for references to unsafe APIs. For more information on what to do with information generated with this tool, see [Repel Attacks on Your Code with the Visual Studio 2005 Safe C and C++ Libraries](/archive/msdn-magazine/2005/may/repel-attacks-with-visual-studio-2005-safe-c-and-c-libraries) by Martyn Lovell. Also, you can get the [banned.h](https://www.microsoft.com/downloads/details.aspx?FamilyID=6aed14bd-4766-4d9d-9ee2-fa86aad1e3c9) header file that can help you remove banned functions from code.

Each of the listed mistakes is not only common but is easily correctable with no significant change in development workload, coding standards, or functionality.

## Examples of Insecure Code

The following is a simple example of all it takes to allow an attacker to perform a buffer overrun attack:


```
void GetPlayerName(char *pDatafromNet)
{
    char playername[256]; 
    strncpy(playername, pDatafromNet, strlen(pDatafromNet));

    // ...
}
```



On the surface this code looks ok — it calls a safe function, after all. Data from the network is copied into a buffer that is 256 bytes. The **strncpy** function relies on finding a NULL terminator in the source string or is limited by the provided buffer count. The problem is that the buffer size is incorrect. If data from the network isn't validated or the buffer size is wrong (as in this example), an attacker could simply provide a large buffer to overwrite stack data, after the buffer ends, with any data in the network packet. This would allow the attacker to execute arbitrary code by overwriting the instruction pointer and changing the return address. The most basic lesson of this example is to never trust input until it has been verified.

Even if data doesn't come from the network initially, there still is potential risk. Modern game development requires many people designing, developing, and testing the same code base. There is no way to know how the function will be called in the future. Always ask yourself where the data came from and what could an attacker control? While network-based attacks are the most common, they are not the only methods of creating security holes. Could an attacker create a mod or edit a saved file in a way that opens a security hole? What about user-supplied image and sound files? Malicious versions of these files could be posted on the Internet and create dangerous security risks for your customers.

As a side note, use strsafe.h or Safe CRT instead of **strncpy** to correct the example. Safe CRT is a complete security overhaul of the C Runtime and comes with part of Visual Studio 2005. More information about Safe CRT can be found in [Security Enhancements in the CRT](https://msdn.microsoft.com/library/8ef0s5kh(VS.80).aspx) by Michael Howard.

## Ways to improve security

There are several ways to improve security in the development cycle. Here are some of the best ways:

<dl> <dt>

<span id="Reading_about_security"></span><span id="reading_about_security"></span><span id="READING_ABOUT_SECURITY"></span>Reading about security
</dt> <dd>

The book, *Writing Secure Code, Second Edition* by Michael Howard and David LeBlanc, provides an in-depth and clear explanation of strategies and methods of preventing attacks and mitigating exploits. Starting with methods of designing security into a release to techniques for securing network applications, the book covers all aspects that a game developer needs to help protect themselves, their products, and their customers from attackers. The book can be used to instill a culture of security in a development studio. Don't just think of code security as a developer's problem or a tester's problem. Think of security as something the whole team — from program manager to designer to developer to tester — should be thinking about when they work on a project. The more eyes that are part of the review process, the greater the chance of catching a security hole prior to release.

*Writing Secure Code, Second Edition* can be found at the [Microsoft Press Store](https://www.microsoftpressstore.com/store/writing-secure-code-9780735617223) and more general security information can be found in [Fending Off Future Attacks by Reducing Attack Surface](/previous-versions/ms972812(v=msdn.10)) by Michael Howard.

Michael Howard, David LeBlanc, and John Viega have written another book on the subject that covers all common operating systems and programming languages entitled, *19 Deadly Sins of Software Security*.

Security presentations focused on games can be found at the [Microsoft XNA Developer Presentations](/previous-versions/dn629515(v=msdn.10)) download page.

</dd> <dt>

<span id="Threat_Modeling_Analysis"></span><span id="threat_modeling_analysis"></span><span id="THREAT_MODELING_ANALYSIS"></span>Threat Modeling Analysis
</dt> <dd>

A threat modeling analysis is a good way of assessing system security, not in a specific language or by using a tool, but in a broad, end-to-end method that can be accomplished in a few meetings. When implemented properly, a thread model can identify all of the strengths and weaknesses of a system, without adding significant workload or meeting time to the project. The method of threat modeling also emphasizes the idea of assessing system security prior to and during the development process to help ensure that a comprehensive assessment is being made while focusing on the most risky features. It can be thought of as a profiler for security. By not being based on a particular language or relying on a specific tool, threat modeling can be used in any development studio working on any project in any genre. Threat modeling is also an excellent method of reinforcing the idea that security is everyone's responsibility and not someone else's problem.

When threat modeling, pay special attention to:

-   UDP data sources
-   Data sources that don't require authentication
-   Data sources that are frequently and normally probed as part of wide-scale information gathering
-   Any ability of a client to directly send data to other clients

These are the areas that have good potential for security weaknesses.

More on Threat Modeling can be found at [Threat Modeling](https://technet.microsoft.com/security/) on the MSDN Security Development Center and in the book [Threat Modeling](https://www.amazon.com/Threat-Modeling-Microsoft-Professional-Swiderski/dp/0735619913) by Frank Swiderski and Window Snyder.

</dd> <dt>

<span id="Data_Execution_Prevention___NX_"></span><span id="data_execution_prevention___nx_"></span><span id="DATA_EXECUTION_PREVENTION___NX_"></span>Data Execution Prevention (/NX)
</dt> <dd>

A recent tool in mitigating multiple exploits is data execution prevention (DEP). If you include the switch **/NX** in the build command, Visual Studio will mark memory pages with flags that denote whether the code has the right to execute or not. Any program attempting to execute in a memory page not flagged with EXECUTE permission will cause a forcible termination of the program. The prevention is enforced on the processor level and will impact developers who are using self-modifying code or native JIT language compilers. Currently, only AMD's Athlon64 and Opteron processors and Intel's Itanium and latest Pentium 4 processors support execution prevention, but it is expected that all 32-bit and 64-bit processors will support execution prevention in the future. (A copy-protection scheme used by a developer may be affected by execution prevention, but Microsoft has been working with copy-protection vendors to minimize the impact.) It is a good practice to use DEP.

For more details on DEP, see [Data Execution Prevention](../memory/data-execution-prevention.md).

</dd> <dt>

<span id="Buffer_Security_Check___GS__and_Image_has_Safe_Exception_Handlers___SAFESEH_"></span><span id="buffer_security_check___gs__and_image_has_safe_exception_handlers___safeseh_"></span><span id="BUFFER_SECURITY_CHECK___GS__AND_IMAGE_HAS_SAFE_EXCEPTION_HANDLERS___SAFESEH_"></span>Buffer Security Check (/GS) and Image has Safe Exception Handlers (/SAFESEH)
</dt> <dd>

*Buffer Security Check*, specified by the compiler flag **/GS**, and *Image has Safe Exception Handlers*, specified by the linker flag **/SAFESEH** (first implemented in Visual Studio .NET 2003), can make the developer's job of securing code a little easier.

Using the **/GS** flag causes the compiler to construct a check for some forms of stack-based buffer overruns that could be exploited to overwrite the return address of a function. Using **/GS** will not detect every potential buffer overrun and shouldn't be considered a catch-all, but a good defense-in-depth technology.

Using the **/SAFESEH** flag will instruct the linker to only generate an executable or DLL if it can also generate a table of the safe exception handlers of the executable or DLL. Safe Structured Exception Handling (SafeSEH) eliminates exception handling as a target of buffer overrun attacks by ensuring that, before an exception is dispatched, the exception handler is registered in the function table located within the image file. These protection benefits are enabled with Windows XP SP2, Windows Server 2003, Windows Vista, and Windows 7. Also for **/SAFESEH** to work properly, it must be used in an all-or-nothing method. All libraries containing code bound to an executable or DLL must be compiled with **/SAFESEH** or the table will not be generated.

More information about [Buffer Security Check](https://msdn.microsoft.com/library/8dbf701c(vs.71).aspx) (**/GS**) and [Image has Safe Exception Handlers](https://msdn.microsoft.com/library/9a89h429(vs.71).aspx) (**/SAFESEH**) can be found in MSDN.

See also info about Microsoft Visual Studio 2012's [**/SDL** flag](/cpp/build/reference/sdl-enable-additional-security-checks) and Visual Studio 2012's [enhancements to the **/GS** flag](https://www.microsoft.com/security/blog/2012/01/26/enhancements-to-gs-in-visual-studio-11/).

</dd> <dt>

<span id="PREfast"></span><span id="prefast"></span><span id="PREFAST"></span>PREfast
</dt> <dd>

PREfast is a free tool offered by Microsoft that analyzes execution paths in compiled C or C++ to help find run-time bugs. PREfast operates by working through all execution paths in all functions and assessing each path for problems. Originally used to develop drivers and other kernel code, this tool can help game developers save time by eliminating some bugs that are hard to find or are ignored by the compiler. Using PREfast is an excellent way of reducing workload and focusing the efforts of both the development team and test team. PREfast is available in Visual Studio Team Suite and Visual Studio Team Edition for Software Developers as Code Analysis, enabled by the compiler switch **/analyze**. (This option is also available in the free version of the compiler that ships with the Windows Software Development Kit.)

> [!Note]  
> Visual Studio 2012 supports **/analyze** in all editions. For more info about code analysis availability in all editions of Visual Studio, see [What’s New in Code Analysis](/archive/blogs/codeanalysis/?m=20123).

 

Through the use of header annotation (particularly for buffer pointer arguments), PREfast can expose additional issues, such as memory overwrite bugs, a common source of crashes and potential security vulnerabilities. This is done by using the Standard Annotation Language (SAL), which is a form of mark-up for C/C++ function prototypes that provide additional information about expected pointer argument semantics and correlation with length parameters, declared buffer sizes, etc. All of the headers for Windows operating systems are annotated, and adding SAL mark-up in public API headers in your own libraries enables PREfast to perform more detailed and aggressive checks in your client code for such APIs. For an introduction to SAL and links to more information, see Michael Howard's blog entry, "[A Brief Introduction to the Standard Annotation Language (SAL)](/archive/blogs/michael_howard/a-brief-introduction-to-the-standard-annotation-language-sal)."

</dd> <dt>

<span id="Windows_Application_Verifier"></span><span id="windows_application_verifier"></span><span id="WINDOWS_APPLICATION_VERIFIER"></span>Windows Application Verifier
</dt> <dd>

The Windows Application Verifier, or AppVerifier, can help testers by providing multiple functions in one tool. The AppVerifier is a tool that was developed to make common programming errors more testable. AppVerifier can check parameters passed to API calls, inject erroneous input to check error handling ability, and log changes to the registry and file system. AppVerifier can also detect buffer overruns in the heap, check that an Access Control List (ACL) has been properly defined, and enforce the safe use of socket APIs. While not exhaustive, AppVerifier can be one tool in the tester's toolbox to help a development studio release a quality product.

For more information about Application Verifier, see [Application Verifier](/previous-versions/visualstudio/visual-studio-2008/ms220948(v=vs.90)) and [Using Application Verifier Within Your Software Development Lifecycle](/previous-versions/aa480483(v=msdn.10)) on MSDN.

</dd> <dt>

<span id="Fuzz_Testing"></span><span id="fuzz_testing"></span><span id="FUZZ_TESTING"></span>Fuzz Testing
</dt> <dd>

*Fuzz testing* is a semi-automated method of testing that can enhance current testing methodologies. The central idea behind fuzz testing is to make a full assessment of all inputs by inputing random data to see what breaks; this includes all network data, mods and saved games, etc. Fuzz testing is fairly easy to do. Simply alter well-formed files or network data by inserting random bytes, flipping adjacent bytes, or negating numerical values. 0xff, 0xffff, 0xffffffff, 0x00, 0x0000, 0x00000000, and 0x80000000 are values that are good at exposing security holes while fuzz testing. You can observe the resulting interaction combinations using AppVerifier. While fuzzing is not exhaustive, it is easy to implement and automate, and it can catch the more elusive and unpredictable bugs.

For more information on fuzz testing, see the [Gamefest 2007](/previous-versions/dn629515(v=msdn.10)) presentation *Practical Steps in Game Security*.

</dd> <dt>

<span id="Authenticode_Signing"></span><span id="authenticode_signing"></span><span id="AUTHENTICODE_SIGNING"></span>Authenticode Signing
</dt> <dd>

Authenticode is a method of ensuring that executable files, DLL files, and Windows installer packages (.msi files) that the user receives are unaltered from what a developer released. By using a combination of cryptographic principles, trusted entities, and industry standards, Authenticode verifies the integrity of executable content. Microsoft provides a cryptographic API, CryptoAPI, that can be used to auto-detect tampering of signed code. If a security leak occurs after a release, a certificate can be revoked and all code signed with that certificate will stop authenticating. Revoking a certificate will revoke the validation of all titles signed with that certificate. Windows has been designed to work with Authenticode signing and will alert a user of unsigned code, in specific situations, that could expose a user's PC to attack.

Authenticode should not be considered a method of eliminating security issues, but a method of detecting tampering after an executable has been released. An executable or DLL that contains an exploitable security issue can be signed and verified using Authenticode, but it will still introduce the security issue to the new system. Only after a product or update has been verified to be secure should the code be signed to assure users that they have a release that hasn't been tampered with.

Even if a developer feels that there is no threat of their releases being modified, other technologies and services rely on Authenticode. Code signing is easy to integrate and automate; there is no reason for developers to not have their releases signed.

For more information on Authenticode signing, see [Authenticode Signing for Game Developers](./authenticode-signing-for-game-developers.md).

</dd> <dt>

<span id="Minimize_Privileges"></span><span id="minimize_privileges"></span><span id="MINIMIZE_PRIVILEGES"></span>Minimize Privileges
</dt> <dd>

In general processes should run with the minimum set of privileges required to operate. On Windows Vista and Windows 7, this is accomplished by using [User Account Control](./user-account-control-for-game-developers.md), allowing the game to run as a Standard User rather than an administrator. For Windows XP, typically games are always running as administrator. Even on Windows Vista and Windows 7, it is sometimes necessary to elevate to full administrator rights for some specific operations.

In the cases where the process is running with full administrative rights, usually only a few rights beyond those of a Standard User are actually required. Administrative access includes many rights that are not required by legitimate code, but could be used by an attacker, through some weakness in the process. Examples of such rights include SE\_TAKE\_OWNERSHIP, SE\_DEBUG, SE\_CREATE\_TOKEN, SE\_ASSIGNPRIMARYTOKEN, SE\_TCB, SE\_SECURITY, SE\_LOAD\_DRIVER, SE\_SYSTEMTIME, SE\_BACKUP, SE\_RESTORE, SE\_SHUTDOWN, and SE\_AUDIT (see [Priviledge Constants](../secauthz/privilege-constants.md)).

While a process cannot gain more rights once started, it can easily give up rights. At startup, the process can immediately use Win32 APIs to remove rights that it does not require.

</dd> <dt>

<span id="Utilize_Windows_Security_Features"></span><span id="utilize_windows_security_features"></span><span id="UTILIZE_WINDOWS_SECURITY_FEATURES"></span>Utilize Windows Security Features
</dt> <dd>

Windows Vista and Windows 7 includes a number of new features that improve code security. [User Account Control](./user-account-control-for-game-developers.md) is certainly the most important one to understand and embrace, but there are other features as well. In addition to the Windows XP SP2 technologies, such as the Windows Firewall, Data Execution Prevention, Buffer Security Check, and Safe Exception Handlers which are also available on Windows Vista and Windows 7, there are three newer security features to consider:

-   The opt-in Address Space Layout Randomization feature. This is enabled by linking with the option **/DYNAMICBASE** on Visual Studio 2005 Service Pack 1 or Visual Studio 2008. This causes the system to randomize the positions of many of the key system DLLs in your process space, making it much more difficult to write exploitable attack programs that propagate broadly across the Internet. This linker flag is ignored by Windows XP and older versions of Windows.
-   Heap corruption can lead to an entire class of security exploits, so the memory system of Windows Vista and Windows 7 now supports a mode which terminates the process if heap corruption is detected. Calling [**HeapSetInformation**](/windows/win32/api/heapapi/nf-heapapi-heapsetinformation) with **HeapEnableTermianteOnCorruption** will opt-in to this behavior. This call fails on Windows XP and older version of Windows.
-   When writing services, they can be configured using a new feature to specify which privileges are actually required, as well as to limit resource access to a specific SID. This is done through [ChangeSeviceConfig2](/windows/win32/api/winsvc/nf-winsvc-changeserviceconfig2a), using SERVICE\_CONFIG\_REQUIRED\_PRIVILEGES\_INFO and SERVICE\_CONFIG\_SERVICE\_SID\_INFO.

</dd> </dl>

## Summary

Developing a game for the current and future marketplace is costly and time consuming. Releasing a game with security issues will ultimately cost more money and time to properly fix. So, it is in the interests of all game developers to integrate tools and techniques to mitigate security exploits prior to release.

The information in this article is just an introduction to what a development studio can do to help themselves and their customers. More information of general security practices and security information can be found at [Microsoft Security Developer Center](https://technet.microsoft.com/security/).

 

 