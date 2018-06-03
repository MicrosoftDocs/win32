---
title: RPC Data Marshaling Functions
description: The functions in this section are Automation implementations of the ACF-type user\_marshal attribute, which provides an efficient way to marshal custom data types that are unknown to MIDL.
ms.assetid: 861666c6-6213-445e-87b6-9d1b8dc2c464
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RPC Data Marshaling Functions

The functions in this section are Automation implementations of the ACF-type user\_marshal attribute, which provides an efficient way to marshal custom data types that are unknown to MIDL.

## In this section



| Topic                                                                          | Description                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BSTR\_UserFree**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_userfree)<br/>                             | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**BSTR\_UserFree64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_userfree64)<br/>                         | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**BSTR\_UserMarshal**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_usermarshal)<br/>                       | Marshals a [**BSTR**](bstr.md) object into the RPC buffer.<br/>                                                                                                                                    |
| [**BSTR\_UserMarshal64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_usermarshal64)<br/>                   | Marshals a [**BSTR**](bstr.md) object into the RPC buffer.<br/>                                                                                                                                    |
| [**BSTR\_UserSize**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_usersize)<br/>                             | Calculates the wire size of the [**BSTR**](bstr.md) object, and gets its handle and data.<br/>                                                                                                     |
| [**BSTR\_UserSize64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_usersize64)<br/>                         | Calculates the wire size of the [**BSTR**](bstr.md) object, and gets its handle and data.<br/>                                                                                                     |
| [**BSTR\_UserUnmarshal**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_userunmarshal)<br/>                   | Unmarshals a [**BSTR**](bstr.md) object from the RPC buffer.<br/>                                                                                                                                  |
| [**BSTR\_UserUnmarshal64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-bstr_userunmarshal64)<br/>               | Unmarshals a [**BSTR**](bstr.md) object from the RPC buffer.<br/>                                                                                                                                  |
| [**LPSAFEARRAY\_Marshal**](lpsafearray-marshal.md)<br/>                 | Marshals a [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object to a user's RPC buffer on the server using information passed in by the [**LPSAFEARRAY\_UserMarshal**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_usermarshal) function.<br/> |
| [**LPSAFEARRAY\_Size**](lpsafearray-size.md)<br/>                       | Calculates the wire size of the [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object, and gets its handle and data needed by the [**LPSAFEARRAY\_UserSize**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_usersize) function.<br/>              |
| [**LPSAFEARRAY\_Unmarshal**](lpsafearray-unmarshal.md)<br/>             | Unmarshals a [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object from the RPC buffer using information passed in by the [**LPSAFEARRAY\_UserUnmarshal**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_userunmarshal) function.<br/>            |
| [**LPSAFEARRAY\_UserFree**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_userfree)<br/>               | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**LPSAFEARRAY\_UserFree64**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_userfree64)<br/>           | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**LPSAFEARRAY\_UserMarshal**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_usermarshal)<br/>         | Marshals data from the specified [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object to the user's RPC buffer on the client or server side. <br/>                                                                 |
| [**LPSAFEARRAY\_UserMarshal64**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_usermarshal64)<br/>     | Marshals data from the specified [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object to the user's RPC buffer on the client or server side. <br/>                                                                 |
| [**LPSAFEARRAY\_UserSize**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_usersize)<br/>               | Calculates the wire size of the [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object, and gets its handle and data.<br/>                                                                                           |
| [**LPSAFEARRAY\_UserSize64**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_usersize64)<br/>           | Calculates the wire size of the [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object, and gets its handle and data.<br/>                                                                                           |
| [**LPSAFEARRAY\_UserUnmarshal**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_userunmarshal)<br/>     | Unmarshals a [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object from the RPC buffer.<br/>                                                                                                                        |
| [**LPSAFEARRAY\_UserUnmarshal64**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_userunmarshal64)<br/> | Unmarshals a [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object from the RPC buffer.<br/>                                                                                                                        |
| [**VARIANT\_UserFree**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_userfree)<br/>                       | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**VARIANT\_UserFree64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_userfree64)<br/>                   | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**VARIANT\_UserMarshal**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_usermarshal)<br/>                 | Marshals a [**VARIANT**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagvariant) object into the RPC buffer.<br/>                                                                                                                              |
| [**VARIANT\_UserMarshal64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_usermarshal64)<br/>             | Marshals a [**VARIANT**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagvariant) object into the RPC buffer.<br/>                                                                                                                              |
| [**VARIANT\_UserSize**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_usersize)<br/>                       | Calculates the wire size of the [**VARIANT**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagvariant) object, and gets its handle and data.<br/>                                                                                               |
| [**VARIANT\_UserSize64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_usersize64)<br/>                   | Calculates the wire size of the [**VARIANT**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagvariant) object, and gets its handle and data.<br/>                                                                                               |
| [**VARIANT\_UserUnmarshal**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_userunmarshal)<br/>             | Unmarshals a [**VARIANT**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagvariant) object from the RPC buffer.<br/>                                                                                                                            |
| [**VARIANT\_UserUnmarshal64**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-variant_userunmarshal64)<br/>         | Unmarshals a [**VARIANT**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagvariant) object from the RPC buffer.<br/>                                                                                                                            |



 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 





