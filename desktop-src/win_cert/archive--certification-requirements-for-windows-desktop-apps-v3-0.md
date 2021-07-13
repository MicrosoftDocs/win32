---
title: Archive Certification requirements for Windows Desktop Apps v3.0
description: Document version 3.0Document date June 29, 2012This document contains the technical requirements and eligibility qualifications that a desktop app must meet in order to participate in the Windows 8 Desktop App Certification Program.
ms.assetid: 7107EF93-8401-481A-B433-8C36A539D790
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Archive: Certification requirements for Windows Desktop Apps v3.0

**Document version:** 3.0

**Document date:** June 29, 2012

This document contains the technical requirements and eligibility qualifications that a desktop app must meet in order to participate in the Windows 8 Desktop App Certification Program. For Windows 7, this program was known as the Windows Software Logo Program.

## Welcome!

The Windows platform supports a broad ecosystem of products and partners. Displaying the Windows logo on your product represents a relationship and a shared commitment to quality between Microsoft and your company. Customers trust the Windows brand on your product because it ensures that it meets compatibility standards and performs well on the Windows platform. Successfully passing Windows App Certification allows for your app to be showcased in the Windows Compatibility Center and it s also a necessary step to listing a desktop app reference in the Windows Store.

The Windows App Certification Program is made up of program and technical requirements to help ensure that third-party apps carrying the Windows brand are both easy to install and reliable on PCs running Windows. Customers value stability, compatibility, reliability, performance, and quality in the systems they purchase. Microsoft focuses its investments to meet these requirements for software apps designed to run on the Windows platform for PCs. These efforts include compatibility tests for consistency of experience, improved performance, and enhanced security on PCs running Windows software. Microsoft compatibility tests have been designed in collaboration with industry partners and are continuously improved in response to industry developments and consumer demand.

The Windows App Certification Kit is used to validate compliance with these requirements and replaces the WSLK used for validation in the Windows 7 Software Logo program. The Windows App Certification Kit is one of the components included in the Windows Software Development Kit (SDK) for Windows 8. It is also integrated within Microsoft Visual Studio 2012 Express for Windows 8.

## App eligibility

For an app to qualify for Windows 8 Desktop App Certification it must meet the following criteria and all the technical requirements listed in this document.

-   It must be a standalone app
-   It must run on a local Windows 8.1 computer
-   It can be a client component of a certified Windows Server app
-   It must be code and feature complete

## 1. Apps are compatible and resilient

The times when an app crashes or stops responding cause much user frustration. Apps are expected to be resilient and stable and eliminating such failures helps ensure that software is more predictable, maintainable, performant and trustworthy.<dl> 1.1 Your app must not take a dependency on Windows compatibility modes, AppHelp message, and or any other compatibility fixes  
1.2 Your app must not take a dependency on the VB6 runtime  
1.3 Your app must not load arbitrary DLLs to intercept Win32 API calls using HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows AppInit\_dlls.  
</dl>

## 2. Apps must adhere to Windows security best practices

Using Windows security best practices will help avoid creating exposure to Windows attack surfaces. Attack surfaces are the entry points that a malicious attacker could use to exploit the operating system by taking advantage of vulnerabilities in the target software. One of the worst security vulnerabilities is the elevation of privilege.

<dl> 2.1 Your app must use strong and appropriate <a href="/windows/desktop/SecAuthZ/access-control-lists">ACLs</a> to secure executable files  
2.2 Your app must use strong and appropriate <a href="/windows/desktop/SecAuthZ/access-control-lists">ACLs</a> to secure directories  
2.3 Your app must use strong and appropriate <a href="/windows/desktop/SecAuthZ/access-control-lists">ACLs</a> to secure registry keys  
2.4 Your app must use strong and appropriate <a href="/windows/desktop/SecAuthZ/access-control-lists">ACLs</a> to secure directories that contain objects  
2.5 Your app must reduce non-administrator access to services that are vulnerable to tampering  
2.6 Your app must prevent services with fast restarts from restarting more than twice every 24 hours  
</dl>**Note: Access should only be granted to the entities that require it.**

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
</dl>**Note: Apps that must block shutdown because of an operation that cannot be interrupted should explain the reason to the user.** Use ShutdownBlockReasonCreate to register a string that explains the reason to the user. When the operation has completed, the app should call ShutdownBlockReasonDestroy to indicate that the system can be shut down.

