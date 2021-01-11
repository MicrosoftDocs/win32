---
description: After you finish with a class or an instance, you may wish to delete that class or instance from WMI.
ms.assetid: 8d4bf548-a332-4058-92d0-d613bbeaa408
ms.tgt_platform: multiple
title: Deleting a Class or Instance
ms.topic: article
ms.date: 05/31/2018
---

# Deleting a Class or Instance

After you finish with a class or an instance, you may wish to delete that class or instance from WMI. Like other object-oriented technologies, you can delete class or instance objects to clean up the WMI namespace and to return system resources. However, many classes and instances in WMI are persistent and are used by a variety of applications at any given time Therefore, you should be careful when deleting a WMI class or instance: your application or another application will probably need the class or instance at a later date.

Deleting a class or an instance is a simple procedure. However, due to the permanent nature of a class, you will probably not need to delete a class often. For example, you are unlikely to delete the [**Win32\_DiskDrive**](/windows/desktop/CIMWin32Prov/win32-diskdrive) class, because it is unlikely that you do not have a disk drive somewhere in your enterprise. Instead, you will be more likely to delete an instance of a class. For more information, see [Deleting an Instance](deleting-an-instance.md).

Although uncommon, you may come across a time where you wish to update a class that you created. For example, you could create a class to represent a third-party application. If the third-party updated their software to the extent that your class no longer properly represented the software, you may need to delete your original class. For more information, see [Deleting a Class](deleting-a-class.md).

## Related topics

<dl> <dt>

[Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)
</dt> </dl>

 

 
