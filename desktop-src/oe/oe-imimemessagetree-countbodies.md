---
title: IMimeMessageTree CountBodies method
description: Gets the number of bodies in the message tree.
ms.assetid: '8ba07b8b-ca8c-424d-a550-b05a95793662'
keywords: ["CountBodies method Windows Mail (formerly Outlook Express)", "CountBodies method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface", "IMimeMessageTree interface Windows Mail (formerly Outlook Express) , CountBodies method"]
topic_type:
- apiref
api_name:
- IMimeMessageTree.CountBodies
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageTree::CountBodies method

Gets the number of bodies in the message tree.

## Syntax


```C++
HRESULT CountBodies(
  [in]  HBODY   hParent,
  [in]  boolean fRecurse,
  [out] ULONG   *pcBodies
);
```



## Parameters

<dl> <dt>

*hParent* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body in which to get the number of bodies.

</dd> <dt>

*fRecurse* \[in\]
</dt> <dd>

Type: **boolean**

Specifies how the method should bodies.



| Value                                                                                                                                | Meaning                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Indicates that the method should count the specified body and its direct children. <br/>                                                            |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Indicates that the method should count the specified body and all of its descendants, that is, it should recurse into multipart child bodies. <br/> |



 

</dd> <dt>

*pcBodies* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a **ULONG** that indicates the number of bodies.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                              |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pcBodies* is **NULL**. <br/>         |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hParent* is an invalid handle. <br/> |



 

## Remarks

The count returned includes the body specified in *hParent*.

The count starts at the root of the message tree when *hParent* is **NULL** or equal to HBODY\_ROOT (0xffffffff).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