## 5. Apps must support a clean, reversible installation

A clean, reversible, installation allows users to successfully manage (deploy and remove) apps on their systems.<dl> 5.1 Your app must properly implement a clean, reversible installation <dl> If the installation fails, the app should be able to roll it back and restore the machine to its previous state.  
</dl> </dd> 5.2 Your app must never force the user to restart the computer immediately <dl> Restarting the computer should never be the only option at the end of an install or update. Users should have the opportunity to restart later.  
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

</dd> </dl>

## 6. Apps must digitally sign files and drivers

An Authenticode digital signature allows users to be sure that the software is genuine. It also allows one to detect whether a file has been tampered with, such as if it has been infected by a virus. Kernel-mode code signing enforcement is a Windows feature known as code integrity (CI), which improves the security of the operating system by verifying the integrity of a file each time the image of the file is loaded into memory. CI detects whether malicious code has modified a system binary file. Also generates a diagnostic and system-audit log event when the signature of a kernel module fails to verify correctly. <dl> 6.1 All executable files (.exe, .dll, .ocx, .sys, .cpl, .drv, .scr) must be signed with an Authenticode certificate  
6.2 All kernel mode drivers installed by the app must have a Microsoft signature obtained through the Windows Hardware Certification program. All File System filter drivers must be signed by Microsoft.  
6.3 Exceptions and Waivers <dl> Waivers will be considered only for unsigned third-party redistributables, excluding drivers. A proof of communication requesting a signed version of the redistributable(s) is required for this waiver to be granted.  
</dl> </dd> </dl>

## 7. Apps don t block installation or app launch based on an operating system version check

It is important that customers are not artificially blocked from installing or running their app when there are no technical limitations. In general, if apps were written for Windows Vista or later versions of Windows, they should not have to check the operating system version.<dl> 7.1 Your app must not perform version checks for equality <dl> If you need a specific feature, check whether the feature itself is available. If you need Windows XP, check for Windows XP or later (>= 5.1). This way, your detection code will continue to work on future versions of Windows. Driver installers and uninstall modules should never check the operating system version.  
</dl> </dd> 7.2 Exceptions and Waivers will be considered for apps meeting the criteria below:

-   Apps that are delivered as one package that also run on Windows XP, Windows Vista, and Windows 7, and need to check the operating system version to determine which components to install on a given operating system.
-   Apps that check only the minimum version of the operating system (during install only, not at runtime) by using only the approved API calls, and that properly list the minimum version requirement in the app manifest.
-   Security apps (antivirus, firewall, etc.), system utilities (for example, defrag, backups, and diagnostics tools) that check the operating system version by using only the approved API calls.

  
</dl>

## 8. Apps don t load services or drivers in safe mode

Safe mode allows users to diagnose and troubleshoot Windows. Drivers and services must not be set to load in safe mode unless they are needed for basic system operations of such as storage device drivers or for diagnostic and recovery purposes, such as anti-virus scanners,. By default, when Windows is in safe mode, it starts only the drivers and services that came preinstalled with Windows.

-   8.1 Exceptions and Waivers <dl> Drivers and services that must be started in safe mode require a waiver. The waiver request must include each applicable driver or service writing to the SafeBoot registry keys, and describe the technical reasons why the app or service must run in safe mode. The app installer must register all such drivers and services using these registry keys:  
    </dl>
    -   HKLM/System/CurrentControlSet/Control/SafeBoot/Minimal
    -   HKLM/System/CurrentControlSet/Control/SafeBoot/Network

**Note:** You must test these drivers and services to ensure that they function in safe mode without any errors.

## 9. Apps must follow User Account Control guidelines

