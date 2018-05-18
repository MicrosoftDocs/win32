---
title: IMimeMessageTree GetOption method
description: Gets the value of an IMimeMessageTree option.
ms.assetid: '599f49b6-2126-4896-bc98-80161005db64'
keywords: ["GetOption method Windows Mail (formerly Outlook Express)", "GetOption method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface", "IMimeMessageTree interface Windows Mail (formerly Outlook Express) , GetOption method"]
topic_type:
- apiref
api_name:
- IMimeMessageTree.GetOption
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageTree::GetOption method

Gets the value of an [**IMimeMessageTree**](oe-imimemessagetree.md) option.

## Syntax


```C++
HRESULT GetOption(
  [in]      const TYPEDID       oid,
  [in, out]       LPPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

*oid* \[in\]
</dt> <dd>

Type: **const TYPEDID**

Specifies the option ID that indicates how the [**IMimeMessageTree**](oe-imimemessagetree.md) object works.



| Value                                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="OID_HANDSOFF_ONSAVE"></span><span id="oid_handsoff_onsave"></span><dl> <dt>**OID\_HANDSOFF\_ONSAVE**</dt> </dl>                              | **VT\_BOOL** that indicates whether to keep a reference to the storage object when the message object is saved. <br/> <dl> <dt>FALSE</dt> <dd> Default. Keep a reference to the storage object. <br/> </dd> <dt>TRUE</dt> <dd> Free the reference to the storage object. <br/> </dd> </dl>                                                                                                                                                                                                                                       |
| <span id="OID_SUPPORT_EXTERNAL_BODY"></span><span id="oid_support_external_body"></span><dl> <dt>**OID\_SUPPORT\_EXTERNAL\_BODY**</dt> </dl>           | **VT\_BOOL** that indicates whether a message body should support the message/external-body [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp). When this option is applied to a message object, it is also applied to all the bodies currently on that message object. <br/> <dl> <dt>FALSE</dt> <dd> Default. Do not support message/external-body. <br/> </dd> <dt>TRUE</dt> <dd> Support message/external-body. <br/> </dd> </dl>                                  |
| <span id="OID_SHOW_MACBINARY"></span><span id="oid_show_macbinary"></span><dl> <dt>**OID\_SHOW\_MACBINARY**</dt> </dl>                                 | **VT\_BOOL** that indicates whether to enable MacBinary attachment support. When this option is applied to a message object, it is also applied to all the bodies currently on that message object. <br/> <dl> <dt>FALSE</dt> <dd> Default. Do not support MacBinary attachments. <br/> </dd> <dt>TRUE</dt> <dd> Support MacBinary attachments. <br/> </dd> </dl>                                                                                                                                                                |
| <span id="OID_HEADER_RELOAD_TYPE"></span><span id="oid_header_reload_type"></span><dl> <dt>**OID\_HEADER\_RELOAD\_TYPE**</dt> </dl>                    | **VT\_UI4** that indicates how a message object resets itself when [IMimeMessageTree::InitNew](http://msdn.microsoft.com/library/com/htm/cmi_n2p_19vb.asp) is called. This option can be used to merge root headers in a message object. Valid values for this option are defined by [**RELOADTYPE**](oe-reloadtype.md). The default value is **RELOAD\_HEADER\_RESET**. <br/>                                                                                                                                                                                                                                                                                 |
| <span id="OID_LOAD_USE_BIND_FILE"></span><span id="oid_load_use_bind_file"></span><dl> <dt>**OID\_LOAD\_USE\_BIND\_FILE**</dt> </dl>                   | **VT\_BOOL** that indicates whether to close the storage object after it is loaded. <br/> <dl> <dt>FALSE</dt> <dd> Default. Keep the storage object open. <br/> </dd> <dt>TRUE</dt> <dd> Close the storage object. <br/> </dd> </dl>                                                                                                                                                                                                                                                                                             |
| <span id="OID_CLEANUP_TREE_ON_SAVE"></span><span id="oid_cleanup_tree_on_save"></span><dl> <dt>**OID\_CLEANUP\_TREE\_ON\_SAVE**</dt> </dl>             | **VT\_BOOL** that indicates whether to clean up the message tree when the message object is saved. Cleanup may include removing TNEF attachments and converting multipart bodies that have only one child to a single body. <br/> <dl> <dt>FALSE</dt> <dd> Do not clean up the message tree when the message object is saved. <br/> </dd> <dt>TRUE</dt> <dd> Default. Clean up the message tree when the message object is saved. <br/> </dd> </dl>                                                                              |
| <span id="OID_SAVEBODY_KEEPBOUNDARY"></span><span id="oid_savebody_keepboundary"></span><dl> <dt>**OID\_SAVEBODY\_KEEPBOUNDARY**</dt> </dl>            | **VT\_BOOL** that indicates whether to reuse existing multipart boundaries (for example, from a previous load) when the message object is saved. <br/> <dl> <dt>FALSE</dt> <dd> Default. Do not reuse multipart boundaries when the message object is saved. <br/> </dd> <dt>TRUE</dt> <dd> Reuse multipart boundaries when the message object is saved. <br/> </dd> </dl>                                                                                                                                                       |
| <span id="OID_CAN_INLINE_TEXT_BODIES"></span><span id="oid_can_inline_text_bodies"></span><dl> <dt>**OID\_CAN\_INLINE\_TEXT\_BODIES**</dt> </dl>       | **VT\_BOOL** that indicates whether to allow the client to insert various text parts of the tree into a single viewer or to convert the text parts to attachments instead. Also see [**IBT\_AUTOATTACH**](oe-imsgbodytype.md). <br/> <dl> <dt>FALSE</dt> <dd> Default. Do not allow inlining multiple text bodies into a single viewer. <br/> </dd> <dt>TRUE</dt> <dd> Allow inlining multiple text bodies into a single viewer. <br/> </dd> </dl>                                                                              |
| <span id="OID_HIDE_TNEF_ATTACHMENTS"></span><span id="oid_hide_tnef_attachments"></span><dl> <dt>**OID\_HIDE\_TNEF\_ATTACHMENTS**</dt> </dl>           | **VT\_BOOL** that indicates whether to show Microsoft TNEF attachments. When this option is applied to a message object, it is also applied to all the bodies currently on that message object. <br/> <dl> <dt>FALSE</dt> <dd> Hide TNEF attachments. <br/> </dd> <dt>TRUE</dt> <dd> Default. Show TNEF attachments. <br/> </dd> </dl>                                                                                                                                                                                           |
| <span id="OID_ALLOW_8BIT_HEADER"></span><span id="oid_allow_8bit_header"></span><dl> <dt>**OID\_ALLOW\_8BIT\_HEADER**</dt> </dl>                       | **VT\_BOOL** that indicates whether to allow 8-bit characters to be saved in the header. This option also indicates whether to allow [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. This option is applied to a body when the message is saved. <br/> <dl> <dt>FALSE</dt> <dd> Default. Disallow 8-bit characters and [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. <br/> </dd> <dt>TRUE</dt> <dd> Allow 8-bit characters and [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. <br/> </dd> </dl> |
| <span id="OID_CBMAX_HEADER_LINE"></span><span id="oid_cbmax_header_line"></span><dl> <dt>**OID\_CBMAX\_HEADER\_LINE**</dt> </dl>                       | **VT\_UI4** that indicates the maximum number of characters for a line when the property set is saved. Headers longer than this length are wrapped. The minimum value for this option is 76 and the maximum is 0xffffffff (no limit). The default value is 1000. This option is applied to a body when the message is saved. <br/>                                                                                                                                                                                                                                                                                                                                    |
| <span id="OID_SAVE_FORMAT"></span><span id="oid_save_format"></span><dl> <dt>**OID\_SAVE\_FORMAT**</dt> </dl>                                          | **VT\_UI4** that indicates in what format the message object should be saved. Valid values for this option are defined by [**MIMESAVETYPE**](oe-mimesavetype.md), **SAVE\_RFC1521** or whatever the format of the message was when it was loaded into the message object. <br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="OID_TRANSMIT_TEXT_ENCODING"></span><span id="oid_transmit_text_encoding"></span><dl> <dt>**OID\_TRANSMIT\_TEXT\_ENCODING**</dt> </dl>        | **VT\_UI4** that indicates the [Content-Transfer-Encoding](http://msdn.microsoft.com/library/cdosys/html/9c3f693c-f9f7-4b33-bba3-be9c872a20d5.asp) to use when saving a text/\* body. It is recommended that clients do not set this option and instead let the message object compute the best encoding. This option takes precedence over the other two options that control text encodings, **OID\_XMIT\_PLAIN\_TEXT\_ENCODING** and **OID\_XMIT\_HTML\_TEXT\_ENCODING**. Valid values for this option are defined by [**ENCODINGTYPE**](oe-encodingtype.md). The default value is **IET\_UNKNOWN**. <br/>                                                  |
| <span id="OID_XMIT_PLAIN_TEXT_ENCODING"></span><span id="oid_xmit_plain_text_encoding"></span><dl> <dt>**OID\_XMIT\_PLAIN\_TEXT\_ENCODING**</dt> </dl> | **VT\_UI4** that indicates the [Content-Transfer-Encoding](http://msdn.microsoft.com/library/cdosys/html/9c3f693c-f9f7-4b33-bba3-be9c872a20d5.asp) to use when saving a text/plain body. It is recommended that clients do not set this option and instead let the message object compute the best encoding. Valid values for this option are defined by [**ENCODINGTYPE**](oe-encodingtype.md). The default value is **IET\_UNKNOWN**. If the **OID\_TRANSMIT\_TEXT\_ENCODING** option is set, this option is ignored. <br/>                                                                                                                                  |
| <span id="OID_XMIT_HTML_TEXT_ENCODING"></span><span id="oid_xmit_html_text_encoding"></span><dl> <dt>**OID\_XMIT\_HTML\_TEXT\_ENCODING**</dt> </dl>    | **VT\_UI4** that indicates the [Content-Transfer-Encoding](http://msdn.microsoft.com/library/cdosys/html/9c3f693c-f9f7-4b33-bba3-be9c872a20d5.asp) to use when saving a text/html body. It is recommended that clients do not set this option and instead let the message object compute the best encoding. Valid values for this option are defined by [**ENCODINGTYPE**](oe-encodingtype.md). The default value is **IET\_UNKNOWN**. If the **OID\_TRANSMIT\_TEXT\_ENCODING** option is set, this option is ignored. <br/>                                                                                                                                   |
| <span id="OID_WRAP_BODY_TEXT"></span><span id="oid_wrap_body_text"></span><dl> <dt>**OID\_WRAP\_BODY\_TEXT**</dt> </dl>                                | **VT\_BOOL** that indicates whether to enable line wrapping when saving text bodies. This option is applied to a body when the message is saved. <br/> <dl> <dt>FALSE</dt> <dd> Do not wrap lines. <br/> </dd> <dt>TRUE</dt> <dd> Default. Wrap text lines so that no line is longer than the maximum line length as determined by **OID\_CBMAX\_BODY\_LINE**. <br/> </dd> </dl>                                                                                                                                                 |
| <span id="OID_CBMAX_BODY_LINE"></span><span id="oid_cbmax_body_line"></span><dl> <dt>**OID\_CBMAX\_BODY\_LINE**</dt> </dl>                             | **VT\_UI4** that indicates the maximum length of a line. This option is used by [**GetTransmitInfo**](oe-imimebody-gettransmitinfo.md) to determine an appropriate [Content-Transfer-Encoding](http://msdn.microsoft.com/library/cdosys/html/9c3f693c-f9f7-4b33-bba3-be9c872a20d5.asp). The default value is 74 characters. The value must be greater than or equal to 30. This option is applied to a body when the message is saved. <br/>                                                                                                                                                                                                                   |
| <span id="OID_GENERATE_MESSAGE_ID"></span><span id="oid_generate_message_id"></span><dl> <dt>**OID\_GENERATE\_MESSAGE\_ID**</dt> </dl>                 | **VT\_BOOL** that indicates whether a [Message-ID](http://msdn.microsoft.com/library/cdosys/html/3f0e28c9-4dc6-4c15-98b6-2f9cc326a343.asp) is computed and stored on the root header of the message when the message object is saved. <br/> <dl> <dt>FALSE</dt> <dd> Default. Do not compute and store the Message-ID. <br/> </dd> <dt>TRUE</dt> <dd> Compute and store the Message-ID. <br/> </dd> </dl>                                                                                                                  |
| <span id="OID_SECURITY_ENCODE_FLAGS"></span><span id="oid_security_encode_flags"></span><dl> <dt>**OID\_SECURITY\_ENCODE\_FLAGS**</dt> </dl>           | **VT\_UI4** that indicates a value used for secure messaging. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="OID_DECODE_RFC1154"></span><span id="oid_decode_rfc1154"></span><dl> <dt>**OID\_DECODE\_RFC1154**</dt> </dl>                                 | **VT\_BOOL** that indicates whether to allow [RFC 1154](http://www.ietf.org/rfc/rfc1154.txt) message headers and to use them to load and parse a message object more efficiently. <br/> <dl> <dt>FALSE</dt> <dd> Default. Disallow [RFC 1154](http://www.ietf.org/rfc/rfc1154.txt) headers. <br/> </dd> <dt>TRUE</dt> <dd> Allow [RFC 1154](http://www.ietf.org/rfc/rfc1154.txt) headers. <br/> </dd> </dl>                                                                                                                      |



 

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
| <dl> <dt>**MIME\_E\_INVALID\_OPTION\_ID**</dt> </dl> | Indicates that *oid* is not a valid [**IMimeMessageTree**](oe-imimemessagetree.md) option. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





