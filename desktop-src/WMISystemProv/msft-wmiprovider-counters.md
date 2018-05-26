---
title: Msft\_WmiProvider\_Counters class
description: Exposes approximate counts of WMI internal operation calls across all providers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b0eee184-787a-4f82-a67c-62c3cbb2e11a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msft_WmiProvider_Counters class
- Msft_WmiProvider_Counters class, described
topic_type:
- apiref
api_name:
- Msft_WmiProvider_Counters
- Msft_WmiProvider_Counters.ProviderOperation_GetObjectAsync
- Msft_WmiProvider_Counters.ProviderOperation_PutClassAsync
- Msft_WmiProvider_Counters.ProviderOperation_DeleteClassAsync
- Msft_WmiProvider_Counters.ProviderOperation_CreateClassEnumAsync
- Msft_WmiProvider_Counters.ProviderOperation_PutInstanceAsync
- Msft_WmiProvider_Counters.ProviderOperation_DeleteInstanceAsync
- Msft_WmiProvider_Counters.ProviderOperation_CreateInstanceEnumAsync
- Msft_WmiProvider_Counters.ProviderOperation_ExecQueryAsync
- Msft_WmiProvider_Counters.ProviderOperation_ExecMethodAsync
- Msft_WmiProvider_Counters.ProviderOperation_QueryInstances
- Msft_WmiProvider_Counters.ProviderOperation_CreateRefresher
- Msft_WmiProvider_Counters.ProviderOperation_CreateRefreshableObject
- Msft_WmiProvider_Counters.ProviderOperation_StopRefreshing
- Msft_WmiProvider_Counters.ProviderOperation_CreateRefreshableEnum
- Msft_WmiProvider_Counters.ProviderOperation_GetObjects
- Msft_WmiProvider_Counters.ProviderOperation_GetProperty
- Msft_WmiProvider_Counters.ProviderOperation_PutProperty
- Msft_WmiProvider_Counters.ProviderOperation_ProvideEvents
- Msft_WmiProvider_Counters.ProviderOperation_NewQuery
- Msft_WmiProvider_Counters.ProviderOperation_CancelQuery
- Msft_WmiProvider_Counters.ProviderOperation_AccessCheck
- Msft_WmiProvider_Counters.ProviderOperation_SetRegistrationObject
- Msft_WmiProvider_Counters.ProviderOperation_FindConsumer
- Msft_WmiProvider_Counters.ProviderOperation_ValidateSubscription
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_WmiProvider\_Counters class

The **MSFT\_WmiProvider\_Counters** singleton [troubleshooting class](https://msdn.microsoft.com/library/aa394604) exposes approximate counts of WMI internal operation calls across all providers. An example of an internal operation call is creating an instance enumeration asynchronously.

## Syntax

``` syntax
[Dynamic, Provider("Msft_ProviderSubSystem"), Singleton, AMENDMENT]
class Msft_WmiProvider_Counters
{
  Uint64 ProviderOperation_GetObjectAsync;
  Uint64 ProviderOperation_PutClassAsync;
  Uint64 ProviderOperation_DeleteClassAsync;
  Uint64 ProviderOperation_CreateClassEnumAsync;
  Uint64 ProviderOperation_PutInstanceAsync;
  Uint64 ProviderOperation_DeleteInstanceAsync;
  Uint64 ProviderOperation_CreateInstanceEnumAsync;
  Uint64 ProviderOperation_ExecQueryAsync;
  Uint64 ProviderOperation_ExecMethodAsync;
  Uint64 ProviderOperation_QueryInstances;
  Uint64 ProviderOperation_CreateRefresher;
  Uint64 ProviderOperation_CreateRefreshableObject;
  Uint64 ProviderOperation_StopRefreshing;
  Uint64 ProviderOperation_CreateRefreshableEnum;
  Uint64 ProviderOperation_GetObjects;
  Uint64 ProviderOperation_GetProperty;
  Uint64 ProviderOperation_PutProperty;
  Uint64 ProviderOperation_ProvideEvents;
  Uint64 ProviderOperation_NewQuery;
  Uint64 ProviderOperation_CancelQuery;
  Uint64 ProviderOperation_AccessCheck;
  Uint64 ProviderOperation_SetRegistrationObject;
  Uint64 ProviderOperation_FindConsumer;
  Uint64 ProviderOperation_ValidateSubscription;
};
```

## Members

The **Msft\_WmiProvider\_Counters** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_WmiProvider\_Counters** class has these properties.

<dl> <dt>

**ProviderOperation\_AccessCheck**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemEventProviderSecurity::AccessCheck**](https://msdn.microsoft.com/library/aa391743).

</dd> <dt>

**ProviderOperation\_CancelQuery**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemEventProviderQuerySink::CancelQuery**](https://msdn.microsoft.com/library/aa391738).

</dd> <dt>

**ProviderOperation\_CreateClassEnumAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::CreateClassEnumAsync**](https://msdn.microsoft.com/library/aa392096).

</dd> <dt>

**ProviderOperation\_CreateInstanceEnumAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098).