Some Windows apps run in the security context of an administrator account, and apps often request excessive user rights and Windows privileges. Controlling access to resources enables users to be in control of their systems and protect them against unwanted changes. An unwanted change can be malicious, such as a rootkit taking control of the computer, or be the result of an action made by people who have limited privileges.. The most important rule for controlling access to resources is to provide the least amount of access  standard user context  necessary for a user to perform his or her necessary tasks. Following user account control (UAC) guidelines provides app with the necessary permissions when they are needed by the app, without leaving the system constantly exposed to security risks. Most apps do not require administrator privileges at run time, and should be just fine running as a standard-user.<dl> 9.1 Your app must have a manifest that defines execution levels and tells the operating system what privileges the app requires in order to run <dl> The app manifest marking only applies to EXEs, not DLLs. This is because UAC does not inspect DLLs during process creation. It is also worth noting that UAC rules do not apply to Microsoft services. The manifest can be either embedded or external.  
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
10.4 Your app s data that is exclusive to a specific user and that is not to be shared with other users of the computer, must be stored in Users\\<username>\\AppData  
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
</dl>**Note:** If an app does not support multiple user sessions or remote access, it must clearly state this when launched from this kind of session.

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



| Date         | Version | Revision description                   | Link to document                                                             |
|--------------|---------|----------------------------------------|------------------------------------------------------------------------------|
| Dec 20, 2011 | 1.0     | Initial draft of document for Preview. |                                                                              |
| Jan 26, 2012 | 1.1     | Update to section \#2.                 | [1.1](archive--certification-requirements-for-windows-desktop-apps-v1-1.md) |
| May 31, 2012 | 1.2     | Added summary test results             | [1.2](archive--certification-requirements-for-windows-desktop-apps-v1-2.md) |
| Jun 29, 2012 | 3.0     | Windows 8 final document               | 3.0                                                                          |



 

## Learn more about desktop app certification



