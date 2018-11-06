---
title: The Evolution of File Systems
description: Before computers were developed to function on disk operating systems, each computer was built to run a single, proprietary application, which had complete and exclusive control of the entire machine.
ms.assetid: 46d497b5-c325-4395-8512-1ed4b88441de
ms.topic: article
ms.date: 05/31/2018
---

# The Evolution of File Systems

Before computers were developed to function on disk operating systems, each computer was built to run a single, proprietary application, which had complete and exclusive control of the entire machine. The application would write its persistent data directly to a disk, or drum, by sending commands directly to the disk controller. The application was responsible for managing the absolute locations of data on the disk, making sure that it was not overwriting already-existing data. Since only one application was running on the computer at any time, this task was not too difficult.

The advent of computer systems that could run more than one application required a mechanism to ensure that applications did not write over each other's data. Application developers addressed this problem by adopting a single standard for distinguishing disk sectors in use from those that were free by marking them accordingly. In time, these standards coalesced to become a disk operating system, which provided various services to the applications, including a file system for managing persistent storage. With the advent of a file system, applications no longer had to deal directly with the physical storage medium. Instead, they simply told the file system to write blocks of data to the disk and let the file system worry about how to do it. In addition, the file system allowed applications to create data hierarchies through an abstraction known as a directory. A directory could contain not only files but other directories, which in turn could contain their own files and directories, and so on.

The file system provided a single level of indirection between applications and the disk, and the result was that every application saw a file as a single contiguous stream of bytes on the disk even though the file system was actually storing the file in discontiguous sectors. The indirection freed the applications from having to track the absolute position of data on a storage device.

Today, virtually all system APIs for file input and output provide applications for writing information into a flat file. Applications see this file as a single stream of bytes that can grow as large as necessary until the disk is full. For a long time these APIs have been sufficient for applications to store their persistent information. Applications have made significant innovations in how they deal with a single stream of information to provide features like incremental "fast" saves.

However, in a world of component objects, storing data in a single flat file is no longer efficient. Just as file systems arose out of the need for multiple applications to share the same storage medium, so, now, do component objects require a system that allows them to share storage within the conceptual framework of a single file. Even though it is possible to store the separate objects using conventional flat-file storage, if one of the objects increases in size, or if you simply add another object, it becomes necessary to load the entire file into memory, insert the new object, and then save the whole file. This process can be extremely time-consuming.

The solution provided by COM is to implement a second level of indirection: a file system within a file. Flat-file storage requires that a large contiguous sequence of bytes on the disk be manipulated through a single file handle with a single seek pointer. By contrast, COM structured storage defines how to treat a single file system entity as a structured collection of two types of objects — storages and streams — that act like directories and files.

 

 




