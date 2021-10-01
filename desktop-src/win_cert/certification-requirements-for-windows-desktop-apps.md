---
title: Desktop certification requirements
description: Document version 10Document date July 29, 2015This document contains the technical requirements and eligibility qualifications that a desktop app must meet in order to participate in the Windows 10 Desktop App Certification Program.
ms.assetid: 0F19774E-5258-4152-BBD7-9C37A05C7F69
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name:
api_type:
api_location:
---

# Certification requirements for Windows Desktop Apps

**Document version:** 10

**Document date:** July 29, 2015

This document contains the technical requirements and eligibility qualifications that a desktop app must meet in order to participate in the Windows 10 Desktop App Certification Program.

## Welcome!

The Windows platform supports a broad ecosystem of products and partners. Displaying the Windows logo on your product represents a relationship and a shared commitment to quality between Microsoft and your company. Customers trust the Windows brand on your product because it ensures that it meets compatibility standards and performs well on the Windows platform. Successfully passing Windows App Certification allows for your app to be showcased in the Windows Compatibility Center and you may display the certification logo on your site.

The Windows App Certification Program is made up of program and technical requirements to help ensure that third-party apps carrying the Windows brand are both easy to install and reliable on PCs running Windows. Customers value stability, compatibility, reliability, performance, and quality in the systems they purchase. Microsoft focuses its investments to meet these requirements for software apps designed to run on the Windows platform for PCs. These efforts include compatibility tests for consistency of experience, improved performance, and enhanced security on PCs running Windows software. Microsoft compatibility tests have been designed in collaboration with industry partners and are continuously improved in response to industry developments and consumer demand.

The Windows App Certification Kit is used to validate compliance with these requirements and replaces the any previous versions of the kit used to validate on Windows 7, Windows 8 or Windows 8.1. The Windows App Certification Kit is one of the components included in the Windows Software Development Kit (SDK) for Windows 10.

## App eligibility

For an app to qualify for Windows 10 Desktop App Certification it must meet the following criteria and all the technical requirements listed in this document.

-   It must be a standalone app
-   It must run on a local Windows 10 PC
-   It can be a client component of a certified Windows Server app
-   It must be code and feature complete
-   It must not communicate with Windows Store apps via local mechanisms, including via files and registry keys, except in the supported enterprise scenarios
-   It must not jeopardize or compromise the security or functionality of the Windows system
-   It must have a unique name and must not be trademarked by others
-   All external components must be certified separately or be compliant with the Windows App Certification Kit
-   It must have an opt-out option for any bundled apps

If the desktop app is submitted to the anti-virus and/or anti-spyware (i.e., antimalware) products category, it must comply with the ANTIMALWARE PLATFORM GUIDELINES. The WINDOWS 10 ANTIMALWARE API LICENSE AND LISTING AGREEMENT must have been signed and in effect before submission. The partner must be a member of, or have researchers that are members of and in good standing in one the organizations listed in the agreement. The functionality must be certified on Windows 10 by one the organizations listed in the agreement. The app must have been tested at least once in the last 12 months, and certified for detection and cleaning.

## 1. Apps are compatible and resilient

The times when an app crashes or stops responding cause much user frustration. Apps are expected to be resilient and stable and eliminating such failures helps ensure that software is more predictable, maintainable, performant and trustworthy.<dl> 1.1 Your app must not take a dependency on Windows compatibility modes, AppHelp message, and or any other compatibility fixes  
1.2 Your app must have a compatibility manifest, and use the appropriate GUIDs for the supported versions of Windows  
1.3 Your app must be DPI-aware by using the application's assembly manifest rather than by calling SetProcessDPIAware  
1.4 Your app must not take a dependency on the VB6 runtime  
1.5 Your app must not load arbitrary DLLs to intercept Win32 API calls using HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows AppInit\_dlls.  
</dl>

## 2. Apps must adhere to Windows security best practices

Using Windows security best practices will help avoid creating exposure to Windows attack surfaces. Attack surfaces are the entry points that a malicious attacker could use to exploit the operating system by taking advantage of vulnerabilities in the target software. One of the worst security vulnerabilities is the elevation of privilege.