| Requirement                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | More details                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compatibility and resiliency                                                    | Crashes & hangs are a major disruption to users and cause frustration. Apps are expected to be resilient and stable, eliminating such failures helps ensure that software is more predictable, maintainable, performant and trustworthy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Windows Vista, Windows 7,and Windows 8 Operating Systems](/previous-versions/windows/it-pro/windows-7/cc722305(v=ws.10))<br/> [Application Verifier](/previous-versions/aa480483(v=msdn.10))<br/> [AppInit DLLs](https://support.microsoft.com/kb/197571)<br/> |
| Adhere to Windows Security Best Practices                                       | Using Windows security best practices will help avoid creating exposure to Windows attack surfaces. Attack surfaces are the entry points that a malicious attacker could use to exploit the operating system by taking advantage of vulnerabilities in the target software. One of the worst security vulnerabilities is the elevation of privilege.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Attack Surface Analyzer](https://technet.microsoft.com/security/gg749821)<br/> [Access Control Lists](/windows/desktop/SecAuthZ/access-control-lists)<br/>                                                                                                                                |
| Support Windows Security Features                                               | The Windows operating system has implemented many measures to support system security and privacy. Applications must support these measures to maintain the integrity of the OS. Improperly compiled applications could cause buffer overruns that in turn could cause denial of service or make malicious code execute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [BinScope tool reference](https://blogs.microsoft.com/cybertrust/2012/08/15/microsofts-free-security-tools-binscope-binary-analyzer/)<br/>                                                                                                                                             |
| Adhere to System Restart Manager Messages                                       | When users initiate shutdown, in the vast majority of cases, they have a strong desire to see shutdown succeed; they may be in a hurry to leave the office and "just want" their computers to turn off. Apps must respect this desire by not blocking shutdown. While in most cases, a shutdown may not be critical, apps must be prepared for the possibility of a critical shutdown.                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Application Shutdown Changes in Windows Vista](/previous-versions/windows/desktop/ms700677(v=vs.85))<br/> [Restart Manager Development](/previous-versions/bb756958(v=msdn.10))<br/>                                                                              |
| Clean Reversible Installation                                                   | A clean, reversible, installation allows users to successfully manage (deploy and remove) apps on their systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [How to: Install Prerequisites with a ClickOnce Application](/visualstudio/deployment/how-to-install-prerequisites-with-a-clickonce-application?view=vs-2015)<br/> [Application Installation on 64-bit Systems](/windows/desktop/WinProg64/application-installation)<br/>                                                |
| Digitally sign files and drivers                                                | An Authenticode digital signature allows users to be sure that the software is genuine. It also allows one to detect whether a file has been tampered with, for example, if it has been infected by a virus. Kernel-mode code signing enforcement is a Windows feature known as code integrity (CI), which improves the security of the operating system by verifying the integrity of a file each time the image of the file is loaded into memory. CI detects whether malicious code has modified a system binary file. Also generates a diagnostic and system-audit log event when the signature of a kernel module fails to verify correctly.                                                                                                                                                                            | [Digital Signatures for Kernel Modules on Windows](/previous-versions/windows/hardware/design/dn653559(v=vs.85))<br/>                                                                                                                                             |
| Do not block installation or app launch based on operating system version check | It is important that customers are not artificially blocked from installing or running their app when there are no technical limitations. In general, if apps were written for Windows Vista or later releases, they should have no reason to check the operating system version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Operating System Versioning](../win7appqual/operating-system-versioning.md)<br/>                                                                                                                                                                                           |
| Do not load Services and Drivers in Safe Mode                                   | Safe mode allows users to diagnose and troubleshoot Windows. Unless needed for basic operations of the system (for example, storage device drivers) or for diagnostic and recovery purposes (for example, anti-virus scanners), drivers and services must not be set to load in safe mode. By default, the safe mode does not start most drivers and services that did not come preinstalled with Windows. They should remain disabled unless the system requires them for basic operations or for diagnostic and recovery purposes.                                                                                                                                                                                                                                                                                         | [Determining Whether the Operating System Is Running in Safe Mode](/windows-hardware/drivers/kernel/determining-whether-the-operating-system-is-running-in-safe-mode)<br/> [How to determine whether the system is running in Safe Mode from a device driver](https://support.microsoft.com/kb/837643)<br/>       |
| Follow User Account Control (UAC) Guidelines                                    | Some Windows app run in the security context of an administrator account, and many require excessive user rights and Windows privileges. Controlling access to resources enables users to be in control of their systems against unwanted changes (An unwanted change can be malicious, such as a rootkit stealthily taking over the machine, or an action from people who have limited privileges, for example, an employee installing prohibited software on a work computer). The most important rule for controlling access to resources is to provide the least amount of access  standard user context  necessary for a user to perform his or her necessary tasks. Following UAC guidelines provides app with the necessary permissions when needed, without leaving the system constantly exposed to security risks. | [User Account Control](/windows/desktop/uxguide/winenv-uac)<br/> [UAC: Application Update Guidelines](/previous-versions/aa480152(v=msdn.10))<br/>                                                                       |
| Install to the Correct Folders by Default                                       | Users should have a consistent and secure experience with the default installation location of files, while maintaining the option to install an app to the location they choose. It is also necessary to store app data in the correct location to allow several people to use the same computer without corrupting or overwriting each other's data and settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Summary of Install/Uninstall Requirements](/previous-versions/ms954376(v=msdn.10))<br/>                                                                                                                                                                                    |
| Support Multi-User Sessions                                                     | Windows users should be able to run concurrent sessions without conflict or disruption.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Remote Desktop Services Programming Guidelines](/windows/desktop/TermServ/terminal-services-programming-guidelines)<br/>                                                                                                                                                                      |
| Support x64 versions of Windows                                                 | As 64-bit hardware becomes more prevalent, users expect app developers to take advantage of the benefits of 64-bit architecture by migrating their apps to 64-bit, or that 32-bit versions of the app run well under 64-bit versions of Windows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [Application Compatibility: Windows Vista 64-Bit](/previous-versions/bb756962(v=msdn.10))<br/>                                                                                                                                                                              |



 

## See also

-   [Windows Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))

 

