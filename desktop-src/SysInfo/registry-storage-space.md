---
description: Although there are few technical limits to the type and size of data an application can store in the registry, certain practical guidelines exist to promote system efficiency.
ms.assetid: fa85ff87-3d72-4f71-856a-f43df7d19aa8
title: Registry Storage Space
ms.topic: article
ms.date: 05/31/2018
---

# Registry Storage Space

Although there are few technical limits to the type and size of data an application can store in the registry, certain practical guidelines exist to promote system efficiency. An application should store configuration and initialization data in the registry, and store other kinds of data elsewhere.

Generally, data consisting of more than one or two kilobytes (K) should be stored as a file and referred to by using a key in the registry rather than being stored as a value. Instead of duplicating large pieces of data in the registry, an application should save the data as a file and refer to the file. Executable binary code should never be stored in the registry.

A value entry uses much less registry space than a key. To save space, an application should group similar data together as a structure and store the structure as a value rather than storing each of the structure members as a separate key. (Storing the data in binary form allows an application to store data in one value that would otherwise be made up of several incompatible types.)

Views of the registry files are mapped in paged pool memory.

**Windows Server 2008 for 32-bit, Windows Vista with SP1 for 32-bit, Windows Vista, Windows Server 2003, Windows XP:** Views of the registry files are mapped in the computer cache address space. Therefore, regardless of the size of the registry data, it is not charged more than 4 megabytes (MB).

The maximum size of a registry hive is 2 GB, except for the system hive.

**Windows Server 2003 with SP1, Windows Server 2003 and Windows XP:** There are no explicit limits on the total amount of space that may be consumed by hives in paged pool memory and in disk space, although system quotas may affect the actual maximum size. The maximum size of a registry hive was limited to 2 GB starting with Windows Server 2003 with Service Pack 2 (SP2).

The maximum size of the system hive is limited by physical memory as shown in the following table. 

| System                      | Maximum size of the system hive                                                                                                                                                                                                            |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| x86-based systems           | 50 percent of physical memory, up to 400 MB.**Windows Server 2003 with SP2, Windows Server 2003 with SP1, Windows Server 2003 and Windows XP:** 25 percent of physical memory, up to 200 MB.<br/>                                    |
| x64-based systems           | 50 percent of physical memory, up to 1.5 GB.**Windows Server 2003 with SP2:** 25 percent of system memory, up to 200 MB.<br/> **Windows Server 2003 with SP1, Windows Server 2003 and Windows XP 64-Bit Edition:** 32 MB.<br/> |
| Intel Itanium-based systems | 50 percent of physical memory, up to 1 GB.**Windows Server 2008, Windows Vista, Windows Server 2003 with SP2, Windows Server 2003 with SP1, Windows Server 2003 and Windows XP 64-Bit Edition:** 32 MB.<br/>                         |



 

## Windows 2000

Registry data is stored in the paged pool, an area of physical memory used for system data that can be written to disk when not in use. The **RegistrySizeLimit** value establishes the maximum amount of paged pool that can be consumed by registry data from all applications. This value is located in the following registry key:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Control
```

By default, the registry size limit is 25 percent of the paged pool. (The default size of the paged pool is 32 MB, so this is 8 MB.) The system ensures that the minimum value of **RegistrySizeLimit** is 4 MB and the maximum is approximately 80 percent of the **PagedPoolSize** value. If the value of this entry is greater than 80 percent of the size of the paged pool, the system sets the maximum size of the registry to 80 percent of the size of the paged pool. This prevents the registry from consuming space needed by processes. Note that setting this value does not allocate space in the paged pool, nor does it assure that the space will be available if needed.

The paged pool size is determined by the **PagedPoolSize** value in the following registry key:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Control
            SessionManager
               MemoryManagement
```

For an example of how to determine the current and maximum sizes of the registry, see [Determining the Registry Size](determining-the-registry-size.md).

The maximum paged pool is approximately 300,470 MB so the registry size limit is 240-376 MB. However, if the /3GB switch is used, the maximum paged pool size is 192 MB, so the registry can be a maximum of 153.6 MB.

 

 




