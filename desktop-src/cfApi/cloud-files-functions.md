---
description: The following functions are used in creating and maintaining placeholder files and directories.
ms.assetid: 68B667E2-E8C6-41F9-A0E2-C8CDF60D6472
title: Cloud Filter Functions
ms.topic: article
ms.date: 03/01/2023
---

# Cloud Filter Functions

The following functions are used in creating and maintaining placeholder files and directories.

## In this section

| Topic | Description |
|--------|--------|
| [**CfCloseHandle**](/windows/win32/api/cfapi/nf-cfapi-cfclosehandle) | Closes the file or directory handle returned by [**CfOpenFileWithOplock**](/windows/win32/api/cfapi/nf-cfapi-cfopenfilewithoplock). This should not be used with standard Win32 file handles, only on handles used within CfApi.h. |
| [**CfConnectSyncRoot**](/windows/win32/api/cfapi/nf-cfapi-cfconnectsyncroot) | Initiates bi-directional communication between a sync provider and the sync filter API. |
| [**CfConvertToPlaceholder**](/windows/win32/api/cfapi/nf-cfapi-cfconverttoplaceholder) | Converts a normal file/directory to a placeholder file/directory. |
| [**CfCreatePlaceholders**](/windows/win32/api/cfapi/nf-cfapi-cfcreateplaceholders) | Creates one or more new placeholder files or directories under a sync root tree. |
| [**CfDisconnectSyncRoot**](/windows/win32/api/cfapi/nf-cfapi-cfdisconnectsyncroot) | Disconnects a communication channel created by [**CfConnectSyncRoot**](/windows/win32/api/cfapi/nf-cfapi-cfconnectsyncroot). |
| [**CfExecute**](/windows/win32/api/cfapi/nf-cfapi-cfexecute) | The main entry point for all connection key based placeholder operations. It is intended to be used by a sync provider to respond to various callbacks from the platform. |
| [**CfGetCorrelationVector**](/windows/win32/api/cfapi/nf-cfapi-cfgetcorrelationvector) | Allows the sync provider to query the current correlation vector for a given placeholder file. |
| [**CfGetPlaceholderInfo**](/windows/win32/api/cfapi/nf-cfapi-cfgetplaceholderinfo) | Gets various characteristics of a placeholder file or folder. |
| [**CfGetPlaceholderRangeInfo**](/windows/win32/api/cfapi/nf-cfapi-cfgetplaceholderrangeinfo) | Gets range information about a placeholder file or folder.|
| [**CfGetPlaceholderRangeInfoForHydration**](/windows/win32/api/cfapi/nf-cfapi-cfgetplaceholderrangeinfoforhydration) | Gets range information about a placeholder file or folder. This range information is identical to what **CfGetPlaceholderRangeInfo** returns. However, it doesn’t take a _fileHandle_ as a parameter. Instead, it uses _ConnectionKey_, _TransferKey_, and _FileId_ to identify the file and the stream for which range information is being requested. |
| [**CfGetPlaceholderStateFromAttributeTag**](/windows/win32/api/cfapi/nf-cfapi-cfgetplaceholderstatefromattributetag) | Gets a set of placeholder states based on the _FileAttributes_ and _ReparseTag_ values of the file. |
| [**CfGetPlaceholderStateFromFileInfo**](/windows/win32/api/cfapi/nf-cfapi-cfgetplaceholderstatefromfileinfo) | Gets a set of placeholder states based on the various information of the file. |
| [**CfGetPlaceholderStateFromFindData**](/windows/win32/api/cfapi/nf-cfapi-cfgetplaceholderstatefromfinddata) | Gets a set of placeholder states based on the WIN32\_FIND\_DATA structure. |
| [**CfGetPlatformInfo**](/windows/win32/api/cfapi/nf-cfapi-cfgetplatforminfo) | Gets the platform version information. |
| [**CfGetSyncRootInfoByHandle**](/windows/win32/api/cfapi/nf-cfapi-cfgetsyncrootinfobyhandle) | Gets various characteristics of the sync root containing a given file specified by a file handle. |
| [**CfGetSyncRootInfoByPath**](/windows/win32/api/cfapi/nf-cfapi-cfgetsyncrootinfobypath) | Gets various sync root information given a file under the sync root. |
| [**CfGetTransferKey**](/windows/win32/api/cfapi/nf-cfapi-cfgettransferkey) | Initiates a transfer of data into a placeholder file or folder. |
| [**CfGetWin32HandleFromProtectedHandle**](/windows/win32/api/cfapi/nf-cfapi-cfgetwin32handlefromprotectedhandle) | Converts a protected handle to a Win32 handle so that it can be used with all handle-based Win32 APIs. |
| [**CfHydratePlaceholder**](/windows/win32/api/cfapi/nf-cfapi-cfhydrateplaceholder) | Hydrates a placeholder file by ensuring that the specified byte range is present on-disk in the placeholder. This is valid for files only. |
| [**CfOpenFileWithOplock**](/windows/win32/api/cfapi/nf-cfapi-cfopenfilewithoplock) | Opens an asynchronous opaque handle to a file or directory (for both normal and placeholder files) and sets up a proper oplock on it based on the open flags. |
| [**CfQuerySyncProviderStatus**](/windows/win32/api/cfapi/nf-cfapi-cfquerysyncproviderstatus) | Queries a sync provider to get the status of the provider. |
| [**CfReferenceProtectedHandle**](/windows/win32/api/cfapi/nf-cfapi-cfreferenceprotectedhandle) | Allows the caller to reference a protected handle to a Win32 handle which can be used with non-CfApi Win32 APIs. |
| [**CfRegisterSyncRoot**](/windows/win32/api/cfapi/nf-cfapi-cfregistersyncroot) | Performs a one time sync root registration. |
| [**CfReleaseProtectedHandle**](/windows/win32/api/cfapi/nf-cfapi-cfreleaseprotectedhandle) | Releases a protected handle referenced by [**CfReferenceProtectedHandle**](/windows/win32/api/cfapi/nf-cfapi-cfreferenceprotectedhandle). |
| [**CfReleaseTransferKey**](/windows/win32/api/cfapi/nf-cfapi-cfreleasetransferkey) | Releases a transfer key obtained by [**CfGetTransferKey**](/windows/win32/api/cfapi/nf-cfapi-cfgettransferkey). |
| [**CfReportProviderProgress**](/windows/win32/api/cfapi/nf-cfapi-cfreportproviderprogress) | Allows a sync provider to report progress out-of-band. |
| [**CfReportSyncStatus**](/windows/win32/api/cfapi/nf-cfapi-cfreportsyncstatus) | Allows a sync provider to notify the platform of its status on a specified sync root without having to connect with a call to [**CfConnectSyncRoot**](/windows/win32/api/cfapi/nf-cfapi-cfconnectsyncroot) first. |
| [**CfRevertPlaceholder**](/windows/win32/api/cfapi/nf-cfapi-cfrevertplaceholder) | Reverts a placeholder back to a regular file, stripping away all special characteristics such as the reparse tag, the file identity, etc. |
| [**CfSetCorrelationVector**](/windows/win32/api/cfapi/nf-cfapi-cfsetcorrelationvector) | Allows a sync provider to instruct the platform to use a specific correlation vector for telemetry purposes on a placeholder file. This is optional. |
| [**CfSetInSyncState**](/windows/win32/api/cfapi/nf-cfapi-cfsetinsyncstate) | Sets the in-sync state for a placeholder file or folder. |
| [**CfSetPinState**](/windows/win32/api/cfapi/nf-cfapi-cfsetpinstate) | This sets the pin state of a placeholder, used to represent a user s intent. Any application (not just the sync provider) can call this function. |
| [**CfUnregisterSyncRoot**](/windows/win32/api/cfapi/nf-cfapi-cfunregistersyncroot) | Unregisters a previously registered sync root. |
| [**CfUpdatePlaceholder**](/windows/win32/api/cfapi/nf-cfapi-cfupdateplaceholder) | Updates characteristics of the placeholder file or directory. |
| [**CfUpdateSyncProviderStatus**](/windows/win32/api/cfapi/nf-cfapi-cfupdatesyncproviderstatus) | Updates the current status of the sync provider. |
