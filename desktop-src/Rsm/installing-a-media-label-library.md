---
Description: 'You must install or provide instructions for installing your media label library in the installation program for your application.'
ms.assetid: 'd51ba281-89c7-4c8a-8dae-b5805813d5fd'
title: Installing a Media Label Library
---

# Installing a Media Label Library

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

You must install or provide instructions for installing your media label library in the installation program for your application. Your installation program must create the appropriate registry entries and copy your media label library to the appropriate directory. Your application must create the following registry node under

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**NTMS**\\**OMID**\\**Tape**

The name of this node can be either your company or product name, but it must be unique. For example, if you wish to name your MLL "STL", the key is:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**NTMS**\\**OMID**\\**Tape**\\**STL**

Under the key for your media label library, the installation program must create two registry values: Description and Path. The Description registry value is of type REG\_SZ and contains a human readable description of the media label library. The Path registry value is of type REG\_SZ or REG\_EXPAND\_SZ and contains the absolute path of the media label library.

Remember the following rules when you develop the installation program for your application:

-   Installations of new media label libraries are restricted to members of the Administrator group.
-   The registry entries that contain the list of media label libraries are accessible only by members of the Administrator group.
-   The folder that contains all the media label library DLLs is typically accessible only by members of the Administrator group. The default location for RSM media label libraries is winnt\\system32.

 

 



