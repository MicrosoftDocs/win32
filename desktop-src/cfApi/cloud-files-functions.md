---
Description: The following functions are used in creating and maintaining placeholder files and directories.
ms.assetid: 68B667E2-E8C6-41F9-A0E2-C8CDF60D6472
title: Cloud Filter Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cloud Filter Functions

The following functions are used in creating and maintaining placeholder files and directories.

## In this section



| Topic                                                                                                  | Description                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CfCloseHandle**](https://msdn.microsoft.com/library/windows/desktop/mt827476)<br/>                                                 | Closes the file or directory handle returned by [**CfOpenFileWithOplock**](https://msdn.microsoft.com/library/windows/desktop/mt827495). This should not be used with standard Win32 file handles, only on handles used within CfApi.h.<br/> |
| [**CfConnectSyncRoot**](https://msdn.microsoft.com/library/windows/desktop/mt827477)<br/>                                         | Initiates bi-directional communication between a sync provider and the sync filter API.<br/>                                                                                                                   |
| [**CfConvertToPlaceholder**](https://msdn.microsoft.com/library/windows/desktop/mt827478)<br/>                               | Converts a normal file/directory to a placeholder file/directory.<br/>                                                                                                                                         |
| [**CfCreatePlaceholders**](https://msdn.microsoft.com/library/windows/desktop/mt827479)<br/>                                   | Creates one or more new placeholder files or directories under a sync root tree.<br/>                                                                                                                          |
| [**CfDisconnectSyncRoot**](https://msdn.microsoft.com/library/windows/desktop/mt827481)<br/>                                   | Disconnects a communication channel created by [**CfConnectSyncRoot**](https://msdn.microsoft.com/library/windows/desktop/mt827477).<br/>                                                                                                       |
| [**CfExecute**](https://msdn.microsoft.com/library/windows/desktop/mt827482)<br/>                                                         | The main entry point for all connection key based placeholder operations. It is intended to be used by a sync provider to respond to various callbacks from the platform.<br/>                                 |
| [**CfGetCorrelationVector**](https://msdn.microsoft.com/library/windows/desktop/mt827483)<br/>                               | Allows the sync provider to query the current correlation vector for a given placeholder file.<br/>                                                                                                            |
| [**CfGetPlaceholderInfo**](https://msdn.microsoft.com/library/windows/desktop/mt827484)<br/>                                   | Gets various characteristics of a placeholder file or folder.<br/>                                                                                                                                             |
| [**CfGetPlaceholderRangeInfo**](https://msdn.microsoft.com/library/windows/desktop/mt827485)<br/>                         | Gets range information about a placeholder file or folder.<br/>                                                                                                                                                |
| [**CfGetPlaceholderStateFromAttributeTag**](https://msdn.microsoft.com/library/windows/desktop/mt827486)<br/> | Gets a set of placeholder states based on the *FileAttributes* and *ReparseTag* values of the file.<br/>                                                                                                       |
| [**CfGetPlaceholderStateFromFileInfo**](https://msdn.microsoft.com/library/windows/desktop/mt827487)<br/>         | Gets a set of placeholder states based on the various information of the file.<br/>                                                                                                                            |
| [**CfGetPlaceholderStateFromFindData**](https://msdn.microsoft.com/library/windows/desktop/mt827488)<br/>         | Gets a set of placeholder states based on the WIN32\_FIND\_DATA structure.<br/>                                                                                                                                |
| [**CfGetPlatformInfo**](https://msdn.microsoft.com/library/windows/desktop/mt827489)<br/>                                         | Gets the platform version information.<br/>                                                                                                                                                                    |
| [**CfGetSyncRootInfoByHandle**](https://msdn.microsoft.com/library/windows/desktop/mt827490)<br/>                         | Gets various characteristics of the sync root containing a given file specified by a file handle.<br/>                                                                                                         |
| [**CfGetSyncRootInfoByPath**](https://msdn.microsoft.com/library/windows/desktop/mt827491)<br/>                             | Gets various sync root information given a file under the sync root.<br/>                                                                                                                                      |
| [**CfGetTransferKey**](https://msdn.microsoft.com/library/windows/desktop/mt827492)<br/>                                           | Initiates a transfer of data into a placeholder file or folder.<br/>                                                                                                                                           |
| [**CfGetWin32HandleFromProtectedHandle**](https://msdn.microsoft.com/library/windows/desktop/mt827493)<br/>     | Converts a protected handle to a Win32 handle so that it can be used with all handle-based Win32 APIs. <br/>                                                                                                   |
| [**CfHydratePlaceholder**](https://msdn.microsoft.com/library/windows/desktop/mt827494)<br/>                                   | Hydrates a placeholder file by ensuring that the specified byte range is present on-disk in the placeholder. This is valid for files only.<br/>                                                                |
| [**CfOpenFileWithOplock**](https://msdn.microsoft.com/library/windows/desktop/mt827495)<br/>                                   | Opens an asynchronous opaque handle to a file or directory (for both normal and placeholder files) and sets up a proper oplock on it based on the open flags.<br/>                                             |
| [**CfQuerySyncProviderStatus**](https://msdn.microsoft.com/library/windows/desktop/mt827496)<br/>                         | Queries a sync provider to get the status of the provider.<br/>                                                                                                                                                |
| [**CfReferenceProtectedHandle**](https://msdn.microsoft.com/library/windows/desktop/mt827497)<br/>                       | Allows the caller to reference a protected handle to a Win32 handle which can be used with non-CfApi Win32 APIs. <br/>                                                                                         |
| [**CfRegisterSyncRoot**](https://msdn.microsoft.com/library/windows/desktop/mt827498)<br/>                                       | Performs a one time sync root registration.<br/>                                                                                                                                                               |
| [**CfReleaseProtectedHandle**](https://msdn.microsoft.com/library/windows/desktop/mt827499)<br/>                           | Releases a protected handle referenced by [**CfReferenceProtectedHandle**](https://msdn.microsoft.com/library/windows/desktop/mt827497).<br/>                                                                                          |
| [**CfReleaseTransferKey**](https://msdn.microsoft.com/library/windows/desktop/mt827500)<br/>                                   | Releases a transfer key obtained by [**CfGetTransferKey**](https://msdn.microsoft.com/library/windows/desktop/mt827492).<br/>                                                                                                                    |
| [**CfReportProviderProgress**](https://msdn.microsoft.com/library/windows/desktop/mt827501)<br/>                           | Allows a sync provider to report progress out-of-band.<br/>                                                                                                                                                    |
| [**CfReportSyncStatus**](https://msdn.microsoft.com/library/windows/desktop/mt845791)<br/>                                       | Allows a sync provider to notify the platform of its status on a specified sync root without having to connect with a call to [**CfConnectSyncRoot**](https://msdn.microsoft.com/library/windows/desktop/mt827477) first. <br/>                 |
| [**CfRevertPlaceholder**](https://msdn.microsoft.com/library/windows/desktop/mt827502)<br/>                                     | Reverts a placeholder back to a regular file, stripping away all special characteristics such as the reparse tag, the file identity, etc.<br/>                                                                 |
| [**CfSetCorrelationVector**](https://msdn.microsoft.com/library/windows/desktop/mt827503)<br/>                               | Allows a sync provider to instruct the platform to use a specific correlation vector for telemetry purposes on a placeholder file. This is optional.<br/>                                                      |
| [**CfSetInSyncState**](https://msdn.microsoft.com/library/windows/desktop/mt827504)<br/>                                           | Sets the in-sync state for a placeholder file or folder.<br/>                                                                                                                                                  |
| [**CfSetPinState**](https://msdn.microsoft.com/library/windows/desktop/mt827505)<br/>                                                 | This sets the pin state of a placeholder, used to represent a user s intent. Any application (not just the sync provider) can call this function.<br/>                                                         |
| [**CfUnregisterSyncRoot**](https://msdn.microsoft.com/library/windows/desktop/mt827506)<br/>                                   | Unregisters a previously registered sync root.<br/>                                                                                                                                                            |
| [**CfUpdatePlaceholder**](https://msdn.microsoft.com/library/windows/desktop/mt827507)<br/>                                     | Updates characteristics of the placeholder file or directory.<br/>                                                                                                                                             |
| [**CfUpdateSyncProviderStatus**](https://msdn.microsoft.com/library/windows/desktop/mt827508)<br/>                       | Updates the current status of the sync provider.<br/>                                                                                                                                                          |



 

 

 




