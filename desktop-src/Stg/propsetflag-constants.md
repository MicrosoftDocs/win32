---
title: PROPSETFLAG Constants
description: Define characteristics of a property set.
ms.assetid: '6f865c8f-bbca-4122-b076-14f2bc56f292'
topic_type:
- apiref
api_name:
- PROPSETFLAG_DEFAULT
- PROPSETFLAG_NONSIMPLE
- PROPSETFLAG_ANSI
- PROPSETFLAG_UNBUFFERED
- PROPSETFLAG_CASE_SENSITIVE
api_location:
- Propidl.h
api_type:
- HeaderDef
---

# PROPSETFLAG Constants

The PROPSETFLAG constants define characteristics of a property set. The values, listed in the following table, are used in the *grfFlags* parameter of [**IPropertySetStorage**](ipropertysetstorage.md) methods, the [**StgCreatePropStg**](stgcreatepropstg.md) function, and the [**StgOpenPropStg**](stgopenpropstg.md) function.



| Constant/value                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PROPSETFLAG_DEFAULT"></span><span id="propsetflag_default"></span><dl> <dt>**PROPSETFLAG\_DEFAULT**</dt> <dt>0</dt> </dl>                       | If left unspecified, by default only simple property values may be written to the property set. Using simple property values prevents property sets from being transacted in the compound file and stand-alone implementations of [**IPropertySetStorage**](ipropertysetstorage.md). Non-e property values must be used for this purpose.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="PROPSETFLAG_NONSIMPLE"></span><span id="propsetflag_nonsimple"></span><dl> <dt>**PROPSETFLAG\_NONSIMPLE**</dt> <dt>1</dt> </dl>                 | If specified, nonsimple property values can be written to the property set and the property set is saved in a storage object. Non-simple property values include those with a VARTYPE of VT\_STORAGE, VT\_STREAM, VT\_STORED\_OBJECT, or VT\_STREAMED\_OBJECT. If this flag is not specified, non-simple types cannot be written into the property set. In the compound file and stand-alone implementations, property sets may be transacted only if **PROPSETFLAG\_NONSIMPLE** is specified.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="PROPSETFLAG_ANSI"></span><span id="propsetflag_ansi"></span><dl> <dt>**PROPSETFLAG\_ANSI**</dt> <dt>2</dt> </dl>                                | If specified, all string values in the property set that are not explicitly Unicode, that is, those other than VT\_LPWSTR, are stored with the current system ANSI code page. For more information, see [**GetACP**](https://msdn.microsoft.com/library/windows/desktop/dd318070). Use of this value is not recommended. For more information, see Remarks.<br/> If this value is absent, string values in the new property set are stored in Unicode. The degree of control that this value provides is necessary so that clients using the property-related interfaces can interoperate with standard property sets such as the OLE2 summary information, which may exist in the ANSI code page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="PROPSETFLAG_UNBUFFERED"></span><span id="propsetflag_unbuffered"></span><dl> <dt>**PROPSETFLAG\_UNBUFFERED**</dt> <dt>4</dt> </dl>              | Used only with the [**StgCreatePropStg**](stgcreatepropstg.md) and [**StgOpenPropStg**](stgopenpropstg.md) functions; that is, in the stand-alone implementations of property set interfaces. If specified in these functions, changes to the property set are not buffered. Instead, changes are always written directly to the property set. Calls to a property set [**IPropertyStorage**](ipropertystorage.md) methods will change it. However, by default, changes are buffered in an internal property set cache and are subsequently written to the property set when the [**IPropertyStorage::Commit**](ipropertystorage-commit.md) method is called. <br/> Setting **PROPSETFLAG\_UNBUFFERED** decreases performance because the property set internal buffer is automatically flushed after every change to the property set. However, writing changes directly will prevent coordination problems. For example, if the storage object is opened in transacted mode, and the property set is buffered. Then, if you call the [**IStorage::Commit**](istorage-commit.md) method on the storage object, the property set changes will not be picked up as part of the transaction, because they are in a buffer that has not been flushed yet. You must call [**IPropertyStorage::Commit**](ipropertystorage-commit.md) prior to calling **IStorage::Commit** to flush the property set buffer before committing changes to the storage. As an alternative to making two calls, you can set **PROPSETFLAG\_UNBUFFERED** so that changes are always written directly to the property set and are never buffered in the property set's internal cache. Then, the changes will be picked up when the transacted storage is committed.<br/> |
| <span id="PROPSETFLAG_CASE_SENSITIVE"></span><span id="propsetflag_case_sensitive"></span><dl> <dt>**PROPSETFLAG\_CASE\_SENSITIVE**</dt> <dt>8</dt> </dl> | If specified, property names are case sensitive. Case-sensitive property names are only possible in the version 1 property set serialization format. For more information, see [Property Set Serialization](version-0-vs--version-1-property-set-serialization.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



## Remarks

These values can be set and checked using bitwise operations that determine how property sets are created and opened. Property sets are created using the [**IPropertySetStorage::Create**](ipropertysetstorage-create.md) method or the [**StgCreatePropStg**](stgcreatepropstg.md) function. They are opened using the [**IPropertySetStorage::Open**](ipropertysetstorage-open.md) method or the [**StgOpenPropStg**](stgopenpropstg.md) function.

It is recommended that property sets be created as Unicode by not setting the **PROPSETFLAG\_ANSI** flag in the *grfFlags* parameter. It is also recommended that you avoid using VT\_LPSTR values, and use VT\_LPWSTR values instead. When the property set code page is Unicode, VT\_LPSTR string values are converted to Unicode when stored, and converted back to multibyte string values when retrieved. When the code page of the property set is not Unicode, property names, VT\_BSTR strings, and nonsimple property values are converted to multibyte strings when stored, and converted back to Unicode when retrieved, all using the current system ANSI code page.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Propidl.h</dt> </dl> |



## See also

<dl> <dt>

[**FmtIdToPropStgName**](fmtidtopropstgname.md)
</dt> <dt>

[**IPropertySetStorage::Create**](ipropertysetstorage-create.md)
</dt> <dt>

[**IPropertySetStorage::Open**](ipropertysetstorage-open.md)
</dt> <dt>

[**PropStgNameToFmtId**](propstgnametofmtid.md)
</dt> <dt>

[**StgCreatePropSetStg**](stgcreatepropsetstg.md)
</dt> <dt>

[**StgCreatePropStg**](stgcreatepropstg.md)
</dt> <dt>

[**StgOpenPropStg**](stgopenpropstg.md)
</dt> </dl>

 

 