Note that tests 2.1   2.6 are applicable only for desktop apps tested on Windows 7, Windows 8 or Windows 8.1.<dl> 2.1 Your app must use strong and appropriate [ACLs](/windows/desktop/SecAuthZ/access-control-lists) to secure executable files  
2.2 Your app must use strong and appropriate [ACLs](/windows/desktop/SecAuthZ/access-control-lists) to secure directories  
2.3 Your app must use strong and appropriate [ACLs](/windows/desktop/SecAuthZ/access-control-lists) to secure registry keys  
2.4 Your app must use strong and appropriate [ACLs](/windows/desktop/SecAuthZ/access-control-lists) to secure directories that contain objects  
2.5 Your app must reduce non-administrator access to services that are vulnerable to tampering  
2.6 Your app must prevent services with fast restarts from restarting more than twice every 24 hours  
</dl>

**Note: Access should only be granted to the entities that require it.**

The Windows App Certification Program will verify that Windows Attack Surfaces are not exposed by verifying that ACLs and Services are implemented in a way that does not put the Windows system at risk.

## 3. Apps support Windows security features

The Windows operating system has many features that support system security and privacy. Apps must support these features to maintain the integrity of the operating system. Improperly compiled apps could cause buffer overruns that can, in turn, cause denial of service or allow malicious code execute. <dl> 3.1 Your app must not use AllowPartiallyTrustedCallersAttribute (APTCA) to ensure secure access to strong-named assemblies  
3.2 Your app must be compiled using the /SafeSEH flag to ensure safe exceptions handling  
3.3 Your app must be compiled using the /NXCOMPAT flag to prevent data execution  
3.4 Your app must be compiled using the /DYNAMICBASE flag for address space layout randomization (ASLR)  
3.5 Your app must not Read/Write the Shared PE Sections  
</dl>

## 4. Apps must adhere to system restart manager messages

When users initiate shutdown, they usually have a strong desire to see shutdown succeed; they may be in a hurry to leave the office and just want their computers to turn off. Apps must respect this desire by not blocking shutdown. While in most cases, a shutdown may not be critical, apps must be prepared for the possibility of a critical shutdown.<dl> 4.1 Your app must handle critical shutdowns appropriately <dl> In a critical shutdown, apps that return FALSE to WM\_QUERYENDSESSION will be sent WM\_ENDSESSION and closed, while those that time out in response to WM\_QUERYENDSESSION will be terminated.  
</dl> </dd> 4.2 A GUI app must return TRUE immediately in preparation for a restart <dl> WM\_QUERYENDSESSION with LPARAM = ENDSESSION\_CLOSEAPP(0x1).  
Console apps can call SetConsoleCtrlHandler to specify the function that will handle shutdown notifications. Service apps can call RegisterServiceCtrlHandlerEx to specify the function that will receive shutdown notifications.  
</dl> </dd> 4.3 Your app must return 0 within 30 seconds and shut down <dl> WM\_ENDSESSION with LPARAM = ENDSESSION\_CLOSEAPP(0x1).  
At a minimum, app should prepare by saving any user data and state the information that is needed after a restart.  
</dl> </dd> 4.4 Console apps that receive the CTRL\_C\_EVENT notification should shut down immediately  
4.5 Drivers must not veto a system shutdown event  
</dl>
<strong>Note: Apps that must block shutdown because of an operation that cannot be interrupted should explain the reason to the user.</strong> Use ShutdownBlockReasonCreate to register a string that explains the reason to the user. When the operation has completed, the app should call ShutdownBlockReasonDestroy to indicate that the system can be shut down.

## 5. Apps must support a clean, reversible installation

A clean, reversible, installation allows users to successfully manage (deploy and remove) apps on their systems.<dl> 5.1 Your app must properly implement a clean, reversible installation <dl> If the installation fails, the app should be able to roll it back and restore the machine to its previous state.  
</dl> </dd> 5.2 Your app must never force the user to restart the computer immediately <dl> Restarting the computer should never be the only option at the end of an install, uninstall or update. Users should have the opportunity to restart later.  
</dl> </dd> 5.3 Your app must never be dependent on 8.3 short file names (SFN)  
5.4 Your app must never block silent install/uninstall  
5.5 Your app installer must create the correct registry entries to allow successful detection and uninstalls <dl> Windows inventory tools and telemetry tools require complete information about installed apps. If you are using an MSI-based installer, MSI automatically creates the registry entries below. If you are not using an MSI installer, the installation module must create the following registry entries during installation:  
</dl>

-   DisplayName
-   InstallLocation
-   Publisher
-   UninstallString
-   VersionMajor or MajorVersion
-   VersionMinor or MinorVersion

