---
title: IRASTransport InitNew method
description: Initializes the Remote Access Service (RAS) transport.
ms.assetid: '14376a21-752b-45d8-a86c-53053a373305'
keywords: ["InitNew method Windows Mail (formerly Outlook Express)", "InitNew method Windows Mail (formerly Outlook Express) , IRASTransport interface", "IRASTransport interface Windows Mail (formerly Outlook Express) , InitNew method"]
topic_type:
- apiref
api_name:
- IRASTransport.InitNew
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRASTransport::InitNew method

\[**IRASTransport::InitNew** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the Remote Access Service (RAS) transport.

## Syntax


```C++
HRESULT InitNew(
  [in] IRASCallback *pCallback
);
```



## Parameters

<dl> <dt>

*pCallback* \[in\]
</dt> <dd>

Type: **[**IRASCallback**](oe-irascallback.md)\***

Specifies a pointer to the callback interface for RAS.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an error has occurred. <br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pCallback* is **NULL**. <br/> |



 

## Remarks

This method must be called to start the transport before any other methods can be called.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





