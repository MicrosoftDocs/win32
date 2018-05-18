---
Description: 'Gets the error state associated with the media key session.'
ms.assetid: '4693b7d5-59ee-472f-83fc-1ecbcc165dac'
title: 'IMFMediaKeySession::GetError method'
---

# IMFMediaKeySession::GetError method

Gets the error state associated with the media key session.

## Syntax


```C++
HRESULT GetError(
   USHORT *code,
   DWORD  *systemCode
);
```



## Parameters

<dl> <dt>

*code* 
</dt> <dd>

The error code.

</dd> <dt>

*systemCode* 
</dt> <dd>

Platform specific error information.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaKeySession**](imfmediakeysession.md)
</dt> </dl>

 

 




