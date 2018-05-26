---
title: IMimePropertySet GetOption method
description: Gets the value of an option.
ms.assetid: 4ffffd39-36d0-4c38-89ee-11eac30ac303
keywords:
- GetOption method Windows Mail (formerly Outlook Express)
- GetOption method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , GetOption method
topic_type:
- apiref
api_name:
- IMimePropertySet.GetOption
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimePropertySet::GetOption method

Gets the value of an option.

## Syntax


```C++
HRESULT GetOption(
  [in]      const TYPEDID       oid,
  [in, out]       LPPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

*oid* \[in\]
</dt> <dd>

Type: **const TYPEDID**

Specifies the option ID.



| Value                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="OID_HEADER_RELOAD_TYPE"></span><span id="oid_header_reload_type"></span><dl> <dt>**OID\_HEADER\_RELOAD\_TYPE**</dt> </dl> | **VT\_UI4** that indicates how the [**IMimePropertySet**](oe-imimepropertyset.md) resets itself when [IMimePropertySet::Load](http://msdn.microsoft.com/library/com/htm/cmi_n2p_63ac.asp) and [IMimePropertySetInitNew](http://msdn.microsoft.com/library/com/htm/cmi_n2p_19vb.asp) are called consecutively. Using this option, a client can load and merge multiple headers into the same object. Valid values for this option are defined by [**RELOADTYPE**](oe-reloadtype.md). The default value is **RELOAD\_HEADER\_NONE**. <br/>                                                                                                                                                                                                                                                                                                            |
| <span id="OID_NO_DEFAULT_CNTTYPE"></span><span id="oid_no_default_cnttype"></span><dl> <dt>**OID\_NO\_DEFAULT\_CNTTYPE**</dt> </dl> | **VT\_BOOL** that indicates whether MimeOLE should default the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) to text/plain when [IMimePropertySet::Save](http://msdn.microsoft.com/library/com/htm/cmi_n2p_47z9.asp) is called and there is no Content-Type header. <br/> <dl> <dt>FALSE</dt> <dd> Default. MimeOLE should set the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) to text/plain.<br/> </dd> <dt>TRUE</dt> <dd> MimeOLE should not set the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp). <br/> </dd> </dl> |
| <span id="OID_ALLOW_8BIT_HEADER"></span><span id="oid_allow_8bit_header"></span><dl> <dt>**OID\_ALLOW\_8BIT\_HEADER**</dt> </dl>    | **VT\_BOOL** that indicates whether to allow 8-bit characters to be saved in the header. This option also indicates whether to allow [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. <br/> <dl> <dt>FALSE</dt> <dd> Default. Disallow 8-bit characters and [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. <br/> </dd> <dt>TRUE</dt> <dd> Allow 8-bit characters and [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. <br/> </dd> </dl>                                                                                                                                                                                                                                                         |
| <span id="OID_CBMAX_HEADER_LINE"></span><span id="oid_cbmax_header_line"></span><dl> <dt>**OID\_CBMAX\_HEADER\_LINE**</dt> </dl>    | **VT\_UI4** that indicates the maximum number of characters for a line when the property set is saved. Headers longer than this length are wrapped. The minimum value for this option is 76 and the maximum is 0xffffffff (no limit). The default value is 1000. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="OID_SAVE_FORMAT"></span><span id="oid_save_format"></span><dl> <dt>**OID\_SAVE\_FORMAT**</dt> </dl>                       | **VT\_UI4** that indicates the header should be saved in [RFC 822](http://www.ietf.org/rfc/rfc822.txt) or [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt) (MIME) format. The default value is [**SAVE\_RFC1521**](oe-mimesavetype.md). <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |



 

</dd> <dt>

*pValue* \[in, out\]
</dt> <dd>

Type: **LPPROPVARIANT**

Receives a pointer to a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the value for the option. MimeOLE sets *pValue*-&gt;vt and the corresponding member in this structure according to the [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) of the option.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                                                           |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pValue* is **NULL**. <br/>                                                        |
| <dl> <dt>**MIME\_E\_INVALID\_OPTION\_ID**</dt> </dl> | Indicates that *oid* is not a valid [**IMimePropertySet**](oe-imimepropertyset.md) option. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





