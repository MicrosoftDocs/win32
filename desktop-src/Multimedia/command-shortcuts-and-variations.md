---
title: Command Shortcuts and Variations
description: Command Shortcuts and Variations
ms.assetid: 4f854c78-435c-4a10-8938-645ad605fff3
ms.topic: article
ms.date: 05/31/2018
---

# Command Shortcuts and Variations

You can use several shortcuts when working with MCI commands. These shortcuts enable you to use a single identifier to refer to all the devices your application has opened, or to open a device without explicitly issuing an [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) command.

You can specify "all" (MCI\_ALL\_DEVICE\_ID) as a device identifier for any command that does not return information. When you specify "all", MCI sends the command sequentially to all devices opened by the current application.

For example, the [**close**](close.md) "all" command closes all open devices and the [**play**](play.md) "all" command starts playing all devices opened by the application. Because MCI sequentially sends the commands to the MCI devices, there is an interval between when the first and last devices receive the command.

Using "all" is a convenient way to broadcast a command to all your devices, but you should not rely on it to synchronize devices; the timing between messages can vary.

When you issue a command and specify a device that is not open, MCI tries to open the device before implementing the command. The following rules apply to automatically opening devices:

-   The automatic open feature works only with the command-string interface.
-   The automatic open feature fails for commands that are specific to custom device drivers.
-   Automatically opened devices do not respond to commands that use "all" as a device name.
-   The automatic open feature does not let your application specify the "type" flag. Without the device name, MCI determines the device name from the entries in the registry. To use a specific device, you can combine the device name with the filename by using the exclamation point, as described in the reference material for the [**open**](open.md) command.

If an application uses the automatic open feature to open a device, the application should check the return value of every subsequent open command to verify that the device is still open. MCI also automatically closes any device that it automatically opens. MCI typically closes a device in the following situations:

-   The command is completed.
-   You abort the command.
-   You request notification in a subsequent command.
-   MCI detects a failure.

 

 




