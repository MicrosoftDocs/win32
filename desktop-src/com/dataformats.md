---
title: DataFormats
description: Specifies the default and main data formats supported by an application.
ms.assetid: '0c9387f9-d7e0-40e7-8d86-96a79a844161'
keywords: ["DataFormats registry key COM"]
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

The *formats* value specifies a list of formats for default implementations of [**EnumFormatEtc**](idataobject-enumformatetc.md), where *n* is a zero-based integer index. For example, *n* = *format*, *aspect*, *medium*, *flag*, where *format* is a clipboard format, *aspect* is one or more members of [**DVASPECT**](dvaspect.md), *medium* is one or more members of [**TYMED**](tymed.md), and *flag* is one or more members of [**DATADIR**](datadir.md).

## Related topics

<dl> <dt>

[**IDataObject::EnumFormatEtc**](idataobject-enumformatetc.md)
</dt> <dt>

[**IDataObject::GetData**](idataobject-getdata.md)
</dt> <dt>

[**IDataObject::SetData**](idataobject-setdata.md)
</dt> </dl>

 

 




