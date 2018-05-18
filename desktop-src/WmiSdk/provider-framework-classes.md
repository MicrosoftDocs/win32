---
Description: 'WMI C++ classes that are part of the WMI Provider Framework are now considered in final state.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '062a7724-0589-4e9d-af7a-39fd9c08e40b'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Provider Framework Classes
---

# Provider Framework Classes

\[WMI C++ classes that are part of the WMI Provider Framework are are now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The provider framework implements the following classes.



| Framework class                                | Description                                                                                                                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CFrameworkQuery**](cframeworkquery.md)     | Contains methods for query processing.                                                                                                                                                                              |
| [**CInstance**](cinstance.md)                 | Contains methods to set and retrieve properties and is an encapsulation of the [**IWbemClassObject**](iwbemclassobject.md) interface. Implementer should not have to access **IWbemClassObject** methods directly. |
| [**CThreadBase**](cthreadbase.md)             | A base class that supplies the internal thread safety mechanisms for the WMI Provider Framework.                                                                                                                    |
| [**CWbemGlueFactory**](cwbemgluefactory.md)   | Part of the WMI Provider Framework. The Provider Framework implements methods of this interface internally to create new instances of classes for the provider.                                                     |
| [**CWbemProviderGlue**](cwbemproviderglue.md) | Implements [**IWbemProviderInit**](iwbemproviderinit.md) and methods that control the loading and unloading of the framework provider.                                                                             |
| [**Provider**](provider.md)                   | Contains helper functions and provides default implementations of the methods of [**IWbemServices**](iwbemservices.md).                                                                                            |



 

Note that many of the framework methods use [**CHString**](chstring.md) parameters. **CHString** supports many of the same methods and properties as the Microsoft Foundation Classes (MFC), but without the overhead of MFC. For more information about **CHString**, see **CHString Class Reference**.

 

 



