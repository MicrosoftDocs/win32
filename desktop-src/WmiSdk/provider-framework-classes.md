---
description: WMI C++ classes that are part of the WMI Provider Framework are now considered in final state.
ms.assetid: 062a7724-0589-4e9d-af7a-39fd9c08e40b
ms.tgt_platform: multiple
title: Provider Framework Classes
ms.topic: article
ms.date: 05/31/2018
---

# Provider Framework Classes

\[WMI C++ classes that are part of the WMI Provider Framework are are now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The provider framework implements the following classes.



| Framework class                                | Description                                                                                                                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CFrameworkQuery**](/windows/desktop/api/FrQuery/nl-frquery-cframeworkquery)     | Contains methods for query processing.                                                                                                                                                                              |
| [**CInstance**](/windows/desktop/api/Instance/nl-instance-cinstance)                 | Contains methods to set and retrieve properties and is an encapsulation of the [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject) interface. Implementer should not have to access **IWbemClassObject** methods directly. |
| [**CThreadBase**](/windows/desktop/api/ThrdBase/nl-thrdbase-cthreadbase)             | A base class that supplies the internal thread safety mechanisms for the WMI Provider Framework.                                                                                                                    |
| [**CWbemGlueFactory**](/windows/desktop/api/WbemGlue/nl-wbemglue-cwbemgluefactory)   | Part of the WMI Provider Framework. The Provider Framework implements methods of this interface internally to create new instances of classes for the provider.                                                     |
| [**CWbemProviderGlue**](/windows/desktop/api/WbemGlue/nl-wbemglue-cwbemproviderglue) | Implements [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) and methods that control the loading and unloading of the framework provider.                                                                             |
| [**Provider**](/windows/desktop/api/Provider/nl-provider-provider)                   | Contains helper functions and provides default implementations of the methods of [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices).                                                                                            |



 

Note that many of the framework methods use [**CHString**](chstring.md) parameters. **CHString** supports many of the same methods and properties as the Microsoft Foundation Classes (MFC), but without the overhead of MFC. For more information about **CHString**, see **CHString Class Reference**.

 

 
