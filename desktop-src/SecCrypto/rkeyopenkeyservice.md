---
description: The RKeyOpenKeyService function is not supported.
ms.assetid: 3af18cf7-bc98-4ebc-a62c-7234e9fbddaa
title: RKeyOpenKeyService function (Rkeysvcc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RKeyOpenKeyService
api_type: 
- HeaderDef
api_location: 
- Rkeysvcc.h
---

# RKeyOpenKeyService function

The **RKeyOpenKeyService** function is not supported.

**Windows Server 2003:** The **RKeyOpenKeyService** function establishes a connection to a remote computer and opens a key service handle. The key service handle can subsequently be used by the [**RKeyPFXInstall**](rkeypfxinstall.md) function. Note that this behavior has changed with Windows Server 2003 with Service Pack 1 (SP1).

## Syntax


```C++
ULONG RKeyOpenKeyService(
  _In_    LPSTR          pszMachineName,
  _In_    KEYSVC_TYPE    OwnerType,
  _In_    LPWSTR         pwszOwnerName,
  _In_    void           *pAuthentication,
  _Inout_ void           *pReserved,
  _Out_   KEYSVCC_HANDLE *phKeySvcCli
);
```



## Parameters

<dl> <dt>

*pszMachineName* \[in\]
</dt> <dd>

Long pointer to a null-terminated string that represents the computer where the key service handle will be opened.

</dd> <dt>

*OwnerType* \[in\]
</dt> <dd>

[**KEYSVC\_TYPE**](keysvc-type.md) value that represents the key type. The only supported value is **KeySvcMachine**.

</dd> <dt>

*pwszOwnerName* \[in\]
</dt> <dd>

Reserved. Set this value to **NULL**.

</dd> <dt>

*pAuthentication* \[in\]
</dt> <dd>

A pointer to a **void** that represents the authentication settings. This pointer can point to a value of zero or the following value.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <span id="RKEYSVC_CONNECT_SECURE_ONLY"></span><span id="rkeysvc_connect_secure_only"></span><dl> <dt>**RKEYSVC\_CONNECT\_SECURE\_ONLY**</dt> <dt></dt> </dl> | The client requires mutual authentication. If this value is specified, fallback to NTLM will fail.<br/> |



 

</dd> <dt>

*pReserved* \[in, out\]
</dt> <dd>

Reserved. Set this value to **NULL**.

</dd> <dt>

*phKeySvcCli* \[out\]
</dt> <dd>

A pointer to a [**KEYSVCC\_HANDLE**](keysvcc-handle.md) that receives the opened key service handle. When you have finished using the handle, free the resource by calling the [**RKeyCloseKeyService**](rkeyclosekeyservice.md) function.

</dd> </dl>

## Return value

If the function is successful, the return value is S\_OK.

If the function fails, the return value is a **ULONG** that indicates the error.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Rkeysvcc.h</dt> </dl> |



## See also

<dl> <dt>

[**RKeyCloseKeyService**](rkeyclosekeyservice.md)
</dt> <dt>

[**RKeyPFXInstall**](rkeypfxinstall.md)
</dt> </dl>

 

 




