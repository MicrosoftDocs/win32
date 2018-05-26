---
Description: WMI C++ classes that are part of the WMI Provider Framework are now considered in final state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 062a7724-0589-4e9d-af7a-39fd9c08e40b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Provider Framework Classes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Provider Framework Classes

\[WMI C++ classes that are part of the WMI Provider Framework are are now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The provider framework implements the following classes.



| Framework class                                | Description                                                                                                                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CFrameworkQuery**](/windows/win32/FrQuery/nl-frquery-cframeworkquery?branch=master)     | Contains methods for query processing.                                                                                                                                                                              |
| [**CInstance**](/windows/win32/Instance/nl-instance-cinstance?branch=master)                 | Contains methods to set and retrieve properties and is an encapsulation of the [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) interface. Implementer should not have to access **IWbemClassObject** methods directly. |
| [**CThreadBase**](/windows/win32/ThrdBase/nl-thrdbase-cthreadbase?branch=master)             | A base class that supplies the internal thread safety mechanisms for the WMI Provider Framework.                                                                                                                    |
| [**CWbemGlueFactory**](/windows/win32/WbemGlue/nl-wbemglue-cwbemgluefactory?branch=master)   | Part of the WMI Provider Framework. The Provider Framework implements methods of this interface internally to create new instances of classes for the provider.                                                     |
| [**CWbemProviderGlue**](/windows/win32/WbemGlue/nl-wbemglue-cwbemproviderglue?branch=master) | Implements [**IWbemProviderInit**](/windows/win32/Wbemprov/nn-wbemprov-iwbemproviderinit?branch=master) and methods that control the loading and unloading of the framework provider.                                                                             |
| [**Provider**](/windows/win32/Provider/nl-provider-provider?branch=master)                   | Contains helper functions and provides default implementations of the methods of [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master).                                                                                            |



 

Note that many of the framework methods use [**CHString**](chstring.md) parameters. **CHString** supports many of the same methods and properties as the Microsoft Foundation Classes (MFC), but without the overhead of MFC. For more information about **CHString**, see **CHString Class Reference**.

 

 



