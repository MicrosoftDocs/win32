---
title: Dynamic-link library search order
description: See the search order that the system uses to search for a specific DLL at load time if you don't specify a path.
ms.date: 02/06/2023
ms.assetid: 44228cf2-6306-466c-8f16-f513cd3ba8b5
ms.topic: article
---

# Dynamic-link library search order

Multiple versions of the same dynamic-link library (DLL) commonly exist in different file system locations within an operating system (OS). You can specify a full path to the location you want to load a DLL from. If you don't specify a path, the system searches for the DLL at load time in the order that this article describes.

> [!TIP]
> For definitions of *packaged* and *unpackaged* apps, see [Advantages and disadvantages of packaging your app](/windows/apps/package-and-deploy/#advantages-and-disadvantages-of-packaging-your-app).

## Factors that affect search

Special search factors affect the DLL search order. These locations appear along with other search locations in the search order for certain app types. The following list introduces and names the locations that appear later in this article:

- **DLL redirection**. For details, see [Dynamic-link library redirection](/windows/win32/dlls/dynamic-link-library-redirection).
- **API sets**. For details, see [Windows API sets](/windows/win32/apiindex/windows-apisets).
- **Side-by-side (SxS) manifest redirection**. For desktop apps only, not UWP apps, you can redirect by using an application manifest, also called a side-by-side manifest or a fusion manifest. For details, see [Manifests](/windows/win32/sbscs/manifests).
- **Loaded module list**. The system can check to see whether a DLL with the same module name is already loaded into memory, no matter what directory it was loaded from.
- **Known DLLs**. If the DLL is on the list of known DLLs for the version of Windows the application is running on, the system uses its copy of the known DLL and its dependent DLLs if any. For a list of known DLLs on the current system, see the registry key **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs**.

If a DLL has dependencies, the system searches for the dependent DLLs by using only their module names, even if the first DLL was loaded by specifying a full path.

> [!IMPORTANT]
> An attacker that gains control of a searched directory can place a malicious copy of the DLL in that directory. For ways to help prevent such attacks, see [Dynamic-link library security](/windows/win32/dlls/dynamic-link-library-security).

## Search order for packaged apps

When a packaged app loads a packaged module or library module *.dll* file by calling the [LoadPackagedLibrary](/windows/win32/api/Winbase/nf-winbase-loadpackagedlibrary) function, the DLL must be in the package dependency graph of the process. When a packaged app loads a module by other means and doesn't specify a full path, the system searches for the DLL and its dependencies at load time as this section describes.

When the system searches for the module or its dependencies, it uses the search order for packaged apps even if a dependency isn't packaged app code.

### Standard search order for packaged apps

For packaged apps, the system searches in this order:

1. DLL redirection.
2. API sets.
3. SxS manifest redirection, for packaged desktop apps only, not UWP apps.
4. Loaded module list.
5. Known DLLs.
6. The package dependency graph of the process. This is the application's package plus any `<PackageDependency>` entries in the `<Dependencies>` section of the application's package manifest. Dependencies are searched in the order they appear in the manifest.
7. The directory the calling process was loaded from, that is the executable's directory.
8. The system directory, *%SystemRoot%\\system32*.

If a DLL has dependencies, the system searches for the dependent DLLs by using only their module names, even if the first DLL was loaded by specifying a full path.

### Alternate search order for packaged apps

If a module changes the standard search order by calling the [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function with **LOAD_WITH_ALTERED_SEARCH_PATH**, the search order is the same as the standard search order, except that in step 7, the system searches the directory that the specified module was loaded from, or the top-loading module's directory, instead of the executable's directory.

## Search order for unpackaged apps

When an unpackaged app loads a module and doesn't specify a full path, the system searches for the DLL at load time as this section describes.

### Standard search order for unpackaged apps

The standard DLL search order the system uses depends on whether or not you enable *safe DLL search mode*.

Safe DLL search mode, which is enabled by default, moves the user's current directory later in the search order. To disable safe DLL search mode, create the **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode** registry key and set it to **0**. Call the [SetDllDirectory](/windows/win32/api/winbase/nf-winbase-setdlldirectorya) function to effectively disable safe DLL search mode when the specified directory is in the search path, and change the search order as this article describes.

If safe DLL search mode is enabled, the search order is as follows:

1. DLL redirection.
2. API sets.
3. SxS manifest redirection.
4. Loaded module list.
5. Known DLLs.
6. **For Windows 11, version 21H2 (10.0; Build 22000) and later**, the package dependency graph of the process. This location is the application's package plus any dependencies specified as `<PackageDependency>` in the `<Dependencies>` section of the application's package manifest. Dependencies are searched in the order they appear in the manifest.
7. The directory that the application loaded from.
8. The system directory. Use the [GetSystemDirectory](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to get the path of this directory.
9. The 16-bit system directory. There's no function that gets the path of this directory, but it's searched.
10. The Windows directory. Use the [GetWindowsDirectory](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
11. The current directory.
12. The directories in the **PATH** environment variable. This path doesn't include the per-application path that the **App Paths** registry key specifies. The system doesn't use the **App Paths** key when computing the DLL search path.

If safe DLL search mode is disabled, the search order is the same except that the current directory moves from position 11 to position 8, immediately after the directory that the application loaded from.

### Alternate search order for unpackaged apps

To change the standard search order the system uses, you can call the [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function with **LOAD_WITH_ALTERED_SEARCH_PATH**. You can also change the standard search order by calling the [SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function.

> [!NOTE]
> You can also affect the standard search order of the process by calling the [SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function in the parent process before the start of the current process.

If you specify an alternate search strategy, its behavior continues until it locates all associated executable modules. After the system starts processing DLL initialization routines, the system reverts to the standard search strategy.

The [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function supports an alternate search order if the call specifies **LOAD_WITH_ALTERED_SEARCH_PATH**, and the `lpFileName` parameter specifies an absolute path.

The standard search strategy and the alternate search strategy differ only in the following way:

- After the initial steps, the standard search strategy begins in the calling application's directory.
- After the initial steps, the alternate search strategy specified by [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) with **LOAD_WITH_ALTERED_SEARCH_PATH** begins in the directory of the executable module that `LoadLibraryEx` loads.

If safe DLL search mode is enabled, the alternate search order is as follows:

Steps 1-6 are the same as the standard search order.

7. The directory that `lpFileName` specifies.
8. The system directory. Use the [GetSystemDirectory](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function to get the path of this directory.
9. The 16-bit system directory. There's no function that gets the path of this directory, but it's searched.
10. The Windows directory. Use the [GetWindowsDirectory](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function to get the path of this directory.
11. The current directory.
12. The directories in the **PATH** environment variable. This path doesn't include the per-application path that the **App Paths** registry key specifies. The system doesn't use the **App Paths** key when computing the DLL search path.

If safe DLL search mode is disabled, then the alternate search order is the same, except that the current directory moves from position 11 to position 8 in the sequence.

The [SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function supports an alternate search order if the `lpPathName` parameter specifies a path. The alternate search order is as follows:

Steps 1-6 are the same as the standard search order.

7. The directory from which the application loaded.
8. The directory that the `lpPathName` parameter of [SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) specifies.
9. The system directory.
10. The 16-bit system directory.
11. The Windows directory.
12. The directories in the **PATH** environment variable.

If the `lpPathName` parameter is an empty string, the call removes the current directory from the search order.

[SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) effectively disables safe DLL search mode when the specified directory is in the search path. To restore safe DLL search mode based on the **SafeDllSearchMode** registry value, and restore the current directory to the search order, call `SetDllDirectory` with `lpPathName` as `NULL`.

### Search order using LOAD_LIBRARY_SEARCH flags

You can specify a search order by using one or more **LOAD_LIBRARY_SEARCH** flags with the [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function. You can also use **LOAD_LIBRARY_SEARCH** flags with the [SetDefaultDllDirectories](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories) function to establish a DLL search order for a process. You can specify more directories for the process DLL search order by using the [AddDllDirectory](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory) or [SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) functions.

The directories that are searched depend on the flags you specify with [SetDefaultDllDirectories](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories) or [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa). If you use more than one flag, the corresponding directories are searched in the following order:

1. **LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR**. The directory that contains the DLL is searched only for dependencies of the DLL to be loaded.
1. **LOAD_LIBRARY_SEARCH_APPLICATION_DIR**. The application directory.
1. **LOAD_LIBRARY_SEARCH_USER_DIRS**. Paths explicitly added with the [AddDllDirectory](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory) or [SetDllDirectory](/windows/win32/api/Winbase/nf-winbase-setdlldirectorya) function. If you add more than one path, the order to search the paths in is unspecified.
1. **LOAD_LIBRARY_SEARCH_SYSTEM32**. The *System* directory.

If you call [LoadLibraryEx](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) with no **LOAD_LIBRARY_SEARCH** flags, or you establish a DLL search order for the process, the system searches for DLLs using either the standard search order or the alternate search order.

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
