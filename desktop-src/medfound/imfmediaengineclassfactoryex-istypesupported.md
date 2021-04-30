---
description: Gets a value that indicates if the specified key system supports the specified media type.
ms.assetid: 6f4f50db-e491-46c2-a8b2-1b8e51033b5b
title: IMFMediaEngineClassFactoryEx::IsTypeSupported method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFMediaEngineClassFactoryEx.IsTypeSupported
api_type: 
- COM
api_location: 
- mfmediaengine.h
---

# IMFMediaEngineClassFactoryEx::IsTypeSupported method

Gets a value that indicates if the specified key system supports the specified media type.

## Syntax


```C++
HRESULT IsTypeSupported(
   BSTR type,
   BSTR keySystem,
   BOOL *isSupported
);
```



## Parameters

<dl> <dt>

*type* 
</dt> <dd>

The MIME type to check support for.

</dd> <dt>

*keySystem* 
</dt> <dd>

The key system to check support for.

</dd> <dt>

*isSupported* 
</dt> <dd>

**true** if type is supported by *keySystem*; otherwise, **false.**

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaEngineClassFactoryEx**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineclassfactoryex)
</dt> </dl>

 

 




