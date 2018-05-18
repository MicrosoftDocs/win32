---
title: IMimeAllocator ReleaseObjects method
description: Frees an array of IUnknown objects.
ms.assetid: '1193eb79-9de5-438e-85d6-ac336944677f'
keywords: ["ReleaseObjects method Windows Mail (formerly Outlook Express)", "ReleaseObjects method Windows Mail (formerly Outlook Express) , IMimeAllocator interface", "IMimeAllocator interface Windows Mail (formerly Outlook Express) , ReleaseObjects method"]
topic_type:
- apiref
api_name:
- IMimeAllocator.ReleaseObjects
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeAllocator::ReleaseObjects method

Frees an array of [IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp) objects.

## Syntax


```C++
HRESULT ReleaseObjects(
  [in] ULONG    cObjects,
  [in] IUnknown **prgpUnknown,
  [in] boolean  fFreeArray
);
```



## Parameters

<dl> <dt>

*cObjects* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the number of elements in the *prgpUnknown* array.

</dd> <dt>

*prgpUnknown* \[in\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\*\***

Specifies a pointer to an array of pointers to [IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp) objects.

</dd> <dt>

*fFreeArray* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the pointer to *prgpUnknown* should also be freed.



| Value                                                                                                                                | Meaning                                     |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Keep the *prgpUnknown* pointer. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Free the *prgpUnknown* pointer. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the following value.



| Return code                                                                          | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





