---
title: Windows Contacts Reference
description: New applications should not use this set of interfaces.
ms.assetid: f275efa5-4741-41ac-848e-5c3259c4b3ea
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Contacts Reference

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

The following topics provide reference information about the Windows Contacts  API, using the C++ programming language and Component Object Model (COM):

### Interfaces



|                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IContact**](/windows/previous-versions/icontact/nn-icontact-icontact?branch=master)Do not use. Defines methods for reading and writing properties for a single contact. <br/>                                                                                                                                                                                                                                  |
| [**IContactCollection**](/windows/previous-versions/Icontact/nn-icontact-icontactcollection?branch=master)Do not use. Enumerates the contacts known by the [**IContactManager**](/windows/previous-versions/icontact/nn-icontact-icontactmanager?branch=master). <br/>                                                                                                                                                                                         |
| [**IContactManager**](/windows/previous-versions/icontact/nn-icontact-icontactmanager?branch=master)Do not use. Used for retrieving a contact, based on a contact ID string. <br/>                                                                                                                                                                                                                                |
| [**IContactProperties**](/windows/previous-versions/icontact/nn-icontact-icontactproperties?branch=master)Do not use. Used to retrieve, set, create, and remove properties on an [**IContact**](/windows/previous-versions/icontact/nn-icontact-icontact?branch=master). Property names and extension mechanisms are described in icontactproperties.h. <br/>                                                                                                  |
| [**IContactPropertyCollection**](/windows/previous-versions/icontact/nn-icontact-icontactpropertycollection?branch=master)Do not use. Used to filter contact data, based on a label or property set. Enumerates contact properties exposed with an [**IContactProperties**](/windows/previous-versions/icontact/nn-icontact-icontactproperties?branch=master) object. For each property, the name, type, version, and modification date can be retrieved.<br/> |



 

### Objects



|                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Contact**](-wincontacts-contact.md)Do not use. The [**Contact**](-wincontacts-contact.md) object implements the [**IContact**](/windows/previous-versions/icontact/nn-icontact-icontact?branch=master) interface. It represents reading and writing properties for a single contact. <br/>                                               |
| [**ContactManager**](-wincontacts-contactmanager.md)Do not use. The [**ContactManager**](-wincontacts-contactmanager.md) object implements the [**IContactManager**](/windows/previous-versions/icontact/nn-icontact-icontactmanager?branch=master) interface. It represents interactions with contacts that have contact ID strings. <br/> |



 

 

 