</dd> 5.6 The app must remove all of its entries from Add/ Remove Programs upon uninstall  
</dl>

## 6. Apps must digitally sign files and drivers

An Authenticode digital signature allows users to be sure that the software is genuine. It also allows one to detect whether a file has been tampered with, such as if it has been infected by a virus. Kernel-mode code signing enforcement is a Windows feature known as code integrity (CI), which improves the security of the operating system by verifying the integrity of a file each time the image of the file is loaded into memory. CI detects whether malicious code has modified a system binary file. Also generates a diagnostic and system-audit log event when the signature of a kernel module fails to verify correctly. <dl> 6.1 All executable files (.exe, .dll, .ocx, .sys, .cpl, .drv, .scr) must be signed with an Authenticode certificate  
6.2 All kernel mode drivers installed by the app must have a Microsoft signature obtained through the Windows Hardware Certification program. All File System filter drivers must be signed by Microsoft.  
6.3 Exceptions and Waivers <dl> Waivers will be considered only for unsigned third-party redistributables, excluding drivers. A proof of communication requesting a signed version of the redistributable(s) is required for this waiver to be granted.  
</dl> </dd> </dl>

## 7. Apps don't block installation or app launch based on an operating system version check

It is important that customers are not artificially blocked from installing or running their app when there are no technical limitations. In general, if apps were written for Windows Vista or later versions of Windows, they should not have to check the operating system version.<dl> 7.1 Your app must not perform version checks for equality <dl> If you need a specific feature, check whether the feature itself is available. If you need Windows 7, check for Windows 7 or later (>= 6.2). This way, your detection code will continue to work on future versions of Windows. Driver installers and uninstall modules should never check the operating system version.  
</dl> </dd> 7.2 Exceptions and Waivers will be considered for apps meeting the criteria below:

-   Apps that are delivered as one package that also run on Windows 7, Windows 8, and Windows 8.1, and need to check the operating system version to determine which components to install on a given operating system.
-   Apps that check only the minimum version of the operating system (during install only, not at runtime) by using only the approved API calls, and that properly list the minimum version requirement in the app manifest.
-   Security apps (antivirus, firewall, etc.), system utilities (for example, defrag, backups, and diagnostics tools) that check the operating system version by using only the approved API calls.


</dl>

## 8. Apps don't load services or drivers in safe mode

Safe mode allows users to diagnose and troubleshoot Windows. Drivers and services must not be set to load in safe mode unless they are needed for basic system operations of such as storage device drivers or for diagnostic and recovery purposes, such as anti-virus scanners,. By default, when Windows is in safe mode, it starts only the drivers and services that came preinstalled with Windows.

-   8.1 Exceptions and Waivers <dl> Drivers and services that must be started in safe mode require a waiver. The waiver request must include each applicable driver or service writing to the SafeBoot registry keys, and describe the technical reasons why the app or service must run in safe mode. The app installer must register all such drivers and services using these registry keys:  
    </dl>
    -   HKLM/System/CurrentControlSet/Control/SafeBoot/Minimal
    -   HKLM/System/CurrentControlSet/Control/SafeBoot/Network

**Note:** You must test these drivers and services to ensure that they function in safe mode without any errors.

## 9. Apps must follow User Account Control guidelines

Some Windows apps run in the security context of an administrator account, and apps often request excessive user rights and Windows privileges. Controlling access to resources enables users to be in control of their systems and protect them against unwanted changes. An unwanted change can be malicious, such as a rootkit taking control of the computer, or be the result of an action made by people who have limited privileges.. The most important rule for controlling access to resources is to provide the least amount of access  standard user context  necessary for a user to perform his or her necessary tasks. Following user account control (UAC) guidelines provides an app with the necessary permissions when they are needed by the app, without leaving the system constantly exposed to security risks. Most apps do not require administrator privileges at run time, and should be just fine running as a standard-user.<dl> 9.1 Your app must have a manifest that defines execution levels and tells the operating system what privileges the app requires in order to run <dl> The app manifest marking only applies to EXEs, not DLLs. This is because UAC does not inspect DLLs during process creation. It is also worth noting that UAC rules do not apply to Microsoft services. The manifest can be either embedded or external.  
To create a manifest, create a file with the name <app\_name>.exe.manifest and store it in the same directory as the EXE. Note that any external manifest is ignored if the app has an internal manifest. For example:  
<requestedExecutionLevel level=""asInvoker \| highestAvailable \| requireAdministrator"" uiAccess=""true\|false""/>  
</dl> </dd> 9.2 Your app s main process must be run as a standard user (asInvoker). <dl> Any administrative features must be moved into a separate process that runs with administrative privileges. User facing apps, such as those accessible through the program group on the Start-Menu, and requiring elevation must be Authenticode signed.  
</dl> </dd> 9.3 Exceptions and Waivers <dl> A waiver is required for apps that run their main process with elevated privileges (requireAdministrator or highestAvailable). The main process is identified as the user s entry point to the app. Waivers will be considered for the following scenarios:

