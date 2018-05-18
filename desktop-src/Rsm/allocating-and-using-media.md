---
Description: 'After you create and configure media pools, you can allocate media using the AllocateNtmsMedia function.'
ms.assetid: '9b6e68ff-5e60-480d-a3f4-3a16b946d12c'
title: Allocating and Using Media
---

# Allocating and Using Media

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

After you create and configure media pools, you can allocate media using the [**AllocateNtmsMedia**](allocatentmsmedia.md) function. This function returns a logical media identifier (LMID). Media can only be allocated by one application at a time. While in this allocated state, a cartridge is considered "in use" by your application may contain valuable data. When your application no longer requires the cartridge it must deallocate the media by calling [**DeallocateNtmsMedia**](deallocatentmsmedia.md). Once deallocated, a cartridge is available to for use by other applications. If the deallocated cartridge remains in your media pool then only other applications that have access to your pool can utilize it for their use. If the deallocated cartridge is returned to the free pool then any other application can utilize it.

To use a cartridge you call [**MountNtmsMedia**](mountntmsmedia.md), which places the cartridge in a drive. After this call, you can use standard I/O functions to read and write the contents of the media. Use the [**DismountNtmsMedia**](dismountntmsmedia.md) function to dismount the cartridge. The following list follows the path of functions you should use to access media in a RSM system.

-   [**OpenNtmsSession**](openntmssession.md)
-   [**AllocateNtmsMedia**](allocatentmsmedia.md) (do this only when you need another cartridge)
-   [**MountNtmsMedia**](mountntmsmedia.md)
-   Use the media (create a file, modify it, close, and so on)
-   [**DismountNtmsMedia**](dismountntmsmedia.md)
-   [**DeallocateNtmsMedia**](deallocatentmsmedia.md)
-   [**CloseNtmsSession**](closentmssession.md)

 

 



