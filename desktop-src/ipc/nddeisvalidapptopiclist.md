---
description: Determines whether an application and topic string (&\#0034;AppName\|TopicName&\#0034;) uses the proper syntax.
ms.assetid: bcf5442b-452e-4b42-95e9-f09bf885be40
title: NDdeIsValidAppTopicList function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeIsValidAppTopicList
- NDdeIsValidAppTopicListA
- NDdeIsValidAppTopicListW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeIsValidAppTopicList function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Determines whether an application and topic string ("*AppName*\|*TopicName*") uses the proper syntax.

## Syntax


```C++
BOOL NDdeIsValidAppTopicList(
  _In_ LPTSTR targetTopic
);
```



## Parameters

<dl> <dt>

*targetTopic* \[in\]
</dt> <dd>

A pointer to the application and topic string to validate. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

If the *targetTopic* parameter has valid syntax, the return value is nonzero.

If the function fails, the return value is zero.

## Remarks

This function is also called by [**NDdeShareAdd**](nddeshareadd.md) when it creates the DDE share.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                      |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>      |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl>    |
| Unicode and ANSI names<br/>   | **NDdeIsValidAppTopicListW** (Unicode) and **NDdeIsValidAppTopicListA** (ANSI)<br/> |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**NDdeShareAdd**](nddeshareadd.md)
</dt> </dl>

 

 




