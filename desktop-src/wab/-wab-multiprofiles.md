---
title: WAB and Multi-User/Multi-Identity Profiles
description: Beginning with version 5.0, the WAB provides support for multiple people who use the same logon name and password in the WAB.
ms.assetid: 'c0df7598-c66b-40d5-9f05-acb4b17666b9'
keywords: ["address books", "Windows Address Book (WAB),identities", "WAB (Windows Address Book),identities", "Windows Address Book (WAB),multi-user profiles", "WAB (Windows Address Book),multi-user profiles", "Windows Address Book (WAB),multi-identity profiles", "WAB (Windows Address Book),multi-identity profiles", "Windows Address Book (WAB),folders", "WAB (Windows Address Book),folders", "WAB API", "Windows Address Book (WAB),Root Table", "WAB (Windows Address Book),Root Table", "Windows Address Book (WAB),enhancements", "WAB (Windows Address Book),enhancements", "Windows Address Book (WAB),what's new", "WAB (Windows Address Book),what's new", "Windows Address Book (WAB),new features", "WAB (Windows Address Book),new features"]
---

# WAB and Multi-User/Multi-Identity Profiles

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

Beginning with version 5.0, the WAB provides support for multiple people who use the same logon name and password in the WAB. This support is provided based on "identities," which are managed by the separate Identity Manager component. Users who have the Identity Manager on their system and who choose to create one or more identities can use the Identity-related features in the WAB.

Typically, users employ identities to create and preserve their personal settings separate from other users. Within the scope of the WAB, identity-users (henceforth referred to as "identities" and is used interchangeably with the term "users") create and maintain their Address Book and contact information separate from other identities. In the typical case, in which multiple identities share a logon name and password, we can assume that the corresponding users share common contact information. An example of this would be a family with several members, each having a separate identity.

The following topics are discussed in this document.

