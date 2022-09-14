---
title: Backing Up and Restoring of DRM Licenses
description: Backing Up and Restoring of DRM Licenses
ms.assetid: ec2777e9-76af-43fe-8bd5-4d7532d2fb32
keywords:
- Windows Media Format SDK,backing up DRM licenses
- Windows Media Format SDK,restoring DRM licenses
- Windows Media Format SDK,DRM licenses
- Windows Media Format SDK,licenses for DRM
- Windows Media Format SDK,Backup Restore feature
- Windows Media Format SDK,License Management Service
- Windows Media Format SDK,fraud detection
- digital rights management (DRM),backing up licenses
- DRM (digital rights management),backing up licenses
- digital rights management (DRM),restoring licenses
- DRM (digital rights management),restoring licenses
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),Backup Restore feature
- DRM (digital rights management),Backup Restore feature
- digital rights management (DRM),License Management Service
- DRM (digital rights management),License Management Service
- digital rights management (DRM),fraud detection
- DRM (digital rights management),fraud detection
- backing up DRM licenses
- restoring DRM licenses
- licenses,DRM
- licenses,backing up DRM
- licenses,restoring DRM
- Backup Restore feature
- License Management Service
- fraud detection
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up and Restoring of DRM Licenses

With the Backup Restore feature, users can back up and restore [*licenses*](wmformat-glossary.md) to the same computer or to other computers. This feature enables users to transfer licenses to a new computer or back to the same computer (after reformatting the hard disk, for example). In addition, users can play protected ASF files on more than one computer.

To encourage legitimate use of a license, a fraud detection policy restricts the number of times a license can be restored. Microsoft provides a service that tracks the number of computers to which a license has been restored; if a limit is reached, the user cannot restore the license.

## Allowing or Disallowing the Right to Back Up and Restore

The Backup Restore feature works only for licenses for which the Backup and Restore right is given. If content owners or license issuers do not want this feature, or if they issue licenses that contain a secure state (such as counted operations or limited time), they can disallow this right.

When a license cannot be restored because a user does not have the right, a [*key ID*](wmformat-glossary.md) is passed to the application. At a minimum, the user should be notified that some licenses could not be backed up, although the user does not know which licenses this message refers to. If you know the key ID for available protected files, you can develop a more robust solution for informing the user.

For example, a player could be developed for a record label that provides protected songs on the Internet. These songs and their key IDs could be tracked in a database. If some licenses could not be backed up, the player application could use the key ID to query the database for the name of the songs, then inform the user for which songs the licenses cannot be backed up. Or, a music library could be created for each user locally, and the key ID could be used to retrieve more information about which licenses could not be backed up.

## The License Management Service

When the Backup Restore feature is implemented, a License Management Service that is hosted by Microsoft manages the restoration of licenses.

First, users back up licenses in the application, for example, by choosing a menu option. All licenses on the computer are backed up to a specified location, such as a floppy disk. Then, users restore licenses by using the application, for example, by choosing a menu option and specifying their backup location.

At this point, the user must be connected to the Internet; a request from the application is sent to the License Management Service. If the computer from which the license was backed up is different from the original computer (or the original computer has been reformatted), the License Management Service issues a new license to the new computer. Otherwise, the license that was previously issued to that computer is reissued.

Because the License Management Service retrieves information from the user, you must display the Microsoft privacy policy or provide a link to that page at the [Microsoft Web site](https://www.microsoft.com/licensing/default).

> [!Note]  
> When an end user restores a license to a different computer and the license requires individualization, the end user must authorize the DRM components to be updated. You must implement a process in your player application to support this feature.

 

## Detecting Fraud

The user is allowed to restore a license a limited number of times. Each time a license is restored, the License Management Service tracks it and increments the count for that license by one. When restoring a license to a computer to which the license has been restored previously (for example, the computer from which the license was backed up), the count is not increased. A computer is considered to be different if it has a new operating system, or the operating system has been re-installed.

In accordance with Microsoft's fraud detection policy, when a license has been restored a certain number of times, the application receives a URL from the DRM components and is responsible for opening a browser and displaying the Web page, which indicates that the license agreement might have been violated. The user must contact the license distributor, who must then determine whether the request is valid.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Backing Up and Restoring Licenses**](backing-up-and-restoring-licenses.md)
</dt> </dl>

 

 




