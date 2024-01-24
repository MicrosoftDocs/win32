---
description: Adds a new enumerator to the SWbemRefresher object. This enumerator is for all the instances of the class that is specified in the strClass parameter.
ms.assetid: 0fa22a47-4050-43ae-aad3-3a8ebbf5e9b2
ms.tgt_platform: multiple
title: SWbemRefresher.AddEnum method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefresher.AddEnum
- ISWbemRefresher.AddEnum
- ISWbemRefresher.AddEnum
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefresher.AddEnum method

The **SWbemRefresher.AddEnum** method adds a new enumerator to the [**SWbemRefresher**](swbemrefresher.md) object. This enumerator is for all the instances of the class that is specified in the *strClass* parameter.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objRefreshEnum = .AddEnum( _
  ByVal objWbemService, _
  ByVal strClass, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedvalueSet ] _
)
```



## Parameters

<dl> <dt>

*objWbemService* 
</dt> <dd>

Required. An [**SWbemServices**](swbemservices.md) object that represents a connection to the namespace in which the object that is being added to the refresher resides.

</dd> <dt>

*strClass* 
</dt> <dd>

Required. String that contains the class that is being added to the refresher. This class is used as an enumerator of the instances of the class. The [**Index**](swbemrefreshableitem-index.md) property of the returned [**SWbemRefreshableItem**](swbemrefreshableitem.md) represents the index of the enumerator in the refresher collection.

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

String that contains the object path of the object for which the method is executed.

</dd> <dt>

*objWbemNamedvalueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that services the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If the call is successful, an [**SWbemRefreshableItem**](swbemrefreshableitem.md) object that contains an enumerator for all the instances for the specified class is returned.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemRefresher<br/>                                                        |
| IID<br/>                      | IID\_ISWbemRefresher<br/>                                                         |



## See also

<dl> <dt>

[**SWbemRefresher**](swbemrefresher.md)
</dt> </dl>

 

 




