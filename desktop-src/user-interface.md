---
description: This section provides guidance for integrating and extending the desktop user-facing features of Windows.
ms.assetid: 1ffeeb4f-b337-45b9-885f-307b81670557
title: Desktop Environment
ms.topic: reference
ms.date: 05/31/2018
---

# Desktop Environment

This section provides guidance for integrating and extending the desktop user-facing features of Windows. You can learn how to ensure your apps and file formats appear and behave properly in Start, in the Taskbar, on the desktop, and in File Explorer. You can also ensure your file formats and data stores are indexable and searchable.

## In this section



| Topic                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Windows Shell](./shell/shell-entry.md)<br/>                                      | The Windows desktop UI provides users with access to a wide variety of objects necessary for running applications and managing the operating system. The most numerous and familiar of these objects are the folders and files that reside on computer disk drives. There are also a number of virtual objects that allow the user to perform tasks such as sending files to remote printers or accessing the Recycle Bin. The Shell organizes these objects into a hierarchical namespace and provides users and applications with a consistent and efficient way to access and manage objects.<br/> |
| [Windows Property System](./properties/windows-properties-system.md)<br/>         | The Windows Property System is an extensible read/write system of data definitions that provides a uniform way of expressing metadata about Shell items. The Windows Property system enables you to store and retrieve metadata for Shell items. A Shell item is any single piece of content, such as a file, folder, email, or contact. A property is an individual piece of metadata associated with a Shell item.<br/>                                                                                                                                                                             |
| [Windows Search](./search/windows-search.md)<br/>                                 | Windows Search is a desktop search platform that has instant search capabilities for most common file and data types such as email, contacts, calendar appointments, documents, photos, multimedia, and other formats that can be extended by third party developers. These capabilities enable users to find, manage, and organize the increasing amount of data common in home and enterprise environments.<br/>                                                                                                                                                                                    |
| [Window Stations and Desktops](./winstation/window-stations-and-desktops.md)<br/> | Windows provides three main categories of objects: user interface, graphics device interface (GDI), and kernel. Kernel objects are securable, while user objects and GDI objects are not. Therefore, to provide additional security, user interface objects are managed using window stations and desktops, which themselves are securable objects.<br/>                                                                                                                                                                                                                                              |
| [Windows Help](/windows/win32/api/winuser/nf-winuser-winhelpa)<br/>                                        | Describes the Help technologies available in Windows.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Consoles](/windows/console/character-mode-applications)<br/>                        | Consoles manage input and output (I/O) for character-mode applications (applications that do not provide their own graphical user interface).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[Windows Application UI Development](./windows-application-ui-development.md)
</dt> </dl>

 

 
