---
title: ResourceLocator.AddOption method (WSManDisp.h)
description: Adds additional data required to process the request. For example, some WMI providers may require an IWbemContext or SWbemNamedValueSet object with provider-specific information.
ms.assetid: c85949fc-41e7-47eb-8aab-9b456490bc81
ms.tgt_platform: multiple
keywords:
- AddOption method Windows Remote Management
- AddOption method Windows Remote Management , ResourceLocator object
- ResourceLocator object Windows Remote Management , AddOption method
topic_type:
- apiref
api_name:
- ResourceLocator.AddOption
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ResourceLocator.AddOption method

Adds additional data required to process the request. For example, some WMI providers may require an [**IWbemContext**](/windows/desktop/api/wbemcli/nn-wbemcli-iwbemcontext) or [**SWbemNamedValueSet**](/windows/desktop/WmiSdk/swbemnamedvalueset) object with provider-specific information. You can provide a [**ResourceLocator**](resourcelocator.md) object instead of specifying a resource URI in [**Session**](session.md) object operations such as [**Session.Get**](session-get.md), [**Session.Put**](session-put.md), or [**Session.Enumerate**](session-enumerate.md).

## Syntax


```VB
ResourceLocator.AddOption( _
  ByVal OptionName, _
  ByVal OptionValue, _
  ByVal mustComply _
)
```



## Parameters

<dl> <dt>

*OptionName* \[in\]
</dt> <dd>

The name (key) of the optional data object.

</dd> <dt>

*OptionValue* \[in\]
</dt> <dd>

A value supplied for the optional data object.

</dd> <dt>

*mustComply* \[in\]
</dt> <dd>

A flag that indicates the option must be processed. The default is **False** (0).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

**IWSManResourceLocator::AddOption** is the corresponding C++ method.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**ResourceLocator**](resourcelocator.md)
</dt> </dl>

 

