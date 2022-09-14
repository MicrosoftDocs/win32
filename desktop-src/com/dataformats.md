---
title: DataFormats
description: Specifies the default and main data formats supported by an application.
ms.assetid: 0c9387f9-d7e0-40e7-8d86-96a79a844161
keywords:
- DataFormats registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# DataFormats

Specifies the default and main data formats supported by an application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      DataFormats
         DefaultFile = file/format
         GetSet
            n = formats
```

## Remarks

The *file/format* value specifies the default main file or object format for objects of this class.

The *formats* value specifies a list of formats for default implementations of [**EnumFormatEtc**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-enumformatetc), where *n* is a zero-based integer index. For example, *n* = *format*, *aspect*, *medium*, *flag*, where *format* is a clipboard format, *aspect* is one or more members of [**DVASPECT**](/windows/win32/api/wtypes/ne-wtypes-dvaspect), *medium* is one or more members of [**TYMED**](/windows/win32/api/objidl/ne-objidl-tymed), and *flag* is one or more members of [**DATADIR**](/windows/win32/api/objidl/ne-objidl-datadir).

## Related topics

<dl> <dt>

[**IDataObject::EnumFormatEtc**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-enumformatetc)
</dt> <dt>

[**IDataObject::GetData**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-getdata)
</dt> <dt>

[**IDataObject::SetData**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-setdata)
</dt> </dl>

 

 