</dd> <dt>

**ProviderOperation\_CreateRefreshableEnum**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemHiPerfProvider::CreateRefreshableEnum**](https://msdn.microsoft.com/library/aa391760).

</dd> <dt>

**ProviderOperation\_CreateRefreshableObject**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemHiPerfProvider::CreateRefreshableObject**](https://msdn.microsoft.com/library/aa391762).

</dd> <dt>

**ProviderOperation\_CreateRefresher**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemHiPerfProvider::CreateRefresher**](https://msdn.microsoft.com/library/aa391763).

</dd> <dt>

**ProviderOperation\_DeleteClassAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::DeleteClassAsync**](https://msdn.microsoft.com/library/aa392100).

</dd> <dt>

**ProviderOperation\_DeleteInstanceAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102).

</dd> <dt>

**ProviderOperation\_ExecMethodAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104).

</dd> <dt>

**ProviderOperation\_ExecQueryAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108).

</dd> <dt>

**ProviderOperation\_FindConsumer**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemEventConsumerProvider::FindConsumer**](https://msdn.microsoft.com/library/aa391491).

</dd> <dt>

**ProviderOperation\_GetObjectAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::GetObjectAsync**](https://msdn.microsoft.com/library/aa392110).

</dd> <dt>

**ProviderOperation\_GetObjects**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemHiPerfProvider::GetObjects**](https://msdn.microsoft.com/library/aa391764).

</dd> <dt>

**ProviderOperation\_GetProperty**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemPropertyProvider::GetProperty**](https://msdn.microsoft.com/library/aa391848).

</dd> <dt>

**ProviderOperation\_NewQuery**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemEventProviderQuerySink::NewQuery**](https://msdn.microsoft.com/library/aa391739).

</dd> <dt>

**ProviderOperation\_ProvideEvents**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemEventProvider::ProvideEvents**](https://msdn.microsoft.com/library/aa391744).

</dd> <dt>

**ProviderOperation\_PutClassAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::PutClassAsync**](https://msdn.microsoft.com/library/aa392114).

</dd> <dt>

**ProviderOperation\_PutInstanceAsync**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemServices::PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116).

</dd> <dt>

**ProviderOperation\_PutProperty**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemPropertyProvider::PutProperty**](https://msdn.microsoft.com/library/aa391849).

</dd> <dt>

**ProviderOperation\_QueryInstances**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemHiPerfProvider::QueryInstances**](https://msdn.microsoft.com/library/aa391765).

</dd> <dt>

**ProviderOperation\_SetRegistrationObject**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ProviderOperation\_SetRegistrationObject is not implemented.

</dd> <dt>

**ProviderOperation\_StopRefreshing**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to [**IWbemHiPerfProvider::StopRefreshing**](https://msdn.microsoft.com/library/aa391766).

</dd> <dt>

**ProviderOperation\_ValidateSubscription**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of calls to **IWbemEventConsumerProviderEx::ValidateSubscription**.

</dd> </dl>

## Examples

The following VBScript code example shows how to use **MSFT\_WmiProvider\_Counters** to obtain data about usage of asynchronous calls.


```VB
On Error Resume Next 
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" _
    & strComputer & "\root\CIMV2") 
Set colItems = objWMIService.ExecQuery( _
    "SELECT * FROM Msft_WmiProvider_Counters",,48) 
For Each objItem in colItems 

    Wscript.Echo "Msft_WmiProvider_Counters instance"
    Wscript.Echo _
        "ProviderOperation_CreateClassEnumAsync: " _
             & objItem.ProviderOperation_CreateClassEnumAsync  _
             & VBNewLine _ 
             &amp;"ProviderOperation_CreateInstanceEnumAsync: " _
             & objItem.ProviderOperation_CreateInstanceEnumAsync _
         & VBNewLine & "ProviderOperation_DeleteClassAsync: " _
             & objItem.ProviderOperation_DeleteClassAsync _
         & VBNewLine & "ProviderOperation_DeleteInstanceAsync: " _
             & objItem.ProviderOperation_DeleteInstanceAsync _
         & VBNewLine & "ProviderOperation_ExecMethodAsync: " _
             & objItem.ProviderOperation_ExecMethodAsync _
         & VBNewLine & "ProviderOperation_ExecQueryAsync: " _
             & objItem.ProviderOperation_ExecQueryAsync _
         & VBNewLine & "ProviderOperation_GetObjectAsync: " _
             & objItem.ProviderOperation_GetObjectAsync _
         & VBNewLine & "ProviderOperation_PutClassAsync: " _
             & objItem.ProviderOperation_PutClassAsync  _
         & VBNewLine & "ProviderOperation_PutInstanceAsync: " _
             & objItem.ProviderOperation_PutInstanceAsync
Next
```



## Requirements



|                      |                                                                                         |
|----------------------|-----------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\CIMV2<br/>                                                                  |
| MOF<br/>       | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>       | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[WMI Troubleshooting Classes](https://msdn.microsoft.com/library/aa394604)
</dt> </dl>

 

 





