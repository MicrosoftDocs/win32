---
Description: 'Readers are standard devices in a smart card system. They are controlled through drivers, and are introduced to and removed from the system through Plug and Play or through the Control Panel Devices item.'
ms.assetid: '694902b9-e43c-4558-8fab-baa853f9fc4d'
title: Smart Card Readers
---

# Smart Card Readers

Readers are standard devices in a [*smart card*](security.s_gly#-security-smart-card-gly) system. They are controlled through drivers, and are introduced to and removed from the system through Plug and Play or through the Control Panel Devices item.

Each reader must be defined for use by the [*smart card subsystem*](security.s_gly#-security-smart-card-subsystem-gly). The subsystem is not responsible for any reader not specifically given to it.

Smart card readers can be divided into logical groups called reader groups. These groups can be defined by the subsystem, as well as defined by administrators and users. A reader can belong to more than one reader group

The smart card subsystem defines the following groups.



| Group                | Description                                                                                                                                                                                            |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCard$AllReaders     | This group contains all the readers in the system. A new reader given to the smart card subsystem is automatically included in the system-wide reader group, SCard$AllReaders.                         |
| SCard$DefaultReaders | This default group, one for each [*terminal*](security.t_gly#-security-terminal-gly), contains all the readers assigned to the terminal that are not reserved for specific use. |



 

 

 



