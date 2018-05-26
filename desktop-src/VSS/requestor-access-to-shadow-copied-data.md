---
Description: Once the shadow copy has completed, the most important mechanism for getting access to the file data it contains is through the use of the shadow copys device object.
ms.assetid: 21efdbd6-a487-4e6f-8e3c-b9224bcf92da
title: Requester Access to Shadow Copied Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Requester Access to Shadow Copied Data

Once the shadow copy has completed, the most important mechanism for getting access to the file data it contains is through the use of the shadow copy's [*device object*](vssgloss-d.md#base-vssgloss-device-object).

The **m\_pwszSnapshotDeviceObject** member of a [**VSS\_SNAPSHOT\_PROP**](/windows/win32/Vss/ns-vss-_vss_snapshot_prop?branch=master) structure is a string containing a shadow-copied volume's device object. A requester can obtain a shadow-copied volume's **VSS\_SNAPSHOT\_PROP** object if it knows the volume's **VSS\_ID** (identifying GUID) and passes it to [**IVssBackupComponents::GetSnapshotProperties**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getsnapshotproperties?branch=master).

A requester can also obtain shadow copy property information by using the **Obj.Snap** member of the [**VSS\_OBJECT\_PROP**](/windows/win32/Vss/ns-vss-_vss_object_prop?branch=master) structure (which is a [**VSS\_SNAPSHOT\_PROP**](/windows/win32/Vss/ns-vss-_vss_snapshot_prop?branch=master) structure) obtained by using [**IVssEnumObject**](/windows/win32/Vss/nn-vss-ivssenumobject?branch=master) to iterate over the list of objects returned by a call to [**IVssBackupComponents::Query**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-query?branch=master).

The device object should be interpreted as the root of a shadow-copied volume. For this reason, the device object contains no backslash ("\\").

Paths on the shadow copied volume are obtained by replacing the root of the original path with the device object. For example, given a path on the original volume of "C:\\DATABASE\\\*.mdb" and a [**VSS\_SNAPSHOT\_PROP**](/windows/win32/Vss/ns-vss-_vss_snapshot_prop?branch=master) instance of snapProp, you would obtain the path on the shadow copied volume by concatenating snapPropm\_pwszShadow copyDeviceObject, "\\", and "\\DATABASE\\\*.mdb".

The VSS file sets might have wildcard characters in their file descriptors, so obtaining a full list of the files on a shadow copy managed by a component might require the use of methods such as **FindFileFirst**, **FindFileFirstEx**, and **FindNextFile**.

 

 