-   Administrative or system tools with execution level set to highestAvailable, and/or requireAdministrator
-   Only Accessibility or UI automation framework app sets the uiAccess flag to true to bypass the user interface privilege isolation (UIPI). To properly start app utilization, this flag must be Authenticode signed, and must reside in a protected location in the file system, namely Program Files.


</dl> </dd> </dl>

## 10. Apps must install to the correct folders by default

Users should have a consistent and secure experience with the default installation location of files, while maintaining the option to install an app in the location of their choice. It is also necessary to store app data in the correct location to allow several people to use the same computer without corrupting or overwriting each other's data and settings. Windows provides specific locations in the file system to store programs and software components, shared app data, and app data specific to a user<dl> 10.1 Your app must be installed in the Program Files folder by default <dl> For native 32-bit and 64-bit apps in %ProgramFiles%, and %ProgramFiles(x86)% for 32-bit apps running on x64. User data or app data must never be stored in this location because of the security permissions configured for this folder.  
</dl> </dd> 10.2 Your app must avoid starting automatically on startup <dl> For example, your app should not set any of the following;  
</dl>

-   Registry run keys HKLM and, or HKCU under Software\\Microsoft\\Windows\\CurrentVersion
-   Registry run keys HKLM, and or HKCU under Software\\Wow6432Node\\Microsoft\\windows\\CurrentVersion
-   Start Menu AllPrograms > STARTUP

</dd> 10.3 Your app data, which must be shared among users on the computer, should be stored within ProgramData  
10.4 Your app s data that is exclusive to a specific user and that is not to be shared with other users of the computer, must be stored in Users\\&lt;username&gt;\\AppData  
10.5 Your app must never write directly to the "Windows" directory and or subdirectories <dl> Use the correct methods for installing files, such as fonts or drivers.  
</dl> </dd> 10.6 Your app must write user data at first run and not during the installation in  per-machine  installations <dl> When the app is installed, there is no correct user location in which to store data. Attempts by an app to modify default association behaviors at a machine level after installation will be unsuccessful. Instead, defaults must be claimed on a per-user level, which prevents multiple users from overwriting each other's defaults.  
</dl> </dd> 10.7 Exceptions and Waivers <dl> A waiver is required for apps that write to the global assembly cache (GAC) .NET apps should keep assembly dependencies private, and store it in the app directory unless sharing an assembly is explicitly required.  
</dl> </dd> </dl>

## 11. Apps must support multi-user sessions

Windows users should be able to run concurrent sessions without conflict or disruption.<dl> 11.1 Your app must ensure that when running in multiple sessions either locally or remotely, the normal functionality of the app is not adversely affected  
11.2 Your app s settings and data files must not persist across users  
11.3 A user s privacy and preferences must be isolated to the user s session  
11.4 Your app s instances must be isolated from each other <dl> This means that user data from one instance is not visible to another instance of the app. Sound in an inactive user session should not be heard in an active user session. In cases where multiple app instances use shared resources, the app must ensure that there is not a conflict.  
</dl> </dd> 11.5 Apps that are installed for multiple users must store data in the correct folder(s) and registry locations <dl> Refer to the UAC requirements.  
</dl> </dd> 11.6 User apps must be able to run in multiple user sessions (Fast User Switching) for both local and remote access  
11.7 Your app must check other terminal service (TS) sessions for existing instances of the app  
</dl>
<strong>Note:</strong> If an app does not support multiple user sessions or remote access, it must clearly state this when launched from this kind of session.

## 12. Apps must support x64 versions of Windows

