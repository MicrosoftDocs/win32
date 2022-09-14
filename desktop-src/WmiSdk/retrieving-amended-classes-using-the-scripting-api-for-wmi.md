---
description: If you are using the Scripting API for WMI to retrieve or store localized class information, specify the locale as part of a moniker.
ms.assetid: 3c64047d-ce3a-4180-8f71-0e66c2e61627
ms.tgt_platform: multiple
title: Retrieving Amended Classes Using the Scripting API for WMI
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Retrieving Amended Classes Using the Scripting API for WMI

If you are using the Scripting API for WMI to retrieve or store localized class information, specify the locale as part of a moniker. Or, you can supply the locale name in the *strLocale* parameter to the [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) method. When reading or writing amended classes, indicate that you want to use localized class definitions by specifying [wbemFlagUseAmendedQualifiers](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemflagenum) as a flag for the *iFlags* parameter of the method you call. For PowerShell, you can use the *-locale* parameter on [Get-WmiObject](/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1&preserve-view=true) to specify the locale.

The following code example shows how to retrieve a localized class by using a WMI scripting moniker or the -locale parameter.


```VB
Set objwbemobject = GetObject("winmgmts:[locale=ms_409]!root/test:myclass")
```


```PowerShell

Get-WmiObject myclass -Namespace &quot;root\test&quot; -Locale &quot;ms_409&quot;
```





The following code example shows how to set the locale parameter and use the [wbemFlagUseAmendedQualifiers](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemflagenum) flag.


```VB
Set Locator = CreateObject("WbemScripting.SWbemLocator")
Set service = Locator.ConnectServer(,"root\test", , , "ms_409")
Set objwbemobject = service.Get("myclass", wbemFlagUseAmendedQualifiers)
```



> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

The following table lists the methods that accept the [wbemFlagUseAmendedQualifiers](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemflagenum) flag.



| Synchronous Method                                                 | Asynchronous Method                                                          |
|--------------------------------------------------------------------|------------------------------------------------------------------------------|
| [**SWbemServices.SubclassesOf**](swbemservices-subclassesof.md)   | [**SWbemServices.SubclassesOfAsync**](swbemservices-subclassesofasync.md)   |
| [**SWbemObject.Subclasses\_**](swbemobject-subclasses-.md)        | [**SWbemObject.SubclassesAsync\_**](swbemobject-subclassesasync-.md)        |
| [**SWbemServices.InstancesOf**](swbemservices-instancesof.md)     | [**SWbemServices.InstancesOfAsync**](swbemservices-instancesofasync.md)     |
| [**SWbemObject.Instances\_**](swbemobject-instances-.md)          | [**SWbemObject.InstancesAsync\_**](swbemobject-instancesasync-.md)          |
| [**SWbemServices.ExecQuery**](swbemservices-execquery.md)         | [**SWbemServices.ExecQueryAsync**](swbemservices-execqueryasync.md)         |
| [**SWbemServices.Get**](swbemservices-get.md)                     | [**SWbemServices.GetAsync**](swbemservices-getasync.md)                     |
| [**SWbemObject.Put\_**](swbemobject-put-.md)                      | [**SWbemObject.PutAsync\_**](swbemobject-putasync-.md)                      |
| [**SWbemServices.ReferencesTo**](swbemservices-referencesto.md)   | [**SWbemServices.ReferencesToAsync**](swbemservices-referencestoasync.md)   |
| [**SWbemObject.References\_**](swbemobject-references-.md)        | [**SWbemObject.ReferencesAsync\_**](swbemobject-referencesasync-.md)        |
| [**SWbemServices.AssociatorsOf**](swbemservices-associatorsof.md) | [**SWbemServices.AssociatorsOfAsync**](swbemservices-associatorsofasync.md) |
| [**SWbemObject.Associators\_**](swbemobject-associators-.md)      | [**SWbemObject.AssociatorsAsync\_**](swbemobject-associatorsasync-.md)      |



 

 

 
