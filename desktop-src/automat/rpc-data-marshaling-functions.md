---
title: RPC Data Marshaling Functions
description: The functions in this section are Automation implementations of the ACF-type user\_marshal attribute, which provides an efficient way to marshal custom data types that are unknown to MIDL.
ms.assetid: 861666c6-6213-445e-87b6-9d1b8dc2c464
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RPC Data Marshaling Functions

The functions in this section are Automation implementations of the ACF-type user\_marshal attribute, which provides an efficient way to marshal custom data types that are unknown to MIDL.

## In this section



| Topic                                                                          | Description                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BSTR\_UserFree**](/windows/previous-versions/oaidl/nf-oaidl-bstr_userfree?branch=master)<br/>                             | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**BSTR\_UserFree64**](/windows/previous-versions/oaidl/nf-oaidl-bstr_userfree64?branch=master)<br/>                         | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**BSTR\_UserMarshal**](/windows/previous-versions/oaidl/nf-oaidl-bstr_usermarshal?branch=master)<br/>                       | Marshals a [**BSTR**](bstr.md) object into the RPC buffer.<br/>                                                                                                                                    |
| [**BSTR\_UserMarshal64**](/windows/previous-versions/oaidl/nf-oaidl-bstr_usermarshal64?branch=master)<br/>                   | Marshals a [**BSTR**](bstr.md) object into the RPC buffer.<br/>                                                                                                                                    |
| [**BSTR\_UserSize**](/windows/previous-versions/oaidl/nf-oaidl-bstr_usersize?branch=master)<br/>                             | Calculates the wire size of the [**BSTR**](bstr.md) object, and gets its handle and data.<br/>                                                                                                     |
| [**BSTR\_UserSize64**](/windows/previous-versions/oaidl/nf-oaidl-bstr_usersize64?branch=master)<br/>                         | Calculates the wire size of the [**BSTR**](bstr.md) object, and gets its handle and data.<br/>                                                                                                     |
| [**BSTR\_UserUnmarshal**](/windows/previous-versions/oaidl/nf-oaidl-bstr_userunmarshal?branch=master)<br/>                   | Unmarshals a [**BSTR**](bstr.md) object from the RPC buffer.<br/>                                                                                                                                  |
| [**BSTR\_UserUnmarshal64**](/windows/previous-versions/oaidl/nf-oaidl-bstr_userunmarshal64?branch=master)<br/>               | Unmarshals a [**BSTR**](bstr.md) object from the RPC buffer.<br/>                                                                                                                                  |
| [**LPSAFEARRAY\_Marshal**](lpsafearray-marshal.md)<br/>                 | Marshals a [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object to a user's RPC buffer on the server using information passed in by the [**LPSAFEARRAY\_UserMarshal**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_usermarshal?branch=master) function.<br/> |
| [**LPSAFEARRAY\_Size**](lpsafearray-size.md)<br/>                       | Calculates the wire size of the [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object, and gets its handle and data needed by the [**LPSAFEARRAY\_UserSize**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_usersize?branch=master) function.<br/>              |
| [**LPSAFEARRAY\_Unmarshal**](lpsafearray-unmarshal.md)<br/>             | Unmarshals a [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object from the RPC buffer using information passed in by the [**LPSAFEARRAY\_UserUnmarshal**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_userunmarshal?branch=master) function.<br/>            |
| [**LPSAFEARRAY\_UserFree**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_userfree?branch=master)<br/>               | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**LPSAFEARRAY\_UserFree64**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_userfree64?branch=master)<br/>           | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**LPSAFEARRAY\_UserMarshal**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_usermarshal?branch=master)<br/>         | Marshals data from the specified [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object to the user's RPC buffer on the client or server side. <br/>                                                                 |
| [**LPSAFEARRAY\_UserMarshal64**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_usermarshal64?branch=master)<br/>     | Marshals data from the specified [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object to the user's RPC buffer on the client or server side. <br/>                                                                 |
| [**LPSAFEARRAY\_UserSize**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_usersize?branch=master)<br/>               | Calculates the wire size of the [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object, and gets its handle and data.<br/>                                                                                           |
| [**LPSAFEARRAY\_UserSize64**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_usersize64?branch=master)<br/>           | Calculates the wire size of the [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object, and gets its handle and data.<br/>                                                                                           |
| [**LPSAFEARRAY\_UserUnmarshal**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_userunmarshal?branch=master)<br/>     | Unmarshals a [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object from the RPC buffer.<br/>                                                                                                                        |
| [**LPSAFEARRAY\_UserUnmarshal64**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_userunmarshal64?branch=master)<br/> | Unmarshals a [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object from the RPC buffer.<br/>                                                                                                                        |
| [**VARIANT\_UserFree**](/windows/previous-versions/oaidl/nf-oaidl-variant_userfree?branch=master)<br/>                       | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**VARIANT\_UserFree64**](/windows/previous-versions/oaidl/nf-oaidl-variant_userfree64?branch=master)<br/>                   | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**VARIANT\_UserMarshal**](/windows/previous-versions/oaidl/nf-oaidl-variant_usermarshal?branch=master)<br/>                 | Marshals a [**VARIANT**](/windows/previous-versions/OaIdl/ns-oaidl-tagvariant?branch=master) object into the RPC buffer.<br/>                                                                                                                              |
| [**VARIANT\_UserMarshal64**](/windows/previous-versions/oaidl/nf-oaidl-variant_usermarshal64?branch=master)<br/>             | Marshals a [**VARIANT**](/windows/previous-versions/OaIdl/ns-oaidl-tagvariant?branch=master) object into the RPC buffer.<br/>                                                                                                                              |
| [**VARIANT\_UserSize**](/windows/previous-versions/oaidl/nf-oaidl-variant_usersize?branch=master)<br/>                       | Calculates the wire size of the [**VARIANT**](/windows/previous-versions/OaIdl/ns-oaidl-tagvariant?branch=master) object, and gets its handle and data.<br/>                                                                                               |
| [**VARIANT\_UserSize64**](/windows/previous-versions/oaidl/nf-oaidl-variant_usersize64?branch=master)<br/>                   | Calculates the wire size of the [**VARIANT**](/windows/previous-versions/OaIdl/ns-oaidl-tagvariant?branch=master) object, and gets its handle and data.<br/>                                                                                               |
| [**VARIANT\_UserUnmarshal**](/windows/previous-versions/oaidl/nf-oaidl-variant_userunmarshal?branch=master)<br/>             | Unmarshals a [**VARIANT**](/windows/previous-versions/OaIdl/ns-oaidl-tagvariant?branch=master) object from the RPC buffer.<br/>                                                                                                                            |
| [**VARIANT\_UserUnmarshal64**](/windows/previous-versions/oaidl/nf-oaidl-variant_userunmarshal64?branch=master)<br/>         | Unmarshals a [**VARIANT**](/windows/previous-versions/OaIdl/ns-oaidl-tagvariant?branch=master) object from the RPC buffer.<br/>                                                                                                                            |



 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 





