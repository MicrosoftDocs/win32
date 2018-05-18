---
title: RendezvousApplication.SetRendezvousSession method
description: Passes IRendezvousSession to the Windows Remote Assistance application. This method is used by the instant messaging application.
ms.assetid: 'e4e8781f-61b2-4ef3-92f8-a2cf13ebdfdd'
keywords: ["SetRendezvousSession method Remote Assistance", "SetRendezvousSession method Remote Assistance , RendezvousApplication object", "RendezvousApplication object Remote Assistance , SetRendezvousSession method"]
topic_type:
- apiref
api_name:
- RendezvousApplication.SetRendezvousSession
api_location:
- RendezvousSession.tlb
api_type:
- COM
---

# RendezvousApplication.SetRendezvousSession method

Passes [**IRendezvousSession**](remoteassist-irendezvoussession.md) to the Windows Remote Assistance application. This method is used by the instant messaging application.

## Syntax


```VB
RendezvousApplication.SetRendezvousSession( _
  ByVal oRendezvousSession As IUnknown _
) As HRESULT
```



## Parameters

<dl> <dt>

*oRendezvousSession* \[in\]
</dt> <dd>Specifies the [**IRendezvousSession**](remoteassist-irendezvoussession.md) object. </dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                  | Description                                                                                                                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The [**IRendezvousSession**](remoteassist-irendezvoussession.md) was passed to the Windows Remote Assistance application successfully. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The session object passed to the method is not valid. <br/>                                                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | A catastrophic error occurred while trying to pass the session to the Windows Remote Assistance application.<br/>                             |



 

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                             |
| Header<br/>                   | <dl> <dt>RendezvousSession.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RendezvousSession.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RendezvousSession.tlb</dt> </dl> |



 

 





