---
Description: 'Gets a unique session id created for this session.'
ms.assetid: '779ebea9-69ff-469a-8ee0-06d570ede6cb'
title: 'IMFMediaKeySession::get\_SessionId method'
---

# IMFMediaKeySession::get\_SessionId method

Gets a unique session id created for this session.

## Syntax


```C++
HRESULT get_SessionId(
   BSTR *sessionId
);
```



## Parameters

<dl> <dt>

*sessionId* 
</dt> <dd>

The media key session id.

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

 

 




