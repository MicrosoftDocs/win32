---
Description: If you are using the COM API for WMI to retrieve or store localized class information, specify the locale in the strLocale parameter to the IWbemLocatorConnectServer interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 940a7bd9-c2ea-4deb-b5d8-207a0ce7a616
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Retrieving Amended Classes Using the COM API for WMI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Retrieving Amended Classes Using the COM API for WMI

If you are using the COM API for WMI to retrieve or store localized class information, specify the locale in the *strLocale* parameter to the [**IWbemLocator::ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master) interface. When reading or writing amended classes, indicate that you want to use localized class definitions by specifying WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS as a flag for the *iFlags* parameter.

The following table lists the synchronous and asynchronous versions of the methods that use the WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS flag.



| Synchronous Method                                                            | Asynchronous Method                                                                     |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**IWbemServices::CreateClassEnum**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-createclassenum?branch=master)       | [**IWbemServices::CreateClassEnumAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync?branch=master)       |
| [**IWbemServices::CreateInstanceEnum**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-createinstanceenum?branch=master) | [**IWbemServices::CreateInstanceEnumAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync?branch=master) |
| [**IWbemServices::ExecQuery**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execquery?branch=master)                   | [**IWbemServices::ExecQueryAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execqueryasync?branch=master)                   |
| [**IWbemServices::GetObject**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobject?branch=master)                   | [**IWbemServices::GetObjectAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobjectasync?branch=master)                   |
| [**IWbemServices::PutClass**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putclass?branch=master)                     | [**IWbemServices::PutClassAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putclassasync?branch=master)                     |
| [**IWbemServices::PutInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstance?branch=master)               | [**IWbemServices::PutInstanceAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync?branch=master)               |



 

 

 



