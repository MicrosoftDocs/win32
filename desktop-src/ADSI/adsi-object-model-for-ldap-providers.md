---
title: ADSI Object Model for LDAP Providers
description: An illustration that shows ADSI objects used for the LDAP provider and interfaces used to access these objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '109fd42e-201e-4b84-a213-2695d81f005b'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# ADSI Object Model for LDAP Providers

The following illustration shows ADSI objects used for the LDAP provider and interfaces used to access these objects.

![object model for ldap provider](images/adsiobjmodldap-gif-1.png)

| Object                        | Interface                                                                                                                                                                                                                                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class<br/>              | [**IADs**](iads.md), [**IADsClass**](iadsclass.md)                                                                                                                                                                                                                                           |
| Property<br/>           | [**IADs**](iads.md), [**IADsProperty**](iadsproperty.md)                                                                                                                                                                                                                                     |
| GenObject<br/>          | [**IADs**](iads.md), [**IADsContainer**](iadscontainer.md), [**IADsDeleteOps**](iadsdeleteops.md), [**IADsObjectOptions**](iadsobjectoptions.md), [**IADsPropertyList**](iadspropertylist.md), [**IDirectoryObject**](iadsopendsobject.md), [**IDirectorySearch**](idirectorysearch.md) |
| Namespace<br/>          | [**IADs**](iads.md), [**IADsContainer**](iadscontainer.md), [**IADsOpenDSObject**](iadsopendsobject.md)                                                                                                                                                                                     |
| RootDSE<br/>            | [**IADs**](iads.md), [**IADsPropertyList**](iadspropertylist.md)                                                                                                                                                                                                                             |
| Pathname<br/>           | [**IADs**](iads.md), [**IADsPathname**](iadspathname.md)                                                                                                                                                                                                                                     |
| Schema<br/>             | [**IADs**](iads.md), [**IADsContainer**](iadscontainer.md)                                                                                                                                                                                                                                   |
| Syntax<br/>             | [**IADs**](iads.md), [**IADsSyntax**](iadssyntax.md)                                                                                                                                                                                                                                         |
| Organization<br/>       | [**IADsO**](iadso.md)                                                                                                                                                                                                                                                                         |
| OrganizationalUnit<br/> | [**IADsOU**](iadsou.md)                                                                                                                                                                                                                                                                       |
| GroupCollection<br/>    | [**IADsMembers**](iadsmembers.md)                                                                                                                                                                                                                                                             |
| Group<br/>              | [**IADsGroup**](iadsgroup.md)                                                                                                                                                                                                                                                                 |
| UserCollection<br/>     | [**IADsMembers**](iadsmembers.md)                                                                                                                                                                                                                                                             |
| User<br/>               | [**IADsUser**](iadsuser.md)                                                                                                                                                                                                                                                                   |
| Locality<br/>           | [**IADsLocality**](iadslocality.md)                                                                                                                                                                                                                                                           |
| NameTranslate<br/>      | [**IADsNameTranslate**](iadsnametranslate.md)                                                                                                                                                                                                                                                 |
| PrintQueue<br/>         | [**IADsPrintQueue**](iadsprintqueue.md), [**IADsPrintQueueOperations**](iadsprintqueueoperations.md)                                                                                                                                                                                         |



 

 

 





