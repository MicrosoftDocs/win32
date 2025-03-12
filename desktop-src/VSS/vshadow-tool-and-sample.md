---
description: VShadow is a command-line tool that you can use to create and manage volume shadow copies.
ms.assetid: 19109f92-b9da-4df7-8628-374e37a3f624
title: VShadow Tool and Sample
ms.topic: sample
ms.date: 11/14/2024
---

# VShadow Tool and Sample

VShadow is a command-line tool that you can use to create and manage volume shadow copies.

> [!NOTE]
> VShadow is included in the Microsoft Windows Software Development Kit (SDK) for Windows Vista and later. The VSS 7.2 SDK includes a version of VShadow that runs only on Windows Server 2003. For information about downloading the Windows SDK and the VSS 7.2 SDK, see [Volume Shadow Copy Service](volume-shadow-copy-service-portal.md).

The VShadow tool uses command-line options and optional flags to identify the work to perform. When used without any command-line options, the VShadow command creates a new shadow copy set.

VShadow commands perform the following operations:

- [Creating a Shadow Copy Set](#creating-a-shadow-copy-set)
- [Importing a Shadow Copy Set](#importing-a-shadow-copy-set)
- [Querying Shadow Copy Properties](#querying-shadow-copy-properties)
- [Deleting Shadow Copies](#deleting-shadow-copies)
- [Breaking a Shadow Copy Set](#breaking-a-shadow-copy-set)
- [Breaking a Shadow Copy Set Using the BreakSnapshotSetEx Method](#breaking-a-shadow-copy-set-using-the-breaksnapshotsetex-method)
- [Exposing a Shadow Copy Locally](#exposing-a-shadow-copy-locally)
- [Exposing a Shadow Copy Remotely](#exposing-a-shadow-copy-remotely)
- [Listing Writer Status and Metadata](#listing-writer-status-and-metadata)
- [Performing Restore Operations](#performing-restore-operations)
- [Reverting to a Previous Shadow Copy](#reverting-to-a-previous-shadow-copy)
- [Resynchronizing LUNs](#resynchronizing-luns)

## Creating a Shadow Copy Set

`vshadow [OptionalFlags] VolumeList`

This command creates a new shadow copy set.

`VolumeList` is a list of volume names. VShadow creates one shadow copy for each volume in the list. A volume name can optionally be terminated with a backslash (`\`). For example, both `C:` and `C:\` are valid volume names. You can also specify mounted folders (for example, `C:\DirectoryName`) or volume GUID names (for example, `\\?\Volume{bbbbcccc-1111-dddd-2222-eeee3333ffff}`).

*OptionalFlags* is a bitmask of optional flag values from the following table.

| Optional Flag Value | Description |
|---------------------|-------------|
| `-ad` | This optional flag specifies differential hardware shadow copies. This flag and the **-ap** flag are mutually exclusive.<br> **Note:** This flag is supported only on Windows server operating systems. |
| `-ap` | This optional flag specifies plex hardware shadow copies. This flag and the **-ad** flag are mutually exclusive.<br> **Note:** This flag is supported only on Windows server operating systems. |
| `-bc=File.xml` | This optional flag specifies non-transportable shadow copies and stores the Backup Components Document into the specified file. This file can be used in a subsequent restore operation. This flag and the **-t** flag are mutually exclusive.<br> **Note:** This flag is supported only on Windows server operating systems. |
| `-exec=<Command>` | This optional flag executes a command or script after the shadow copies are created but before the VShadow tool exits. `<Command>` can specify an executable shell command or a CMD file. If it specifies a shell command, no command parameters can be specified.<br> **Note:** For security reasons and to keep the implementation simple, the `-exec` optional flag will not accept parameters to be passed to the command or script. The entire string passed to the `-exec` optional flag is treated as a single CMD or EXE file. For more information about this limitation, see the VShadow source code. |
| `-forcerevert` | This optional flag specifies that the shadow copy operation should be completed only if all disk signatures can be reverted.<br> **Note:** This flag is supported only on Windows server operating systems.<br>**Windows Server 2003:** Not supported. |
| `-mask` | This optional flag specifies that the shadow copy LUNs should be masked from the computer when the shadow copy set is broken.<br> **Note:** This flag is supported only on Windows server operating systems.<br>**Windows Server 2003:** Not supported. |
| `-nar` | This optional flag specifies shadow copies without auto-recovery. For more information about this option, see the documentation for the `VSS_VOLSNAP_ATTR_NO_AUTORECOVERY` flag of the [_VSS_VOLUME_SNAPSHOT_ATTRIBUTES](/windows/win32/api/Vss/ne-vss-vss_volume_snapshot_attributes)] enumeration. |
| `-norevert` | This optional flag specifies that disk signatures should not be reverted.<br> **Note:** This flag is supported only on Windows server operating systems.<br>**Windows Server 2003:** Not supported. |
| `-nw` | This optional flag specifies shadow copies without involving writers. For more information about shadow copies without writer participation, see [Shadow Copy Creation Details](shadow-copy-creation-details.md). This flag and the `-wi` and `-wx` flags are mutually exclusive. |
| `-p` | This optional flag specifies [persistent shadow copies](vssgloss-p.md).<br> **Note:** This flag is supported only on Windows server operating systems. |
| `-rw` | This optional flag specifies that the shadow copy LUNs should be made read/write when the shadow copy set is broken.<br> **Note:** This flag is supported only on Windows server operating systems.<br>**Windows Server 2003:** Not supported. |
| `-scsf` | This optional flag specifies [**client-accessible shadow copies**](vssgloss-c.md).<br> **Note:** This flag is supported only on Windows server operating systems. |
| `-script=File.cmd` | This optional flag generates a CMD file containing environment variables related to the created shadow copies, such as shadow copy IDs and shadow copy set IDs. |
| `-t=File.xml` | This optional flag specifies transportable shadow copies and stores the Backup Components Document into the file specified by the `File.xml` parameter. This file can be used in a subsequent import and/or restore operation. This flag and the `-bc` flag are mutually exclusive.<br/>**Windows Server 2003, Standard Edition and Windows Server 2003, Web Edition:** Transportable shadow copies are not supported. All editions of Windows Server 2003 with Service Pack 1 (SP1) support transportable shadow copies. |
| `-tr` | This optional flag specifies that TxF recovery should be enforced during shadow copy creation.<br> **Note:** This flag is supported only on Windows server operating systems. |
| `-tracing` | This optional flag generates verbose output that can be used for troubleshooting. |
| `-wait` | This optional flag causes the VShadow tool to wait for user confirmation before exiting. |
| `-wi=<Writer>` | This optional flag verifies that the specified writer or component is included in the shadow copy. `<Writer>` can specify a component path, writer name, writer ID, or writer instance ID. This flag and the `-nw` flag are mutually exclusive. |
| `-wx=<Writer>` | This optional flag verifies that the specified writer or component is excluded from the shadow copy. `<Writer>` can specify a component path, writer name, writer ID, or writer instance ID. This flag and the `-nw` flag are mutually exclusive. |

## Importing a Shadow Copy Set

`vshadow [OptionalFlags] -i=File.xml`

The `-i` command-line option imports a transportable shadow copy set.

> [!NOTE]
> This command-line option is supported only on Windows server operating systems.

The `File.xml` file must be a Backup Components Document file for a transportable shadow copy set that was created with the `-t` or `-bc` optional flag.

A shadow copy set is a [persistent shadow copy](vssgloss-p.md) if it was created with the `-p` optional flag. If the transportable shadow copy set is nonpersistent, it appears for a short time while the shadow copy creation command is running, and is automatically deleted when the command returns. You can import nonpersistent shadow copies only during shadow copy creation, by creating the shadow copy set using the `-exec` optional flag to execute a CMD file that calls VShadow `-i`.

The `-i` command-line option cannot be combined with other command-line options.

`OptionalFlags` is a bitmask of optional flag values from the following table.

| Optional Flag Value | Description |
|---------------------|-------------|
| `-exec=<Command>` | This optional flag executes a command or script after the shadow copies are imported but before the VShadow tool exits. `<Command>` can specify an executable shell command or a CMD file. If it specifies a shell command, no command parameters can be specified. |
| `-tracing` | This optional flag generates verbose output that can be used for troubleshooting. |
| `-wait` | This optional flag causes the VShadow tool to wait for user confirmation before exiting. |

## Querying Shadow Copy Properties

`vshadow -q`

`vshadow -qx=<ShadowCopySetId>`

`vshadow -s=<ShadowCopyId>`

The `-q` command-line option lists the properties of all shadow copies on the computer.

The `-qx` command-line option lists the properties of all shadow copies in the shadow copy set whose ID is specified by `<ShadowCopySetId>`.

The `-s` command-line option lists the properties of the shadow copy whose ID is specified by `<ShadowCopyId>`.

These command-line options use a combination of [IVssBackupComponents::Query](/windows/win32/api/VsBackup/nf-vsbackup-ivssbackupcomponents-query) and [IVssBackupComponents::GetSnapshotProperties](/windows/win32/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getsnapshotproperties) to get the properties of the given set of shadow copies.

The `-q`, `-qx`, and `-s` command-line options are mutually exclusive and cannot be combined with other command-line options.

## Deleting Shadow Copies

`vshadow** -da`

`vshadow -do`

`vshadow -dx=<ShadowCopySetId>`

`vshadow -ds=<ShadowCopyId>`

The `-da` command deletes all shadow copies on the computer.

> [!NOTE]
> The `-da` command-line option requires user confirmation.

The `-do` command-line option deletes the oldest shadow copy on the computer.

The `-dx` command-line option deletes all shadow copies in the shadow copy set whose ID is specified by `<ShadowCopySetId>`.

The `-ds` command-line option deletes the shadow copy whose ID is specified by `<ShadowCopyId>`.

These command-line options are for use with [persistent shadow copies](vssgloss-p.md) only. Nonpersistent shadow copies do not need to be explicitly deleted, because they are automatically deleted when the VShadow creation command exits.

The `-da`, `-do`, `-dx`, and `-ds` command-line options are mutually exclusive and cannot be combined with other command-line options.

## Breaking a Shadow Copy Set

`vshadow -b=<ShadowCopySetId>`

`vshadow -bw=<ShadowCopySetId>`

The `-b=<ShadowCopySetId>` command-line option converts each shadow copy in the shadow copy set into a stand-alone read-only volume.

The `-bw=<ShadowCopySetId>` command-line option converts each shadow copy in the shadow copy set into a stand-alone writable volume.

> [!NOTE]
> The `-b` and `-bw` command-line options are supported only on Windows server operating systems.

For information about breaking a shadow copy set, see [Breaking Shadow Copies](breaking-shadow-copies.md).

After the shadow copy set is broken, the shadow copy set and the individual shadow copies no longer exist and cannot be managed using VSS commands.

A shadow copy set is persistent if it was created with the `-p` optional flag. If the transportable shadow copy set is nonpersistent, it appears for a short time while the shadow copy creation command is running, and is automatically deleted when the command returns. You can break nonpersistent shadow copy sets only during shadow copy creation, by creating the shadow copy set using the `-exec` optional flag to execute a CMD file that calls `vshadow -b` or `vshadow -bw`.

The `-b` and `-bw` command-line options are mutually exclusive and cannot be combined with other command-line options.

## Breaking a Shadow Copy Set Using the BreakSnapshotSetEx Method

`vshadow -bex`

The `-bex` command-line option breaks a shadow copy set according to the options specified by the optional `-mask`, `-rw`, `-forcerevert`, and `-norevert` flags. This command-line option is similar to the `-b` and `-bw` command-line options. The `-bex` command-line option uses the [IVssBackupComponentsEx2::BreakSnapshotSetEx](/windows/win32/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-breaksnapshotsetex) method, whereas the `-b` and `-bw` command-line options use the [IVssBackupComponents::BreakSnapshotSet](/windows/win32/api/VsBackup/nf-vsbackup-ivssbackupcomponents-breaksnapshotset) method.

For information about breaking a shadow copy set, see [Breaking Shadow Copies](breaking-shadow-copies.md).

> [!NOTE]
> The `-bex` command-line option is supported only on Windows server operating systems.

`vshadow -bex -mask`

The `-mask` flag specifies that the shadow copy LUN will be masked from the host. If the `-mask` flag is specified, the `-rw`, `-forcerevert`, and `-norevert` flags cannot be specified.

`vshadow -bex -rw`

The `-rw` flag specifies that the shadow copy LUN will be exposed to the host as a read/write volume.

`vshadow -bex -forcerevert`

The `-forcerevert` flag specifies that the disk identifiers of all of the shadow copy LUNs will be reverted to that of the original LUNs. However, if any of the original LUNs are present on the system, the operation will fail and none of the identifiers will be reverted. This flag and the `-norevert` flag are mutually exclusive.

`vshadow -bex -norevert`

The `-norevert` flag specifies that none of the shadow copy LUN disk identifiers will be reverted. This flag and the `-forcerevert` flag are mutually exclusive.

## Exposing a Shadow Copy Locally

`vshadow -el=<ShadowCopyId>,<LocalEmptyDirectory>`

`vshadow -el=<ShadowCopyId>,<UnusedDriveLetter>`

The `-el` command-line option assigns a mounted folder or a drive letter to a persistent shadow copy. Note that the volume contents will remain read-only unless you subsequently call `vshadow -bw` to break the shadow copy set.

> [!NOTE]
> Nonpersistent shadow copies and [client-accessible shadow copies](vssgloss-c.md) cannot be exposed locally.

For example, if `{bbbbcccc-1111-dddd-2222-eeee3333ffff}` is the GUID of an existing persistent shadow copy, and `X:` is an unused drive letter, the following command exposes the shadow copy under `X:`:

`vshadow -el={bbbbcccc-1111-dddd-2222-eeee3333ffff},x:`

The following example shows how to expose the same shadow copy under the mounted folder `C:\ShadowCopies\June23`:

`mkdir c:\ShadowCopies\June23`

`vshadow -el={bbbbcccc-1111-dddd-2222-eeee3333ffff},c:\ShadowCopies\June23`

The `-el` command-line option cannot be combined with other command-line options.

## Exposing a Shadow Copy Remotely

`vshadow -er=<ShadowCopyId>,<UnusedShareName>`

`vshadow -er=<ShadowCopyId>,<UnusedShareName>,<PathFromRootOnShadow>`

The `-er` command-line option assigns a read-only share name to the root directory (or a subdirectory) from the shadow copy. Note that the share contents will remain read-only unless you subsequently call `vshadow -bw` to break the shadow copy set.

> [!NOTE]
> [Client-accessible shadow copies](vssgloss-c.md) cannot be exposed remotely.

For example, if `{bbbbcccc-1111-dddd-2222-eeee3333ffff}` is the GUID of an existing persistent shadow copy, and `share_123` is an unused share name, the following command exposes the shadow copy under `share_123`:

`vshadow -er={bbbbcccc-1111-dddd-2222-eeee3333ffff},share_123`

The following example shows how to expose only a subtree (named `Folder1\Folder2`) of the same shadow copy under the same share:

`vshadow -er={bbbbcccc-1111-dddd-2222-eeee3333ffff},share_123,Folder1\Folder2`

The `-er` command-line option cannot be combined with other command-line options.

## Listing Writer Status and Metadata

`vshadow -ws`

`vshadow -wm`

`vshadow -wm2`

`vshadow -wm3`

The `-ws` command-line option enumerates the VSS writers that are currently running on the computer and describes their state. This command is the equivalent of the [Vssadmin list writers](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc754968(v=ws.11)) command. There are six possible state values: `Stable`, `Failed`, `Unknown`, `Waiting for freeze`, `Frozen`, and `Waiting for completion`.

The `-wm` command-line option lists a summary of the writer metadata, including the affected volumes.

The `-wm2` command-line option lists all writer metadata.

The `-wm3` command-line option lists all writer metadata in raw XML format.

**Windows Vista and Windows Server 2003:** The `-wm3` command-line option is not supported.

You can use this information to determine which volumes to include in the volume shadow copy set.

> [!NOTE]
> If the writer state is Stable or Waiting for completion, the writer can be considered to be in a stable state, ready for the next backup.

The `-ws`, `-wm`, `-wm2`, and `-wm3` command-line options are mutually exclusive and cannot be combined with other command-line options.

## Performing Restore Operations

`vshadow [OptionalFlags] -r=File.xml`

`vshadow [OptionalFlags] -rs=File.xml`

The `-r` command-line option performs a restore operation.

The `-rs` command-line option performs a simulated restore operation.

The `File.xml` file must be a Backup Components Document file for a shadow copy set that was created with the `-t` or `-bc` optional flag.

The `-r` and `-rs` command-line options are mutually exclusive and cannot be combined with other command-line options.

`OptionalFlags` is a bitmask of optional flag values from the following table.

| Optional Flag Value | Description |
|---------------------|-------------|
| `-wi=<Writer>` | This optional flag verifies that the specified writer or component is included in the restore. `<Writer>` can specify a component path, writer name, writer ID, or writer instance ID. |
| `-wx=<Writer>` | This optional flag verifies that the specified writer or component is excluded from the restore. `<Writer>` can specify a component path, writer name, writer ID, or writer instance ID. |
| `-exec=<Command>` | This optional flag executes a command or script between the pre-restore and post-restore events that are sent to the writers. `<Command>` can specify an executable shell command or a CMD file. If it specifies a shell command, no command parameters can be specified. |
| `-tracing` | This optional flag generates verbose output that can be used for troubleshooting. |

## Reverting to a Previous Shadow Copy

`vshadow -revert=<ShadowCopyId>`

> [!NOTE]
> This command-line option is supported only on Windows server operating systems.

**Windows Server 2008 and Windows Server 2003:** Not supported.

The `-revert` command-line option reverts a volume to the previous shadow copy whose ID is specified by `<ShadowCopyId>`.

The `-revert` command-line option cannot be combined with other command-line options.

## Resynchronizing LUNs

`vshadow** -addresync=<ShadowCopyId> -resync=<BCDFileName> [OptionalResyncFlags]`

`vshadow -addresync=<ShadowCopyId>, <TargetVolumeDriveLetter> -resync=<BCDFileName> [OptionalResyncFlags]`

The `-addresync` command-line option specifies the volumes to be included in a LUN resynchronization operation. The `<ShadowCopyId>` parameter specifies the identifier of the shadow copy. The optional `<TargetVolumeDriveLetter>` parameter specifies the destination volume where the contents of the shadow copy volume are to be copied.

The `-resync` command-line option initiates a LUN resynchronization operation. After the operation is complete, the signature of each target LUN should be identical to that of the target volume LUN. The `<BCDFileName>` parameter specifies the name of the XML file that contains the Backup Component Document.

> [!NOTE]
> The `-addresync` and `-resync` command-line options are supported only on Windows server operating systems.

**Windows Server 2008 and Windows Server 2003:** Not supported.

`OptionalResyncFlags` is a bitmask of optional flag values from the following table.

| Optional flag value | Description |
|---------------------|-------------|
| `-revertsig` | This optional flag specifies that after the operation is complete, the signature of each target LUN should be identical to that of the original LUN that was used to create the shadow copy, not the target volume LUN.<br> **Note:** The `-revertsig` flag is supported only on Windows server operating systems.<br>**Windows Server 2008 and Windows Server 2003:** Not supported. |
| `-novolcheck` | This optional flag specifies that the VSS service should not check for unselected volumes that would be overwritten by the LUN resynchronization operation.<br> **Note:** The `-novolcheck` flag is supported only on Windows server operating systems.<br>**Windows Server 2008 and Windows Server 2003:** Not supported. |

## See also

[Volume Shadow Copy Service](volume-shadow-copy-service-portal.md)

[Volume Shadow Copy API Reference](volume-shadow-copy-reference.md)
