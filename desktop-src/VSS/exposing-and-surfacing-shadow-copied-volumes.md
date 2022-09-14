---
description: In addition to being accessed through the IVssBackupComponents interface by means of its copy's device object, a requester can make a shadow copy available to other processes as a mounted read-only device.
ms.assetid: 0898c2dc-992a-411b-81df-4f5e129f6a80
title: Exposing and Surfacing Shadow Copied Volumes
ms.topic: article
ms.date: 05/31/2018
---

# Exposing and Surfacing Shadow Copied Volumes

In addition to being accessed through the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface by means of its copy's [*device object*](vssgloss-d.md), a requester can make a shadow copy available to other processes as a mounted read-only device.

This process is known as [*exposing a shadow copy*](vssgloss-e.md), and is performed using the [**IVssBackupComponents::ExposeSnapshot**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-exposesnapshot) method.

A shadow copy can be exposed as a local volume—assigned a drive letter or associated with a mounted folder—or as a file share.

To illustrate, consider a shadow copy made of a volume on the system exposedSys mounted at F:\\ on whose root are the directories dirOne and dirTwo, and the file FileOne.

## Exposing a Shadow Copy Locally

When mounted as a local volume, the shadow copy's root is always visible at the mount point (drive letter or mounted folder) and all the shadow-copied files are visible.

If the shadow copy was locally exposed through the mounted folder C:\\ShadowOfF, you would find all files present on disk mounted at F:\\ at the time of the shadow copy available under C:\\ShadowOfF. Examining C:\\ShadowOfF would reveal two directories, dirOne and dirTwo, and one file, fileOne, under C:\\ShadowOfF.

A call to locally expose the shadow copy might be:

``` syntax
  IVssBackupComponents *pReq;
  VSS_ID snapID;
  PWSTR wszExposed;
  //    .
  //    .
  hr = pReg->ExposeSnapshot(
         snapID,                           // VSS_ID SnapshotId,
         NULL,                             // VSS_PWSZ wszPathFromRoot
         VSS_VOLSNAP_ATTR_EXPOSED_LOCALLY, // LONG lAttributes
         L"C:\ShadowOfF",                  // VSS_PWSZ wszExpose
         LPWSTR &wszExposed,               // VSS_PWSZ* pwszExposed
       );
```

If the shadow copy was successfully exposed locally, *wszExposed* should contain the wide character string "C:\\ShadowOfF."

The shadow copy can later be unexposed by calling [**IVssBackupComponentsEx2::UnexposeSnapshot**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-unexposesnapshot).

Only persistent shadow copies—that is, shadow copies created with either VSS\_CTX\_NAS\_ROLLBACK or VSS\_CTX\_APP\_ROLLBACK—can be exposed locally.

## Exposing a Shadow Copy as a Remote Share

Alternatively, you could choose to make the shadow copy of the disk mounted at F:\\ available as a remote file share, and expose only data under dirTwo as the file share dirTwoOfF.

In this case, systems could access the shadow copy of files under F:\\dirTwo by mapping \\\\exposedSys\\dirTwoOfF as a network drive.

A call to implement remote exposing the shadow copy as a share might be the following:

``` syntax
  IVssBackupComponents *pReq;
  VSS_ID snapID;
  LPWSTR wszExposed;
  //    .
  //    .
  hr = pReg->ExposeSnapshot(
               snapID,                            // VSS_ID SnapshotId,
               L"\dirTwo",                        // VSS_PWSZ wszPathFromRoot
               VSS_VOLSNAP_ATTR_EXPOSED_REMOTELY, // LONG lAttributes
               L"dirTwoOfF",                      // VSS_PWSZ wszExpose
               LPWSTR &wszExposed,                // VSS_PWSZ* pwszExposed
       );
```

If the shadow copy was successfully exposed remotely, *wszExposed* should contain the wide character string "dirTwoOfF."

Any system currently mapping the network share of dirTwoOfF could disconnect from it, just as it might disconnect from any ordinary share.

## Surfacing a Shadow Copy

A [*surfaced shadow copy*](vssgloss-s.md) is one in which the shadow copy is known to a system's Mount Manager namespace.

This means that you can locate such shadow copies just as you would locate any other available but not-yet-mounted volume—by using **FindFirstVolume** and **FindNextVolume**, for example.

Clearly, then, exposed shadow copies are also surfaced shadow copies. However, the reverse is not necessarily true.

If a locally exposed shadow copy was dismounted, or a system chose to disconnect a remotely exposed shadow copy, that shadow copy would no longer be exposed. However, as long as the shadow copy persisted, the volumes would be surfaced. This means they could be mounted like any other read-only volume.

 

 



