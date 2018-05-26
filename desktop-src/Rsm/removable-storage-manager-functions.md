---
Description: The following are the Removable Storage Manager functions.
ms.assetid: f13e716e-21a4-4d3d-bfcf-31d23dca49a4
title: Removable Storage Manager Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Removable Storage Manager Functions

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

The following are the Removable Storage Manager functions.

## Change Detection Functions

RSM does not detect inject and eject operations on standalone drives unless requested to do so by the application. Although some RSM functions automatically begin change detection of certain devices, applications that require current information on the presence or absence of media in standalone drives must use these functions to request RSM to detect the changes. With change detection enabled, an application can use database notification functions to be notified when media is injected and ejected. You can use the following functions:

-   [**BeginNtmsDeviceChangeDetection**](/windows/win32/Ntmsapi/nf-ntmsapi-beginntmsdevicechangedetection?branch=master)
-   [**EndNtmsDeviceChangeDetection**](/windows/win32/Ntmsapi/nf-ntmsapi-endntmsdevicechangedetection?branch=master)
-   [**SetNtmsDeviceChangeDetection**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsdevicechangedetection?branch=master)

## Cleaner Management Functions

RSM can automatically clean tape drives that become dirty through use. Use the following functions to control drive cleaning:

-   [**CleanNtmsDrive**](/windows/win32/Ntmsapi/nf-ntmsapi-cleanntmsdrive?branch=master)
-   [**EjectNtmsCleaner**](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmscleaner?branch=master)
-   [**InjectNtmsCleaner**](/windows/win32/Ntmsapi/nf-ntmsapi-injectntmscleaner?branch=master)
-   [**ReleaseNtmsCleanerSlot**](/windows/win32/Ntmsapi/nf-ntmsapi-releasentmscleanerslot?branch=master)
-   [**ReserveNtmsCleanerSlot**](/windows/win32/Ntmsapi/nf-ntmsapi-reserventmscleanerslot?branch=master)

## Database Backup and Recovery Functions

RSM uses a database to store information about the removable media devices and cartridges in a system. Like any system resource, this database should be backed up in case it becomes lost or corrupted. Use the following functions for RSM database backup and recovery:

-   [**ExportNtmsDatabase**](/windows/win32/Ntmsapi/nf-ntmsapi-exportntmsdatabase?branch=master)
-   [**ImportNtmsDatabase**](/windows/win32/Ntmsapi/nf-ntmsapi-importntmsdatabase?branch=master)

## Database Notification Functions

You can use the following functions to get notifications when RSM database objects change:

-   [**CloseNtmsNotification**](/windows/win32/Ntmsapi/nf-ntmsapi-closentmsnotification?branch=master)
-   [**OpenNtmsNotification**](/windows/win32/Ntmsapi/nf-ntmsapi-openntmsnotification?branch=master)
-   [**WaitForNtmsNotification**](/windows/win32/Ntmsapi/nf-ntmsapi-waitforntmsnotification?branch=master)

## Library Control Functions

Library control functions control injecting, ejecting, and moving media. They also enable and disable drive and changer resources. The following are the library control functions:

-   [**AccessNtmsLibraryDoor**](/windows/win32/Ntmsapi/nf-ntmsapi-accessntmslibrarydoor?branch=master)
-   [**CancelNtmsLibraryRequest**](/windows/win32/Ntmsapi/nf-ntmsapi-cancelntmslibraryrequest?branch=master)
-   [**DeleteNtmsDrive**](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsdrive?branch=master)
-   [**DeleteNtmsLibrary**](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmslibrary?branch=master)
-   [**DeleteNtmsRequests**](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsrequests?branch=master)
-   [**DismountNtmsDrive**](/windows/win32/Ntmsapi/nf-ntmsapi-dismountntmsdrive?branch=master)
-   [**EjectDiskFromSADrive**](/windows/win32/Ntmsapi/nf-ntmsapi-ejectdiskfromsadrivea?branch=master)
-   [**EjectNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmsmedia?branch=master)
-   [**GetNtmsRequestOrder**](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsrequestorder?branch=master)
-   [**GetNtmsUIOptions**](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsuioptionsa?branch=master)
-   [**GetVolumesFromDrive**](/windows/win32/Ntmsapi/nf-ntmsapi-getvolumesfromdrivea?branch=master)
-   [**IdentifyNtmsSlot**](/windows/win32/Ntmsapi/nf-ntmsapi-identifyntmsslot?branch=master)
-   [**InjectNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-injectntmsmedia?branch=master)
-   [**InventoryNtmsLibrary**](/windows/win32/Ntmsapi/nf-ntmsapi-inventoryntmslibrary?branch=master)
-   [**SetNtmsUIOptions**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsuioptionsa?branch=master)
-   [**SetNtmsRequestOrder**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsrequestorder?branch=master)

