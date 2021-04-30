---
description: The IUpdate interface defines the following properties.
ms.assetid: d87544f1-a107-440f-8ce0-77d9f2d90578
title: IUpdate Properties
ms.topic: article
ms.date: 05/31/2018
---

# IUpdate Properties

The [**IUpdate**](/windows/desktop/api/Wuapi/nn-wuapi-iupdate) interface defines the following properties.



| Property                                                                           | Description                                                                                                                                                                         |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AutoSelectOnWebSites**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_autoselectonwebsites)                       | Gets a Boolean value that indicates whether the update is flagged to be automatically selected by Windows Update.                                                                   |
| [**BundledUpdates**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_bundledupdates)                                   | Gets an interface that contains information about the ordered list of the bundled updates for the update.                                                                           |
| [**CanRequireSource**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_canrequiresource)                               | Gets a Boolean value that indicates whether the source media of the update is required for installation or uninstallation.                                                          |
| [**Categories**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_categories)                                           | Gets an interface that contains a collection of categories to which the update belongs.                                                                                             |
| [**Deadline**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_deadline)                                               | Gets the date by which the update must be installed.                                                                                                                                |
| [**DeltaCompressedContentAvailable**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_deltacompressedcontentavailable) | Gets a Boolean value that indicates whether delta-compressed content is available on a server for the update.                                                                       |
| [**DeltaCompressedContentPreferred**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_deltacompressedcontentpreferred) | Gets a Boolean value that indicates whether to prefer delta-compressed content during the download and install or uninstall of the update if delta-compressed content is available. |
| [**DeploymentAction**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_deploymentaction)                               | Gets the action for which the update is deployed.                                                                                                                                   |
| [**Description**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_description)                                         | Gets the localized description of the update.                                                                                                                                       |
| [**DownloadContents**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_downloadcontents)                               | Gets file information about the download contents of the update.                                                                                                                    |
| [**DownloadPriority**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_downloadpriority)                               | Gets the suggested download priority of the update.                                                                                                                                 |
| [**EulaAccepted**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_eulaaccepted)                                       | Gets a Boolean value that indicates whether the Microsoft Software License Terms that are associated with the update are accepted for the computer.                                 |
| [**EulaText**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_eulatext)                                               | Gets the full localized text of the Microsoft Software License Terms that are associated with the update.                                                                           |
| [**HandlerID**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_handlerid)                                             | Gets the install handler of the update.                                                                                                                                             |
| [**Identity**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_identity)                                               | Gets an interface that contains the unique identifier of the update.                                                                                                                |
| [**Image**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_image)                                                     | Gets an interface that contains information about an image that is associated with the update.                                                                                      |
| [**InstallationBehavior**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_installationbehavior)                       | Gets an interface that contains the installation options of the update.                                                                                                             |
| [**IsBeta**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_isbeta)                                                   | Gets a Boolean value that indicates whether the update is a beta release.                                                                                                           |
| [**IsDownloaded**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_isdownloaded)                                       | Gets a Boolean value that indicates whether all the update content is cached on the computer.                                                                                       |
| [**IsHidden**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_ishidden)                                               | Gets a Boolean value that indicates whether an update is hidden by a user.                                                                                                          |
| [**IsInstalled**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_isinstalled)                                         | Gets a Boolean value that indicates whether the update is installed on a computer when the search is performed.                                                                     |
| [**IsMandatory**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_ismandatory)                                         | Gets a Boolean value that indicates whether the installation of the update is mandatory.                                                                                            |
| [**IsUninstallable**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_isuninstallable)                                 | Gets a Boolean value that indicates whether a user can uninstall the update from a computer.                                                                                        |
| [**KBArticleIDs**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_kbarticleids)                                       | Gets a collection of Microsoft Knowledge Base article IDs that are associated with the update.                                                                                      |
| [**Languages**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_languages)                                              | Gets an interface that contains the languages that are supported by the update.                                                                                                     |
| [**LastDeploymentChangeTime**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_lastdeploymentchangetime)               | Gets the last published date of the update, in Coordinated Universal Time (UTC) date and time, on the server that deploys the update.                                               |
| [**MaxDownloadSize**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_maxdownloadsize)                                 | Gets the maximum download size of the update.                                                                                                                                       |
| [**MinDownloadSize**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_mindownloadsize)                                 | Gets the minimum download size of the update.                                                                                                                                       |
| [**MoreInfoUrls**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_moreinfourls)                                       | Gets a collection of language-specific strings that specify the hyperlinks to more information about the update.                                                                    |
| [**MsrcSeverity**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_msrcseverity)                                       | Gets the Microsoft Security Response Center severity rating of the update.                                                                                                          |
| [**RecommendedCPUSpeed**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_recommendedcpuspeed)                         | Gets the recommended CPU speed used to install the update, in megahertz (MHz).                                                                                                      |
| [**RecommendedHardDiskSpace**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_recommendedharddiskspace)               | Gets the recommended free space that should be available on the hard disk before you install the update. The free space is specified in megabytes (MB).                             |
| [**RecommendedMemory**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_recommendedmemory)                             | Gets the recommended physical memory size that should be available in your computer before you install the update. The physical memory size is specified in megabytes (MB).         |
| [**ReleaseNotes**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_releasenotes)                                       | Gets the localized release notes for the update.                                                                                                                                    |
| [**SecurityBulletinIDs**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_securitybulletinids)                         | Gets a collection of string values that contain the security bulletin IDs that are associated with the update.                                                                      |
| [**SupersededUpdateIDs**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_supersededupdateids)                         | Gets a collection of update identifiers. This collection of identifiers specifies the updates that are superseded by the update.                                                    |
| [**SupportUrl**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_supporturl)                                           | Gets a hyperlink to the language-specific support information for the update.                                                                                                       |
| [**Title**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_title)                                                     | Gets the localized title of the update.                                                                                                                                             |
| [**Type**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_type)                                                       | Gets the type of the update.                                                                                                                                                        |
| [**UninstallationBehavior**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_uninstallationbehavior)                   | Gets an interface that contains the uninstallation options for the update.                                                                                                          |
| [**UninstallationNotes**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_uninstallationnotes)                         | Gets the uninstallation notes for the update.                                                                                                                                       |
| [**UninstallationSteps**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_uninstallationsteps)                         | Gets an interface that contains the uninstallation steps for the update.                                                                                                            |



 

 

 



