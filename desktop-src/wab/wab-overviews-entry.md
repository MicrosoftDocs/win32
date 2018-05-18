---
title: Windows Address Book Overviews and Tutorials
description: The following overview and tutorial articles outline techniques for programming an address book.
ms.assetid: '2d937e09-b62a-4745-87c2-5f3325f6126c'
keywords: ["Windows Address Book (WAB),backward compatibility", "WAB (Windows Address Book),backward compatibility", "Windows Address Book (WAB),Windows Contacts", "WAB (Windows Address Book),Windows Contacts", "Windows Contacts", "Windows Contacts", "address books"]
---

# Windows Address Book Overviews and Tutorials

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

The following overview and tutorial articles outline techniques for programming an address book.

### Overview/Tutorial



| Topic                                                                                  | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Windows Address Book](-wab-overview.md)                                        | Windows provides an address book for storing contact information. The WAB is an application and service that enables users to keep track of people. The WAB has a local database and user interface for finding and editing information about people, and it can query network directory servers using Lightweight Directory Access Protocol (LDAP). Other applications can use the WAB. For example, Microsoft Outlook uses the WAB as its e-mail address book.<br/> |
| [Extending the WAB Property Sheets](-wab-extending-prop-sheets.md)                    | The WAB has an extensibility mechanism by which a client application can add its own property sheets to the WAB's predefined set of property sheets. This document describes how to extend the WAB Property Sheets for WAB contacts and groups.<br/>                                                                                                                                                                                                                  |
| [Extending the WAB Toolbar and Context Menu Actions](-wab-extending-context-menus.md) | Clients wishing to extend the WAB's set of "Actions" on contacts (such as "Send Mail") can do so by implementing the [IContextMenu Interface](_win32_IContextMenu) and the [**IWABExtInit**](-wab-iwabextinit.md) interfaces and then registering them with the WAB.<br/>                                                                                                                                                                                            |
| [Importing and Exporting Named Properties Through vCards](-wab-vcardprops.md)         | If the predefined MAPI schema is insufficient to meet the needs of a client application, that application typically extends the schema using named properties. In order to enable the exchange of data stored in named properties, the vCard conversion engine in the WAB can be extended to import and export named-property data through vCards.<br/>                                                                                                               |
| [UNICODE Support in WAB](-wab-unicode.md)                                             | Versions 5.0 and later of the WAB support UNICODE.<br/>                                                                                                                                                                                                                                                                                                                                                                                                               |
| [WAB and Multi-User/Multi-Identity Profiles](-wab-multiprofiles.md)                   | Beginning with version 5.0, the WAB provides support for multiple people who use the same logon name and password in the WAB.<br/>                                                                                                                                                                                                                                                                                                                                    |



 

 

 





