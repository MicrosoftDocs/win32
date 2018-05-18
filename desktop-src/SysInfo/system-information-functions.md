---
Description: 'The following functions are used to retrieve or set system information.'
ms.assetid: 'aa7deebf-7dce-4147-8a15-1d7411aea0fa'
title: System Information Functions
---

# System Information Functions

The following functions are used to retrieve or set system information.



| Function                                                                     | Description                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CeipIsOptedIn**](ceipisoptedin.md)                                       | Checks whether the user has opted in for SQM data collection as part of the Customer Experience Improvement Program (CEIP).                                                                                                       |
| [**DnsHostnameToComputerName**](dnshostnametocomputername.md)               | Converts a DNS name to a NetBIOS name.                                                                                                                                                                                            |
| [**EnumSystemFirmwareTables**](enumsystemfirmwaretables.md)                 | Enumerates all system firmware tables of the specified type.                                                                                                                                                                      |
| [**ExpandEnvironmentStrings**](expandenvironmentstrings.md)                 | Replaces environment-variable strings with their defined values.                                                                                                                                                                  |
| [**GetComputerName**](getcomputername.md)                                   | Retrieves the NetBIOS name of the local computer.                                                                                                                                                                                 |
| [**GetComputerNameEx**](getcomputernameex.md)                               | Retrieves the NetBIOS or DNS name of the local computer.                                                                                                                                                                          |
| [**GetComputerObjectName**](getcomputerobjectname.md)                       | Retrieves the local computer's name in a specified format.                                                                                                                                                                        |
| [**GetCurrentHwProfile**](getcurrenthwprofile.md)                           | Retrieves the current hardware profile for the local computer.                                                                                                                                                                    |
| [**GetFirmwareEnvironmentVariable**](getfirmwareenvironmentvariable.md)     | Retrieves the value of the specified firmware environment variable from NVRAM.                                                                                                                                                    |
| [**GetFirmwareEnvironmentVariableEx**](getfirmwareenvironmentvariableex.md) | Retrieves the value of the specified firmware environment variable and its attributes.                                                                                                                                            |
| [**GetFirmwareType**](getfirmwaretype.md)                                   | Retrieves the firmware type of the local computer.                                                                                                                                                                                |
| [**GetIntegratedDisplaySize**](getintegrateddisplaysize.md)                 | Retrieves the best estimate of the diagonal size of the built-in screen, in inches.                                                                                                                                               |
| [**GetNativeSystemInfo**](getnativesysteminfo.md)                           | Retrieves information about the current system for an application running under WOW64.                                                                                                                                            |
| [**GetProductInfo**](getproductinfo.md)                                     | Retrieves the product type for the operating system on the local computer, and maps the type to the product types supported by the specified operating system.                                                                    |
| [**GetSystemDirectory**](getsystemdirectory.md)                             | Retrieves the path of the system directory.                                                                                                                                                                                       |
| [**GetSystemFirmwareTable**](getsystemfirmwaretable.md)                     | Retrieves the specified firmware table from the firmware table provider.                                                                                                                                                          |
| [**GetSystemInfo**](getsysteminfo.md)                                       | Retrieves information about the current system.                                                                                                                                                                                   |
| [**GetSystemRegistryQuota**](getsystemregistryquota.md)                     | Retrieves the current size of the registry and the maximum size that the registry is allowed to attain on the system.                                                                                                             |
| [**GetSystemWindowsDirectory**](getsystemwindowsdirectory.md)               | Retrieves the path of the shared Windows directory on a multi-user system.                                                                                                                                                        |
| [**GetSystemWow64Directory**](getsystemwow64directory.md)                   | Retrieves the path of the system directory used by WOW64.                                                                                                                                                                         |
| [**GetSystemWow64Directory2**](getsystemwow64directory2.md)                 | Retrieves the path of the system directory used by WOW64, using the specified image file machine type.                                                                                                                            |
| [**GetUserName**](getusername.md)                                           | Retrieves the user name of the current thread.                                                                                                                                                                                    |
| [**GetUserNameEx**](getusernameex.md)                                       | Retrieves the name of the user or other security principal associated with the calling thread. You can specify the format of the returned name.                                                                                   |
| [**GetVersion**](getversion.md)                                             | Retrieves the version number of the current operating system.                                                                                                                                                                     |
| [**GetVersionEx**](getversionex.md)                                         | Retrieves information about the current operating system.                                                                                                                                                                         |
| [**GetWindowsDirectory**](getwindowsdirectory.md)                           | Retrieves the path of the Windows directory.                                                                                                                                                                                      |
| [**IsNativeVhdBoot**](isnativevhdboot.md)                                   | Indicates if the OS was booted from a VHD container.                                                                                                                                                                              |
| [**IsWow64GuestMachineSupported**](iswow64guestmachinesupported.md)         |                                                                                                                                                                                                                                   |
| [**IsProcessorFeaturePresent**](isprocessorfeaturepresent.md)               | Determines whether a processor feature is supported by the current computer.                                                                                                                                                      |
| [**IsWow64Message**](https://msdn.microsoft.com/library/windows/desktop/ms684136)                                    | Determines whether the last message read from the queue of the current process originated from a WOW64 process.                                                                                                                   |
| [**IsWow64Process**](https://msdn.microsoft.com/library/windows/desktop/ms684139)                                    | Determines whether a process is running under WOW64.                                                                                                                                                                              |
| [**QueryPerformanceCounter**](queryperformancecounter.md)                   | Retrieves the current value of the high-resolution performance counter.                                                                                                                                                           |
| [**QueryPerformanceFrequency**](queryperformancefrequency.md)               | Retrieves the frequency of the high-resolution performance counter.                                                                                                                                                               |
| [**RtlGetSuiteMask**](rtlgetsuitemask.md)                                   | Retrieves a bit mask that identifies the product suites available on the system. If this function is called in an application that runs in the context of a server silo, the suite mask for the server silo is retrieved instead. |
| [**SetComputerName**](setcomputername.md)                                   | Sets a new NetBIOS name for the local computer.                                                                                                                                                                                   |
| [**SetComputerNameEx**](setcomputernameex.md)                               | Sets a new NetBIOS or DNS name for the local computer.                                                                                                                                                                            |
| [**SetFirmwareEnvironmentVariable**](setfirmwareenvironmentvariable.md)     | Sets the value of the specified firmware environment variable.                                                                                                                                                                    |
| [**SetFirmwareEnvironmentVariableEx**](setfirmwareenvironmentvariableex.md) | Sets the value of the specified firmware environment variable and its attributes.                                                                                                                                                 |
| [**TranslateName**](translatename.md)                                       | Converts a directory service object name from one format to another.                                                                                                                                                              |
| [**VerifyVersionInfo**](verifyversioninfo.md)                               | Compares a set of version requirements to the values for the current operating system.                                                                                                                                            |
| [**VerSetConditionMask**](versetconditionmask.md)                           | Builds the condition mask for the [**VerifyVersionInfo**](verifyversioninfo.md) function.                                                                                                                                        |
| [**Wow64DisableWow64FsRedirection**](https://msdn.microsoft.com/library/windows/desktop/aa365743)    | Disables file system redirection for the calling thread.                                                                                                                                                                          |
| [**Wow64EnableWow64FsRedirection**](https://msdn.microsoft.com/library/windows/desktop/aa365744)      | Enables or disables file system redirection for the calling thread.                                                                                                                                                               |
| [**Wow64RevertWow64FsRedirection**](https://msdn.microsoft.com/library/windows/desktop/aa365745)      | Restores file system redirection for the calling thread.                                                                                                                                                                          |



 

## Obsolete Functions

-   [**NtQuerySystemInformation**](ntquerysysteminformation.md)
-   [**ZwQuerySystemInformation**](zwquerysysteminformation.md)

 

 



