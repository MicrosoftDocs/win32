---
Description: 'The following are the Removable Storage Manager functions.'
ms.assetid: 'f13e716e-21a4-4d3d-bfcf-31d23dca49a4'
title: Removable Storage Manager Functions
---

# Removable Storage Manager Functions

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

The following are the Removable Storage Manager functions.

## Change Detection Functions

RSM does not detect inject and eject operations on standalone drives unless requested to do so by the application. Although some RSM functions automatically begin change detection of certain devices, applications that require current information on the presence or absence of media in standalone drives must use these functions to request RSM to detect the changes. With change detection enabled, an application can use database notification functions to be notified when media is injected and ejected. You can use the following functions:

-   [**BeginNtmsDeviceChangeDetection**](beginntmsdevicechangedetection.md)
-   [**EndNtmsDeviceChangeDetection**](endntmsdevicechangedetection.md)
-   [**SetNtmsDeviceChangeDetection**](setntmsdevicechangedetection.md)

## Cleaner Management Functions

RSM can automatically clean tape drives that become dirty through use. Use the following functions to control drive cleaning:

-   [**CleanNtmsDrive**](cleanntmsdrive.md)
-   [**EjectNtmsCleaner**](ejectntmscleaner.md)
-   [**InjectNtmsCleaner**](injectntmscleaner.md)
-   [**ReleaseNtmsCleanerSlot**](releasentmscleanerslot.md)
-   [**ReserveNtmsCleanerSlot**](reserventmscleanerslot.md)

## Database Backup and Recovery Functions

RSM uses a database to store information about the removable media devices and cartridges in a system. Like any system resource, this database should be backed up in case it becomes lost or corrupted. Use the following functions for RSM database backup and recovery:

-   [**ExportNtmsDatabase**](exportntmsdatabase.md)
-   [**ImportNtmsDatabase**](importntmsdatabase.md)

## Database Notification Functions

You can use the following functions to get notifications when RSM database objects change:

-   [**CloseNtmsNotification**](closentmsnotification.md)
-   [**OpenNtmsNotification**](openntmsnotification.md)
-   [**WaitForNtmsNotification**](waitforntmsnotification.md)

## Library Control Functions

Library control functions control injecting, ejecting, and moving media. They also enable and disable drive and changer resources. The following are the library control functions:

-   [**AccessNtmsLibraryDoor**](accessntmslibrarydoor.md)
-   [**CancelNtmsLibraryRequest**](cancelntmslibraryrequest.md)
-   [**DeleteNtmsDrive**](deletentmsdrive.md)
-   [**DeleteNtmsLibrary**](deletentmslibrary.md)
-   [**DeleteNtmsRequests**](deletentmsrequests.md)
-   [**DismountNtmsDrive**](dismountntmsdrive.md)
-   [**EjectDiskFromSADrive**](ejectdiskfromsadrive.md)
-   [**EjectNtmsMedia**](ejectntmsmedia.md)
-   [**GetNtmsRequestOrder**](getntmsrequestorder.md)
-   [**GetNtmsUIOptions**](getntmsuioptions.md)
-   [**GetVolumesFromDrive**](getvolumesfromdrive.md)
-   [**IdentifyNtmsSlot**](identifyntmsslot.md)
-   [**InjectNtmsMedia**](injectntmsmedia.md)
-   [**InventoryNtmsLibrary**](inventoryntmslibrary.md)
-   [**SetNtmsUIOptions**](setntmsuioptions.md)
-   [**SetNtmsRequestOrder**](setntmsrequestorder.md)

## Media Label Library Functions

Your media label library must support the following functions. RSM uses these functions to communicate with media label libraries.

-   [**ClaimMediaLabel**](claimmedialabel.md)
-   [**MaxMediaLabel**](maxmedialabel.md)

## Media Services Functions

Media services functions are used for mounting and dismounting media and managing media pools. The following are the media services functions:

-   [**AddNtmsMediaType**](addntmsmediatype.md)
-   [**AllocateNtmsMedia**](allocatentmsmedia.md)
-   [**ChangeNtmsMediaType**](changentmsmediatype.md)
-   [**CreateNtmsMedia**](createntmsmedia.md)
-   [**CreateNtmsMediaPool**](createntmsmediapool.md)
-   [**DeallocateNtmsMedia**](deallocatentmsmedia.md)
-   [**DecommissionNtmsMedia**](decommissionntmsmedia.md)
-   [**DeleteNtmsMedia**](deletentmsmedia.md)
-   [**DeleteNtmsMediaPool**](deletentmsmediapool.md)
-   [**DeleteNtmsMediaType**](deletentmsmediatype.md)
-   [**DismountNtmsMedia**](dismountntmsmedia.md)
-   [**GetNtmsMediaPoolName**](getntmsmediapoolname.md)
-   [**MountNtmsMedia**](mountntmsmedia.md)
-   [**MoveToNtmsMediaPool**](movetontmsmediapool.md)
-   [**SetNtmsMediaComplete**](setntmsmediacomplete.md)
-   [**SwapNtmsMedia**](swapntmsmedia.md)

## Object Management Functions

You can use the following functions to enumerate, get, and set information about RSM objects:

-   [**DisableNtmsObject**](disablentmsobject.md)
-   [**EnableNtmsObject**](enablentmsobject.md)
-   [**EnumerateNtmsObject**](enumeratentmsobject.md)
-   [**GetNtmsObjectAttribute**](getntmsobjectattribute.md)
-   [**GetNtmsObjectInformation**](getntmsobjectinformation.md)
-   [**GetNtmsObjectSecurity**](getntmsobjectsecurity.md)
-   [**SetNtmsObjectAttribute**](setntmsobjectattribute.md)
-   [**SetNtmsObjectInformation**](setntmsobjectinformation.md)
-   [**SetNtmsObjectSecurity**](setntmsobjectsecurity.md)

## On-Media-Identifier Management Functions

RSM identifies media in a system by reading an on-media identifier (OMID) The following function updates the RSM database when a new OMID is written:

-   [**UpdateNtmsOmidInfo**](updatentmsomidinfo.md)

## Operator Request Functions

You can use the following functions to manage and control requests to system operators:

-   [**CancelNtmsOperatorRequest**](cancelntmsoperatorrequest.md)
-   [**SatisfyNtmsOperatorRequest**](satisfyntmsoperatorrequest.md)
-   [**SubmitNtmsOperatorRequest**](submitntmsoperatorrequest.md)
-   [**WaitForNtmsOperatorRequest**](waitforntmsoperatorrequest.md)

## Session Management Functions

Before calling any other functions, an application must open an RSM session, and the session must be closed before the application exits. The following session management functions open and close RSM sessions:

-   [**CloseNtmsSession**](closentmssession.md)
-   [**OpenNtmsSession**](openntmssession.md)

> [!Note]  
> The Removable Storage Manager functions were defined when the technology was previously named NTMS. As a result, many function names contain the prefix "Ntms". Similarly, the "scratch" pool was renamed "free", and the "foreign" pool was renamed "unrecognized". The term "partition" was replaced with the term "side".

 

 

 