## Media Label Library Functions

Your media label library must support the following functions. RSM uses these functions to communicate with media label libraries.

-   [**ClaimMediaLabel**](/windows/win32/NtmsMli/nc-ntmsmli-claimmedialabel?branch=master)
-   [**MaxMediaLabel**](/windows/win32/NtmsMli/nc-ntmsmli-maxmedialabel?branch=master)

## Media Services Functions

Media services functions are used for mounting and dismounting media and managing media pools. The following are the media services functions:

-   [**AddNtmsMediaType**](/windows/win32/Ntmsapi/nf-ntmsapi-addntmsmediatype?branch=master)
-   [**AllocateNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-allocatentmsmedia?branch=master)
-   [**ChangeNtmsMediaType**](/windows/win32/Ntmsapi/nf-ntmsapi-changentmsmediatype?branch=master)
-   [**CreateNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-createntmsmediaa?branch=master)
-   [**CreateNtmsMediaPool**](/windows/win32/Ntmsapi/nf-ntmsapi-createntmsmediapool?branch=master)
-   [**DeallocateNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-deallocatentmsmedia?branch=master)
-   [**DecommissionNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-decommissionntmsmedia?branch=master)
-   [**DeleteNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmedia?branch=master)
-   [**DeleteNtmsMediaPool**](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmediapool?branch=master)
-   [**DeleteNtmsMediaType**](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmediatype?branch=master)
-   [**DismountNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-dismountntmsmedia?branch=master)
-   [**GetNtmsMediaPoolName**](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsmediapoolnamea?branch=master)
-   [**MountNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-mountntmsmedia?branch=master)
-   [**MoveToNtmsMediaPool**](/windows/win32/Ntmsapi/nf-ntmsapi-movetontmsmediapool?branch=master)
-   [**SetNtmsMediaComplete**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsmediacomplete?branch=master)
-   [**SwapNtmsMedia**](/windows/win32/Ntmsapi/nf-ntmsapi-swapntmsmedia?branch=master)

## Object Management Functions

You can use the following functions to enumerate, get, and set information about RSM objects:

-   [**DisableNtmsObject**](/windows/win32/Ntmsapi/nf-ntmsapi-disablentmsobject?branch=master)
-   [**EnableNtmsObject**](/windows/win32/Ntmsapi/nf-ntmsapi-enablentmsobject?branch=master)
-   [**EnumerateNtmsObject**](/windows/win32/Ntmsapi/nf-ntmsapi-enumeratentmsobject?branch=master)
-   [**GetNtmsObjectAttribute**](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectattributea?branch=master)
-   [**GetNtmsObjectInformation**](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectinformation?branch=master)
-   [**GetNtmsObjectSecurity**](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectsecurity?branch=master)
-   [**SetNtmsObjectAttribute**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectattributea?branch=master)
-   [**SetNtmsObjectInformation**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectinformation?branch=master)
-   [**SetNtmsObjectSecurity**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity?branch=master)

## On-Media-Identifier Management Functions

RSM identifies media in a system by reading an on-media identifier (OMID) The following function updates the RSM database when a new OMID is written:

-   [**UpdateNtmsOmidInfo**](/windows/win32/Ntmsapi/nf-ntmsapi-updatentmsomidinfo?branch=master)

## Operator Request Functions

You can use the following functions to manage and control requests to system operators:

-   [**CancelNtmsOperatorRequest**](/windows/win32/Ntmsapi/nf-ntmsapi-cancelntmsoperatorrequest?branch=master)
-   [**SatisfyNtmsOperatorRequest**](/windows/win32/Ntmsapi/nf-ntmsapi-satisfyntmsoperatorrequest?branch=master)
-   [**SubmitNtmsOperatorRequest**](/windows/win32/Ntmsapi/nf-ntmsapi-submitntmsoperatorrequesta?branch=master)
-   [**WaitForNtmsOperatorRequest**](/windows/win32/Ntmsapi/nf-ntmsapi-waitforntmsoperatorrequest?branch=master)

## Session Management Functions

Before calling any other functions, an application must open an RSM session, and the session must be closed before the application exits. The following session management functions open and close RSM sessions:

-   [**CloseNtmsSession**](/windows/win32/Ntmsapi/nf-ntmsapi-closentmssession?branch=master)
-   [**OpenNtmsSession**](/windows/win32/Ntmsapi/nf-ntmsapi-openntmssessiona?branch=master)

> [!Note]  
> The Removable Storage Manager functions were defined when the technology was previously named NTMS. As a result, many function names contain the prefix "Ntms". Similarly, the "scratch" pool was renamed "free", and the "foreign" pool was renamed "unrecognized". The term "partition" was replaced with the term "side".

 

 

 



