---
title: RPC Data Marshaling Functions
description: The functions in this section are Automation implementations of the ACF-type user\_marshal attribute, which provides an efficient way to marshal custom data types that are unknown to MIDL.
ms.assetid: '861666c6-6213-445e-87b6-9d1b8dc2c464'
---

# RPC Data Marshaling Functions

The functions in this section are Automation implementations of the ACF-type user\_marshal attribute, which provides an efficient way to marshal custom data types that are unknown to MIDL.

## In this section



| Topic                                                                          | Description                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BSTR\_UserFree**](bstr-userfree.md)<br/>                             | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**BSTR\_UserFree64**](bstr-userfree64.md)<br/>                         | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**BSTR\_UserMarshal**](bstr-usermarshal.md)<br/>                       | Marshals a [**BSTR**](bstr.md) object into the RPC buffer.<br/>                                                                                                                                    |
| [**BSTR\_UserMarshal64**](bstr-usermarshal64.md)<br/>                   | Marshals a [**BSTR**](bstr.md) object into the RPC buffer.<br/>                                                                                                                                    |
| [**BSTR\_UserSize**](bstr-usersize.md)<br/>                             | Calculates the wire size of the [**BSTR**](bstr.md) object, and gets its handle and data.<br/>                                                                                                     |
| [**BSTR\_UserSize64**](bstr-usersize64.md)<br/>                         | Calculates the wire size of the [**BSTR**](bstr.md) object, and gets its handle and data.<br/>                                                                                                     |
| [**BSTR\_UserUnmarshal**](bstr-userunmarshal.md)<br/>                   | Unmarshals a [**BSTR**](bstr.md) object from the RPC buffer.<br/>                                                                                                                                  |
| [**BSTR\_UserUnmarshal64**](bstr-userunmarshal64.md)<br/>               | Unmarshals a [**BSTR**](bstr.md) object from the RPC buffer.<br/>                                                                                                                                  |
| [**LPSAFEARRAY\_Marshal**](lpsafearray-marshal.md)<br/>                 | Marshals a [**SAFEARRAY**](safearray.md) object to a user's RPC buffer on the server using information passed in by the [**LPSAFEARRAY\_UserMarshal**](lpsafearray-usermarshal.md) function.<br/> |
| [**LPSAFEARRAY\_Size**](lpsafearray-size.md)<br/>                       | Calculates the wire size of the [**SAFEARRAY**](safearray.md) object, and gets its handle and data needed by the [**LPSAFEARRAY\_UserSize**](lpsafearray-usersize.md) function.<br/>              |
| [**LPSAFEARRAY\_Unmarshal**](lpsafearray-unmarshal.md)<br/>             | Unmarshals a [**SAFEARRAY**](safearray.md) object from the RPC buffer using information passed in by the [**LPSAFEARRAY\_UserUnmarshal**](lpsafearray-userunmarshal.md) function.<br/>            |
| [**LPSAFEARRAY\_UserFree**](lpsafearray-userfree.md)<br/>               | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**LPSAFEARRAY\_UserFree64**](lpsafearray-userfree64.md)<br/>           | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**LPSAFEARRAY\_UserMarshal**](lpsafearray-usermarshal.md)<br/>         | Marshals data from the specified [**SAFEARRAY**](safearray.md) object to the user's RPC buffer on the client or server side. <br/>                                                                 |
| [**LPSAFEARRAY\_UserMarshal64**](lpsafearray-usermarshal64.md)<br/>     | Marshals data from the specified [**SAFEARRAY**](safearray.md) object to the user's RPC buffer on the client or server side. <br/>                                                                 |
| [**LPSAFEARRAY\_UserSize**](lpsafearray-usersize.md)<br/>               | Calculates the wire size of the [**SAFEARRAY**](safearray.md) object, and gets its handle and data.<br/>                                                                                           |
| [**LPSAFEARRAY\_UserSize64**](lpsafearray-usersize64.md)<br/>           | Calculates the wire size of the [**SAFEARRAY**](safearray.md) object, and gets its handle and data.<br/>                                                                                           |
| [**LPSAFEARRAY\_UserUnmarshal**](lpsafearray-userunmarshal.md)<br/>     | Unmarshals a [**SAFEARRAY**](safearray.md) object from the RPC buffer.<br/>                                                                                                                        |
| [**LPSAFEARRAY\_UserUnmarshal64**](lpsafearray-userunmarshal64.md)<br/> | Unmarshals a [**SAFEARRAY**](safearray.md) object from the RPC buffer.<br/>                                                                                                                        |
| [**VARIANT\_UserFree**](variant-userfree.md)<br/>                       | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**VARIANT\_UserFree64**](variant-userfree64.md)<br/>                   | Frees resources on the server side when called by RPC stub files.<br/>                                                                                                                              |
| [**VARIANT\_UserMarshal**](variant-usermarshal.md)<br/>                 | Marshals a [**VARIANT**](variant.md) object into the RPC buffer.<br/>                                                                                                                              |
| [**VARIANT\_UserMarshal64**](variant-usermarshal64.md)<br/>             | Marshals a [**VARIANT**](variant.md) object into the RPC buffer.<br/>                                                                                                                              |
| [**VARIANT\_UserSize**](variant-usersize.md)<br/>                       | Calculates the wire size of the [**VARIANT**](variant.md) object, and gets its handle and data.<br/>                                                                                               |
| [**VARIANT\_UserSize64**](variant-usersize64.md)<br/>                   | Calculates the wire size of the [**VARIANT**](variant.md) object, and gets its handle and data.<br/>                                                                                               |
| [**VARIANT\_UserUnmarshal**](variant-userunmarshal.md)<br/>             | Unmarshals a [**VARIANT**](variant.md) object from the RPC buffer.<br/>                                                                                                                            |
| [**VARIANT\_UserUnmarshal64**](variant-userunmarshal64.md)<br/>         | Unmarshals a [**VARIANT**](variant.md) object from the RPC buffer.<br/>                                                                                                                            |



 

## Related topics

<dl> <dt>

[Conversion and Manipulation Functions](conversion-and-manipulation-functions.md)
</dt> </dl>

 

 





