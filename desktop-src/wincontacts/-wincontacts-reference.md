---
title: Windows Contacts Reference
description: New applications should not use this set of interfaces.
ms.assetid: f275efa5-4741-41ac-848e-5c3259c4b3ea
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Contacts Reference

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

The following topics provide reference information about the Windows Contacts  API, using the C++ programming language and Component Object Model (COM):

### Interfaces



|                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IContact**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontact)Do not use. Defines methods for reading and writing properties for a single contact. <br/>                                                                                                                                                                                                                                  |
| [**IContactCollection**](/previous-versions/windows/desktop/api/Icontact/nn-icontact-icontactcollection)Do not use. Enumerates the contacts known by the [**IContactManager**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontactmanager). <br/>                                                                                                                                                                                         |
| [**IContactManager**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontactmanager)Do not use. Used for retrieving a contact, based on a contact ID string. <br/>                                                                                                                                                                                                                                |
| [**IContactProperties**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontactproperties)Do not use. Used to retrieve, set, create, and remove properties on an [**IContact**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontact). Property names and extension mechanisms are described in icontactproperties.h. <br/>                                                                                                  |
| [**IContactPropertyCollection**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontactpropertycollection)Do not use. Used to filter contact data, based on a label or property set. Enumerates contact properties exposed with an [**IContactProperties**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontactproperties) object. For each property, the name, type, version, and modification date can be retrieved.<br/> |



 

### Objects



|                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Contact**](-wincontacts-contact.md)Do not use. The [**Contact**](-wincontacts-contact.md) object implements the [**IContact**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontact) interface. It represents reading and writing properties for a single contact. <br/>                                               |
| [**ContactManager**](-wincontacts-contactmanager.md)Do not use. The [**ContactManager**](-wincontacts-contactmanager.md) object implements the [**IContactManager**](/previous-versions/windows/desktop/api/icontact/nn-icontact-icontactmanager) interface. It represents interactions with contacts that have contact ID strings. <br/> |



 

 

 





