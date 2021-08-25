---
title: Windows App Certification Kit tests
description: Below are test details for certifying dekstop apps.
ms.assetid: FA160F46-C266-4F89-B77F-166FEA9ED96B
ms.topic: article
ms.date: 05/31/2018
---

# Windows App Certification Kit tests

Below are test details for certifying dekstop apps. For information, please refer to [Using the Windows App Certification Kit](using-the-windows-app-certification-kit.md).

-   [Clean reversible install](#clean-reversible-install)
-   [Install to the correct folders test](#install-to-the-correct-folders-test)
-   [Digitally signed file test](#digitally-signed-file-test)
-   [Support x64 Windows test](#support-x64-windows-test)
-   [OS version checking test](#os-version-checking-test)
-   [User account control (UAC) test](#user-account-control-uac-test)
-   [Adhere to system restart manager messages](#adhere-to-system-restart-manager-messages)
-   [Safe mode test](#safe-mode-test)
-   [Multiuser session test](#multiuser-session-test)
-   [Crashes and hangs test](#crashes-and-hangs-test)
-   [Compatibility and resiliency test](#compatibility-and-resiliency-test)
-   [Windows Security best practices test](#windows-security-best-practices-test)
-   [Windows Security features test](#windows-security-features-test)
-   [High DPI test](#high-dpi-test)

## Clean reversible install

Installs and uninstalls the app and checks for residual files and registry entries.

-   Background
    -   A clean, reversible installation enables users to deploy and remove apps. To pass this test, the app must do the following:
        -   The app doesn't force the system to restart immediately after installing or uninstalling the app. *An app's install or uninstall process should never require a system restart right after it completes. If this requires the system to be restarted, users should be able to restart the system at their convenience.*
        -   The app isn't dependent on 8.3 short file names (SFN). *The app's install and uninstall processes must be able to use long file names and folder paths.*
        -   The app doesn't block silent install/uninstall
        -   The app makes the required entries in the system registry. *Windows inventory tools and telemetry tools require complete info about installed apps. App installers must create the correct registry entries to allow successful detection and uninstalls.*
    -   If you are using an MSI-based installer, MSI automatically creates the registry entries below. If you are not using an MSI installer, the installation module must create the following registry entries during installation:
        -   DisplayName
        -   InstallLocation
        -   Publisher
        -   UninstallString
        -   VersionMajor or MajorVersion
        -   VersionMinor or MinorVersion
    -   The app must remove all of its entries in Add/Remove Programs.
-   Test details
    -   This test checks the app's install and uninstall processes for the required behavior.
-   Corrective Action
    -   Review the app's design and behavior against the requirements described above.

## Install to the correct folders test

Verifies that the app writes its program and data files to the correct folders.

-   Background
    -   Apps must user system and per-user folders correctly so it can access the data and settings it needs while protecting the user's data and settings from unauthorized access.
-   Program Files folders
    -   The app must be installed in the Program Files folder by default (%ProgramFiles% for native 32-bit and 64-bit apps, and %ProgramFiles(x86)% for 32-bit apps running on x64).
    -   **Note:** The app must not store user data or app data in a Program Files folder because of the security permissions configured for this folder.
    -   The ACLs on Windows system folders allow only administrator accounts to read and write to them. As a result, standard user accounts will not have access to these folders. File virtualization, however, lets apps store a file, such as a configuration file, in a system location that is typically writeable only by administrators. Running programs as a standard user in this situation could result in failure if they can't access a required file.
    -   Apps should use [Known Folders](/previous-versions/windows/desktop/legacy/bb776911(v=vs.85)) to ensure they will be able to access their data.
    -   **Note:** Windows provides file virtualization to improve app compatibility and eliminate problems when apps run as a standard user on Windows. Your app should not rely on virtualization being present in future versions of Windows.
-   User-specific app data folders
    -   In “per-machine” installations, the app must not write user-specific data during the installation. User-specific installation data should only be written when a user starts the app for the first time. This is because there is no correct user location at which to store data at time of installation. Attempts by an app to modify default association behaviors at a machine level after installation will be unsuccessful. Instead, defaults must be claimed on a per-user level, which prevents multiple users from overwriting each other's defaults.
    -   All app data exclusive to a specific user and not to be shared with other users of the computer must be stored in Users\\&lt;username&gt;\\AppData.
    -   All app data that must be shared among users on the computer should be stored within ProgramData.
-   Other system folders and registry keys
    -   The app should never write directly to the Windows directory and or subdirectories. Use the correct methods for installing files, such as fonts or drivers, to these directories.
    -   Apps should not start automatically on startup, such as by adding an entry to one or more of these locations:
        -   Registry run keys HKLM and, or HKCU under Software\\Microsoft\\Windows\\CurrentVersion
        -   Registry run keys HKLM, and or HKCU under Software\\Wow6432Node\\Microsoft\\windows\\CurrentVersion
        -   Start Menu AllPrograms > STARTUP
-   Test details
    -   This test verifies that the app uses the specific locations in the file system that Windows provides to store programs and software components, shared app data, and app data that is specific to a user.
-   Corrective actions
    -   Review how the app uses the system's folders and make sure it's using them correctly.
-   Exceptions and Waivers
    -   A waiver is required for desktop apps writing to the global assembly cache (GAC) (.NET apps should keep assembly dependencies private, and store it in the app's directory unless sharing an assembly is explicitly required).
    -   Installation to the Programs Files folder is not a requirement for Desktop SW packages to achieve SW Logo, only under the SW Fundamentals category.

## Digitally signed file test

Tests executable files and device drivers to verify they have a valid digital signature.

-   Background
    -   Digitally signed files make it possible to verify the file is genuine and to detect if the file has been tampered with.
    -   Kernel-mode code signing enforcement is a Windows feature that is also known as code integrity (CI). CI improves the security of Windows by verifying the integrity of a file each time it is loaded into memory. CI detects whether malicious code has modified a system binary file and generates a diagnostic and system-audit log event when the signature of a kernel module fails to verify correctly.
    -   If the app requires elevated permissions, the elevation prompt displays contextual info about the executable file that is requesting elevated access. Depending on whether the app is Authenticode signed, the user may see the consent prompt or the credential prompt.
    -   Strong names prevent third parties from spoofing your code, as long as you keep the private key secure. The .NET Framework verifies the digital signature either when it loads the assembly or installs it in the GAC. Without access to the private key, a malicious user cannot modify your code and sign it again.
-   Test details
    -   All executable files, such as those with file extensions of .exe, .dll, .ocx, .sys, .cpl, .drv, and .scr, must be signed with an Authenticode certificate.
    -   All kernel mode drivers installed by the app must have a Microsoft signature obtained through the WHQL or DRS program. All file system filter drivers must be WHQL signed.
-   Corrective Action
    -   Sign the app’s executable files.
    -   Use makecert.exe to generate a certificate or obtain a code-signing key from one of the commercial certification authorities (CAs), such as VeriSign, Thawte, or a Microsoft CA.
-   Exceptions and waivers
    -   Waivers will be considered only for unsigned third-party redistributables. A proof of communication requesting a signed version of the redistributable(s) is required for this waiver to be granted.
    -   Device value-added software packages are exempt from the kernel mode driver certification, because drivers must be certified in by Windows Hardware Certification.

## Support x64 Windows test

Test the app to make sure the .exe is built for the platform architecture onto which it will be installed.

-   Background
    -   The executable file must be built for the processor architecture on which it is installed. Some executable files might run on a different processor architecture, but this is not reliable.
    -   Architecture compatibility is important because 32-bit processes cannot load 64-bit DLLs and 64-bit processes cannot load 32-bit DLLs. Likewise, 64-bit versions of Windows does not support running 16-bit Windows-based applications because handles have 32 significant bits on 64-bit Windows an so they can't be passed to 16-bit applications. Therefore, trying to launch a 16-bit application will fail on 64-bit versions of Windows.
    -   32-bit device drivers cannot run on 64-bit versions of Windows and therefore, they must be ported to the 64-bit architecture.
    -   For user-mode applications, 64-bit Windows includes WOW64, which enables 32-bit Windows applications to execute on systems running 64-bit Windows, albeit with some loss of performance. No equivalent translation layer exists for device drivers.
    -   To maintain compatibility with 64-bit versions of Windows, apps must natively support 64-bit or, at a minimum, 32-bit Windows-based apps must run seamlessly on 64-bit systems:
        -   Apps and their installers mustn't contain any 16-bit code or rely on any 16-bit component.
        -   App setup must detect and install the proper drivers and components on 64-bit versions of Windows.
        -   Any shell plug-ins must run on 64-bit versions of Windows.
        -   Apps that run under the WoW64 emulator should not attempt to bypass Wow64 virtualization mechanisms. If there are specific scenarios where apps need to detect if they are running in a WoW64 emulator, they should do so by calling [**IsWow64Process**](/windows/desktop/api/wow64apiset/nf-wow64apiset-iswow64process).
-   Test details
    -   The app should not install any 16-bit binaries. The app should not install a 32-bit kernel mode driver if it is supposed to run on a 64-bit machine.
-   Corrective Actions
    -   Build the executable files and drivers for the processor architecture for which you want to install them.

## OS version checking test

Tests how the app checks for the version of Windows on which it's running.

-   Background
    -   Apps check the OS version by testing for a version that is greater than or equal to the required version to ensure compatibility with future versions of Windows.
-   Test details
    -   Simulates running the app on different versions of Windows to see how it reacts.
-   Corrective actions
    -   Test for the correct version of Windows by testing if the current version is greater-than or equal to the version your app, service, or driver needs.
    -   Driver installers and uninstall modules must never check the OS version.
-   Exceptions and Waivers
    -   Waivers will be considered for apps that meet the following criteria: *(Applies to desktop app certification only)*
        -   Apps that are delivered as one package that runs on Windows XP, Windows Vista, and Windows 7 and need to check the OS version to determine which components to install on a given operating system.
        -   Apps that check only the minimum version of the OS (during install only, not at runtime) by using only the approved API calls and list the minimum version requirement in the app manifest as required.
        -   Security apps such as antivirus and firewall apps, system utilities such as defrag utilities and backup apps, and diagnostics tools that check the OS version by using only the approved API calls.

## User account control (UAC) test

Tests the app to verify that it doesn't need unnecessarily elevated permissions to run.

-   Background
    -   An app that operates or installs only when the user is an administrator forces users to run the app with unnecessarily elevated permissions, which can allow malware to enter the user's computer.
    -   When users are always forced to run apps with elevated access tokens, the app can server as an entry point for deceptive or malicious code. This malware can easily modify the operating system, or worse, affect other users. It is nearly impossible to control a user that has full administrator access, because Administrators can install apps and run any apps or script on the computer. IT managers are always seeking ways to create "standard desktops" where users log on as standard users. Standard desktops greatly reduce help desk costs and reduce IT overhead.
    -   Most applications don't require administrator privileges at run time. A standard-user account should be able to run them. Windows apps must have a manifest (embedded or external) to define its execution level that tells OS the privileges needed to run the app. The app manifest only applies to .exe files, not .dll files. User Account Control (UAC) does not inspect DLLs during the creation of the process. UAC rules don't apply to Microsoft services. The app manifest can be embedded or external.
    -   To create a manifest, create a file with the name <app\_name>.exe.manifest and store it in the same directory as the EXE. Note that any external manifest is ignored if the app has an internal manifest.
        -   For example, <requestedExecutionLevel level=""asInvoker \| highestAvailable \| requireAdministrator"" uiAccess=""true\|false""/>
        -   The main process of the app must be run as a standard user (**asInvoker**). Any administrative features must be moved into a separate process that runs with administrative privileges.
        -   User facing apps that require elevated privileges must be Authenticode signed.
-   Test details
    -   All the user facing exes should be marked with asInvoker attribute. If they are marked as highestAvailable or requireAdministrator then they should be correctly authenticode signed. Any app exe should not have the uiAccess attribute set to true. Any exe which runs as a service is excluded from this particular check.
-   Corrective actions
    -   Review the app's manifest file for the correct entries and permission levels.
-   Exceptions and waivers
    -   A waiver is required for apps that run their main process with elevated privileges (**requireAdministrator** or **highestAvailable**). The main process is the process that provides the user’s entry point to the app.
    -   Waivers will be considered for the following scenarios:
        -   Administrative or system tools with execution level set to **highestAvailable**, **requireAdministrator**, or both.
        -   Only Accessibility or UI automation framework app sets the uiAccess flag to TRUE to bypass the user interface privilege isolation (UIPI). To properly start app utilization, this flag must be Authenticode signed, and must reside in a protected location in the file system, such as Program Files.

## Adhere to system restart manager messages

Tests how the app responds to system shutdown and restart messages.

-   Background
    -   Apps must exit as quickly as possible when they are notified the system is shutting down to provide a responsive shutdown or power-off experience for the user.
    -   In a critical shutdown, apps that return FALSE to [**WM\_QUERYENDSESSION**](/windows/desktop/Shutdown/wm-queryendsession) will be sent **WM\_ENDSESSION** and closed, while those that time out in response to WM\_QUERYENDSESSION will be forcibly terminated.
-   Test details
    -   Examines how the app responds to shut down and exit messages.
-   Corrective actions
    -   If your app fails this test, review how it handles these Windows messages:
        -   [**WM\_QUERYENDSESSION**](/windows/desktop/Shutdown/wm-queryendsession) with *LPARAM* = **ENDSESSION\_CLOSEAPP**(0x1): Desktop apps must respond (TRUE) immediately in preparation for a restart. Console apps can call [**SetConsoleCtrlHandler**](/windows/console/setconsolectrlhandler) to receive shutdown notification. Services can call [**RegisterServiceCtrlHandlerEx**](/windows/desktop/api/winsvc/nf-winsvc-registerservicectrlhandlerexa) to receive shutdown notifications in a handler routine.
        -   [**WM\_ENDSESSION**](/windows/desktop/Shutdown/wm-queryendsession) with *LPARAM* = **ENDSESSION\_CLOSEAPP**(0x1): Apps must return a 0 value within 30 seconds and shut down. At a minimum, apps should prepare by saving any user data and state the info that is needed after a restart.
    -   Console apps that receive the **CTRL\_C\_EVENT** notification should shut down immediately. Drivers must not veto a system shutdown event.
    -   **Note:** Apps that must block shutdown because of an operation that cannot be interrupted should use [**ShutdownBlockReasonCreate**](/windows/desktop/api/winuser/nf-winuser-shutdownblockreasoncreate) to register a string that explains the reason to the user. When the operation has completed, the app should call [**ShutdownBlockReasonDestroy**](/windows/desktop/api/winuser/nf-winuser-shutdownblockreasondestroy) to indicate that the system can be shut down.

## Safe mode test

Tests if the driver or service is configured to start in safe mode.

-   Background
    -   Safe mode allows users to diagnose and troubleshoot problems with Windows. Only drivers and services that are necessary to the basic operation of the operating system or provide diagnostic and recovery services should load in safe mode. Loading other files in safe mode makes it more difficult to troubleshoot problems with the operating system.
    -   By default, only the drivers and services that come pre-installed with Windows start in safe mode. All other drivers and services should be disabled unless the system requires them for basic operations or for diagnostic and recovery purposes.
-   Test details
    -   Drivers installed by the app should not be marked for loading in safe mode.
-   Corrective actions
    -   If the driver or service should not start in safe mode, remove the app's entries from the registry keys.
-   Exceptions and waivers
    -   Drivers and services that must start in safe mode require a waiver to be certified. The waiver request must include each driver and service to add to the SafeBoot registry keys and describe the technical reasons for why the driver or service must run in safe mode. The app installer must register all such drivers and services in these registry keys:
        -   HKLM/System/CurrentControlSet/Control/SafeBoot/Minimal
        -   HKLM/System/CurrentControlSet/Control/SafeBoot/Network
-   **Note:** You must test the drivers and services you want to start in safe mode to ensure that they function in safe mode without any errors.

## Multiuser session test

Test how the app behaves when run in multiple sessions at the same time.

-   Background
    -   Windows users must be able to run concurrent sessions. Apps must ensure that when they run in multiple sessions, either locally or remotely, the normal functionality of the app is not adversely affected. App settings and data files must be user-specific and the user's privacy and preferences must be restricted to the user's session.
-   Test details
    -   Runs multiple concurrent instances of the app to test the following:
        -   Multiple instances of an app running at the same time are isolated from each other.
    -   This means that user data from one instance is not visible to another instance. Sound in an inactive user session should not be heard in an active user session. In cases where multiple app instances use shared resources, the app must ensure that there is not a conflict.
        -   If the app was installed for multiple users, it stores data in the correct folder(s) and registry locations.
        -   The app can run in multiple user sessions (Fast User Switching) for both local and remote access.
    -   To ensure this, the app must check other terminal service (TS) sessions for existing instances of the app. If the app does not support multiple user sessions or remote access, it must clearly say this to the user when it's launched from such a session.
-   Corrective action
    -   Make sure that the app doesn’t store system-wide data files or settings in user-specific data stores, such as User Profile or HKCU. If it does, that info won’t be available to other users.
    -   Your app must install system-wide configuration and data files during installation and create the user-specific files and settings after installation when a user runs it.
    -   Make sure that the app doesn’t block multiple concurrent sessions, either locally or remotely. The app must not depend on global mutexes or other named-objects to check for or block multiple concurrent sessions.
    -   If the app can’t allow multiple concurrent sessions per user, use per-user or per-session namespaces for mutexes and other named-objects.

## Crashes and hangs test

Monitors the app during certification testing to record when it crashes or hangs.

-   Background
    -   App failures such as crashes and hangs are a major disruption to users and cause frustration. Eliminating such failures improves app stability and reliability, and overall, provides users with a better app experience. Apps that stop responding or crash can cause the user to lose data and have a poor experience.
-   Test details
    -   We test the app resilience and stability throughout the certification testing.
    -   The Windows App Certification Kit calls [**IApplicationActivationManager::ActivateApplication**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationactivationmanager-activateapplication) to launch Windows Store apps. For **ActivateApplication** to launch an app, User Account Control (UAC) must be enabled and the screen resolution must be at least 1024 x 768 or 768 x 1024. If either condition is not met, your app will fail this test.
-   Corrective Actions
    -   Make sure UAC is enabled on the test computer.
    -   Make sure you are running the test on a computer with large enough screen.
    -   If your app fails to launch and your test platform satisfies the prerequisites of [**ActivateApplication**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationactivationmanager-activateapplication), you can troubleshoot the problem by reviewing the activation event log. To find these entries in the event log:
        1.  Open eventvwr.exe and navigate to the \\Windows Logs\\Application node.
        2.  Filter the view to show Event Ids: 5900-6000.
        3.  Review the log entries for info that might explain why the app didn't launch.
    -   Troubleshoot the file with the problem, identify and fix the problem. Rebuild and re-test the app.
-   Additional resources
    -   [Using Application Verifier Within Your Software Development Lifecycle](https://blogs.msdn.com/b/ntdebugging/archive/2014/01/13/debugging-a-windows-8-1-store-app-crash-dump.aspx)
    -   [Application Verifier]( https://go.microsoft.com/fwlink/p/?LinkId=708300)
    -   [Using Application Verifier](https://www.microsoft.com/?ref=go)
    -   [AppInit DLLs](https://www.microsoft.com/?ref=go)
    -   [Minimize startup time (Windows Store apps using C#/VB/C++ and XAML)](/previous-versions/windows/apps/hh994639(v=win.10))

## Compatibility and resiliency test

-   Background
    -   This check will validate two aspects of an app, the app main executable(s) e.g. user facing app entry point must be manifested for compatibility, as well as declaring the right GUID. To support this new test the report will have a sub node under ‘Compatibility & resiliency’. The app will fail if one or both of these conditions are missing.
-   Test Details
    -   **Compatibility:** Apps must be fully functional without using Windows compatibility modes, AppHelp messages, or other compatibility fixes. A compatibility manifest allows Windows to provide your app the proper compatibility behavior under the different versions of the OS
    -   **AppInit:** Apps must not list DLLs to load in the HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\AppInit\_DLLs registry key.
    -   **Switchback:** The application must provide the switchback manifest. If the manifest is missing, Windows App Certification Kit gives a warning message. Windows App Certification Kit will also verify the manifest contains valid OS GUID.
-   Corrective actions
    -   Fix the app's component that uses the compatibility fix.
    -   Make sure that the app doesn’t rely on compatibility fixes for its functionality.
    -   Ensure your app is manifested and the compatibility section include the appropriate values
-   Additional Information
    -   See [AppInit DLLs](/previous-versions/windows/apps/hh994639(v=win.10)) for more info.

## Windows Security best practices test

-   Background
    -   An app should not change the default Windows security settings
-   Test Details
    -   Tests the app's security by running the Attack Surface Analyzer. The approach will be to add categories of failure on a per test basis. For example some categories for security test may include:
        -   Initialization failure
        -   Security Architecture failure
        -   Possible Buffer overflow failure
        -   Crash failure
    -   For details, refer [here](/previous-versions/windows/hh920280(v=win.10)).
-   Corrective actions
    -   Troubleshoot and fix the problem identified by the tests. Rebuild and re-test the app.

## Windows security features test

-   Background
    -   Applications must opt-into Windows security features. Changing the default Windows security protections can put customers at increased risk.
-   Test details
    -   Tests the app's security by running the BinScope Binary Analyzer. For details, refer [here](/previous-versions/windows/hh920280(v=win.10)).
-   Corrective actions
    -   Troubleshoot and fix the problem identified by the tests. Rebuild and re-test the app.

## High DPI test

It is highly recommended for the Win32 apps to be DPI aware. It is the key to make the app UI look consistently good across a wide variety of high-DPI display settings. A non-DPI-aware app running on a high-DPI display setting may have problems such as incorrect scaling of UI elements, clipped text, and blurry images. There are two ways to declare an app is DPI aware. One is to declare DPI.

-   Background
    -   This check will validate two aspects of an app, the main executable(s) e.g. user facing app entry points must be manifested for HIGH-DPI awareness and that the proper APIs are being called to support HIGH-DPI. The app will fail if one or both of these conditions are missing. This check will introduce a new section in the desktop report, see example below.
-   Test Details
    -   Test will generate a warning when we detect any of the following:
        -   The main EXE doesn’t declare DPI awareness in its manifest and it doesn’t call SetProcessDPIAware API. (Warn the developer if he forgets to add DPI awareness manifest).
        -   The main EXE doesn’t declare DPI awareness in its manifest, but it calls SetProcessDPIAware API (Warn the developer that he should use manifest to declare DPI awareness instead of calling the API).
        -   The mainEXE declares DPI awareness in its manifest, but it also calls SetProcessDPIAware API (Warn the developer that calling that API is not necessary).
        -   For the binaries which are not main EXEs, if they calls the API, give a warning (Calling the API is not recommended).
-   Corrective actions
    -   The use of SetProcessDPIAware() function is discouraged. If a DLL caches DPI settings during its initialization, invoking SetProcessDPIAware() in the app may generate a race condition. Calling SetProcessDPIAware() function in a DLL is not a good practice either.
-   Additional Information
    -   [Writing High-DPI apps](https://msdn.microsoft.com/library/windows/desktop/mt843498(v=vs.85).aspx(d=robot))

 

 
