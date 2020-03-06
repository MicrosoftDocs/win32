---
Description: Applications can control the location from which a DLL is loaded by specifying a full path or using another mechanism such as a manifest. If these methods are not used, the system searches for the DLL at load time as described in this topic.
ms.assetid: 44228cf2-6306-466c-8f16-f513cd3ba8b5
title: Dynamic-Link Library Search Order
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Library Search Order

A system can contain multiple versions of the same dynamic-link library (DLL). Applications can control the location from which a DLL is loaded by specifying a full path or using another mechanism such as a manifest. If these methods are not used, the system searches for the DLL at load time as described in this topic.

-   [Factors That Affect Searching](#factors-that-affect-searching)
-   [Search Order for Windows Store apps](#search-order-for-windows-store-apps)
    -   [Standard Search Order for Windows Store apps](#standard-search-order-for-windows-store-apps)
    -   [Alternate Search Order for Windows Store apps](#alternate-search-order-for-windows-store-apps)
-   [Search Order for Desktop Applications](#search-order-for-desktop-applications)
    -   [Standard Search Order for Desktop Applications](#standard-search-order-for-desktop-applications)
    -   [Alternate Search Order for Desktop Applications](#alternate-search-order-for-desktop-applications)
    -   [Search Order Using **LOAD\_LIBRARY\_SEARCH** Flags](https://docs.microsoft.com/windows)
-   [Related topics](#related-topics)

## Factors That Affect Searching

The following factors affect whether the system searches for a DLL:

-   If a DLL with the same module name is already loaded in memory, the system checks only for redirection and a manifest before resolving to the loaded DLL, no matter which directory it is in. The system does not search for the DLL.
-   If the DLL is on the list of known DLLs for the version of Windows on which the application is running, the system uses its copy of the known DLL (and the known DLL's dependent DLLs, if any) instead of searching for the DLL. For a list of known DLLs on the current system, see the following registry key: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\KnownDLLs**.
-   If a DLL has dependencies, the system searches for the dependent DLLs as if they were loaded with just their module names. This is true even if the first DLL was loaded by specifying a full path.

## Search Order for Windows Store apps

When a Windows Store app loads a packaged module by calling the [**LoadPackagedLibrary**](/windows/desktop/api/Winbase/nf-winbase-loadpackagedlibrary) function, the DLL must be in the package dependency graph of the process. For more information, see **LoadPackagedLibrary**. When a Windows Store app loads a module by other means and does not specify a full path, the system searches for the DLL and its dependencies at load time as described in this section.

**Windows 7, Windows Server 2008 R2, Windows Vista, Windows Server 2008, Windows Server 2003 and Windows XP:** Windows Store apps are supported starting with Windows 8 and Windows Server 2012.

Before the system searches for a DLL, it checks the following:

-   If a DLL with the same module name is already loaded in memory, the system uses the loaded DLL, no matter which directory it is in. The system does not search for the DLL.
-   If the DLL is on the list of known DLLs for the version of Windows on which the application is running, the system uses its copy of the known DLL (and the known DLL's dependent DLLs, if any). The system does not search for the DLL. For a list of known DLLs on the current system, see the following registry key: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\KnownDLLs**.

If the system must search for a module or its dependencies, it always uses the search order for Windows Store apps even if a dependency is not Windows Store app code.

### Standard Search Order for Windows Store apps

If the module is not already loaded or on the list of known DLLs, the system searches these locations in this order:

1.  The package dependency graph of the process. This is the application's package plus any dependencies specified as `<PackageDependency>` in the `<Dependencies>` section of the application's package manifest. Dependencies are searched in the order they appear in the manifest.
2.  The directory the calling process was loaded from.
3.  The system directory (%SystemRoot%\\system32).

If a DLL has dependencies, the system searches for the dependent DLLs as if they were loaded with just their module names. This is true even if the first DLL was loaded by specifying a full path.

### Alternate Search Order for Windows Store apps

If a module changes the standard search order by calling the [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function with **LOAD\_WITH\_ALTERED\_SEARCH\_PATH**, the system searches the directory the specified module was loaded from instead of the directory of the calling process. The system searches these locations in this order:

1.  The package dependency graph of the process. This is the application's package plus any dependencies specified as `<PackageDependency>` in the `<Dependencies>` section of the application's package manifest. Dependencies are searched in the order they appear in the manifest.
2.  The directory the specified module was loaded from.
3.  The system directory (%SystemRoot%\\system32).

## Search Order for Desktop Applications

Desktop applications can control the location from which a DLL is loaded by specifying a full path, using [DLL redirection](dynamic-link-library-redirection.md), or by using a [manifest](https://docs.microsoft.com/windows/desktop/SbsCs/manifests). If none of these methods are used, the system searches for the DLL at load time as described in this section.

Before the system searches for a DLL, it checks the following:

-   If a DLL with the same module name is already loaded in memory, the system uses the loaded DLL, no matter which directory it is in. The system does not search for the DLL.
-   If the DLL is on the list of known DLLs for the version of Windows on which the application is running, the system uses its copy of the known DLL (and the known DLL's dependent DLLs, if any). The system does not search for the DLL. For a list of known DLLs on the current system, see the following registry key: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\KnownDLLs**.

If a DLL has dependencies, the system searches for the dependent DLLs as if they were loaded with just their module names. This is true even if the first DLL was loaded by specifying a full path.

> [!IMPORTANT]
> If an attacker gains control of one of the directories that is searched, it can place a malicious copy of the DLL in that directory. For ways to help prevent such attacks, see [Dynamic-Link Library Security](dynamic-link-library-security.md).

 

### Standard Search Order for Desktop Applications

The standard DLL search order used by the system depends on whether safe DLL search mode is enabled or disabled. Safe DLL search mode places the user's current directory later in the search order.

Safe DLL search mode is enabled by default. To disable this feature, create the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager**\\**SafeDllSearchMode** registry value and set it to 0. Calling the [**SetDllDirectory**](https://docs.microsoft.com/windows/desktop/api/winbase/nf-winbase-setdlldirectorya) function effectively disables **SafeDllSearchMode** while the specified directory is in the search path and changes the search order as described in this topic.

**Windows XP:** Safe DLL search mode is disabled by default. To enable this feature, create the **SafeDllSearchMode** registry value and set it to 1. Safe DLL search mode is enabled by default starting with Windows XP with Service Pack 2 (SP2).

If **SafeDllSearchMode** is enabled, the search order is as follows:

1.  The directory from which the application loaded.
2.  The system directory. Use the [**GetSystemDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to get the path of this directory.
3.  The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
4.  The Windows directory. Use the [**GetWindowsDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
5.  The current directory.
6.  The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the **App Paths** registry key. The **App Paths** key is not used when computing the DLL search path.

If **SafeDllSearchMode** is disabled, the search order is as follows:

1.  The directory from which the application loaded.
2.  The current directory.
3.  The system directory. Use the [**GetSystemDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to get the path of this directory.
4.  The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
5.  The Windows directory. Use the [**GetWindowsDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
6.  The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the **App Paths** registry key. The **App Paths** key is not used when computing the DLL search path.

### Alternate Search Order for Desktop Applications

The standard search order used by the system can be changed by calling the [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function with **LOAD\_WITH\_ALTERED\_SEARCH\_PATH**. The standard search order can also be changed by calling the [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya) function.

**Note:** The standard search order of the process will also be affected by calling the [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya) function in the parent process before start of the current process.

**Windows XP:** Changing the standard search order by calling [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya) is not supported until Windows XP with Service Pack 1 (SP1).

If you specify an alternate search strategy, its behavior continues until all associated executable modules have been located. After the system starts processing DLL initialization routines, the system reverts to the standard search strategy.

The [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function supports an alternate search order if the call specifies **LOAD\_WITH\_ALTERED\_SEARCH\_PATH** and the *lpFileName* parameter specifies an absolute path.

Note that the standard search strategy and the alternate search strategy specified by [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) with **LOAD\_WITH\_ALTERED\_SEARCH\_PATH** differ in just one way: The standard search begins in the calling application's directory, and the alternate search begins in the directory of the executable module that **LoadLibraryEx** is loading.

If **SafeDllSearchMode** is enabled, the alternate search order is as follows:

1.  The directory specified by *lpFileName*.
2.  The system directory. Use the [**GetSystemDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to get the path of this directory.
3.  The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
4.  The Windows directory. Use the [**GetWindowsDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
5.  The current directory.
6.  The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the **App Paths** registry key. The **App Paths** key is not used when computing the DLL search path.

If **SafeDllSearchMode** is disabled, the alternate search order is as follows:

1.  The directory specified by *lpFileName*.
2.  The current directory.
3.  The system directory. Use the [**GetSystemDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to get the path of this directory.
4.  The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
5.  The Windows directory. Use the [**GetWindowsDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
6.  The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the **App Paths** registry key. The **App Paths** key is not used when computing the DLL search path.

The [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya) function supports an alternate search order if the *lpPathName* parameter specifies a path. The alternate search order is as follows:

1.  The directory from which the application loaded.
2.  The directory specified by the *lpPathName* parameter of [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya).
3.  The system directory. Use the [**GetSystemDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to get the path of this directory. The name of this directory is System32.
4.  The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched. The name of this directory is System.
5.  The Windows directory. Use the [**GetWindowsDirectory**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
6.  The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the **App Paths** registry key. The **App Paths** key is not used when computing the DLL search path.

If the *lpPathName* parameter is an empty string, the call removes the current directory from the search order.

[**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya) effectively disables safe DLL search mode while the specified directory is in the search path. To restore safe DLL search mode based on the **SafeDllSearchMode** registry value and restore the current directory to the search order, call **SetDllDirectory** with *lpPathName* as NULL.

### Search Order Using **LOAD\_LIBRARY\_SEARCH** Flags

An application can specify a search order by using one or more **LOAD\_LIBRARY\_SEARCH** flags with the [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function. An application can also use **LOAD\_LIBRARY\_SEARCH** flags with the [**SetDefaultDllDirectories**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories) function to establish a DLL search order for a process. The application can specify additional directories for the process DLL search order by using the [**AddDllDirectory**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory) or [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya) functions.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** The **LOAD\_LIBRARY\_SEARCH** flags are available on systems with [KB2533623](https://support.microsoft.com/kb/2533623) installed.

**Windows Server 2003 and Windows XP:** The **LOAD\_LIBRARY\_SEARCH** flags are not supported.

The directories that are searched depend on the flags specified with [**SetDefaultDllDirectories**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa). If more than one flag is used, the corresponding directories are searched in the following order:

1.  The directory that contains the DLL (**LOAD\_LIBRARY\_SEARCH\_DLL\_LOAD\_DIR**). This directory is searched only for dependencies of the DLL to be loaded.
2.  The application directory (**LOAD\_LIBRARY\_SEARCH\_APPLICATION\_DIR**).
3.  Paths explicitly added with the [**AddDllDirectory**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory) function (**LOAD\_LIBRARY\_SEARCH\_USER\_DIRS**) or the [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya) function. If more than one path has been added, the order in which the paths are searched is unspecified.
4.  The System directory (**LOAD\_LIBRARY\_SEARCH\_SYSTEM32**).

If the application does not call [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) with any **LOAD\_LIBRARY\_SEARCH** flags or establish a DLL search order for the process, the system searches for DLLs using either the standard search order or the alternate search order.

## Related topics

<dl> <dt>

[**AddDllDirectory**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory)
</dt> <dt>

[Application Registration](https://docs.microsoft.com/windows/desktop/shell/app-registration)
</dt> <dt>

[Dynamic-Link Library Redirection](dynamic-link-library-redirection.md)
</dt> <dt>

[Dynamic-Link Library Security](dynamic-link-library-security.md)
</dt> <dt>

[**LoadLibrary**](https://msdn.microsoft.com/library/ms684175(v=VS.85).aspx)
</dt> <dt>

[**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa)
</dt> <dt>

[**LoadPackagedLibrary**](/windows/desktop/api/Winbase/nf-winbase-loadpackagedlibrary)
</dt> <dt>

[**SetDefaultDllDirectories**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories)
</dt> <dt>

[**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya)
</dt> <dt>

[Side-by-side Components](https://docs.microsoft.com/windows/desktop/SbsCs/isolated-applications-and-side-by-side-assemblies-portal)
</dt> </dl>

 

 



