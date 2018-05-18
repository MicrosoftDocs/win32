---
title: Virtual Server Features
description: Microsoft Virtual Server contains many of the same features as Microsoft Virtual PC, in addition to many powerful new features.
ms.assetid: '2fdc6715-139c-4835-af46-210daaf8bab0'
---

# Virtual Server Features

Microsoft Virtual Server contains many of the same features as Microsoft Virtual PC, in addition to many powerful new features.

## Features common with Microsoft Virtual PC

The following features are common with Microsoft Virtual PC:

-   Isolated virtual machine environment.

    Each virtual machine session can be viewed as a totally separate hardware environment. Different operating systems and configurations can be run in separate sessions, and failures are isolated to that specific virtual machine session without affecting other sessions or the underlying hardware hosting Virtual Server.

-   Standardized hardware.

    Each virtual machine session is based on identical virtualized hardware. This allows systems to be configured and tested using only one installation, which can then be deployed in any virtual machine session without customization.

-   Virtual hard disk support.

    Virtual machine sessions can be configured for a fixed, dynamic, differencing, or undo virtual hard disk.

-   Self-contained Configurations.

    Each virtual machine session environment is stored in a single folder and can be easily duplicated or moved.

## Features specific to Microsoft Virtual Server

The following additional features are specific to Microsoft Virtual Server. These include:

-   Loads and runs during start-up.

    Virtual Server runs as a service in Windows Server 2003 and will automatically load and run during start-up before any administrator user has logged on.

-   Large memory support for virtual machine sessions.

    Virtual Server provides support for up to 3.6 gigabytes of RAM per virtual machine session, up to the limit of RAM supported by the server operating system running Virtual Server.

-   Support of up to 64 sessions.

    Virtual Server can run up to 64 virtual machine sessions simultaneously, provided the server running Virtual Server has adequate resources.

-   Virtual networking.

    Virtual Server supports up to 4 virtual Ethernet NICs per virtual machine session, and an unlimited number of virtual networks.

-   Virtual SCSI disk support.

    Virtual Server supports up to 4 virtual SCSI controllers per virtual machine session, and each controller can support up to 7 virtual hard disks. These are in addition to the virtual IDE hard disks supported by Virtual Server.

-   Resource limiting and reservations.

    Virtual Server can set minimum and maximum CPU usage limits separately for each virtual machine session.

-   Web interface controls and virtual machine Remote Desktop administration.

    Virtual Server provides a native Virtual Machine Remote Control (VMRC) that allows remote users to manage any type of virtual machine session desktop from within a browser.

-   Virtual machine threading.

    All virtual machine sessions are threaded to take advantage of multiple processors in the Virtual Server's host server hardware.

-   COM-based architecture and scripting support.

    Virtual Server is based entirely on a COM architecture. This allows developers to control Virtual Server with any language that can control COM objects, such as Visual Basic.NET, Visual C#, and so on.

-   Crash detection, recovery, logging, and monitoring.

    Virtual Server can detect when a virtual machine session crashes and initiate event notices to external scripts. Extensive logging is available for each virtual machine session.

-   Pmon and Microsoft Management Console (MMC) integration.

    Extensive logging, performance monitoring, and resource monitoring are directly accessible from Pmon.

 

 




