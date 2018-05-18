---
title: Gadgets for Windows Sidebar - System Object Reference
description: This section describes the Windows Sidebar scripting elements that provide access to system functionality, such as file, network, and operating system information.
ms.assetid: 'be8fed31-6fe0-460b-85e7-18509e2bf32f'
---

# Gadgets for Windows Sidebar - System Object Reference

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

This section describes the Windows Sidebar scripting elements that provide access to system functionality, such as file, network, and operating system information.

## System Reference

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>System.Contact</strong>](system-contact.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and methods of each member of the [<strong>Contacts</strong>](system-contactmanager-contacts.md) collection. <br/></td>
</tr>
<tr class="even">
<td>[<strong>System.ContactManager</strong>](system-contactmanager.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties for the [<strong>Contacts</strong>](system-contactmanager-contacts.md) collection. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Contact</strong>](system-contact.md) can only be accessed through the [<strong>Contacts</strong>](system-contactmanager-contacts.md) collection. This collection is a member of [<strong>System.ContactManager</strong>](system-contactmanager.md).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.Debug</strong>](system-debug.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the method available for debugging Sidebar gadget script.<br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Diagnostics.EventLog</strong>](system-diagnostics-eventlog.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the method available for writing an <strong>Application</strong> event log entry.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.Environment</strong>](system-environment.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and methods for determining system and user environment variables.<br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Machine</strong>](system-machine.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties for determining machine processor and memory characteristics as well as the properties for the [<strong>CPUs</strong>](system-machine-cpus.md) collection. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Machine.CPU</strong>](system-machine-cpu.md) can only be accessed through the [<strong>CPUs</strong>](system-machine-cpus.md) collection. This collection is a member of [<strong>System.Machine</strong>](system-machine.md).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.Machine.CPU</strong>](system-machine-cpu.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and methods of each member of the [<strong>System.Machine.CPU</strong>](system-machine-cpu.md) collection. <br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Machine.PowerStatus</strong>](system-machine-powerstatus.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and events for the computer's power status. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.MessageStore</strong>](system-messagestore.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties for the Windows Mail (formerly Outlook Express) [<strong>Folders</strong>](system-messagestore-folders.md) collection. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.MessageStore.Folder</strong>](system-messagestore-folder.md) can only be accessed through the [<strong>Folders</strong>](system-messagestore-folders.md) collection. This collection is a member of [<strong>System.MessageStore</strong>](system-messagestore.md).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>System.MessageStore.Folder</strong>](system-messagestore-folder.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties for individual Windows Mail folders as well as the properties for the [<strong>Messages</strong>](system-messagestorefolder-messages.md) collection. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.MessageStore.Message</strong>](system-messagestore-message.md) can only be accessed through the [<strong>Messages</strong>](system-messagestorefolder-messages.md) collection. This collection is a member of [<strong>System.MessageStore.Folder</strong>](system-messagestore-folder.md).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.MessageStore.Message</strong>](system-messagestore-message.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties of each member of the Windows Mail [<strong>Messages</strong>](system-messagestorefolder-messages.md) collection. <br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Network.Wireless</strong>](system-network-wireless.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and events for determining wireless network connectivity and interface settings. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.Shell</strong>](system-shell.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and methods used to expose [Windows Shell](http://msdn.microsoft.com/library/bb773177.aspx) characteristics. <br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Shell.Drive</strong>](system-shell-drive.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties used to expose system storage device characteristics. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.Shell.Folder</strong>](system-shell-folder.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and methods for performing file management operations as well as the properties for the [<strong>Items</strong>](system-shell-folder-items.md) collection. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Shell.Item</strong>](system-shell-item.md) can only be accessed through the [<strong>Items</strong>](system-shell-folder-items.md) collection. This collection is a member of [<strong>System.Shell.Folder</strong>](system-shell-folder.md).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Shell.Item</strong>](system-shell-item.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties of each member of the [<strong>Items</strong>](system-shell-folder-items.md) collection. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.Shell.RecycleBin</strong>](system-shell-recyclebin.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties, methods, and events used to expose <strong>Recycle Bin</strong> characteristics. <br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Sound</strong>](system-sound.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the methods available for playing sounds.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>System.Time</strong>](system-time.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and methods for determining system time information as well as the properties for the [<strong>timeZones</strong>](system-time-timezones.md) collection. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Time.timeZone</strong>](system-time-timezone.md) can only be accessed through the [<strong>timeZones</strong>](system-time-timezones.md) collection. This collection is a member of [<strong>System.Time</strong>](system-time.md).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>System.Time.timeZone</strong>](system-time-timezone.md)<br/></td>
<td><blockquote>
[!Note]<br />
The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.
</blockquote>
<br/> Defines the properties and methods of each member of the [<strong>System.Time.timeZone</strong>](system-time-timezone.md) collection. <br/></td>
</tr>
</tbody>
</table>



 

 

 





