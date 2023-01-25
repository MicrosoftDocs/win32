---
title: Dynamic-link library search order
description: You can control the specific location from which any given DLL is loaded by specifying a full path, or by using another mechanism such as a manifest. If you don't use one of those methods, then the system searches for the DLL at load time as described in this topic.
ms.date: 01/25/2023
ms.assetid: 44228cf2-6306-466c-8f16-f513cd3ba8b5
ms.topic: article
---

# Dynamic-link library search order

It's common for multiple versions of the same dynamic-link library (DLL) to exist in different file system locations in an operating system (OS). You can control the specific location from which any given DLL is loaded by specifying a full path; or by using another mechanism such as redirection or an application manifest (also known as a side-by-side application manifest, or a fusion manifest).

* [Dynamic-link library redirection](/windows/win32/dlls/dynamic-link-library-redirection).
* [Manifests](/windows/win32/sbscs/manifests).

If you don't use one of those methods, then the system searches for the DLL at load time as described in this topic.

> [!TIP]
> For definitions of *packaged* and *unpackaged* apps, see [Advantages and disadvantages of packaging your app](/windows/apps/package-and-deploy/#advantages-and-disadvantages-of-packaging-your-app).

## Factors that affect searching

These factors affect whether or not the system searches for a DLL:

* **A DLL with the same module name is already loaded into memory**. In this case the system checks for either redirection or a manifest; in their absense, the system resolves to the already-loaded DLL no matter which directory it's in. Either way, the system doesn't search for the DLL.
* **The DLL is on the list of known DLLs for the version of Windows on which the application is running**. In this case, instead of searching for the DLL, the system uses its copy of the known DLL (and the known DLL's dependent DLLs, if any). For a list of known DLLs on the current system, see the registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs`.
* **The DLL has dependencies**. In this case, the system searches for the dependent DLLs as if they were loaded via only their module names. That's true even if the first DLL was loaded by specifying a full path.

## Search order for packaged apps

When a packaged app loads a packaged module (specifically, a library module: a `.dll` file) by calling the [**LoadPackagedLibrary**](/windows/win32/api/Winbase/nf-winbase-loadpackagedlibrary) function, the DLL must be in the package dependency graph of the process. For more information, see **LoadPackagedLibrary**. When a packaged app loads a module by other means, and doesn't specify a full path, the system searches for the DLL and its dependencies at load time as described in this section.

Before the system searches for a DLL, it checks the [Factors that affect searching](#factors-that-affect-searching).

If the system must search for a module or its dependencies, then it always uses the search order for packaged apps; even if a dependency is not packaged app code.

### Standard search order for packaged apps

The system searches these locations in this order:

1. The package dependency graph of the process. This is the application's package plus any dependencies specified as `<PackageDependency>` in the `<Dependencies>` section of the application's package manifest. Dependencies are searched in the order they appear in the manifest.
1. The directory the calling process was loaded from.
1. The system directory (`%SystemRoot%\system32`).

If a DLL has dependencies, then the system searches for the dependent DLLs as if they were loaded with just their module names (even if the first DLL was loaded by specifying a full path).

### Alternate search order for packaged apps

If a module changes the standard search order by calling the [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function with **LOAD_WITH_ALTERED_SEARCH_PATH**, then the system searches the directory that the specified module was loaded from instead of the directory of the calling process. The system searches these locations in this order:

1. The package dependency graph of the process. This is the application's package plus any dependencies specified as `<PackageDependency>` in the `<Dependencies>` section of the application's package manifest. Dependencies are searched in the order they appear in the manifest.
1. The directory the specified module was loaded from.
1. The system directory (`%SystemRoot%\system32`).

## Search order for unpackaged apps

An unpackaged app can control the location from which a DLL is loaded by either specifying a full path, using redirection, or by using a manifest. If you don't use one of those methods, then the system searches for the DLL at load time as described in this section.

Before the system searches for a DLL, it checks the [Factors that affect searching](#factors-that-affect-searching).

> [!IMPORTANT]
> If an attacker gains control of one of the directories that's searched, then it can place a malicious copy of the DLL in that directory. For ways to help prevent such attacks, see [Dynamic-link library security](/windows/win32/dlls/dynamic-link-library-security).

### Standard search order for unpackaged apps

The standard DLL search order used by the system depends on whether or not *safe DLL search mode* is enabled.

Safe DLL search mode (which is enabled by default) moves the user's current directory later in the search order. To disable safe DLL search mode, create the `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode` registry value, and set it to 0. Calling the [**SetDllDirectory**](/windows/win32/api/winbase/nf-winbase-setdlldirectorya) function effectively disables safe DLL search mode (while the specified directory is in the search path), and changes the search order as described in this topic.

If safe DLL search mode is enabled, then the search order is as follows:

1. The directory from which the application loaded.
2. The system directory. Use the [**GetSystemDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to retrieve the path of this directory.
3. The 16-bit system directory. There's no function that obtains the path of this directory, but it is searched.
4. The Windows directory. Use the [**GetWindowsDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
5. The current directory.
6. The directories that are listed in the `PATH` environment variable. This doesn't include the per-application path specified by the **App Paths** registry key. The **App Paths** key isn't used when computing the DLL search path.

If safe DLL search mode is *disabled*, then the search order is the same except that *the current directory* moves from position 5 to position 2 in the sequence.

### Alternate search order for unpackaged apps

To change the standard search order used by the system, you can call the [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function with **LOAD_WITH_ALTERED_SEARCH_PATH**. You can also change the standard search order by calling the [**SetDllDirectory**](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function.

> [!NOTE]
> The standard search order of the process will also be affected by calling the [**SetDllDirectory**](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function in the parent process before the start of the current process.

If you specify an alternate search strategy, then its behavior continues until all associated executable modules have been located. After the system starts processing DLL initialization routines, the system reverts to the standard search strategy.

The [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function supports an alternate search order if the call specifies **LOAD_WITH_ALTERED_SEARCH_PATH**, and the *lpFileName* parameter specifies an absolute path.

* The standard search strategy begins in the calling application's directory.
* The alternate search strategy specified by [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) with **LOAD_WITH_ALTERED_SEARCH_PATH** begins in the directory of the executable module that **LoadLibraryEx** is loading.

That's the only way in which they differ.

If safe DLL search mode is enabled, then the alternate search order is as follows:

1. The directory specified by *lpFileName*.
2. The system directory. Use the [**GetSystemDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to retrieve the path of this directory.
3. The 16-bit system directory. There's no function that obtains the path of this directory, but it is searched.
4. The Windows directory. Use the [**GetWindowsDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
5. The current directory.
6. The directories that are listed in the `PATH` environment variable. This doesn't include the per-application path specified by the **App Paths** registry key. The **App Paths** key isn't used when computing the DLL search path.

If safe DLL search mode is *disabled*, then the alternate search order is the same except that *the current directory* moves from position 5 to position 2 in the sequence.

The [**SetDllDirectory**](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function supports an alternate search order if the *lpPathName* parameter specifies a path. The alternate search order is as follows:

1. The directory from which the application loaded.
1. The directory specified by the *lpPathName* parameter of [**SetDllDirectory**](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya).
1. The system directory.
1. The 16-bit system directory.
1. The Windows directory.
1. The directories that are listed in the `PATH` environment variable.

If the *lpPathName* parameter is an empty string, then the call removes the current directory from the search order.

[**SetDllDirectory**](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) effectively disables safe DLL search mode while the specified directory is in the search path. To restore safe DLL search mode based on the **SafeDllSearchMode** registry value, and restore the current directory to the search order, call **SetDllDirectory** with *lpPathName* as NULL.

> [!NOTE]
> As of Windows 11, version 21H2 (10.0; Build 22000), the The package dependency graph can apply to unpackaged apps.

### Search order using LOAD_LIBRARY_SEARCH flags

You can specify a search order by using one or more **LOAD_LIBRARY_SEARCH** flags with the [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function. You can also use **LOAD_LIBRARY_SEARCH** flags with the [**SetDefaultDllDirectories**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories) function to establish a DLL search order for a process. You can specify additional directories for the process DLL search order by using the [**AddDllDirectory**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory) or [**SetDllDirectory**](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) functions.

The directories that are searched depend on the flags specified with [**SetDefaultDllDirectories**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories) or [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa). If you use more than one flag, then the corresponding directories are searched in this order:

1. **LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR**. The directory that contains the DLL is searched. This directory is searched only for dependencies of the DLL to be loaded.
1. **LOAD_LIBRARY_SEARCH_APPLICATION_DIR**. The application directory is searched.
1. **LOAD_LIBRARY_SEARCH_USER_DIRS**. Paths explicitly added with the [**AddDllDirectory**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory) function or the [**SetDllDirectory**](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function are searched. If you add more than one path, then the order in which the paths are searched is unspecified.
1. **LOAD\_LIBRARY\_SEARCH\_SYSTEM32**. The System directory is searched.

If you call [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) with no **LOAD_LIBRARY_SEARCH** flags, or you establish a DLL search order for the process, then the system searches for DLLs using either the standard search order or the alternate search order.

## Related topics

* [Application registration](/windows/win32/shell/app-registration)
* [Dynamic-link library redirection](dynamic-link-library-redirection.md)
* [Dynamic-link library security](dynamic-link-library-security.md)
* [Side-by-side components](/windows/win32/SbsCs/isolated-applications-and-side-by-side-assemblies-portal)
* [AddDllDirectory](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory)
* [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)
* [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa)
* [LoadPackagedLibrary](/windows/win32/api/Winbase/nf-winbase-loadpackagedlibrary)
* [SetDefaultDllDirectories](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories)
* [SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya)