As 64-bit hardware becomes more common, users expect app developers to take advantage of the benefits of 64-bit architecture by migrating their apps to 64-bit, or that 32-bit versions of the app run well under 64-bit versions of Windows.<dl> 12.1 Your app must natively support 64-bit or, at a minimum, 32-bit Windows-based apps must run seamlessly on 64-bit systems to maintain compatibility with 64-bit versions of Windows  
12.2 Your app and its installers must not contain any 16-bit code or rely on any 16-bit component  
12.3 Your app s setup must detect and install the proper drivers and components for the 64-bit architecture  
12.4 Any shell plug-ins must run on 64-bit versions of Windows  
12.5 App running under the WoW64 emulator should not attempt to subvert or bypass Wow64 virtualization mechanisms <dl> If there are specific scenarios where apps need to detect whether they are running under the WoW64 emulator, they should do so by calling IsWow64Process.  
</dl> </dd> </dl>

## Conclusion

As these requirements evolve, we will note the changes in the revision history below. Stable requirements are critical to doing your best work, so we will aim to ensure the changes we do make are sustainable and continue to protect and enhance your apps.

Thank you again for joining in our commitment to delivering great customer experiences.

## Revision history



| Date          | Version | Revision description                   | Link to document                                                                 |
|---------------|---------|----------------------------------------|----------------------------------------------------------------------------------|
| Dec 20, 2011  | 1.0     | Initial draft of document for Preview. |                                                                                  |
| Jan 26, 2012  | 1.1     | Update to section \#2.                 | [1.1](archive--certification-requirements-for-windows-desktop-apps-v1-1.md)     |
| May 31, 2012  | 1.2     | Added summary test results             | [1.2](archive--certification-requirements-for-windows-desktop-apps-v1-2.md)     |
| Jun 29, 2012  | 3.0     | Windows 8 final document               | [3.0](archive--certification-requirements-for-windows-desktop-apps-v3-0.md)     |
| Jun 18, 2013  | 3.1     | Windows 8.1 document                   | [3.1](archive--certification-requirements-for-windows-desktop-apps-v3-1.md)     |
| Feb 20, 2014  | 3.2     | Internal update                        |                                                                                  |
| Mar 18, 2014  | 3.3     | Windows 8.1 Update 1                   | [3.3](https://www.bing.com/search?q=3.3) |
| July 29, 2015 | 10      | Windows 10 Update                      | 10                                                                               |





## Learn more about desktop app certification



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Requirement</td>
<td>Description</td>
</tr>
<tr class="even">
<td>Compatibility and resiliency</td>
<td>Crashes & hangs are a major disruption to users and cause frustration. Apps are expected to be resilient and stable, eliminating such failures helps ensure that software is more predictable, maintainable, performant and trustworthy.<br/> User facing app entry point must be manifested for compatibility, as well as declaring the right GUID. <br/> User facing app entry points must be manifested for HIGH-DPI awareness and that the proper APIs are being called to support HIGH-DPI.<br/> For more information see:
<ul>
<li><a href="https://support.microsoft.com/kb/197571">AppInit DLLs</a></li>
<li><a href="/windows/desktop/w8cookbook/application--executable--manifest">App (executable) manifest</a></li>
<li><a href="/windows/desktop/hidpi/high-dpi-desktop-application-development-on-windows">Writing High-DPI Win32 Applications</a></li>
</ul>
<br/></td>
</tr>
<tr class="odd">
<td>Adhere to Windows Security Best Practices</td>
<td>Using Windows security best practices will help avoid creating exposure to Windows attack surfaces. Attack surfaces are the entry points that a malicious attacker could use to exploit the operating system by taking advantage of vulnerabilities in the target software. One of the worst security vulnerabilities is the elevation of privilege.<br/> For more information see:
<ul>
<li><a href="https://technet.microsoft.com/security/gg749821">Attack Surface Analyzer</a></li>
<li><a href="/windows/desktop/SecAuthZ/access-control-lists">Access Control Lists</a></li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>Support Windows Security Features</td>
<td>The Windows operating system has implemented many measures to support system security and privacy. Applications must support these measures to maintain the integrity of the OS. Improperly compiled applications could cause buffer overruns that in turn could cause denial of service or make malicious code execute. For more information see the <a href="https://blogs.microsoft.com/cybertrust/2012/08/15/microsofts-free-security-tools-binscope-binary-analyzer/">BinScope tool reference</a>.</td>
</tr>
<tr class="odd">
<td>Adhere to System Restart Manager Messages</td>
<td>When users initiate shutdown, in the vast majority of cases, they have a strong desire to see shutdown succeed; they may be in a hurry to leave the office and &quot;just want&quot; their computers to turn off. Apps must respect this desire by not blocking shutdown. While in most cases, a shutdown may not be critical, apps must be prepared for the possibility of a critical shutdown.</td>
</tr>
<tr class="even">
<td>Clean Reversible Installation</td>
<td>A clean, reversible, installation allows users to successfully manage (deploy and remove) apps on their systems. For more information see, <a href="/visualstudio/deployment/how-to-install-prerequisites-with-a-clickonce-application?view=vs-2015">How to: Install Prerequisites with a ClickOnce Application</a>.</td>
</tr>
<tr class="odd">
<td>Digitally sign files and drivers</td>
<td>An Authenticode digital signature allows users to be sure that the software is genuine. It also allows one to detect whether a file has been tampered with, for example, if it has been infected by a virus. Kernel-mode code signing enforcement is a Windows feature known as code integrity (CI), which improves the security of the operating system by verifying the integrity of a file each time the image of the file is loaded into memory. CI detects whether malicious code has modified a system binary file. Also generates a diagnostic and system-audit log event when the signature of a kernel module fails to verify correctly.<br/></td>
</tr>
<tr class="even">
<td>Do not block installation or app launch based on operating system version check</td>
<td>It is important that customers are not artificially blocked from installing or running their app when there are no technical limitations. In general, if apps were written for Windows Vista or later releases, they should have no reason to check the operating system version. For more information see, <a href="/windows/desktop/Win7AppQual/operating-system-versioning">Operating System Versioning</a>.</td>
</tr>
<tr class="odd">
<td>Do not load Services and Drivers in Safe Mode</td>
<td>Safe mode allows users to diagnose and troubleshoot Windows. Unless needed for basic operations of the system (for example, storage device drivers) or for diagnostic and recovery purposes (for example, anti-virus scanners), drivers and services must not be set to load in safe mode. By default, the safe mode does not start most drivers and services that did not come preinstalled with Windows. They should remain disabled unless the system requires them for basic operations or for diagnostic and recovery purposes.<br/> For more information see:
<ul>
<li><a href="/windows-hardware/drivers/kernel/determining-whether-the-operating-system-is-running-in-safe-mode">Determining Whether the Operating System Is Running in Safe Mode</a></li>
<li><a href="https://support.microsoft.com/kb/837643">How to determine whether the system is running in Safe Mode from a device driver</a></li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>Follow User Account Control (UAC) Guidelines</td>
<td>Some Windows app run in the security context of an administrator account, and many require excessive user rights and Windows privileges. Controlling access to resources enables users to be in control of their systems against unwanted changes (An unwanted change can be malicious, such as a rootkit stealthily taking over the machine, or an action from people who have limited privileges, for example, an employee installing prohibited software on a work computer). The most important rule for controlling access to resources is to provide the least amount of access  standard user context  necessary for a user to perform his or her necessary tasks. Following UAC guidelines provides app with the necessary permissions when needed, without leaving the system constantly exposed to security risks.<br/> For more information see:
<ul>
<li><a href="/windows/desktop/uxguide/winenv-uac">User Account Control</a></li>
<li><a href="/previous-versions/aa480152(v=msdn.10)">UAC: Application Update Guidelines</a></li>
</ul>
<br/></td>
</tr>
<tr class="odd">
<td>Install to the Correct Folders by Default</td>
<td>Users should have a consistent and secure experience with the default installation location of files, while maintaining the option to install an app to the location they choose. It is also necessary to store app data in the correct location to allow several people to use the same computer without corrupting or overwriting each other's data and settings. For more information see, <a href="/previous-versions/ms954376(v=msdn.10)">Summary of Install/Uninstall Requirements</a>.</td>
</tr>
<tr class="even">
<td>Support Multi-User Sessions</td>
<td>Windows users should be able to run concurrent sessions without conflict or disruption. For more information see, <a href="/windows/desktop/TermServ/terminal-services-programming-guidelines">Remote Desktop Services Programming Guidelines</a>.</td>
</tr>
<tr class="odd">
<td>Support x64 versions of Windows</td>
<td>As 64-bit hardware becomes more prevalent, users expect app developers to take advantage of the benefits of 64-bit architecture by migrating their apps to 64-bit, or that 32-bit versions of the app run well under 64-bit versions of Windows.</td>
</tr>
</tbody>
</table>





## See also

-   [Windows Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))
-   [How to use the Windows App Certification Kit](./using-the-windows-app-certification-kit.md)
