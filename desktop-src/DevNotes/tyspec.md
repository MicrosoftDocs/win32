---
description: Defines ways of mapping to a class ID.
ms.assetid: 1af170e3-1edd-411f-acba-d4b244107996
title: TYSPEC enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TYSPEC
api_type: 
- IDLDef
api_location: 
- Wtypes.idl
---

# TYSPEC enumeration

Defines ways of mapping to a class ID.

## Syntax


```C++
typedef enum tagTYSPEC { 
  TYSPEC_CLSID,
  TYSPEC_FILEEXT,
  TYSPEC_MIMETYPE,
  TYSPEC_FILENAME,
  TYSPEC_PROGID,
  TYSPEC_PACKAGENAME,
  TYSPEC_OBJECTID
} TYSPEC;
```



## Constants

<dl> <dt>

<span id="TYSPEC_CLSID"></span><span id="tyspec_clsid"></span>**TYSPEC\_CLSID**
</dt> <dd>

A CLSID.

</dd> <dt>

<span id="TYSPEC_FILEEXT"></span><span id="tyspec_fileext"></span>**TYSPEC\_FILEEXT**
</dt> <dd>

A file name extension. This value is not currently supported.

</dd> <dt>

<span id="TYSPEC_MIMETYPE"></span><span id="tyspec_mimetype"></span>**TYSPEC\_MIMETYPE**
</dt> <dd>

A MIME type. This value is not currently supported.

</dd> <dt>

<span id="TYSPEC_FILENAME"></span><span id="tyspec_filename"></span>**TYSPEC\_FILENAME**
</dt> <dd>

A file name. This value is not currently supported.

</dd> <dt>

<span id="TYSPEC_PROGID"></span><span id="tyspec_progid"></span>**TYSPEC\_PROGID**
</dt> <dd>

A PROGID. This value is not currently supported.

</dd> <dt>

<span id="TYSPEC_PACKAGENAME"></span><span id="tyspec_packagename"></span>**TYSPEC\_PACKAGENAME**
</dt> <dd>

A package name. This value is not currently supported.

</dd> <dt>

<span id="TYSPEC_OBJECTID"></span><span id="tyspec_objectid"></span>**TYSPEC\_OBJECTID**
</dt> <dd>

An object ID. This value is not currently supported.

</dd> </dl>

## Remarks

The **uCLSSPEC** union is defined as follows:

``` syntax
typedef union switch(DWORD tyspec) {
    case TYSPEC_CLSID:
        CLSID clsid;
    case TYSPEC_FILEEXT:
        LPOLESTR pFileExt;
    case TYSPEC_MIMETYPE:
        LPOLESTR pMimeType;
    case TYSPEC_PROGID:
        LPOLESTR pProgId;
    case TYSPEC_FILENAME:
        LPOLESTR pFileName;
    case TYSPEC_PACKAGENAME:
        struct {
        LPOLESTR pPackageName;
        GUID PolicyId;
        } ByName;
    case TYSPEC_OBJECTID:
        struct {
        GUID ObjectId;
        GUID PolicyId;
        } ByObjectId;
} uCLSSPEC;
```

## Requirements



| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>Wtypes.idl</dt> </dl> |



## See also

<dl> <dt>

[**CoInstall**](/windows/win32/api/objbase/nf-objbase-coinstall)
</dt> </dl>

 

 
