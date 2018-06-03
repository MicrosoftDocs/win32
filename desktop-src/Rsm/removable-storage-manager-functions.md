---
Description: The following are the Removable Storage Manager functions.
ms.assetid: f13e716e-21a4-4d3d-bfcf-31d23dca49a4
title: Removable Storage Manager Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Removable Storage Manager Functions

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

The following are the Removable Storage Manager functions.

## Change Detection Functions

RSM does not detect inject and eject operations on standalone drives unless requested to do so by the application. Although some RSM functions automatically begin change detection of certain devices, applications that require current information on the presence or absence of media in standalone drives must use these functions to request RSM to detect the changes. With change detection enabled, an application can use database notification functions to be notified when media is injected and ejected. You can use the following functions:

-   [**BeginNtmsDeviceChangeDetection**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-beginntmsdevicechangedetection)
-   [**EndNtmsDeviceChangeDetection**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-endntmsdevicechangedetection)
-   [**SetNtmsDeviceChangeDetection**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsdevicechangedetection)

## Cleaner Management Functions

RSM can automatically clean tape drives that become dirty through use. Use the following functions to control drive cleaning:

-   [**CleanNtmsDrive**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cleanntmsdrive)
-   [**EjectNtmsCleaner**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-ejectntmscleaner)
-   [**InjectNtmsCleaner**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-injectntmscleaner)
-   [**ReleaseNtmsCleanerSlot**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-releasentmscleanerslot)
-   [**ReserveNtmsCleanerSlot**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-reserventmscleanerslot)

## Database Backup and Recovery Functions

RSM uses a database to store information about the removable media devices and cartridges in a system. Like any system resource, this database should be backed up in case it becomes lost or corrupted. Use the following functions for RSM database backup and recovery:

-   [**ExportNtmsDatabase**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-exportntmsdatabase)
-   [**ImportNtmsDatabase**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-importntmsdatabase)

## Database Notification Functions

You can use the following functions to get notifications when RSM database objects change:

-   [**CloseNtmsNotification**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-closentmsnotification)
-   [**OpenNtmsNotification**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-openntmsnotification)
-   [**WaitForNtmsNotification**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-waitforntmsnotification)

## Library Control Functions

Library control functions control injecting, ejecting, and moving media. They also enable and disable drive and changer resources. The following are the library control functions:

-   [**AccessNtmsLibraryDoor**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-accessntmslibrarydoor)
-   [**CancelNtmsLibraryRequest**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cancelntmslibraryrequest)
-   [**DeleteNtmsDrive**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsdrive)
-   [**DeleteNtmsLibrary**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmslibrary)
-   [**DeleteNtmsRequests**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsrequests)
-   [**DismountNtmsDrive**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-dismountntmsdrive)
-   [**EjectDiskFromSADrive**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-ejectdiskfromsadrivea)
-   [**EjectNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-ejectntmsmedia)
-   [**GetNtmsRequestOrder**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsrequestorder)
-   [**GetNtmsUIOptions**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsuioptionsa)
-   [**GetVolumesFromDrive**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getvolumesfromdrivea)
-   [**IdentifyNtmsSlot**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-identifyntmsslot)
-   [**InjectNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-injectntmsmedia)
-   [**InventoryNtmsLibrary**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-inventoryntmslibrary)
-   [**SetNtmsUIOptions**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsuioptionsa)
-   [**SetNtmsRequestOrder**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsrequestorder)

## Media Label Library Functions

Your media label library must support the following functions. RSM uses these functions to communicate with media label libraries.

-   [**ClaimMediaLabel**](/windows/desktop/api/NtmsMli/nc-ntmsmli-claimmedialabel)
-   [**MaxMediaLabel**](/windows/desktop/api/NtmsMli/nc-ntmsmli-maxmedialabel)

## Media Services Functions

Media services functions are used for mounting and dismounting media and managing media pools. The following are the media services functions:

-   [**AddNtmsMediaType**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-addntmsmediatype)
-   [**AllocateNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-allocatentmsmedia)
-   [**ChangeNtmsMediaType**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-changentmsmediatype)
-   [**CreateNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-createntmsmediaa)
-   [**CreateNtmsMediaPool**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-createntmsmediapool)
-   [**DeallocateNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deallocatentmsmedia)
-   [**DecommissionNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-decommissionntmsmedia)
-   [**DeleteNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmedia)
-   [**DeleteNtmsMediaPool**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmediapool)
-   [**DeleteNtmsMediaType**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmediatype)
-   [**DismountNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-dismountntmsmedia)
-   [**GetNtmsMediaPoolName**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsmediapoolnamea)
-   [**MountNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-mountntmsmedia)
-   [**MoveToNtmsMediaPool**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-movetontmsmediapool)
-   [**SetNtmsMediaComplete**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsmediacomplete)
-   [**SwapNtmsMedia**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-swapntmsmedia)

## Object Management Functions

You can use the following functions to enumerate, get, and set information about RSM objects:

-   [**DisableNtmsObject**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-disablentmsobject)
-   [**EnableNtmsObject**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-enablentmsobject)
-   [**EnumerateNtmsObject**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-enumeratentmsobject)
-   [**GetNtmsObjectAttribute**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectattributea)
-   [**GetNtmsObjectInformation**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectinformation)
-   [**GetNtmsObjectSecurity**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectsecurity)
-   [**SetNtmsObjectAttribute**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectattributea)
-   [**SetNtmsObjectInformation**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectinformation)
-   [**SetNtmsObjectSecurity**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity)

## On-Media-Identifier Management Functions

RSM identifies media in a system by reading an on-media identifier (OMID) The following function updates the RSM database when a new OMID is written:

-   [**UpdateNtmsOmidInfo**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-updatentmsomidinfo)

## Operator Request Functions

You can use the following functions to manage and control requests to system operators:

-   [**CancelNtmsOperatorRequest**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cancelntmsoperatorrequest)
-   [**SatisfyNtmsOperatorRequest**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-satisfyntmsoperatorrequest)
-   [**SubmitNtmsOperatorRequest**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-submitntmsoperatorrequesta)
-   [**WaitForNtmsOperatorRequest**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-waitforntmsoperatorrequest)

## Session Management Functions

Before calling any other functions, an application must open an RSM session, and the session must be closed before the application exits. The following session management functions open and close RSM sessions:

-   [**CloseNtmsSession**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-closentmssession)
-   [**OpenNtmsSession**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-openntmssessiona)

> [!Note]  
> The Removable Storage Manager functions were defined when the technology was previously named NTMS. As a result, many function names contain the prefix "Ntms". Similarly, the "scratch" pool was renamed "free", and the "foreign" pool was renamed "unrecognized". The term "partition" was replaced with the term "side".

 

 

 



