---
title: Endpoint data loss prevention functions
description: Functions used by the endpoint data loss prevention feature.
ms.topic: article
ms.date: 03/18/2021
---

# Endpoint data loss prevention functions

The following endpoint data loss prevention APIs are deployed as part of Windows Defender. The Data Loss Prevention (DLP) feature requires a Windows Enterprise license to use.

## Office interaction

This set of functions used by the endpoint DLP feature are intended to offer integration with Microsoft Office products.

| Functions                                                       | Description                                                           |
|-------------------------------------------------------------------|-----------------------------------------------------------------------|
| [DlpNotifyCloseDocument](endpointdlp-dlpnotifyclosedocument.md)                       | Provides the system with information about a document before the document close operation is initiated.                                  |
| [DlpNotifyCloseDocumentFile](endpointdlp-dlpnotifyclosedocumentfile.md)                       | Provides the system with information about a document before the document close operation is initiated.                                  |
| [DlpNotifyEnterDropTarget](endpointdlp-dlpnotifyenterdroptarget.md)                       | Provides the system with information about a document when a drop target is entered.                                  |
| [DlpGetEnforcementApiVersion](endpointdlp-dlpgetenforcementapiversion.md)                       | Retrieves the version of the endpoint Data Loss Prevention (DLP) API on the current device.                                  |
| [DlpInitializeEnforcementMode](endpointdlp-dlpinitializeenforcementmode.md)                       | Notifies the system of the desired enforcement modes for a set of endpoint Data Loss Prevention (DLP) operations.                                  |
| [DlpMustPasteFromSystemClipboard](endpointdlp-dlpmustpastefromsystemclipboard.md)                       | Determines whether the app must pull the data from the system clipboard rather than taking it from its internal cache.                                  |
| [DlpNotifyLeaveDropTarget](endpointdlp-dlpnotifyleavedroptarget.md)                       | Provides the system with information about a document when a drop target is exited.                                  |
| [DlpNotifyPostCopyToClipboard](endpointdlp-dlpnotifypostcopytoclipboard.md)                         | Provides the system with information about a document after a copy to clipboard operation is completed.  |
| [DlpNotifyPostDragDrop](endpointdlp-dlpnotifypostdragdrop.md)                         | Provides the system with information about a document after a drag drop operation is completed.  |
| [DlpNotifyPostOpenDocument](endpointdlp-dlpnotifypostopendocument.md)                       | Provides the system with information about a document after the open operation is completed.                                  |
| [DlpNotifyPostOpenDocumentFile](endpointdlp-dlpnotifypostopendocumentfile.md)                       | Provides the system with information about a document after the open operation is completed.                                  |
| [DlpNotifyPostPasteFromClipboard](endpointdlp-dlpnotifypostpastefromclipboard.md)                       | Provides the system with information about a document after a paste from clipboard operation has completed.                                  |
| [DlpNotifyPostPrint](endpointdlp-dlpnotifypostprint.md)                       | Provides the system with information about a document after a print operation has completed.                                  |
| [DlpNotifyPostSaveAsDocument](endpointdlp-dlpnotifypostsaveasdocument.md)                       | Provides the system with information about a document after the save as operation is completed.                                  |
| [DlpNotifyPostStartPrint](endpointdlp-dlpnotifypoststartprint.md)                       | Provides the system with information about a document after an print operation has started.                                  |
| [DlpNotifyPostStashClipboard](endpointdlp-dlpnotifypoststashclipboard.md)                       | Provides the system with status information after a stash clipboard operation is completed.                                  |
| [DlpNotifyPreCopyToClipboard](endpointdlp-dlpnotifyprecopytoclipboard.md)                         | Provides the system with information about a document before a copy to clipboard operation is initiated.  |
| [DlpNotifyPreDragDrop](endpointdlp-dlpnotifypredragdrop.md)                         | Provides the system with information about a document before a drag drop operation is initiated.  |
| [DlpNotifyPreOpenDocument](endpointdlp-dlpnotifypreopendocument.md)                         | Provides the system with information about a document before the open operation is initiated.  |
| [DlpNotifyPreOpenDocumentFile](endpointdlp-dlpnotifypreopendocumentfile.md)                         | Provides the system with information about a document before the open operation is initiated.  |
| [DlpNotifyPrePasteFromClipboard](endpointdlp-dlpnotifyprepastefromclipboard.md)                         | Provides the system with information about a document before a paste from clipboard operation is initiated.  |
| [DlpNotifyPrePrint](endpointdlp-dlpnotifypreprint.md)                         | Provides the system with information about a document before a print operation is initiated.  |
| [DlpNotifyPreSaveDocument](endpointdlp-dlpnotifypresaveasdocument.md)                       | Provides the system with information about a document before a save as operation is initiated.                                  |
| [DlpNotifyPreStashClipboard](endpointdlp-dlpnotifyprestashclipboard.md)                       | Notifies the system before a stash clipboard operation is initiated.                                  |

