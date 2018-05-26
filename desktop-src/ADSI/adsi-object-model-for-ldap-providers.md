---
title: ADSI Object Model for LDAP Providers
description: An illustration that shows ADSI objects used for the LDAP provider and interfaces used to access these objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 109fd42e-201e-4b84-a213-2695d81f005b
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Object Model for LDAP Providers

The following illustration shows ADSI objects used for the LDAP provider and interfaces used to access these objects.

![object model for ldap provider](images/adsiobjmodldap-gif-1.png)

| Object                        | Interface                                                                                                                                                                                                                                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class<br/>              | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsClass**](/windows/win32/Iads/nn-iads-iadsclass?branch=master)                                                                                                                                                                                                                                           |
| Property<br/>           | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsProperty**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master)                                                                                                                                                                                                                                     |
| GenObject<br/>          | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master), [**IADsDeleteOps**](/windows/win32/Iads/nn-iads-iadsdeleteops?branch=master), [**IADsObjectOptions**](/windows/win32/Iads/nn-iads-iadsobjectoptions?branch=master), [**IADsPropertyList**](/windows/win32/Iads/nn-iads-iadspropertylist?branch=master), [**IDirectoryObject**](/windows/win32/Iads/nn-iads-iadsopendsobject?branch=master), [**IDirectorySearch**](/windows/win32/Iads/nn-iads-idirectorysearch?branch=master) |
| Namespace<br/>          | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master), [**IADsOpenDSObject**](/windows/win32/Iads/nn-iads-iadsopendsobject?branch=master)                                                                                                                                                                                     |
| RootDSE<br/>            | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsPropertyList**](/windows/win32/Iads/nn-iads-iadspropertylist?branch=master)                                                                                                                                                                                                                             |
| Pathname<br/>           | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsPathname**](/windows/win32/Iads/nn-iads-iadspathname?branch=master)                                                                                                                                                                                                                                     |
| Schema<br/>             | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master)                                                                                                                                                                                                                                   |
| Syntax<br/>             | [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsSyntax**](/windows/win32/Iads/nn-iads-iadssyntax?branch=master)                                                                                                                                                                                                                                         |
| Organization<br/>       | [**IADsO**](/windows/win32/Iads/nn-iads-iadso?branch=master)                                                                                                                                                                                                                                                                         |
| OrganizationalUnit<br/> | [**IADsOU**](/windows/win32/Iads/nn-iads-iadsou?branch=master)                                                                                                                                                                                                                                                                       |
| GroupCollection<br/>    | [**IADsMembers**](/windows/win32/Iads/nn-iads-iadsmembers?branch=master)                                                                                                                                                                                                                                                             |
| Group<br/>              | [**IADsGroup**](/windows/win32/Iads/nn-iads-iadsgroup?branch=master)                                                                                                                                                                                                                                                                 |
| UserCollection<br/>     | [**IADsMembers**](/windows/win32/Iads/nn-iads-iadsmembers?branch=master)                                                                                                                                                                                                                                                             |
| User<br/>               | [**IADsUser**](/windows/win32/Iads/nn-iads-iadsuser?branch=master)                                                                                                                                                                                                                                                                   |
| Locality<br/>           | [**IADsLocality**](/windows/win32/Iads/nn-iads-iadslocality?branch=master)                                                                                                                                                                                                                                                           |
| NameTranslate<br/>      | [**IADsNameTranslate**](/windows/win32/Iads/nn-iads-iadsnametranslate?branch=master)                                                                                                                                                                                                                                                 |
| PrintQueue<br/>         | [**IADsPrintQueue**](/windows/win32/Iads/nn-iads-iadsprintqueue?branch=master), [**IADsPrintQueueOperations**](/windows/win32/Iads/nn-iads-iadsprintqueueoperations?branch=master)                                                                                                                                                                                         |



 

 

 