-   [Multi-user Implementation](#multi-user-implementation)
-   [Folders](#folders)
-   [API Behavior](#api-behavior)
-   [Root Contents Table](#root-contents-table)
-   [Enhancements to API functionality](#enhancements-to-api-functionality)

## Multi-user Implementation

When working with multiple users, most applications segregate each user's data into separate data files. Because this requires the creation of a separate Address Book for each user, data sharing between users is eliminated and users are required to create and maintain multiple copies of any common information.

The WAB instead maintains a single store location for all identities within a Windows logon name and password. As in previous implementations of the WAB, there is a single .wab file per Windows logon name. Each identity, however, can create a "view" into the WAB that consists of all or a subset of the data in the WAB.

Because all the data resides in the same common .wab file, there is no implemented or implied privacy for contact information in the WAB. Any user can view any other user's contacts. Implementing a per-identity based privacy solution is beyond the scope of the WAB at present. The emphasis of the current implementation is to promote data-sharing between users. For home and family users—the majority audience for the WAB—sharing contact data between identities can be useful and desirable.

The single-file approach also allows for backward compatibility between the new WAB and older versions of WAB, and for older clients using older versions of the WAB. The .wab file format in WAB5 is identical to the .wab format used in Windows Internet Explorer 4.0x WAB. Users can safely go back and forth between WAB4 and WAB5 without losing any relevant data. Therefore, clients written for WAB4 and beyond can work safely with WAB5.

Since the identity functionality is closely dependent on the identity manager, unavailability of the identity manager forces the WAB to work in a single-user, identity non-aware mode. Multiple identity support is also not available currently when the WAB has been set to share its data store with Microsoft Outlook.

## Folders

For WAB 5.0 and later, users can create folders to organize their data.

Each identity starts with a default main folder and can then have one or more sub-folders as part of a profile. An identity can be used to create personal folders, in which case other identities by default do not see these folders . An identity can also create shared folders. These folders are part of every identity's "view" into the WAB. If a user wanted to maintain a single common set of contacts between identities, these contacts could be placed in a shared location. If a user had contacts other users did not want to see, these contacts could be placed in a personal folder.

When a user creates a folder, the WAB creates an [IABContainer : IMAPIContainer](d495fd99-2d3a-44ef-9415-34c7c0272f12) object. Thus, a user's profile consists of one or more containers. Applications can treat each container individually or can access multiple container contents simultaneously.

## API Behavior

Support for multiple identities has been added to the WAB while fully preserving backward compatibility with any application shipped with a version of the WAB predating Microsoft Internet Explorer 5. Old applications continue to work as before with the new WAB. With new applications, users can choose either to take advantage of the WAB's multiple-user support capability or to continue in a single-user mode.

To take advantage of multiple-user support, an application calls [**WABOpen**](-wab-wabopen.md) and sets the **WAB\_ENABLE\_PROFILES** flag in the **ulFlags** member of the [**WAB\_PARAM**](-wab-wab-param.md) structure that is passed into **WABOpen**.

The exact behavior of the WAB depends on a combination of the following things:

1.  Whether the Identity Manager exists on the system;
2.  Whether identities have ever been configured for the particular file;
3.  Whether the current application uses the WAB to enhance identity-dependent behavior.

The behavior of the WAB is summarized in the table below. The following definitions apply:

-   "Without identities configured" means that the Identity Manager was never installed and the .wab file has no identity-specific information.
-   "Identities with identity support" means that the Identity Manager has been installed, the user has employed identities, and the current application has requested this support by passing in **WAB\_ENABLE\_PROFILES**.
-   "Identities without identity support" means that the identity information exists and has been used by some applications, but the current application ignores identities by not passing in the **WAB\_ENABLE\_PROFILES** flag, or the current application is an "old" application that does not support identities.



|                                                                              | Without identities configured                                                                                      | Identities with identity support                                                                                                                                                                                                                           | Identities without identity support                                                                                                                                                          |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WAB Session                                                                  | No multiple-users functionality. Everything is based on a single user.                                             | WAB checks with Identity Manager to see who the current user is.                                                                                                                                                                                           | WAB does not know who the current user is.                                                                                                                                                   |
| Main WAB UI                                                                  | User can create top level folders. These folders are not represented programmatically as separate containers.      | A top level "Shared Contacts" folder exists and is common to all users. Each identity has a personal top-level folder not shared with other users. User can create one or more subfolders under the personal or shared top-level folder.                   | All folders are shown in the UI for all users because the WAB cannot tell who the current user is.                                                                                           |
| RootContentsTable                                                            | Consists of a single WAB container followed by configured Lightweight Directory Access Protocol (LDAP) containers. | Consists of a set of WAB containers. There is a separate container for each of the user's personal folders and a separate container for each shared folder, followed by LDAP containers.                                                                   | Consists of all containers corresponding to every folder in the WAB, followed by LDAP containers.                                                                                            |
| [**GetPAB**](-wab-iaddrbook-getpab.md)                                      | Returns the EntryID of the default WAB container. A single container represents the entire WAB.                    | Returns the EntryID of the default folder corresponding to the current identity. If an application manipulates data in this container, the data go directly into the current identity's default folder location.                                           | Returns the EntryID of the top level "Shared Contacts" folder. The WAB does not know who is using it, so the data go to a common place where all identities will be able to see it.          |
| [**GetContentsTable**](-wab-iabcontainer-getcontentstable.md)               | Returns list of all the WAB contents.                                                                              | Returns a list of contents corresponding to the current container only. An application can pass the flag **WAB\_PROFILE\_CONTENTS** to override this behavior and get a complete set of contents for all the personal and shared data of the current user. | Returns a list of all the WAB contents.                                                                                                                                                      |
| [**ResolveName**](-wab-iaddrbook-resolvename.md)                            | Resolves names first against the complete WAB and then the LDAP contents.                                          | Resolves names against the current user's set of folders, the shared folders, and finally the LDAP contents.                                                                                                                                               | Resolves names against the full WAB, followed by LDAP.                                                                                                                                       |
| LDAP Configuration                                                           | Consists of a single list of LDAP accounts                                                                         | Consists of a separate set of LDAP accounts for each identity. Accounts used for name resolution, shown in either the Root Contents Table or in the Find People dialog box, are all based on the current identity.                                         | The list of accounts that are used or displayed corresponds to the set of LDAP accounts for the default identity. The default identity is designated through the Identity Manager component. |
| [**GetMe**](-wab-iwabobject-getme.md)[**SetMe**](-wab-iwabobject-setme.md) | Acts upon one ME entry per WAB                                                                                     | Manipulates a per-identity ME entry. Each identity can specify its own ME.                                                                                                                                                                                 | Returns/Sets ME entry for the default identity.                                                                                                                                              |



 

## Root Contents Table

A client can enumerate all the containers within the WAB by obtaining a Root Table. The Root Table is a MAPITABLE that contains a list of all the containers within the WAB. The Root object can be obtained by calling [**OpenEntry**](-wab-iaddrbook-openentry.md) with a **NULL** EntryID. The client then calls [**GetContentsTable**](-wab-iabcontainer-getcontentstable.md) on the Root Object to obtain the Root Table.

In older versions of the WAB, the first entry in the root table represented the default WAB container, which contained all the contents in the address book. Any additional containers represented LDAP Directory Services specified by the user. In cases for which the WAB store was set to share data with Outlook, the first container represents the "Contacts" folder in the Outlook store, followed by containers representing additional Outlook Contact Folders, followed by any specified LDAP Directory Services.

In the new WAB, a profile-independent session behaves like an old WAB in that a single container (the default WAB Container) represents the complete address book followed by LDAP containers. However, if the client has specified profile-aware functionality, the first container in the table represents the current user's main folder, followed by other personal folders, followed by the shared folders, followed by any specified LDAP Directory Services.

Note that the default WAB container is the same as the container that is directly accessed through the [**GetPAB**](-wab-iaddrbook-getpab.md) method.

If the client wishes to enumerate only containers pertinent to the local address book and ignore LDAP containers, the client can specify the new flag, **WAB\_LOCAL\_CONTAINERS**, when calling [**GetContentsTable**](-wab-iabcontainer-getcontentstable.md) on the Root Object. The resulting Root Table will not contain any LDAP containers.

## Enhancements to API functionality

The following changes have been made to allow profile-enabled access to the WAB Data.

-   The [**IABContainer**](-wab-iabcontainer.md) interface works with all folder containers, instead of working only with the default WAB container.
-   [**GetPAB**](-wab-iaddrbook-getpab.md) returns the EntryID of the default WAB container. For a WAB that is identity-aware, this container corresponds to the current user's default folder. For identity-aware applications running in non-identity mode, this container corresponds to the "Shared Contacts" folder. For the non-identity WAB, this container corresponds to the entire WAB.
-   When calling [**NewEntry**](-wab-iaddrbook-newentry.md), the caller can specify a container EntryID. The new entry will be created in that particular folder or container.
-   If you call [**ResolveName**](-wab-iaddrbook-resolvename.md) with profile support turned off, the name resolution process works as before. Calling **ResolveName** with profiles turned on causes the name resolution to search containers linked to the current profile first. If no matches are found in the profile's container list, the name resolution process searches the entire address book, followed by appropriate LDAP servers.
-   [**CreateEntry**](-wab-iabcontainer-createentry.md) creates the new entry in the folder represented by the current Container.
-   [**ResolveNames**](-wab-iabcontainer-resolvenames.md) performs name resolution only within the current container. The given name is matched only with the contacts that belong to the current folder-container. When calling **ResolveNames** on the default WAB container, there may be occasions when a profile-enabled client application will be required to resolve the name against the contents of the entire WAB, not just against the contacts belonging to the default WAB container (and show up in the "Contacts" folder). In this case, the client can specify a **WAB\_IGNORE\_PROFILES** flag, and the resolution will span the entire address book. This flag works only with the default WAB container.
-   [**DeleteEntries**](-wab-iabcontainer-deleteentries.md) deletes the entry from the current container.
-   [**GetContentsTable**](-wab-iabcontainer-getcontentstable.md) gets a contents table containing only the contents of the current folder-container. It is sometimes useful to the profile-enabled client to obtain a complete list of contents associated with a particular profile in a single contents-table, instead of having to call **GetContentsTable** on each table separately and then collate the results. To obtain this list, call **GetContentsTable** on the default WAB Container and specify the flag **WAB\_PROFILE\_CONTENTS**. The resulting contents-table will contain all the contacts associated with the profile.

 

 