## Edge interaction

This set of functions used by the endpoint DLP feature are intended to offer integration with Microsoft Edge or other web browsers.

| Functions                                                       | Description                                                           |
|-------------------------------------------------------------------|-----------------------------------------------------------------------|
| [DlpInitialize](endpointdlp-dlpinitialize.md) | Initializes the internal data structure for endpoint Data Loss Prevention (DLP) functions. |
| [DlpGetFileCloudApplicationPolicy](endpointdlp-dlpgetfilecloudapplicationpolicy.md) | Returns the enforcement level of a file uploaded to a cloud application. |
| [DlpGetFileCloudApplicationPolicyEx](endpointdlp-dlpgetfilecloudapplicationpolicyex.md) | Returns the enforcement level of a file uploaded to a cloud application. This function is designed to be called from external sources such as Microsoft Edge, that do not have innate acess to the User SID. The SID will be detected from the currect process where endpointDlp is located. |
| [DlpGetFileApplicationAccessEx](endpointdlp-dlpgetfileapplicationaccessex.md) | Returns a list of DlpAction objects that contain the enforcement level of each operation in a specified file. |
| [DlpAuditFileAccessEvent](endpointdlp-dlpauditfileaccessevent.md) | Deprecated - Generates an Enforcement event for the specified file. |
| [DlpAuditFileAccessEventEx](endpointdlp-dlpauditfileaccesseventex.md) | Deprecated - Generates an ETW event for the specified file, and allows a business justification to be provided for that enforcement event. |
| [DlpAuditOperationEnforcementEvent](endpointdlp-dlpauditoperationenforcementevent.md) | Generates an ETW event for the specified file. |
| [DlpAuditOperationEnforcementEventEx2](endpointdlp-dlpauditoperationenforcementeventex.md) | Generates an ETW event for the specified file, with additional parameter options. |
| [DlpGetFileLocation](endpointdlp-dlpgetfilelocation.md) | Returns whether a specified file is local, on a network share, or on removeable media. |
| [DlpDelegateEnforcement](endpointdlp-dlpdelegateenforcement.md) | Allows DLP enforcement to be delegated to Windows Defender or to DLP-enlightened applications, as needed. |
| [AuditBrowserOperationEvent](endpointdlp-auditbrowseroperationevent.md) | Generates an ETW event for a browser operation. |
| [AuditBrowserFileOperationEvent](endpointdlp-auditbrowserfileoperationevent.md) | Generates an ETW event for a browser file operations. |
| [GetBrowserExtensionConfiguration](endpointdlp-getbrowserextensionconfiguration.md) | Returns whether DLP/IRM is enabled upon the browser. |
| [DlpIsWebsitePolicyConfigured](endpointdlp-dlpiswebsitepolicyconfigured.md) | Returns whether any website rules have been configured for DLP. |
| [DlpGetWebSiteAccess](endpointdlp-dlpgetwebsiteaccess.md) | Returns whether any website rules have been configured for DLP. |
| [DlpFreeArchiveFileTraceInfo](endpointdlp-dlpfreearchivefiletraceinfo.md) | Frees the members of a DlpTraceInfoEx data structure. |
| [DlpGetNotificationSettings](endpointdlp-dlpgetnotificationsettings.md) | Returns the notification settings and strings for a given DLP rule and website action type. |
| [DlpGetWebSiteNotificationSettings](endpointdlp-dlpgetwebsitenotificationsettings.md) | Returns the notification settings and strings for a given DLP rule and action type. |
| [AuditBrowserWebSiteOperation](endpointdlp-auditbrowserwebsiteoperation.md) | Generates an ETW event for a browser website operation. |
| [DlpIsSensitiveStream](endpointdlp-dlpissensitivestream.md) | Checks to see is an input buffer pasted to a browser is sensitive. |